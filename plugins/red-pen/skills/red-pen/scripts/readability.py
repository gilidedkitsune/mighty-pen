#!/usr/bin/env python3
"""Readability and concreteness report for a draft.

Input is plain text on stdin, or a path to a UTF-8 text or Markdown file. Word documents are
refused: extract the text first. Output is JSON with:
  overall      reading-ease and grade-level figures for the whole draft
  long_sentences  the longest sentences (30+ words), for pacing
  concreteness    how picturable the vocabulary is, when a norms file is present
  sections        per-section reading ease, when the draft has headers

Usage:
    echo "text" | python3 readability.py
    python3 readability.py draft.md
"""

import json
import os
import re
import sys

NORMS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "concreteness.csv")
BINARY_SIGNATURES = (b"PK\x03\x04", b"%PDF", b"\xd0\xcf\x11\xe0")
BINARY_EXTENSIONS = (".docx", ".doc", ".pdf", ".xlsx", ".pptx")

# Words that pronunciation rules get wrong. Syllable counts are hand-set for these.
SYLLABLE_OVERRIDES = {
    "the": 1, "be": 1, "he": 1, "she": 1, "we": 1, "me": 1, "are": 1, "were": 1,
    "there": 1, "where": 1, "here": 1, "fire": 1, "hire": 1, "more": 1, "store": 1,
    "core": 1, "real": 1, "create": 2, "created": 3, "every": 3, "different": 3,
    "business": 3, "area": 3, "idea": 3,
}

# Function words left out of the concreteness average, so it reflects content words.
FUNCTION_WORDS = frozenset("""
a about above after again against all also am an and any are as at be because been before
being below between both but by can could did do does down during each either else few for
from further had has have having he her here hers him his how i if in into is it its just me
might more most must my no nor not now of off on once only or other our out over own same
she should so some such than that the their them then there these they this those through to
too under until up us very was we were what when where which while who whom why will with
would yet you your
""".split())

_NORMS = None


def count_syllables(word):
    token = word.lower().strip(".,!?;:\"'()[]-")
    if not token:
        return 0
    if token in SYLLABLE_OVERRIDES:
        return SYLLABLE_OVERRIDES[token]

    groups = len(re.findall(r"[aeiouy]+", token))
    if token.endswith("e") and not re.search(r"(le|ce|se|ge|ve|ze)$", token) and groups > 1:
        groups -= 1
    if re.search(r"[^td]ed$", token) and groups > 1:
        groups -= 1
    if re.search(r"[^s](es)$", token) and groups > 1 and not re.search(r"(ses|zes|ces|ges)$", token):
        groups -= 1
    return max(1, groups)


