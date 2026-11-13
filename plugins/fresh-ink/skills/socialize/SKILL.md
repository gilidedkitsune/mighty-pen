---
name: socialize
description: >
  The social writing skill: drafts native posts for LinkedIn, X, Threads, Bluesky, Mastodon,
  Reddit, Hacker News, Instagram, TikTok, YouTube Shorts, newsletters, and email, either from
  scratch or by rebuilding a finished piece (blog post, report, essay, webinar, talk, case study)
  for each channel. Every platform has its own reference with formats, limits, what the feed
  rewards right now, and what gets a post ignored. Trigger on "LinkedIn post", "tweet", "X post",
  "thread", "Threads post", "Bluesky", "Reddit post", "Show HN", "caption", "carousel", "Reel
  script", "TikTok script", "socialize this", "repurpose this", "turn this into a post", "cut this
  down for the newsletter", "atomize", or any request for social copy. Drafts only; never
  publishes.
---

# Socialize

Social copy that reads like a person with a point of view wrote it for the place it's posted. Two jobs, one standard:

- **Draft:** a new post (or a few) from a topic, notes, a transcript, or a context dump.
- **Repurpose:** rebuild a finished piece for other channels. Not shrink it: rebuild it. A LinkedIn post that reads like a blog intro with the rest cut off gets scrolled past.

Every feed now punishes the same thing: fluent, polished copy with no stance and nothing only this author could have said. AI help isn't the problem; perspective-free polish is. So the whole skill bends toward one question: **what does this author know, think, or have that nobody else does?**

## Step 1: Pin the brief

Ask only what the request hasn't answered (AskUserQuestion, up to 4 per round):

1. **Platforms** (`multiSelect: true`). Then read only the matching references below.
2. **Whose account.** That sets the voice (Step 2) and whether "I" is allowed.
3. **The author's stake.** A claim, a number, an event, a mistake, or an experience only they have. Without one, stop and ask; there's no post yet, only a topic.
4. **The goal.** Reach, conversation, clicks, signups, or reputation. It decides the closer and where the link goes.

For a repurpose, read the whole source first and write its promise in one sentence (craft Step 1: who it's for, what they walk away with). If you can't, the source isn't finished; say so.

## Step 2: Voice

- **Company account:** tone-and-guidelines in the register the content calls for (usually B2B tech buyer for product content). `${CLAUDE_PLUGIN_ROOT}/skills/tone-and-guidelines/SKILL.md`
- **Taylor's own account:** professional register for career and industry posts, personal for everything else.
- **A named person's account:** their profile from `${CLAUDE_PLUGIN_ROOT}/skills/voice-profiles/SKILL.md`. Offer the roster as a menu (the default voice first, then each profile's Menu blurb). No profile for that person: say so and offer to capture one; never invent a voice.

Then adjust for the platform's own register, which each reference describes. Reddit gets the most casual version of any voice; LinkedIn the most composed.

## Step 3: Find the atoms

List the 5 to 10 strongest standalone units in the source or the user's notes: a number, a quote, a contrarian claim, a short story, a how-to step, a before-and-after, a mistake and what it cost. Each post is built from one to three atoms, never a summary of everything.

Match atoms to platforms: a sharp claim suits X and Threads; a story with a lesson suits LinkedIn; a teardown with receipts suits Reddit and Hacker News; a sequence of steps suits a carousel or a thread; a moment you can show suits short video.

## Step 4: Draft, per platform

Read the reference for each platform before drafting for it:

| Platform | Reference |
|---|---|
| LinkedIn (posts, document carousels, polls) | `${CLAUDE_PLUGIN_ROOT}/skills/socialize/references/linkedin.md` |
| X (posts, threads, replies, quote posts) | `${CLAUDE_PLUGIN_ROOT}/skills/socialize/references/x.md` |
| Threads, Bluesky, Mastodon | `${CLAUDE_PLUGIN_ROOT}/skills/socialize/references/threads-bluesky-mastodon.md` |
| Reddit, Hacker News | `${CLAUDE_PLUGIN_ROOT}/skills/socialize/references/reddit-hn.md` |
| Instagram, TikTok, YouTube Shorts (captions, carousels, video scripts) | `${CLAUDE_PLUGIN_ROOT}/skills/socialize/references/instagram-tiktok-shorts.md` |
| Newsletter section, promotional or nurture email | `${CLAUDE_PLUGIN_ROOT}/skills/socialize/references/newsletter-email.md` |
| Character limits, truncation points, hashtag caps | `${CLAUDE_PLUGIN_ROOT}/skills/socialize/references/platform-limits.md` |

