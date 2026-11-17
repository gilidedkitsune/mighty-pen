#!/usr/bin/env python3
"""Repetition check for a draft: which content words recur, how densely, and how clustered.

Counts content words after dropping function words and merging word forms (default, defaults,
defaulted). Proper nouns and acronyms are listed on their own. Subject terms (taken from the
title, plus anything passed with --terms) are counted but never flagged, because a piece is
supposed to keep returning to its subject.

Usage:
    echo "text" | python3 repetition.py --terms "forge,model"
    python3 repetition.py draft.md --terms "forge,model,plan"

Standard library only. Word documents are refused; extract the text first.
"""

import json
import os
import re
import sys
from collections import Counter, defaultdict

FUNCTION_WORDS = frozenset("""
a about above across after again against all almost also although always am among an and
another any anyone anything are around as at be because been before being below beside
between beyond both but by can cannot could did do does doing done down during each either
else enough even ever every everyone everything few for from further get gets getting got
had has have having he her here hers herself him himself his how however i if in into is
it its itself just least less let like likely made make many may me might more most much
must my myself neither never next no nobody none nor not nothing now of off often on once
one only onto or other others otherwise our ours ourselves out over own per perhaps quite
rather really same several shall she should since so some something sometimes somewhat still
such than that the their theirs them themselves then there these they this those though
through throughout thus to too toward towards under until up upon us very via was we well
were what whatever when whenever where whether which while who whoever whole whom whose why
will with within without would yet you your yours yourself yourselves
""".split())

# Irregular forms that suffix rules can't reach.
IRREGULAR = {
    "went": "go", "gone": "go", "made": "make", "built": "build", "said": "say",
    "took": "take", "taken": "take", "gave": "give", "given": "give", "ran": "run",
    "wrote": "write", "written": "write", "saw": "see", "seen": "see", "knew": "know",
    "known": "know", "thought": "think", "found": "find", "left": "leave", "told": "tell",
    "kept": "keep", "began": "begin", "begun": "begin", "brought": "bring", "bought": "buy",
    "chose": "choose", "chosen": "choose", "grew": "grow", "grown": "grow", "held": "hold",
    "led": "lead", "lost": "lose", "met": "meet", "paid": "pay", "sent": "send",
    "showed": "show", "shown": "show", "spent": "spend", "stood": "stand",
    "understood": "understand", "won": "win", "broke": "break", "broken": "break",
    "spoke": "speak", "spoken": "speak", "fell": "fall", "felt": "feel", "meant": "mean",
    "sold": "sell", "taught": "teach", "caught": "catch", "drew": "draw", "drawn": "draw",
    "threw": "throw", "thrown": "throw", "wore": "wear", "worn": "wear", "rose": "rise",
    "risen": "rise", "people": "person", "children": "child", "men": "man", "women": "woman",
    "teams": "team", "better": "good", "best": "good", "worse": "bad", "worst": "bad",
}

SHORT_RED_FLAGS = {"thing", "things", "way", "ways", "lot", "lots", "kind", "sort"}


def strip_markup(text):
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"`[^`]*`", " ", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"^\s{0,3}#{1,6}\s*", "", text, flags=re.M)
    text = re.sub(r"^\s*[-*+>]\s+", "", text, flags=re.M)
    text = re.sub(r"[*_]{1,3}", "", text)
    return text


def base_form(word, seen_surfaces):
    """Reduce a word to a shared base, preferring a base that already appears in the text."""
    if word in IRREGULAR:
        return IRREGULAR[word]
    options = []
    n = len(word)
    if n > 4 and word.endswith("ies"):
        options.append(word[:-3] + "y")
    if n > 4 and word.endswith("ied"):
        options.append(word[:-3] + "y")
    if n > 4 and word.endswith("sses"):
        options.append(word[:-2])
    if n > 3 and word.endswith("es") and word[-3] in "sxz":
        options.append(word[:-2])
    if n > 5 and word.endswith("ing"):
        stem = word[:-3]
        options += [stem + "e", stem, stem[:-1] if len(stem) > 2 and stem[-1] == stem[-2] else stem]
    if n > 4 and word.endswith("ed"):
        stem = word[:-2]
        options += [stem + "e", stem, stem[:-1] if len(stem) > 2 and stem[-1] == stem[-2] else stem]
    if n > 3 and word.endswith("s") and not word.endswith("ss"):
        options.append(word[:-1])
    if n > 4 and word.endswith("ly"):
        options.append(word[:-2])

    for option in options:
        if option in seen_surfaces:
            return option
    for option in options:
        if option + "e" in seen_surfaces:
            return option + "e"
    return options[0] if options else word


def is_title_line(paragraphs, title_match):
    if title_match:
        return title_match.group(1)
    if len(paragraphs) < 2:
        return ""
    first = paragraphs[0].split("\n")[0].strip()
    if len(first.split()) <= 15 and not first.endswith((".", "!", "?")):
        return first
    return ""


def tier_of(lemma_total, paragraph_peak, per_thousand, marked):
    if paragraph_peak >= 3 or (lemma_total >= 8 and per_thousand >= 10) or (marked and lemma_total >= 8):
        return "red"
    if (lemma_total >= 5 and per_thousand >= 5 and paragraph_peak >= 2) or (marked and lemma_total >= 5):
        return "yellow"
    return "note"


