# Mighty Pen

Three Claude Code plugins for written content, plus an optional fourth for data. One researches, one writes, one edits. Install the three and they form a find-then-make-then-fix workflow; add Insights if you have analytics to connect.

- **cited-works** researches: stats, quotes, and sources traced to their primary origin, with a do-not-cite trap list and ready-to-use citations.
- **fresh-ink** writes the draft (10 skills behind one routing spine).
- **red-pen** edits the draft (verdict-first review, then quick-fix or full report; developmental and proofread-only modes too).
- **insights** (optional) measures: live GA4 and Search Console numbers and AI-answer visibility. Dormant until you wire it up; without a connection it says so in one line and stays out of the way.

## Plugins and skills at a glance

| Plugin | Role | Skills |
|---|---|---|
| **cited-works** | Find: research and fact-checking | cited-works |
| **fresh-ink** | Make: writing | craft, tone-and-guidelines, voice-profiles, content-formats, blog, ogilvy-copywriting, no-slops, search-weave, headline-lab, socialize |
| **red-pen** | Fix: editing | red-pen |
| **insights** (optional) | Measure: data, dormant until wired | seo-geo, aeo-insights |

## Install (one time)

In Claude Code, add this marketplace, then install the three core plugins:

```
/plugin marketplace add gilidedkitsune/mighty-pen
/plugin install cited-works@mighty-pen
/plugin install fresh-ink@mighty-pen
/plugin install red-pen@mighty-pen
```

Optional, if you'll connect GA4, Search Console, or an AI-visibility tool:

