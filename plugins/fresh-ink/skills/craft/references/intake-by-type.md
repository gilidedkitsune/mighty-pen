# Intake by content type

Questions to ask for each content type, used in craft Step 1. Open only the block for the type you've detected. Choose the two that matter most for Round 1, which go into the same AskUserQuestion call as the mode and audience questions. Carry the rest into Round 2. Drop any question the brief already answers.

If a block points to a template in `content-formats`, that template's pre-draft checklist counts as part of the intake for that type.

---

**Blog:** routed to `blog`, which runs its own intake. Don't repeat it here.

**Customer story:**
- Work through the pre-draft checklist in `${CLAUDE_PLUGIN_ROOT}/skills/content-formats/references/customer-story-template.md`
- The customer, their company, what they built, what was broken before, and the measurable result
- Materials available: an interview transcript, quotes, screenshots, data

**Social:** routed to `socialize`, which runs its own brief (platforms, the account, the author's stake, the goal).

**Email:**
- The kind of email: announcement, nurture, transactional, or a sequence
- A subject line direction, if one is already in mind
- The one action the reader should take

**Website copy:**
- The page type. General web copy covers homepages, feature, pricing, solution, persona, and industry pages. Single-use landing pages cover campaigns, ads, and events.
- The primary action

Then the follow-ups for that page type:
- **General web copy:** the page's main job, the kind of page, and the differentiators or messages it has to land.
- **Single-use landing page:** the traffic source (paid, email, social, event), what the referring content promised, and the one conversion goal.

**Long-form** (whitepaper, ebook, guide, survey or research report):
- The topic and the thesis
- Target length, roughly 2,000 to 5,000 words or more
- The chapter or section plan, if the user has one
- Sources and citation limits. The format is fixed: Chicago superscripts with a Works Cited list, per tone-and-guidelines.
- For a research report, also: the data source (spreadsheet, survey tool, raw files), the findings to foreground, and which tables or charts should be described

**Ad copy:**
- Platform and format (search, paid social, professional network, display)
- Character limits
- The target reader, since it drives how many variants to produce
- The key message or offer
- The landing page URL, so the ad and the page match

**Executive summary or one-pager:**
- Format: an executive summary (one or two pages, condensing a source document) or a one-pager (a single standalone page)
- The source document or subject, and what it should accomplish
- The decisions, recommendations, or must-include points
- Where it will be used: a sales leave-behind, a conference handout, an email attachment

**Byline or thought piece:**
- The named author and their perspective or voice
- The target publication, if any
- The core argument or thesis

**Webinar:**
- Work through the event-details section of `${CLAUDE_PLUGIN_ROOT}/skills/content-formats/references/webinar-bom-template.md` first
- Title, date and time, format, platform, and speakers
- Partner details, if it's co-hosted
- The target reader and funnel stage
- Which assets are needed from the checklist: landing page, emails, social, slides, recap
- Voice: the default voice, except social posts that go out under a named person's account (Webinar-specific, craft Step 4)

**Sales enablement:**
- Work through the matching asset checklist in `${CLAUDE_PLUGIN_ROOT}/skills/content-formats/references/sales-enablement-template.md`
- Which asset: battle card, objection handler, or one-sheet
- The target buyer
- The objections or the competitive position to address

**Creator brief:**
- Work through the pre-brief checklist in `${CLAUDE_PLUGIN_ROOT}/skills/content-formats/references/creator-brief-template.md`
- The kind of creator: influencer, content partner, or agency
- The deliverables
- The key messages and the guardrails

**Career documents** (cover letter, resume, bio, LinkedIn About):
- Build the proof bank first, using `${CLAUDE_PLUGIN_ROOT}/skills/content-formats/references/career-docs-template.md`
- Which documents, and for what target: paste the job description, or name the venue or audience
- Source material: the current resume, past bios, portfolio links, LinkedIn
- What to emphasize, what to leave out, and any requirement they know they don't meet

**Pitch** (op-ed, guest post, story):
- The pitch section of the career-docs template
- The target outlet and, if known, the editor
- The argument in one sentence, and why it matters now
- Clips to link, and whether a draft exists

**Personal essay:**
- Where it will run (a newsletter, a publication, their own site) and the target length
- The moment or scene at the center
- What the reader should feel or understand by the end. The emotional truth, not a lesson.
- What's off limits: people who shouldn't be named, details that stay private
