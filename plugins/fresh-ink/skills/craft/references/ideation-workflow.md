# Content ideation workflow

Research and strategy only, with no drafting. The output is a prioritized list of content ideas, each one backed by data, competitor context, and audience insight.

craft loads this when a request routes to **Ideation** ("brainstorm," "content ideas," "what should we write," "topic ideas," "content plan"). The promise module in craft Step 1 still runs first. Even an ideation session names who the work is for and what it's meant to do before it generates anything.

---

## Intake

Ask in one AskUserQuestion round:

1. **Goal:** organic traffic, AI citation visibility, leads, thought leadership, product education, or competitive positioning.
2. **Scope:** a single topic in depth, a full calendar, a specific gap, or a brainstorm around a theme.
3. **Constraints:** the audience, any keywords already chosen, competitors to watch, the buyer stage to focus on, and a timeline.

## Trend scan

Before the research pass, run WebSearch on recent coverage of AI, AI app building, AI coding, and "vibe coding." Check the major tech and business press, plus developer surveys and the Hacker News front page.

Condense the results into **five trending topics**. For each one, give:
- **Topic:** a one-line description.
- **Why now:** the news or cultural moment driving it.
- **Sources:** which publications covered it, with links where possible.
- **Angle for us:** how it connects to something this subject could credibly write about.

Show the five to the user before continuing. They're context for the conversation, not commitments. The user may build on one, ignore them all, or use them as background for something else.

## Research pass

Run a focused SEO and GEO pass so the ideas rest on evidence, and weave the findings into the conversation rather than dumping a report. Without data tools, that means the trend scan plus whatever keywords, queries, or performance numbers the user can share. If the Insights plugin is installed and wired, its `seo-geo` skill supplies the tool sequence and the site's real numbers, and `aeo-insights` supplies AI-answer visibility. Delegate there instead of repeating that here.

The useful order for ideation: content strategy and pillars first, then keyword and SERP research, then competitor and gap analysis, then topic clustering, then the site's own traffic numbers where they sharpen the angle. Offer deeper passes from Insights' map, where it's installed, based on the goal.

Run only the steps whose data source is connected. For anything else, ask the user for the data rather than inventing volumes, difficulty, or rankings. The trend scan and the strategy steps work with no data source at all.

## Schwartz pass on each idea

After research and before the final list, run each strong idea through a quick Schwartz diagnosis. This shows how the piece should open, not only what it covers.

For each top idea, answer:
1. **Reader awareness:** where the target reader stands (unaware through most aware).
2. **Market sophistication:** how crowded the conversation is (stages 1 to 5).
3. **Messaging implication:** what the headline and lead need to do at that intersection. For example, "problem-aware and stage 3 means lead with the mechanism, not the promise."

Work this into each idea as one or two sentences. Don't build a table. The idea description should tell the user how to write the piece, not only what to write. The grid is in `${CLAUDE_PLUGIN_ROOT}/skills/craft/references/schwartz-5x5-matrix.md`. Flag unusual intersections, such as unaware and stage 5, because those need longer copy and a different approach.

## Output

Present a prioritized list. For each idea:
- **Working title and target keyword(s)**, with volume and difficulty if a data source supplied them
- **Content type:** blog, landing page, comparison page, long-form, and so on
- **Buyer stage:** awareness, consideration, or decision
- **Messaging angle:** the Schwartz-informed direction for the headline and lead, in one or two sentences
- **Why this one:** the data point or gap that justifies it
- **Effort:** light, medium, or heavy
- **AI citation opportunity:** grounded in an aeo-insights pull, with its window stated. If that isn't available, mark it "not grounded" rather than guessing.

Order by impact: quick wins first, then strategic investments, then long-tail topics.

## Handoff

After the user picks, offer to start the full writing workflow on that topic. Use the content type's standard path (Full, Medium, Light, or Template). The Schwartz pass carries forward, so don't repeat it unless the audience changes. If the user wants a brief before writing, the blog skill's brief workflow covers it.