```
/plugin install insights@mighty-pen
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
- "Work these keywords into the post" or "AEO pass" starts search-weave.
- "How's our search traffic" or "are we cited by AI" starts Insights' seo-geo or aeo-insights, if it's installed and wired.

To call one explicitly, plugin skills are namespaced `plugin:skill`:

```
/cited-works:cited-works      # research a claim, a stat, a landscape; fact-check a draft
/fresh-ink:craft              # start any piece (it routes to the right skill)
/fresh-ink:blog               # blog post, brief, optimize, or outrank
/fresh-ink:socialize          # social posts, or repurpose a finished piece
/fresh-ink:headline-lab       # headline or subject-line options, scored
/fresh-ink:search-weave       # SEO and AEO pass on a finished draft
/fresh-ink:voice-profiles     # build or use a voice profile
/red-pen:red-pen              # edit, proofread, or developmental edit
/insights:seo-geo             # GA4 and Search Console numbers (if wired)
/insights:aeo-insights        # AI-answer visibility (if wired)
```

### The find-make-fix flow

1. **Research** in cited-works, when a piece needs real stats, quotes, or a competitive landscape, not vibes. Every finding is traced to its primary source, dated, checked against the trap list, and handed back as a stat card ready to paste. fresh-ink hands its sourcing needs here by name, so there's one sourcing standard, not five.
2. **Draft** in fresh-ink. It picks the workflow for your content type and the voice register that goes with it (personal, professional, or B2B tech buyer; or a specific person's, from voice-profiles), asks who it's for, uses the keywords and sources you give it (or Insights' data, if that's installed and wired), and treats no-slops's rules as drafting constraints from the first sentence, not a cleanup pass.
3. **Sharpen** with the edit menu, structure first and sentences last: the no-slops gate, then whichever the piece needs (the Schwartz re-angle, the Ogilvy pass for persuasion, search-weave to work target keywords, questions, and citations into anything bound for publication), then red-pen's copyedit, then a final no-slops sweep. red-pen flags unverified claims and hands them back to cited-works to verify.
4. **Loop** as needed. A structural rewrite goes back to fresh-ink (or red-pen's developmental mode first); line-level polish stays in red-pen; a thin or stale source goes back to cited-works.

> **Using red-pen on its own?** It catches the slop that survives a cleaning and flags heavy clusters, but the full AI-tell filter and 35/50 rubric live in no-slops, which ships in fresh-ink. Without fresh-ink installed, red-pen's slop pass is the lighter one. Install both for the full check.

## What is in fresh-ink

craft is the front door; it loads the others only when a job needs them.

| Skill | Job |
|---|---|
| craft | The writer and routing spine |
| tone-and-guidelines | The default voice in three registers (personal; professional for cover letters, bios, and pitches; B2B tech buyer for product and sales content), plus editorial rules and writing tips |
| voice-profiles | Voice profiles for writing as a specific person, plus a capture routine that builds one from 3 to 5 samples (with an authorship check) |
| content-formats | Templates for fixed-shape content (customer story, webinar, sales enablement, creator brief, and career docs: cover letter, resume bullets, bio, LinkedIn About, editor pitch) |
| blog | The blog content-type default: write, brief, optimize, outrank a competitor |
| ogilvy-copywriting | Persuasion principles, plus an optional voice |
| no-slops | The AI-tells filter and the 35/50 gate, applied as drafting constraints |
| search-weave | The SEO and AEO structural pass: give it target keywords, questions, and citations, and it weaves them into the copy so it ranks and AI engines can lift and credit it. No data connection needed |
| headline-lab | About 10 headline variants on different angles, scored against Ogilvy and search-weave's term winnability |
| socialize | Social posts from scratch or rebuilt from a finished piece, with one reference per platform: LinkedIn, X, Threads, Bluesky, Mastodon, Reddit, Hacker News, Instagram, TikTok, Shorts, newsletter, email |

There's no persona library anymore: craft asks who a piece is for directly (role, seniority, what they already know) instead of picking from a ranked list.

## What is in insights (optional)

| Skill | Job |
|---|---|
| seo-geo | Your site's real GA4 and Search Console numbers, plus the map of which SEO tools to run at each stage |
| aeo-insights | AI-answer visibility: named versus cited, per engine, term winnability, and before-and-after measurement (needs a Cairrot connector or similar) |

Both are **dormant until wired**. Each one checks for its connection first; if it isn't there, it says so in one line and stops, and fresh-ink carries on with whatever keywords and citations you supplied. When they are wired, search-weave can pull its inputs from them instead of asking you.

**Setup (per person, only if you want the data):** seo-geo reads GA4 and Search Console through **your own** Google sign-in; credentials live in `~/.config/claude-seo/` on your machine and never in this repo, and the property and domain come from a `config.json` you create. aeo-insights needs an AI-visibility connector added in Claude's settings. Ask either skill to "set it up" and it walks you through the steps.

## cited-works setup (per person)

Nothing to configure. cited-works isn't wired to any tool: the first time a job needs a place to read from or file to, it asks, for example "Where do you want to store this research hub?" Answer with a link, a folder path, "create one," or "nowhere yet" and it uses that for the rest of the session. It asks about five things, and only when a job touches them:

| It asks about | Used for |
|---|---|
| Research hub | Filing finished reports and checking for prior research |
| Verified source library | Stats you've already traced to origin |
| Do Not Cite list | Known-bad stats to never use (can live inside the library) |
| Competitive set | The companies to track by default for market intel |
| Export location | Where documents get saved |

To skip the questions in future sessions, let it save your answers to your CLAUDE.md (it offers once), or write them there yourself. Starting from nothing is fine: the libraries fill up as you go, because the skill offers to deposit verified finds and newly discovered traps every time it runs.

## Credits and licenses

Outside sources, their licenses, and what each one contributed are listed in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). That includes the concreteness word norms used by red-pen (a research dataset whose header says "research use"), and the MIT-licensed skills whose structure and ideas informed socialize and no-slops. The Wikipedia-derived AI-tell catalog in no-slops is CC BY-SA, which carries share-alike terms.

## Getting updates

When a new version is pushed, you receive it automatically on next launch, or pull it now:

```
/plugin update cited-works@mighty-pen
/plugin update fresh-ink@mighty-pen
/plugin update red-pen@mighty-pen
/plugin update insights@mighty-pen     # if installed
```

## For the maintainer

The plugin copies are **generated** from the live skills in `~/.claude/skills/` by `build.py`, which rewrites every cross-skill path to the `${CLAUDE_PLUGIN_ROOT}` form that installed plugins require. The live skills stay the single source of truth. To ship an update:

1. Edit the skills in `~/.claude/skills/` as usual.
2. Regenerate with a bumped version, higher than the current one: `python3 build.py 2.8.0`
3. Commit and push (or publish from GitHub Desktop).

Bumping the version is what triggers teammates' updates. Pushing new commits without a version bump will not deliver changes.

This marketplace is the **only** distribution channel. The claude.ai Shared Skills library was retired (Jul 2026): uploads there went stale between deploys and duplicate copies hijacked skill routing in desktop sessions. Don't re-upload skills to it; point people here.
