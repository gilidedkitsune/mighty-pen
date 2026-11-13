---
name: repurpose
description: >
  Turns one finished piece (a blog post, report, essay, webinar, talk, or case study) into
  native versions for other channels: LinkedIn post, X post or thread, newsletter section, and
  email. Each version is rebuilt for its channel, not trimmed, and keeps the source's claims
  and citations intact. Trigger on "repurpose this", "turn this into a LinkedIn post", "make a
  thread from this", "socialize this", "cut this down for the newsletter", "atomize", or "get
  more mileage out of this post". Works on a finished piece only; for a new social post from
  scratch, use quill.
---

# Repurpose

One good piece, rebuilt for the places its readers actually are. Repurposing is not shrinking: a LinkedIn post that reads like a blog intro with the rest cut off gets scrolled past. Each channel has its own physics, and each version earns its own read.

## Before you start

1. **Read the whole source.** Then write its promise in one sentence (quill Step 1): who it's for and what they walk away with. If you can't, the source isn't finished; say so.
2. **Pull the atoms.** List the 5 to 10 strongest standalone units in the source: a number, a quote, a contrarian claim, a short story, a how-to step, a before-and-after. Each version is built from one to three atoms, never a summary of the whole piece.
3. **Ask which channels** (AskUserQuestion, `multiSelect: true`): LinkedIn, X, newsletter, email, or others the user names. Also ask whose account each one goes out from, since that sets the voice.

## Voice

- Company account: the register the source used (usually B2B tech buyer for product content).
- A person's account: their profile from `${CLAUDE_PLUGIN_ROOT}/skills/voice-profiles/SKILL.md` if one exists; Taylor's own account uses the professional or personal register from `${CLAUDE_PLUGIN_ROOT}/skills/tone-and-guidelines/SKILL.md`. No profile for the named person: say so and use the default rather than inventing a voice.

## Channel specs

### LinkedIn post
- 150 to 300 words. The first two lines show before "see more" and decide whether anyone reads the rest: lead with the sharpest atom, not context.
- Short paragraphs, one idea each. White space is fine; one-word-per-line drama is a tell.
- One point of view. End with the takeaway or a specific question, not "Thoughts?"
- Link in the post body is fine; say what's behind it.
- No hashtag walls; zero to three, only if the user uses them.

### X post or thread
- Single post: under about 280 characters, one atom, with the number or the claim up front.
- Thread (only when the source has a sequence: steps, a story, a list): 4 to 8 posts. Post 1 stands alone and makes the promise; each post after it is one move; the last post links to the source.
- No "🧵" or "A thread:" openers. No numbering unless it's a list.

### Newsletter section
- 100 to 250 words, in the newsletter's own voice: a short intro on why it matters to this list now, the one or two most useful atoms, and the link.
- Write it as a note from a person to their readers, not a press release.

### Email (promotional or nurture)
- Subject line: 30 to 50 characters; run `${CLAUDE_PLUGIN_ROOT}/skills/headline-lab/SKILL.md` for options if it matters.
- Preview text that adds to the subject, not repeats it.
- 75 to 200 words, one atom, one call to action, matched to the reader's stage.

## Rules for every version

- **Same facts, same citations.** Any stat that survives carries its source. Never round a number up, drop a qualifier, or turn a finding into a stronger claim to make it punchier. If the attribution won't fit, cut the stat.
- **No new claims.** Everything in a version comes from the source. If a version needs something the source doesn't have, ask.
- **Native, not truncated.** Each version should make sense to someone who will never click through.
- **Different lead per channel**, so a reader who follows the user everywhere doesn't see the same post four times.
- Run no-slops's mechanical checks on every version (`${CLAUDE_PLUGIN_ROOT}/skills/no-slops/SKILL.md`): §0 fingerprints, Tier 1 vocabulary, banned phrases, em dashes. Short copy is where tells leak most.

## Present

Each version under a channel heading, with character or word count, the atom it's built on, and the account it's for. Then offer: alternate leads for any version, a posting sequence (which goes first, spacing), or a second pass in a different voice.
