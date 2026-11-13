# Webinar Bill of Materials (BOM) Template

A production checklist and content template for webinars. Covers everything from planning through post-event content. Work through each section in order; skip what doesn't apply.

---

## Export the finished BOM (optional)

By default the finished package (all drafted assets plus the run of show) exports like any other piece: a `.docx` through craft's Step 6. If the user keeps a team wiki or an editorial calendar and it's connected to the session, offer to file it there instead. Never assume either exists; ask which one, if any.

### Option A: a team wiki page (Notion, Confluence, or similar)

One page per webinar, filed under whatever parent page the user names (for example, a Webinar Hub).

- **Title:** the webinar title (append the date if the title alone is ambiguous)
- **Content:** the filled-in BOM below. Use the wiki's collapsible sections for the Content Review Checklist, Partner Details, and SEO & GEO; checkboxes for checklist items; tables for the content BOM tracker and the run-of-show timeline.
- For Notion, fetch its enhanced-markdown spec resource (`notion://docs/enhanced-markdown-spec`) before building the page so the syntax renders.
- Confirm with the user before creating; return the new page URL when done.

### Option B: an editorial calendar entry

If the user tracks content in a calendar tool and it's connected (through its own connector or a database connector), log the webinar there.

- Ask which workspace or project it belongs to, then confirm exactly what you're about to create.
- Fields to fill, mapped to whatever the tool calls them: title, content type (Webinar), status, channel, due or publish date (the webinar date), owner, and a one-line description **with the wiki page URL from Option A**, if there is one, so the entry and the doc stay connected.
- Optionally offer one entry per major asset (landing page, email invite, social, recap) instead of a single entry.
- If the tool is a database, check the current columns before writing (a `SELECT ... LIMIT 1` or equivalent), and confirm with the user before any write.

---

## Event details

Fill these in first. Everything else flows from them.

- **Webinar title:**
- **Date and time:** (include timezone)
- **Duration:** (default: 45 min + 15 min Q&A)
- **Format:** (live demo, panel, fireside chat, workshop, AMA)
- **Platform:** (Luma, Zoom, StreamYard, etc.)
- **Recording plan:** (live only, recorded for replay, both)

### Speakers and roles

| Role | Name | Company | Bio needed? | Headshot needed? |
|------|------|---------|-------------|-----------------|
| Host / moderator | | | | |
| Speaker 1 | | | | |
| Speaker 2 | | | | |
| Guest / partner | | | | |

### Partner details

If co-hosted or co-marketed with a partner:

- **Partner company:**
- **Co-marketing goals:** (what both sides want out of this)
- **Partner goals:** (what the partner specifically needs: leads, brand exposure, product demo)
- **Partner deliverables:** (what they're providing: speaker, audience, promotion, content)
- **Approval process:** (who signs off on what, and by when)

---

## Audience and positioning

- **Target audience:** (ask directly: role, seniority, and what they already know. There is no general-reader option; a broad webinar still names a specific reader.)
- **Funnel stage:** (TOFU / MOFU / BOFU)
- **Campaign type:** (thought leadership, product education, customer showcase, partner co-marketing)
- **What the audience gets out of it:** (be specific: not "learn about AI" but "see how to build a working site in 30 minutes")
- **Why they should care enough to register:** (the hook: what makes this worth an hour of their day)

---

## Content BOM

Every webinar generates multiple content assets. Check off what's needed and track status. Date fields are blank by default; fill in as dates are confirmed.

### Pre-event content

| Asset | Owner | Due date | Status | Notes |
|-------|-------|----------|--------|-------|
| Landing page / Luma description | | | | |
| Registration confirmation email | | | | |
| Reminder email (24 hours before) | | | | |
| Reminder email (1 hour before) | | | | |
| Email invite to existing list | | | | |
| Social: [Speaker] LinkedIn announcement | | | | |
| Social: [Speaker] X announcement | | | | |
| Social: Brand LinkedIn announcement | | | | |
| Social: Brand X announcement | | | | |
| Social: LinkedIn reminder (day of) | | | | |
| Social: X reminder (day of) | | | | |
| Partner cross-promotion posts | | | | |
| Slide deck / visual assets | | | | |
| Speaker prep doc / talking points | | | | |
| Demo script (if live demo) | | | | |

### Day-of content

| Asset | Owner | Due date | Status | Notes |
|-------|-------|----------|--------|-------|
| Opening script / host intro | | | | |
| Q&A moderation plan | | | | |
| Live social posts during event | | | | |
| CTA slide / closing offer | | | | |

### Post-event content

| Asset | Owner | Due date | Status | Notes |
|-------|-------|----------|--------|-------|
| Recording upload and hosting | | | | |
| Follow-up email (attendees) | | | | |
| Follow-up email (no-shows + recording link) | | | | |
| Social: [Speaker] recap (LinkedIn) | | | | |
| Social: [Speaker] recap (X) | | | | |
| Social: Brand recap (LinkedIn) | | | | |
| Social: Brand recap (X) | | | | |
| Blog recap or writeup | | | | |
| Short video clips from recording | | | | |
| Quote cards from speakers | | | | |
| Slide deck share (if applicable) | | | | |

---

## Copy templates

### Landing page / Luma description

Structure:
1. **Hook**: one sentence on why this matters right now
2. **What you'll learn**: three to four bullet points, outcome-oriented
3. **Who this is for**: one sentence targeting the persona
4. **Speaker bios**: two to three sentences each, credibility-focused
5. **CTA**: register button with specific language ("Save your spot" not "Submit")

### Email invite

- **Subject line:** specific and benefit-led. No "Join us for a webinar." Say what they'll get.
- **Body:** hook → what they'll learn (bullets) → speaker credibility → date/time → CTA
- **CTA:** single, clear ("Register now" or "Save your spot")

### Reminder emails

- **24-hour reminder:** restate the hook + logistics (date, time, link). Keep it short.
- **1-hour reminder:** just the link and a one-liner. "Starting in an hour. Here's your link."

### Follow-up emails

- **Attendees:** thank you → key takeaway → recording link → CTA (try the product, book a demo, etc.)
- **No-shows:** no guilt trip. "Here's what you missed" → recording link → same CTA

---

## Social promotion

### Voice

Voice rules for webinar content live in craft's Webinar-specific section: the default voice for everything, with one exception for social posts that go out under a named person's account (drafted by socialize in that person's profile).

### LinkedIn posts

Draft three posts minimum per account ([Speaker] + brand):
1. **Announcement** (one to two weeks before): what the webinar covers and why it matters
2. **Reminder** (day of or day before): shorter, urgency-focused, link to register
3. **Recap** (day after): key takeaway, link to recording

Target 800-1,300 characters. Professional with a sense of humor.

### X posts

Draft three posts minimum per account ([Speaker] + brand):
1. **Announcement**: hook + link. Target ~250 characters.
2. **Day-of reminder**: "Starting in [time]" + link
3. **Recap / highlight**: one standout moment or quote + link to recording

Brevity first. More room for personality than LinkedIn.

---

## SEO and GEO

If the webinar generates a blog recap or landing page that will be published:

### SEO
- **Primary keyword:**
- **Secondary keywords:**
- **Search intent:** (informational / navigational / commercial / transactional)
- **Target SERP feature:** (featured snippet / people also ask / image pack / etc.)
- **Slug / URL:**
- **Meta title:**
- **Meta description:**
- **Internal links to include:**
- **External references:**

### GEO (Generative Engine Optimization)
- **Target AI platforms:** (ChatGPT / Perplexity / Google AI Overview / etc.)
- **Entity coverage:** (what brand, product, or concept should this content reinforce?)
- **Citation-worthy claims:** (stats, quotes, or definitions that should be clearly attributable)
- **Structured answer blocks:** (FAQ-style sections or direct answers to include)

---

## Content review checklist

### Writer self-review
- [ ] All copy is complete and on-brief
- [ ] Facts and claims verified
- [ ] Internal links added where applicable
- [ ] SEO / GEO elements incorporated (if web-published)
- [ ] Default voice (tone-and-guidelines) applied to all content (landing page, emails, brand social, slides, recap)
- [ ] [Speaker]'s tone applied to their social posts only

### Editor review
- [ ] Tone and voice on-brand
- [ ] Legal / compliance check (if needed)
- [ ] Final copy approved

### SME review
- [ ] Product specs and demo claims accurate
- [ ] Speaker bios and titles correct
- [ ] Approved

**Reviewer notes:**

---

## Timeline

| Milestone | Target date | Owner | Complete |
|-----------|------------|-------|----------|
| Event details locked | | | - [ ] |
| Speaker prep doc complete | | | - [ ] |
| Landing page live | | | - [ ] |
| First email invite sent | | | - [ ] |
| Social announcements posted | | | - [ ] |
| Slide deck finalized | | | - [ ] |
| Reminder emails scheduled | | | - [ ] |
| Webinar day | | | - [ ] |
| Recording uploaded | | | - [ ] |
| Follow-up emails sent | | | - [ ] |
| Social recaps posted | | | - [ ] |
| Blog recap published | | | - [ ] |
