---
name: content-formats
description: >
  Structural templates and asset specs for content types that have a fixed shape: customer stories / case studies, webinars (full bill of materials), sales enablement assets (battle cards, objection handlers, competitive one-sheets), creator briefs, career documents (cover letters, resume bullets, bios, LinkedIn About, editor pitches), plus an answer-first document scaffold (Minto/SCQA) for executive summaries, 1-pagers, bylines, and sales arguments. This skill owns FORMAT and STRUCTURE, not writing craft, and is the single source of truth for "what sections or assets does this content type need." It is loaded by craft during the matching content-type workflow. Do NOT use this skill to write or create content. It only supplies the structural skeleton. All content creation, including for these types, goes through craft, which loads these templates itself. For HOW to write (voice, persuasion, quality), see craft: this skill defines the shape, that one fills it with great copy.
---

# Content Formats

Structural scaffolding for the content types that have a defined shape. Writing craft lives in `craft`; asset shape lives here. When a content-type workflow needs a structure, load the matching reference file below and work through its checklist. Voice, tone, persuasion, and the quality bar get applied on top, from craft.

| Content type | Scaffold | What it defines |
|---|---|---|
| Customer story / case study | [references/customer-story-template.md](references/customer-story-template.md) | Pre-draft checklist, the 9-section narrative structure, interview question bank, tone reminders |
| Webinar | [references/webinar-bom-template.md](references/webinar-bom-template.md) | Full bill of materials, event details, asset checklist, optional export to a connected team wiki or calendar, timeline |
| Sales enablement | [references/sales-enablement-template.md](references/sales-enablement-template.md) | Battle card, objection handler, and competitive one-sheet formats with worked examples |
| Creator brief | [references/creator-brief-template.md](references/creator-brief-template.md) | The 9-section brief: objective, audience, key messages, deliverables, guardrails, timeline |
| Career docs and pitches | [references/career-docs-template.md](references/career-docs-template.md) | The truth gate and proof bank, then cover letter, resume bullet, three-length bio, LinkedIn About, and editor-pitch specs |
| Exec summary / 1-pager / byline / sales argument | [references/minto-scaffold.md](references/minto-scaffold.md) | Answer-first document skeleton: governing thesis, SCQA lead, MECE supporting arguments, integrity check |

These scaffolds carry structure plus any content-type-specific reminders. They do not define brand voice, tone of voice, or persuasion strategy: those come from `craft` and its sources (`tone-and-guidelines`, `voice-profiles`).
