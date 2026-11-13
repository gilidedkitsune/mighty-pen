---
name: aeo-insights
description: >
  Part of the Insights plugin, and dormant until wired: if no AI-visibility source (an MCP
  connector or a local puller) is connected, it says so in one line and does nothing else. Once
  wired, it measures how AI answer engines (ChatGPT, Perplexity, Google AI Overviews, Gemini,
  Claude, Copilot, DeepSeek, Grok) treat your site for a topic: named versus cited, per engine,
  against competitors, before and after a piece ships. Also checks whether a target term is
  winnable before a piece is outlined, and pulls the sub-questions engines actually ran, which
  fresh-ink's search-weave can use as the question tree. Trigger on "are we cited by AI", "AI
  visibility", "share of voice in AI answers", "named vs cited", "is this term winnable", "did
  the AEO work", "measure this page in AI answers". Do not trigger for writing or editing; that's
  search-weave in fresh-ink.
---

# AEO Insights

The measurement half of AEO. fresh-ink's `search-weave` shapes a draft so engines can find, lift, and credit it; this skill tells you whether that's happening, where it's failing, and whether the change worked. Without it, every AEO pass is a guess that never gets graded. With it, you know which page to fix, for which engine, and whether the fix moved the number.

## Dormant until wired (check this first, every time)

Look for an AI-visibility source, in this order:
1. **An AI-visibility MCP connector.** Load its tools with ToolSearch, using the tool vendor's name as the keyword (the server prefix changes between sessions; search by name, never by prefix), then run `list_projects`.
2. **A local REST puller** against the same API, if the user has one set up.

- **Neither is there:** say so in one line ("No AI-visibility source is connected, so I can't measure this") and stop. Don't estimate, don't walk through setup unless asked, and don't block the writing skill that called you: search-weave runs on what the user supplies.
- **Connected:** carry on below. Treat the connector as read-only, always.

## The one number: named versus cited

**Named** is an engine writing your brand or product name in its answer. **Cited** is an engine linking your URL. They move independently, and the gap between them is the whole job. A project named in 6% of tracked answers but cited in 0.4% is the classic pattern: engines know the brand and credit someone else.

**How to pull it.** Over the MCP: read `get_index_schema`, build a filter with `build_lucene_query` scoped to the topic and a 30-day window, then run `search_mentions` (named) and `search_citations` (cited). With a puller: its `topics` view. Name the window on every number.

Connector tools and what they're for (as of September 2026; if they've moved, `list_projects` and `get_index_schema` will orient you):
- `list_projects`, `get_project`: pick the project this content belongs to
- `get_index_schema`, `build_lucene_query`: field names, then a scoped query
- `search_mentions`: named
- `search_citations`: cited
- `search_fanouts`: the sub-questions an engine ran to build its answer, in its own words
- `search_crawler_hits`: which AI crawlers fetched which pages
- `search_sentiment_phrases`, `search_runs`, `generate_report`: sentiment, run history, a rolled-up report

## The diagnosis table

Pull the topic closest to the piece, then read the pair:

| Named | Cited | What it means | What search-weave should work hardest |
|---|---|---|---|
| High | Low | Engines retrieve you and credit someone else. The best target on the board: the page is the only thing failing. | Answer-first sections, the definitional block, receipts, liftable formats |
| Low | Low | A retrieval problem, not a citability problem. Restructuring won't fix it. | The term and the question tree; reconsider the target |
| Low | High | Rare. Narrow authority. Protect it and build around it. | Freshness and cluster links |
| High | High | Working. Leave it and find the next topic. | Nothing |

**Per-engine targeting.** Break the topic down by engine (a model filter on `search_mentions` and `search_citations`) and aim the next pass at the engine you're losing, not the one you already win. A topic might run Perplexity 43%, AI Overviews 15%, ChatGPT 3%: that's a Perplexity-shaped page ChatGPT ignores.

## Three jobs

### 1. Winnability check (before the outline)
Is the target term winnable, and are you already in the answer without credit?
- **Named often, cited rarely:** the highest-value target; retrieval works and only the page fails.
- **Neither named nor cited:** a slower, more expensive bet, often the wrong one.
- **A greenfield term** (nobody owns it in AI answers yet): go for the bare question, "What is X?"
- **An owned term** (an established concept, a competitor's brand, a saturated head query): engines already have their answer. Scope it to the entity: not "What is a message queue?" but "What is the message queue in [Product]?" Only you can answer the scoped question.
Use the competitor view (`search_mentions` and `search_citations` with `search_fanouts` for who else gets pulled in) to see who wins the answer today. Hand search-weave the verdict, the winnable phrasing, and the fanout sub-questions.

### 2. Baseline (before the piece ships)
Topic, named %, cited %, per engine, and the window. search-weave puts this at the top of its report so the target is on record.

### 3. Measure (after the engines re-crawl)
Re-pull the same topic, same filters, after a few weeks. Report named and cited **separately**: only a cited gain means the structure work paid off. Check `search_crawler_hits` first to confirm the engines have actually fetched the new version.

## Reality checks

- **Never fabricate a metric.** An empty pull is reported as empty.
- **Small samples swing.** A tracked prompt set is usually small, so single-window moves are noise. Prefer the trend over any one pull.
- **It measures your configured prompt set,** not the whole internet. Competitor numbers compare fairly with yours on that basis, but they can't support a public "Nth most visible" claim.
- **Never mix tools.** If you switch AI-visibility tools, don't put their numbers in one table or one sentence: different prompt sets aren't comparable, and the gap reads as a collapse when it's only a change of instrument.
- **Read-only.** The keyword and competitor lists are edited with calls that replace the whole list; one careless write wipes the tracking everyone's numbers rest on. Query; never edit.

## One-time setup: the connector (per user, about five minutes)

Only when the user asks to wire it up.
1. **Get an API login** for the project from the tool's account settings (create an API key). Prefer a project-scoped key, and treat it like a password. Prefer a project-scoped key, and treat it like a password: never paste it into chat, a doc, or a skill file.
2. **Add the connector** in Claude: Settings, Connectors, add a custom connector. Server: the vendor's MCP address from its documentation. Auth: whatever the vendor specifies (usually OAuth, with the API key as the client secret). If adding a custom connector isn't offered, a workspace admin may need to allow it.
3. **Confirm** in a new session (an open one won't see the new tools): ToolSearch with the vendor's name, then `list_projects`. If the project is listed, it's wired.

Any AI-visibility tool that reports named and cited data per topic and per engine works the same way; map its calls onto the three jobs above.