def analyze(raw, extra_terms):
    text = strip_markup(raw)
    paragraphs = [p for p in re.split(r"\n\s*\n", text) if p.strip()]
    title = is_title_line(paragraphs, re.search(r"^\s{0,3}#\s+(.+)$", raw, flags=re.M))
    token_pattern = re.compile(r"[A-Za-z][A-Za-z.\-']*[A-Za-z]|[A-Za-z]")

    surface_counts = Counter()
    capitalized_mid = Counter()
    lowercase_uses = Counter()
    total_tokens = 0
    for para in paragraphs:
        for sentence in re.split(r"(?<=[.!?])\s+", para.strip()):
            tokens = token_pattern.findall(sentence)
            mostly_capitalized = len(tokens) <= 12 and sum(t[0].isupper() for t in tokens) >= 0.6 * max(len(tokens), 1)
            for index, token in enumerate(tokens):
                total_tokens += 1
                key = re.sub(r"'(s|re|ve|ll|d|m|t)$", "", token.lower().strip(".-'"))
                if not key:
                    continue
                surface_counts[key] += 1
                if token[0].isupper() and index > 0 and not mostly_capitalized:
                    capitalized_mid[key] += 1
                if token[0].islower():
                    lowercase_uses[key] += 1

    proper = {k for k, c in capitalized_mid.items() if c >= 2 and c >= 2 * lowercase_uses[k] and k not in FUNCTION_WORDS}
    for token in set(re.findall(r"\b[A-Z]{2,5}\b", raw)):
        proper.add(token.lower())

    subject = set()
    for token in token_pattern.findall(title):
        key = token.lower().strip(".-'")
        if key and key not in FUNCTION_WORDS and len(key) >= 3:
            subject.add(base_form(key, surface_counts))
    subject |= {base_form(t, surface_counts) for t in extra_terms}

    lemma_count = Counter()
    lemma_forms = defaultdict(Counter)
    lemma_paras = defaultdict(Counter)
    proper_count = Counter()
    content_total = 0
    for p_index, para in enumerate(paragraphs):
        for token in token_pattern.findall(para):
            key = re.sub(r"'(s|re|ve|ll|d|m|t)$", "", token.lower().strip(".-'"))
            if not key or key in FUNCTION_WORDS or len(key) < 3 or key.isdigit():
                continue
            if key in proper or "." in key:
                proper_count[key if "." in key else token.strip(".,")] += 1
                continue
            lemma = base_form(key, surface_counts)
            content_total += 1
            lemma_count[lemma] += 1
            lemma_forms[lemma][key] += 1
            lemma_paras[lemma][p_index] += 1

    def per_thousand(n):
        return round(n * 1000 / max(total_tokens, 1), 1)

    rows, subject_rows = [], []
    for lemma, count in lemma_count.most_common(60):
        if count < 2:
            break
        peak = max(lemma_paras[lemma].values())
        row = {
            "lemma": lemma,
            "count": count,
            "per_1k_words": per_thousand(count),
            "forms": dict(lemma_forms[lemma].most_common()),
            "paragraphs_touched": len(lemma_paras[lemma]),
            "max_in_one_paragraph": peak,
        }
        if lemma in subject:
            subject_rows.append(row)
            continue
        marked = len(lemma) >= 7 or "-" in lemma or lemma in SHORT_RED_FLAGS
        row["tier"] = tier_of(count, peak, per_thousand(count), marked)
        row["why"] = ("clusters" if peak >= 3 else
                      "marked word, recurs" if marked and count >= 5 else
                      "dense" if per_thousand(count) >= 5 else "")
        rows.append(row)

    rows.sort(key=lambda r: ({"red": 0, "yellow": 1, "note": 2}[r["tier"]], -r["max_in_one_paragraph"], -r["count"]))
    flagged = [r for r in rows if r["tier"] != "note"]
    quiet = [r for r in rows if r["tier"] == "note"][:10]
    return {
        "words_total": total_tokens,
        "paragraphs": len(paragraphs),
        "content_words": content_total,
        "unique_content_lemmas": len(lemma_count),
        "content_variety": round(len(lemma_count) / max(content_total, 1), 3),
        "reds": sum(r["tier"] == "red" for r in rows),
        "yellows": sum(r["tier"] == "yellow" for r in rows),
        "title_detected": title,
        "subject_terms_untiered": subject_rows[:10],
        "repeaters": flagged + quiet,
        "proper_nouns_and_acronyms": [{"term": k, "count": v} for k, v in proper_count.most_common(12)],
        "how_to_read": ("max_in_one_paragraph is the figure a reader feels. Subject terms and proper nouns "
                        "are counted but never flagged; pass more with --terms. A tic is fixed by restructuring "
                        "the sentence, never by swapping in a synonym."),
    }


def read_source(args):
    if args:
        path = args[0]
        if path.lower().endswith((".docx", ".doc", ".pdf")):
            return None, "Binary document. Extract the text first, then pass it in."
        if not os.path.exists(path):
            return None, f"File not found: {path}"
        with open(path, encoding="utf-8", errors="replace") as fh:
            return fh.read(), None
    return sys.stdin.read(), None


def main():
    argv = sys.argv[1:]
    extra_terms = set()
    if "--terms" in argv:
        at = argv.index("--terms")
        if at + 1 < len(argv):
            extra_terms = {t.strip().lower() for t in argv[at + 1].split(",") if t.strip()}
        del argv[at:at + 2]

    raw, problem = read_source(argv)
    if problem:
        print(json.dumps({"error": problem}))
        return
    if not raw or not raw.strip():
        print(json.dumps({"error": "No text provided"}))
        return
    print(json.dumps(analyze(raw, extra_terms), indent=2))


if __name__ == "__main__":
    main()