**The hook.** Write at least five first lines for the main post, each from a different angle (specific result, contrarian claim, story in motion, before-and-after, a question in the reader's own words), and keep the strongest. Fill every pattern with the author's real material; a hook formula with nothing specific in it is a tell. For headline-shaped first lines (Threads, a Show HN title, a Reel's on-screen text), `${CLAUDE_PLUGIN_ROOT}/skills/headline-lab/SKILL.md` scores the options.

**The body.** What it is, a concrete example, why now, what the reader can do with it. One concrete detail per abstract claim.

**The closer.** End on the point, a consequence, or a specific question you'd actually want answered. Never a request for engagement.

## Rules for every post

- **Facts stay facts.** Every stat carries its source, or it's cut. Never round up, drop a qualifier, or turn a finding into a bigger claim to make it punchier. On a repurpose, nothing gets claimed that the source doesn't support; anything new goes to cited-works first.
- **No invented experience.** Never write a first-person story, result, or feeling the author didn't give you. Ask.
- **Native, not truncated.** Each post makes sense to someone who never clicks through.
- **A different lead per platform**, so a follower who sees the author everywhere doesn't read the same post four times.
- **Links cost reach** on most feeds right now (each reference says how much and what to do). Put substance first; the link goes last, in a reply, or nowhere, depending on the goal.
- **Hashtags** only where the platform still uses them, and only if the author does.
- **Disclosure.** Sponsored or paid posts get a clear disclosure. If a post is substantially AI-written and goes out unedited on a matter of public interest (politics, health, economics) to an EU audience, it needs either a named human editor who takes responsibility or an AI label; say which applies.

## Social tells (kill on sight)

These are on top of no-slops's rulebook (`${CLAUDE_PLUGIN_ROOT}/skills/no-slops/SKILL.md`), which runs on every post:

- **Broetry:** one short sentence per line, every line, for the whole post. Write paragraphs; break lines where a person would pause.
- **Engagement bait:** "Agree?" "Thoughts?" "Let that sink in." "Read that again." "Comment GUIDE and I'll DM you." These now cost reach, and the X ranker models predicted mutes and "not interested" as negatives.
- **Manufactured vulnerability:** "I'll be honest, I was terrified..." with no real story behind it.
- **Emoji bullets:** 🚀 ✅ 💡 leading every line.
- **Hook with nothing in it:** "Unpopular opinion:" followed by a popular opinion; "Here's what nobody tells you" followed by what everybody tells you.
- **Thread theater:** "🧵", "A thread:", "1/" numbering on posts that aren't a list.
- **Contrast reveals and colon reveals:** "It's not X, it's Y." "The result? 3x faster." State the thing.

## Step 5: Check and present

1. Run no-slops's mechanical checks on every post (§0 fingerprints, Tier 1 vocabulary, banned phrases, em dashes, adverbs). Short copy ships most often, which makes it the main leak.
2. Check each post against its platform's character limit and truncation point.
3. Present each post under a platform heading, in a plain code block so line breaks paste cleanly, with: character or word count, the account it's for, the atom it's built on, and where the link goes. Then one line on why the chosen hook wins, and the runner-up hooks.
4. Offer: alternate hooks, a posting sequence (which goes first and the spacing between them), or a version in a different voice.

**Drafts only.** If the user has a scheduling tool connected, offer to create the posts there as drafts. Never publish, schedule, or send without an explicit go-ahead for that specific post.

## Keeping this current

Platform mechanics change monthly. Each reference has a **Last checked** date and tags every mechanic by confidence: **[platform]** for the platform's own statement or published code, **[study]** for third-party data with a stated sample, **[reported]** for a single or vendor source. Lean on [platform] rules; treat [reported] numbers as direction, not fact. If a reference is more than three months past its date, say so and offer to re-check it with cited-works before relying on its numbers. Where this research came from: `${CLAUDE_PLUGIN_ROOT}/skills/socialize/references/sources.md`.
