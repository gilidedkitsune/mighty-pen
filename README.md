# Mighty Pen

Three Claude Code plugins for written content. One researches, one writes, one edits. Install all three and they form a find-then-make-then-fix workflow.

- **cited-works** researches: stats, quotes, and sources traced to their primary origin, with a do-not-cite trap list and ready-to-use citations.
- **fresh-ink** writes the draft (11 skills behind one routing spine).
- **red-pen** edits the draft (verdict-first review, then quick-fix or full report; developmental and proofread-only modes too).

## Install (one time)

In Claude Code, add this marketplace, then install all three plugins:

```
/plugin marketplace add gilidedkitsune/mighty-pen
/plugin install cited-works@mighty-pen
/plugin install fresh-ink@mighty-pen
/plugin install red-pen@mighty-pen
```

You will be asked to trust the marketplace the first time. After that you are set.

> This repo is public, so no invite or GitHub sign-in is needed to add the marketplace.

## How to use them

The skills **trigger automatically** when you describe a task, so most of the time you just talk:

- "Find stats for this piece" or "what's the competitive landscape" starts cited-works.
- "Draft a customer story about a team that shipped in a weekend" starts fresh-ink.
- "Edit this" with a pasted draft starts red-pen. "Proofread this" or "developmental edit" picks its other modes.
- "Fact-check this draft" starts cited-works' verify job.
- "Give me headline options" starts headline-lab. "Write a LinkedIn post about this" or "turn this into a thread" starts socialize.
- "Build a voice profile from these samples" starts voice-profiles' capture routine.

To call one explicitly, plugin skills are namespaced `plugin:skill`:

```
/cited-works:cited-works             # research a claim, a stat, a landscape
/fresh-ink:quill     # start a piece
/red-pen:red-pen                     # edit a piece
```

### The find-make-fix flow

1. **Research** in cited-works, when a piece needs real stats, quotes, or a competitive landscape, not vibes. Every finding is traced to its primary source, dated, checked against the trap list, and handed back as a stat card ready to paste. fresh-ink hands its sourcing needs here by name, so there's one sourcing standard, not five.
2. **Draft** in fresh-ink. It picks the workflow for your content type and the voice register that goes with it (personal, professional, or B2B tech buyer; or a specific person's, from voice-profiles), asks who it's for, pulls live SEO/GEO data when the piece needs it, and treats no-slops's rules as drafting constraints from the first sentence, not a cleanup pass.
3. **Sharpen** with the edit menu, structure first and sentences last: the no-slops gate, then whichever the piece needs (the Schwartz re-angle, the Ogilvy pass for persuasion, aeo-craft for citability on anything bound for publication), then red-pen's copyedit, then a final no-slops sweep. red-pen flags unverified claims and hands them back to cited-works to verify.
4. **Loop** as needed. A structural rewrite goes back to fresh-ink (or red-pen's developmental mode first); line-level polish stays in red-pen; a thin or stale source goes back to cited-works.

> **Using red-pen on its own?** It catches the slop that survives a cleaning and flags heavy clusters, but the full AI-tell filter and 35/50 rubric live in no-slops, which ships in fresh-ink. Without fresh-ink installed, red-pen's slop pass is the lighter one. Install both for the full check.

## What is in fresh-ink

quill is the front door; it loads the others only when a job needs them.

| Skill | Job |
|---|---|
| quill | The writer and routing spine |
| tone-and-guidelines | The default voice in three registers (personal; professional for cover letters, bios, and pitches; B2B tech buyer for product and sales content), plus editorial rules and writing tips |
| voice-profiles | Voice profiles for writing as a specific person, plus a capture routine that builds one from 3 to 5 samples (with an authorship check) |
| content-formats | Templates for fixed-shape content (customer story, webinar, sales enablement, creator brief, and career docs: cover letter, resume bullets, bio, LinkedIn About, editor pitch) |
| blog | The blog content-type default: write, brief, optimize, outrank a competitor |
| ogilvy-copywriting | Persuasion principles, plus an optional voice |
| no-slops | The AI-tells filter and the 35/50 gate, applied as drafting constraints |
| aeo-craft | The citability sculpt for published work: gets a draft found, extracted, and cited by AI answer engines |
| seo-geo | Live SEO/GEO data and tooling (setup below) |
| headline-lab | About 10 headline variants on different angles, scored against Ogilvy and aeo-craft winnability |
| socialize | Social posts from scratch or rebuilt from a finished piece, with one reference per platform: LinkedIn, X, Threads, Bluesky, Mastodon, Reddit, Hacker News, Instagram, TikTok, Shorts, newsletter, email |

There's no persona library anymore: quill asks who a piece is for directly (role, seniority, what they already know) instead of picking from a ranked list.

## seo-geo setup (per person)

seo-geo reads your site's real Google Analytics and Search Console numbers using **your own** Google sign-in. Credentials live in `~/.config/claude-seo/` on your machine and are never stored in this repo; the GA4 property and Search Console domain it targets come from a `config.json` you set up, not a baked-in default. The first time you use it, follow the setup steps inside the skill.

## cited-works setup (per person)

cited-works points at your own research libraries so verified finds and known-bad stats compound over time instead of getting re-researched every run. It ships with five placeholders left blank in `cited-works/SKILL.md`; fill each in with wherever that material lives for you (a Notion page, a Google Doc, a folder, a URL, it doesn't matter):

| Placeholder | What to put there |
|---|---|
| `[VERIFIED SOURCE LIBRARY]` | Where you keep stats you've already traced to origin |
| `[TRAP LIST LOCATION]` | Your Do Not Cite list of known-bad stats (can live inside the library) |
| `[RESEARCH HUB]` | Where finished research reports get filed |
| `[YOUR COMPETITIVE SET]` | The companies to track by default for market intel |
| `[YOUR DOCS LOCATION]` | Where exported documents should be saved |

Starting from nothing is fine: create two empty pages, a source library and a research hub, and let them fill up. The skill offers to deposit verified finds and newly discovered traps every time it runs.

## Getting updates

When a new version is pushed, you receive it automatically on next launch, or pull it now:

```
/plugin update cited-works@mighty-pen
/plugin update fresh-ink@mighty-pen
/plugin update red-pen@mighty-pen
```

## For the maintainer

The plugin copies are **generated** from the live skills in `~/.claude/skills/` by `build.py`, which rewrites every cross-skill path to the `${CLAUDE_PLUGIN_ROOT}` form that installed plugins require. The live skills stay the single source of truth. To ship an update:

1. Edit the skills in `~/.claude/skills/` as usual.
2. Regenerate with a bumped version: `python3 build.py 1.1.0`
3. Commit and push (or publish from GitHub Desktop).

Bumping the version is what triggers teammates' updates. Pushing new commits without a version bump will not deliver changes.

This marketplace is the **only** distribution channel. The claude.ai Shared Skills library was retired (Jul 2026): uploads there went stale between deploys and duplicate copies hijacked skill routing in desktop sessions. Don't re-upload skills to it; point people here.