def clean_markdown(text):
    text = re.sub(r"```[\s\S]*?```", " ", text)
    text = re.sub(r"`[^`]*`", " ", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"^\s*#{1,6}\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\s*(?:[-*+]|\d+\.|>)\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"[*_]{1,3}", "", text)
    return text


def sentences_of(text):
    protected = clean_markdown(text)
    for abbrev in ("Mr", "Mrs", "Ms", "Dr", "Prof", "vs", "etc", "Inc", "Ltd"):
        protected = re.sub(rf"\b{abbrev}\.", abbrev + "\u0000", protected)
    protected = re.sub(r"(\d)\.(\d)", "\\1\u0000\\2", protected)
    protected = re.sub(r"\b([A-Z])\.", "\\1\u0000", protected)
    parts = re.split(r"[.!?]+(?=\s|$)", protected)
    return [p.replace("\u0000", ".").strip() for p in parts if p.strip()]


def words_of(text):
    return re.findall(r"[A-Za-z][A-Za-z'-]*", clean_markdown(text))


def is_long_word(word):
    """Gunning Fog's 'complex' word: three or more syllables, not capitalized, not hyphenated."""
    return word[0].islower() and "-" not in word and count_syllables(word) >= 3


def reading_level(flesch):
    bands = [
        (80, "Easy (about 6th grade): conversational, reaches almost everyone"),
        (70, "Fairly easy (about 7th grade): suits broad audiences"),
        (60, "Standard (8th to 9th grade): the usual target for most content"),
        (50, "Fairly difficult (10th to 12th grade): getting dense"),
        (30, "Difficult (college level): specialist territory"),
    ]
    for floor, label in bands:
        if flesch >= floor:
            return label
    return "Very difficult (graduate level): academic or legal density"


def measure(text):
    sentences = sentences_of(text)
    words = words_of(text)
    if not sentences or not words:
        return None

    n_words, n_sentences = len(words), len(sentences)
    syllables = sum(count_syllables(w) for w in words)
    long_words = sum(1 for w in words if is_long_word(w))

    words_per_sentence = n_words / n_sentences
    syllables_per_word = syllables / n_words
    long_share = 100.0 * long_words / n_words

    ease = 206.835 - 1.015 * words_per_sentence - 84.6 * syllables_per_word
    ease = round(min(100.0, max(0.0, ease)), 1)
    grade = round(max(0.0, 0.39 * words_per_sentence + 11.8 * syllables_per_word - 15.59), 1)
    fog = round(0.4 * (words_per_sentence + long_share), 1)

    return {
        "total_words": n_words,
        "total_sentences": n_sentences,
        "avg_sentence_length": round(words_per_sentence, 1),
        "avg_syllables_per_word": round(syllables_per_word, 2),
        "flesch_reading_ease": ease,
        "flesch_level": reading_level(ease),
        "fk_grade_level": grade,
        "gunning_fog": fog,
        "complex_word_pct": round(long_share, 1),
    }


def split_by_headers(text):
    sections, title, body = [], "Opening (no header)", []

    def flush():
        chunk = "\n".join(body).strip()
        if chunk:
            sections.append({"title": title, "text": chunk})

    for line in text.split("\n"):
        heading = re.match(r"^#{1,6}\s+(.+)$", line)
        if heading:
            flush()
            title, body = heading.group(1).strip(), []
        else:
            body.append(line)
    flush()
    return sections


def longest_sentences(text, floor=30, keep=5):
    found = []
    for sentence in sentences_of(text):
        n = len(words_of(sentence))
        if n >= floor:
            found.append({"words": n, "preview": " ".join(sentence.split()[:12]) + "..."})
    return sorted(found, key=lambda row: row["words"], reverse=True)[:keep]


def load_norms():
    """Word-to-rating table from concreteness.csv (1 abstract to 5 concrete). Read once."""
    global _NORMS
    if _NORMS is not None:
        return _NORMS
    if not os.path.exists(NORMS_FILE):
        return None
    table = {}
    with open(NORMS_FILE, encoding="utf-8") as fh:
        for raw in fh:
            if raw.startswith("#") or raw.startswith("word,"):
                continue
            fields = raw.rstrip("\n").split(",")
            if len(fields) == 2:
                try:
                    table[fields[0]] = float(fields[1])
                except ValueError:
                    pass
    _NORMS = table
    return table


def concreteness(text):
    """How picturable the content words are. A flag for judgment, not a rule."""
    table = load_norms()
    if table is None:
        return {"unavailable": "no concreteness table found next to this script"}

    content = [w.lower() for w in words_of(text) if w.lower() not in FUNCTION_WORDS and len(w) > 1]
    rated = [(w, table[w]) for w in content if w in table]
    if len(rated) < 5:
        return None

    mean = sum(score for _, score in rated) / len(rated)
    per_sentence = []
    for sentence in sentences_of(text):
        scores = [table[w.lower()] for w in words_of(sentence)
                  if w.lower() in table and w.lower() not in FUNCTION_WORDS]
        if len(scores) >= 4:
            per_sentence.append({
                "score": round(sum(scores) / len(scores), 2),
                "preview": " ".join(sentence.split()[:12]) + ("..." if len(sentence.split()) > 12 else ""),
            })

    vaguest = []
    for word, score in sorted(set(rated), key=lambda pair: pair[1]):
        if score < 2.5 and word not in vaguest:
            vaguest.append(word)
        if len(vaguest) == 8:
            break

    if mean < 2.5:
        band = "abstract-heavy: much of the language is hard to picture"
    elif mean < 3.2:
        band = "mixed: some concrete language, some abstract"
    else:
        band = "concrete: mostly picturable, specific language"

    return {
        "mean": round(mean, 2),
        "scored_words": len(rated),
        "coverage_pct": round(100.0 * len(rated) / len(content), 1) if content else 0.0,
        "band": band,
        "most_abstract_sentences": sorted(per_sentence, key=lambda row: row["score"])[:3],
        "vaguest_words": vaguest,
    }


def read_input(argv):
    if len(argv) < 2:
        return sys.stdin.read()

    path = argv[1]
    if path.lower().endswith(BINARY_EXTENSIONS):
        return None
    try:
        with open(path, "rb") as fh:
            raw = fh.read()
    except FileNotFoundError:
        raise SystemExit(json.dumps({"error": f"File not found: {path}"}))
    if raw.startswith(BINARY_SIGNATURES):
        return None
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        return None


def fail(message):
    print(json.dumps({"error": message}))
    sys.exit(1)


def main():
    text = read_input(sys.argv)
    if text is None:
        fail("Binary file (for example .docx) isn't supported. Extract the text first, then pass it in.")
    if not text.strip():
        fail("No text provided")

    overall = measure(text)
    if overall is None:
        fail("Could not analyze text: too short or no sentences found")

    report = {"overall": overall}
    long_rows = longest_sentences(text)
    if long_rows:
        report["long_sentences"] = long_rows
    scored = concreteness(text)
    if scored:
        report["concreteness"] = scored

    sections = split_by_headers(text)
    if len(sections) > 1:
        rows = []
        for section in sections:
            stats = measure(section["text"])
            if stats:
                rows.append({
                    "section": section["title"],
                    "flesch_reading_ease": stats["flesch_reading_ease"],
                    "avg_sentence_length": stats["avg_sentence_length"],
                    "word_count": stats["total_words"],
                })
        if rows:
            report["sections"] = rows

    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
