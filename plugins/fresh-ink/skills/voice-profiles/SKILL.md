---
name: voice-profiles
description: >
  Library of individual voice and tone profiles, for writing in a specific person's voice
  instead of the default, plus the routine that builds a new profile from 3 to 5 writing
  samples. Trigger on "build a voice profile", "capture my voice", "capture [name]'s voice",
  "write like [person]", "add a voice", or "make a tone profile from these". craft reads the
  roster at draft time; without a profile, everything uses tone-and-guidelines.
metadata:
  version: 2.1.0
---

# Skill: Voice-Profiles

**Goal:** Provide structured voice and tone reference profiles for writing convincingly as a specific person, when that's the job, and build new ones from real samples. This is the exception path; the default voice for everything is `tone-and-guidelines`.

## Available Voices

| Person | Role | Handle | Menu blurb | File |
|---|---|---|---|---|
| *(none loaded yet)* | | | | |

This table is the **single source of truth for the voice roster**. craft builds its voice-selection menu from it at draft time (the default voice from `tone-and-guidelines` plus these rows via their Menu blurbs). **Adding a voice:** run the capture routine below, which writes the profile file to `${CLAUDE_PLUGIN_ROOT}/skills/voice-profiles/references/` and adds the row here; craft's menu follows automatically, no edit there.

## How to Use
1. Read the relevant person's tone file before drafting content in their voice.
2. Match their sentence patterns and topic framing.
3. Avoid anything listed in their "What they avoid" section.
4. Keep the register's limits: a profile replaces the default voice's personality, not the rules of the register the content type calls for (tone-and-guidelines, "Choosing a register").
5. If no profile exists for the person the draft needs, say so and offer to capture one. Never invent a voice; until there's a profile, fall back to the default voice.

## Capture a voice (build a profile from samples)

### 1. Collect samples
Ask for 3 to 5 pieces, ideally 3,000 words or more in total, that the person wrote themselves. Range beats volume: a long piece, a short one, and something informal (an email, a post) show more of the voice than five blog posts. Accept pasted text, files, or links the session can open.

### 2. Authorship check (before analyzing anything)
A profile built from the wrong text reproduces the wrong voice. For each sample, confirm with the user:
- **Who wrote it?** Solo, co-written, ghostwritten, or heavily edited by someone else. Ghostwritten and heavily edited pieces are out; co-written pieces count only for the sections the person wrote.
- **Was it AI-drafted or AI-polished?** Run no-slops's §0 fingerprint sweep and Tier 1 vocabulary check on each sample. If a sample carries several tells, ask before using it: a profile built from AI-polished text teaches the writer to sound like the model, which is the opposite of the job.
- **Do they have the right to share it, and is the person aware?** Building a profile of someone who doesn't know about it is a line. If the person isn't the user, confirm they've agreed to have their voice captured.

Drop any sample that fails, and tell the user which and why. If fewer than 3 survive, ask for more before going on.

### 3. Analyze
Read every surviving sample in full, then extract, with a short quoted example from the samples for each trait:
- **Core traits:** 4 to 6 named qualities, each with one line on how it shows up on the page
- **Sentence patterns:** typical length and variation, openings, how they use fragments, questions, lists, and punctuation
- **Word choice:** recurring words and phrases, register (formal, casual, profane), jargon they use and jargon they avoid
- **Structure habits:** how they open, how they move between points, how they close
- **Humor and stance:** where it comes from, how often, who it's aimed at
- **What they avoid:** patterns conspicuously absent across every sample
- **Tone spectrum:** how the voice shifts between their formal and informal samples

Quote, don't paraphrase. A profile that says "conversational" with no example is useless.

### 4. Write the profile
Fill `${CLAUDE_PLUGIN_ROOT}/skills/voice-profiles/references/profile-template.md` and save it as `references/<first-last>.md`. Then add the person's row to the Available Voices table with a Menu blurb of 10 words or fewer.

Installed plugins live in a cache that updates overwrite, so tell the user where the profile was written and that it needs to be committed to their own copy of the plugin repo (or kept somewhere persistent and pasted in when needed) to survive the next update.

### 5. Test it
Write a 150-word paragraph in the new voice on a topic none of the samples covered, and ask the user (or the person) whether it sounds like them. Adjust the profile from their notes, not from your own guess about what was off.
