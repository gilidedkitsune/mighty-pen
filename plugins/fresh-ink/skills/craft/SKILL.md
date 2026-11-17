---
name: craft
description: >
  The writing agent and routing spine. Takes any request for written content (blog posts,
  customer stories, social posts, emails, website copy, long-form, ads, executive summaries,
  one-pagers, bylines, webinars, sales enablement, creator briefs, cover letters, resumes, bios,
  LinkedIn About sections, editor pitches, personal essays, ideation), works out what kind of
  piece it is, asks who it's for and what it's meant to do, and runs the matching workflow
  through to a finished draft. Hands headlines to headline-lab, social posts and repurposing to
  socialize, and blog work to blog. Trigger on "I need a [content type]", "write a", "draft a",
  "brainstorm content ideas", "content plan", "webinar", or any request to create written
  content, including career documents ("cover letter", "resume bullets", "bio", "pitch an
  editor"). If the output will be read beyond this conversation, this skill applies.
---

# Craft

You write, and craft is the router: it works out what the piece is, gets the decisions that have to come first, and runs the steps that match that kind of piece. Nothing ships without the promise, the edit passes, and the final sweep.

## Read these before you write

1. **The craft:** `${CLAUDE_PLUGIN_ROOT}/skills/craft/references/prose-craft.md`. How the prose is built, from the promise through the cut. Its pass 0 puts no-slops's rulebook in front of you as drafting constraints, so the tells are known before the first sentence.
2. **The voice:** `${CLAUDE_PLUGIN_ROOT}/skills/tone-and-guidelines/SKILL.md`. Voice registers, house style, and the editorial rules that apply to every type.
3. **A specific person's voice, when the job is one:** `${CLAUDE_PLUGIN_ROOT}/skills/voice-profiles/SKILL.md`. It lists the profiles available.

The steps below add the workflow and the rules for each content type.

**Where each rule lives.** Each rule has one home, and everything else points to it, so the copies can't drift apart:

| Rules about | Live in |
|---|---|
| Voice registers and house style (citations, numbers, dashes, brand names, casing) | tone-and-guidelines |
| AI tells, active voice, adverbs, the mechanical sweep, the 35/50 score | no-slops |
| Leads, sentences, rhythm, concreteness, endings, the cut | prose-craft (this skill's reference) |
| Writing for search and AI answers | SEO-GEO-drafting (this skill's reference), applied to the finished draft by search-weave |
| A content type's shape, length, and type-specific reminders | that type's template in content-formats |
| Platform formats and limits | socialize's references |

If a rule shows up in two places, the copy outside its home should become a pointer.

## Step 1: Route, then the promise, then intake

Detect the content type from the user's first message, using the table below. If the type is delegated, hand it off now. Delegated skills run their own promise step and intake, so nothing here runs twice. For everything craft keeps, the promise comes next, before the mode or any other question.

### Content types

| Type | Trigger phrases | Workflow | Reference |
|---|---|---|---|
| Ideation | "brainstorm", "content ideas", "what should we write", "topic ideas", "content plan" | Ideation | `${CLAUDE_PLUGIN_ROOT}/skills/craft/references/ideation-workflow.md` |
| Blog | "blog post", "article", "content brief", "blog brief", "outrank" | Delegate to **blog** | blog's own references |
| Customer story | "customer story", "case study" | Template | `${CLAUDE_PLUGIN_ROOT}/skills/content-formats/references/customer-story-template.md` |
| Social | "social", "LinkedIn", "X post", "tweet", "thread", "Threads", "Bluesky", "Reddit", "Show HN", "caption", "Reel script" | Delegate to **socialize** | socialize's platform references |
| Email | "email", "newsletter", "drip", "email sequence" | Light | `${CLAUDE_PLUGIN_ROOT}/skills/craft/references/micro-formulas.md` |
| Website copy | "website copy", "landing page", "hero copy" | Medium | `${CLAUDE_PLUGIN_ROOT}/skills/craft/references/web-copy-best-practices.md` and `SEO-GEO-drafting.md` |
| Long-form | "whitepaper", "ebook", "guide", "manual", "survey report", "research report", "findings" | Full | `${CLAUDE_PLUGIN_ROOT}/skills/craft/references/SEO-GEO-drafting.md` |
| Ad copy | "ad", "ad copy", "campaign copy" | Medium | `${CLAUDE_PLUGIN_ROOT}/skills/craft/references/schwartz-copywriting.md` and `schwartz-5x5-matrix.md` |
| Executive brief or one-pager | "exec summary", "executive summary", "1-pager", "one-pager" | Medium | `${CLAUDE_PLUGIN_ROOT}/skills/content-formats/references/minto-scaffold.md` |
| Byline | "byline", "thought leadership", "op-ed", "ghostwrite" | Full | `${CLAUDE_PLUGIN_ROOT}/skills/content-formats/references/minto-scaffold.md` |
| Webinar | "webinar", "webinar BOM", "webinar content" | Template | `${CLAUDE_PLUGIN_ROOT}/skills/content-formats/references/webinar-bom-template.md` |
| Sales enablement | "sales deck copy", "battle card", "objection handling" | Template | `${CLAUDE_PLUGIN_ROOT}/skills/content-formats/references/sales-enablement-template.md` |
| Creator brief | "creator brief", "influencer brief" | Template | `${CLAUDE_PLUGIN_ROOT}/skills/content-formats/references/creator-brief-template.md` |
| Career documents | "cover letter", "resume", "resume bullets", "CV", "bio", "speaker bio", "LinkedIn About" | Template | `${CLAUDE_PLUGIN_ROOT}/skills/content-formats/references/career-docs-template.md` |
| Pitch | "pitch", "op-ed pitch", "pitch an editor", "story pitch", "guest post pitch" | Template | `${CLAUDE_PLUGIN_ROOT}/skills/content-formats/references/career-docs-template.md` |
| Personal essay | "personal essay", "essay", "memoir", "personal piece", "newsletter essay" | Medium | None |
| Headlines | "headline options", "headline variants", "title ideas", "subject lines", "headline lab" | Delegate to **headline-lab** | headline-lab's references |
| Repurpose | "socialize", "repurpose", "turn this into", "cut this down for", "atomize" | Delegate to **socialize** | socialize's references |

**No reference listed** means there's no template for the type. Follow tone-and-guidelines and the type rules in Step 4.

**Register.** Each type has a voice register (personal, professional, or B2B tech buyer), set by the table in tone-and-guidelines. Look it up at routing, because it changes intake and drafting, not just polish: a cover letter and a battle card both need proof, but different proof, in a different voice. If a type falls between registers, ask and give a recommendation.

**Folded types** (no standalone row): research reports run as Long-form with findings first. Event copy (conference, meetup, booth) is built from the Email, Social, and Website rules: short, punchy, one call to action, with date and time formatted for the region.

**Workflow depth:**
- **Ideation:** promise, strategy intake, research, ideas, prioritize, hand off to writing.
- **Full:** promise, intake, research, outline, draft, edit, present.
- **Medium:** promise, intake, outline, draft, edit, present. No deep research.
- **Light:** promise, intake, draft, edit, present. No research or outline.
- **Template:** promise, intake, load the type's scaffold from content-formats, work its checklist, draft, edit, present.
- **Delegate:** hand the whole job to the owning skill, promise included.

If the content type isn't clear, ask.

### The promise

Every piece craft keeps starts here, at every depth, including quick drafts. Three questions in one AskUserQuestion round, before the mode or any other intake. Use what the brief already answers, and ask only about the gaps, but all three get answered.

1. **Who is it for?** Name a specific reader: role, seniority, and what they already know. A general reader doesn't exist; calibrate register and jargon to the one you named.
2. **What is it for?** One purpose. It decides the shape before drafting:
   - **Search and AI answers.** The piece has to be found, extracted, and cited. Answer-first sections and question-shaped headers (`${CLAUDE_PLUGIN_ROOT}/skills/craft/references/SEO-GEO-drafting.md`), then the search-weave pass in Step 5. Most blog and web content is here.
   - **Awareness.** The reader meets the idea or product for the first time. Accessible register, a light mention, a "try it" action.
   - **Consideration.** The reader is weighing options. Proof, comparison, the customer's own words, and the Schwartz diagnosis matter most here.
   - **Decision.** The reader is ready to act. Objections, specifics, pricing where it belongs, and a call to action for the exact next step. The Ogilvy review is usually worth running.
   A search-led piece still has a stage, and it's worth naming both.
3. **Why should they care?** Draft one sentence from the brief and confirm it: "The promise: [sentence]. Does that hold?" Offer to confirm, adjust, or name the real reason. If neither the brief nor you can answer, stop. The piece has no thesis yet, and research and outlining can't supply one.

The three answers become the promise (prose-craft pass 1), one sentence that goes above the outline and the draft. Every later step checks against it.

### Mode

Infer the mode from the request first:

- **Quick:** "quick," "fast," "just need a," "rough draft," "knock it out," source material already attached, or any Light type (email).
- **Full workflow:** "full workflow," "deep dive," "SEO research," "the works," "let's do this right," ideation, or a request that names a voice, a Schwartz lens, or an edit pass.

If the signals are clear, state the mode and go ("This reads as a quick one. I'll skip the outline and get you clean copy."). The user can override. If they're unclear, ask in AskUserQuestion: **Quick** (promise, source material, clean copy back) or **Full** (the complete workflow, with research, an outline, and the edit menu).

**Quick workflow:** the promise (confirmed in one round, from the brief where possible), then a draft built on prose-craft pass 0 and the passes that follow, with tone-and-guidelines applied. Skip research, outline, and the type-specific intake. Edit with no-slops only. Present clean copy with a suggested title and, for web pages, a meta description. Don't offer the optional edit passes.

**Full workflow:** every step below, in order.

### Intake

Put as many questions as possible into one AskUserQuestion call (four at most). The aim is fewer round trips, not fewer questions.

**Round 1:** the mode, if it wasn't inferred, plus up to two type-specific questions from `${CLAUDE_PLUGIN_ROOT}/skills/craft/references/intake-by-type.md`: the two that matter most for this type.

**Round 2**, if needed: the remaining type questions, plus constraints and references (source material, links, angles, keywords, quotes from executives, publish dates, tone changes).

The promise questions come first and stand alone. Don't fold them into a type round. Skip anything the user already said, and never re-ask what the brief covers. Don't invent defaults.

## Step 2: Research

Applies to Full and Medium workflows. Light workflows skip it unless the user supplies source material.

Research serves two craft passes and nothing else. The **promise** (what the reader gets that they can't get elsewhere) tells you what to look for. **Concreteness** (prose-craft pass 4) tells you what to collect: the numbers, proper nouns, dates, and artifacts that let each abstract claim touch the ground. Anything that serves neither can be skipped. That's what "don't go down a rabbit hole" means here.

### Web research
Use WebSearch for the current conversation on the topic (news, competitor moves, trends), credible figures to support the piece, and what has already been published, so this piece adds something.

### Internal research (when connected)
If the session has workspace connectors (a docs wiki, an issue tracker, team chat), pull specs, positioning notes, shipped milestones, prior content, and customer feedback from them. If none are connected, ask the user for source material. Never assume a tool is available, and never invent internal facts.

If the user supplied source material during intake, use it first and supplement, not duplicate.

### Sourcing goes to cited-works

Content with factual claims needs credible sources: internal data, usage figures, customer feedback, industry reports, research, or reputable publications. Ideally a mix.

Sourcing is cited-works' job. List each stat, quote, or claim the piece needs, one line each ("a 2025 figure on developer time lost to flaky tests, primary source"), and hand the list to cited-works (job 1, content research). It traces each claim to its original source, dates it, checks the do-not-cite list, and returns a citation ready to paste, in the piece's format: the two-part inline format for web copy, Chicago superscripts for long-form. Use what comes back as it is. Drop any claim cited-works couldn't source, rather than softening it into an unsourced one.

If cited-works isn't installed, apply its core rule by hand: cite the origin, not the middleman (tone-and-guidelines, Bibliography and attribution), and flag any claim you couldn't trace instead of shipping it.

### Content strategy check (web, ad, and long-form)

Position the piece in the broader plan: which content pillar it belongs to, where internal links go, and what angle this piece adds that doesn't exist yet. That last one is the research half of the promise.

### Customer language (Full workflow; lean-in types)

For content where customers' words matter (customer stories, conversion copy, sales enablement, nurture email), pull customer language first, using `${CLAUDE_PLUGIN_ROOT}/skills/craft/references/voc-message-mining.md`. Sort reviews, forum posts, support threads, and call notes into its six buckets, then let them supply real phrasing and surface objections. It sharpens the draft; it never blocks it. For search-led or creative work, keep it as an optional gut-check.

### Schwartz diagnosis (web, ad, landing, and sales enablement)

Before drafting persuasive copy, place the reader on two scales, using `${CLAUDE_PLUGIN_ROOT}/skills/craft/references/schwartz-copywriting.md`:

1. **Awareness:** where the reader is right now (unaware through most aware).
2. **Sophistication:** how many competitors have already made this promise to this audience (stage 1 through stage 5).

Then look up the intersection in `${CLAUDE_PLUGIN_ROOT}/skills/craft/references/schwartz-5x5-matrix.md`. It gives the headline strategy, the lead, the length, the proof, and the call to action. This step is strongly recommended whenever the headline and lead depend on how close the reader is to buying. For ad copy, it drives the Schwartz variant.

### Four forces (switching and conversion copy)

For copy that asks the reader to switch or adopt (web and landing copy, ads, nurture email, "vs" and migration pages), check `${CLAUDE_PLUGIN_ROOT}/skills/craft/references/jtbd-four-forces.md` after the Schwartz diagnosis. Schwartz sets the angle. The four forces make sure the draft builds on the push and the pull, and handles the two forces against the switch: the anxiety about the new option and the habit of the current one. Those are usually the real blockers.

## Step 3: Outline

Applies to Full and Medium workflows. Light workflows skip it: they go from the promise straight to drafting, and the lead and kicker get written in Step 4 instead.

Build the outline with the same passes that drive the draft, at section level, before any paragraph exists. A draft built on a weak outline inherits every weakness in it. Present the outline and **wait for approval before drafting.**

**Build it in this order:**

1. **The promise** (pass 1), at the top. It's the test for everything below.
2. **The lead** (pass 2): the fact, number, person, or scene the piece opens on, and why it's arguable or picturable. Write one or two sentences, not a description of them.
3. **The sections** (pass 6): each one is a single move (it states a claim, proves one, or turns the argument). Name the move. Check the joints: each section follows from the one before with *but* or *therefore*. A section that could open with "additionally" hasn't earned its place; make it a real turn or fold it into a neighbor. Give weight where the point is.
4. **The specifics** (pass 4): under each section, the number, name, quote, or artifact it will carry, from research. A section with only a principle gives the reader nothing to hold. Find its specific, or cut the section.
5. **The kicker candidate** (pass 7): the fact, image, or consequence the piece lands on. It may change during drafting. Naming it now stops the piece from ending on a summary.
6. **The cut** (pass 8): check every section against the promise. Anything that doesn't serve it dies here, before it costs a draft.

Then name the call to action: where the reader goes next.

**Structure by type** shapes the sections above without replacing the passes:
- **Customer story:** follows the template's nine sections (`${CLAUDE_PLUGIN_ROOT}/skills/content-formats/references/customer-story-template.md`), with one named move and specifics in each.
- **Executive brief, one-pager, byline, or sales argument:** follows the answer-first scaffold in `${CLAUDE_PLUGIN_ROOT}/skills/content-formats/references/minto-scaffold.md`: thesis first, an SCQA lead, then three to five non-overlapping supporting points.
- **Other types:** adapt to the format. A long-form outline is its chapter plan, with the promise each chapter serves. An email is subject, body flow, and call to action. A landing page is the above-the-fold promise, then the section order in `${CLAUDE_PLUGIN_ROOT}/skills/craft/references/web-copy-best-practices.md`.
- **Blog:** no outline here. blog runs its own brief.

Keep the outline scannable. The user should be able to approve, revise, or redirect within a minute. What they're approving is the promise, the lead, and the moves.

## Step 4: Draft

This step is the craft: what happens while the draft is written. What happens to the finished draft (the audit, the copyedit, the persuasion review, the citation pass) is Step 5. Don't run edit passes while writing. Write clean, then verify.

**The craft first.** Work prose-craft in order (`${CLAUDE_PLUGIN_ROOT}/skills/craft/references/prose-craft.md`):

0. **Know the tells before you type.** no-slops's rulebook is a set of constraints, not an audit to face later. A tell that reaches Step 5 means Step 4 failed.
1. **The promise.** Above the draft, for you alone. It's the test for every section.
2. **The lead.** Start with the thing, not the topic. The first sentence should be arguable or picturable.
3. **Sentences.** The doer is the subject and the action is the verb. Subject and verb within six words. End each weighty sentence on its payload. Use verbs a camera could record. Limit the copulas.
4. **Concreteness.** Every abstract claim touches something concrete within a sentence. Prefer the proper noun.
5. **Rhythm.** In any run of five sentences, one under eight words and one over twenty. Save the period for what matters. Watch the colons that appear once em dashes are gone.
6. **Paragraphs and flow.** One move per paragraph. Connect with *but* or *therefore*, never *and then*. Let the weight be uneven.
7. **The ending.** A fact, an image, or a consequence. Never a recap. The kicker is the second-best line.
8. **The cut.** Trim around a tenth of the draft. The first paragraph, adverbs, "that," stacked prepositions, the favorite line. Under 5% means the cut didn't really happen.

Apply these to every piece longer than a single line. Drafting inside pass 0's constraints is what lets Step 5a come back clean. It still runs, as a check.

**Then the voice.** Apply tone-and-guidelines (`${CLAUDE_PLUGIN_ROOT}/skills/tone-and-guidelines/SKILL.md`) in the register set at routing: **personal** (the full voice), **professional** (the same voice with less grit, for pieces under the author's name that a hiring manager, editor, or client will judge), or **B2B tech buyer** (precise, evidence-first, unhyped, for technical product content). That file is the source for voice and house style. Read it there. A loaded voice profile changes the personality, never the limits of the register.

**For blog, long-form, and web copy,** also apply `${CLAUDE_PLUGIN_ROOT}/skills/craft/references/SEO-GEO-drafting.md`. Those rules cover passage-level extractability, answer-first structure, specific claims, and citation practice. They sit on top of the voice rules. Long-form uses Chicago superscripts instead of inline attribution; tone-and-guidelines explains the difference.

### Short-form skeletons

For email, ads, and other quick copy (the Light types, which skip the Schwartz diagnosis), start from a skeleton in `${CLAUDE_PLUGIN_ROOT}/skills/craft/references/micro-formulas.md`. Social posts have their own hooks in socialize. For long-form and persuasion-heavy work, the Schwartz diagnosis leads, and the skeletons are only a fast way to shape a first draft.

### Type rules

#### Voice selection (social)
Social is delegated to `socialize`, which runs its own voice menu: the default voice in the right register first, then each person in the voice-profiles roster by its menu blurb. For a webinar or launch post that goes out under a named person's account, hand it to socialize with that person named.

#### Blog-specific
Blog is delegated at routing (Step 1). It owns the blog's shape, on-page SEO, and its workflows. Citations follow tone-and-guidelines like everything else. For a post in a specific person's voice, tell blog, which reads the profile.

#### Customer story-specific
- Follow `${CLAUDE_PLUGIN_ROOT}/skills/content-formats/references/customer-story-template.md`. Its nine sections, length budgets, and tone notes all live there.
- **Ogilvy review on by default** (Step 5c). Its promise and proof questions fit this type closely: one promise (what the customer achieved), a headline that carries it, facts over adjectives, and the product as the hero.

#### Social-specific
Delegated to `socialize` at routing. It owns platform formats, limits, current feed mechanics, and the social tells. Nothing here repeats them.

#### Email-specific
- Subject line and body. A subject that's specific and concise, not clickbait.
- One clear call to action.
- Personal details where they fit.

#### Website copy-specific
Read `${CLAUDE_PLUGIN_ROOT}/skills/craft/references/web-copy-best-practices.md` before drafting. It covers the five-question test, the first screen, headlines, calls to action, objections, mobile writing, and the page-type patterns. Apply SEO-GEO-drafting too, for any page that will be found on the web.

Additional rules for all website copy:
- **Product name:** full name first, short form after (tone-and-guidelines, Product and brand names).
- Headline casing on heroes and headers follows tone-and-guidelines.
- Show the product: screenshots, demos, real output. No stock illustration.
- Citations follow tone-and-guidelines, including its note on citing sparingly on conversion pages.
- **Ogilvy review on by default** (Step 5c). Conversion copy is its home ground: position before promise, headline as a standalone claim, product as the hero.

#### Long-form-specific
- Organized into chapters or major sections.
- Citations: Chicago superscripts tied to a Works Cited list. Long-form is exempt from inline attribution (tone-and-guidelines, Bibliography and attribution).
- Depth without padding.
- For a research report: findings and the executive summary first. Tables and structured data where they help. Every claim sourced, with a methodology section when one applies. Explain what the numbers mean; don't just list them.

#### Ad copy-specific
Ad copy produces multiple versions: two drafts and one review.
1. **Default-voice draft:** tone-and-guidelines in its register (B2B tech buyer for technical products). Direct, benefit-led, conversational.
2. **Schwartz draft:** the awareness and sophistication diagnosis (`${CLAUDE_PLUGIN_ROOT}/skills/craft/references/schwartz-5x5-matrix.md`) sets whether the ad leads with the problem, the mechanism, the proof, or the offer.
3. **Ogilvy review** (Step 5c, on by default for ads): run both drafts through the diagnostic questions and present the edited versions. The review is an edit applied to the two angles, not a third draft.

For several audiences, produce a full set per audience, labeled by audience and angle. Rules for every version: respect the platform's character limits, lead with the strongest hook, cut filler, and match the call to action exactly to the landing page's offer. Present the versions side by side. no-slops runs on each draft before the review, and the final sweep (5f) runs after it.

#### Byline-specific
- In the named author's voice, and sounding like them.
- Authoritative, not stiff.
- Claims supported with specifics.

#### Executive brief and one-pager-specific
- Written for decision-makers who won't read the whole document. Findings and recommendations come first.
- Scannable: headers, bullets, and bold used sparingly.
- Executive summary: one or two pages, anchored to its source document.
- One-pager: one page. Lead with the problem, present the solution, close with the call to action.

#### Sales enablement-specific
- Follow `${CLAUDE_PLUGIN_ROOT}/skills/content-formats/references/sales-enablement-template.md` (battle card, objection handler, or one-sheet). B2B tech buyer register.
- **Ogilvy review on by default** (Step 5c). A battle card rests on one promise and facts a rep can say aloud. Burying the news is its main failure.

#### Webinar-specific
- **The default voice applies to all webinar content:** landing pages, emails, reminders, slides, recaps, and brand social. Don't apply a personal profile to them.
- **Exception: posts under a named person's account.** When a teammate posts about the webinar from their own account, hand the post to socialize with that person named. It drafts in their profile, so it reads like them talking about the event, not marketing copy about it. If that person has no profile, flag it and use the default voice rather than inventing one.
- Follow the checklist in `${CLAUDE_PLUGIN_ROOT}/skills/content-formats/references/webinar-bom-template.md`. Work through the sections the user needs; don't dump the whole template.
- Draft assets in the order they're needed: landing page, invite, social announcement, reminders, day-of, follow-up, recap.
- **Filing (optional):** by default a webinar package is delivered like any other piece (Step 6). If the user keeps a team wiki or editorial calendar that's connected, offer to file it there. The template's "Filing the finished package" section covers the steps.

#### Career docs and pitch-specific
- Professional register (tone-and-guidelines, Register 2). Per-document rules are in `${CLAUDE_PLUGIN_ROOT}/skills/content-formats/references/career-docs-template.md`: cover letters, resume bullets, bios in three lengths, LinkedIn About, and editor pitches.
- **Truth gate:** build the proof bank first, per the template. Never add a skill, credential, or result that the source material doesn't support. Ask instead.
- Tailored to one target. With a job description, pull its top five requirements first, and answer each with proof or flag it as a gap.
- Numbers first: result, scale, and timeframe ahead of the color.
- Run red-pen in Proofread-only mode before anything is sent. A typo in a cover letter costs the job.

#### Personal essay-specific
- Personal register (tone-and-guidelines, Register 1), at full strength.
- The promise is an emotional truth, not a takeaway. The reader should leave seeing something differently.
- Scene first. Reflection earns its place once the reader is in the room.
- Specifics carry it: names, objects, prices, the exact words someone used.
- End on an image or a turn, not a moral. If the piece ends by explaining itself, cut the last paragraph and check whether the one before is the real ending.
- For a long draft, red-pen's Developmental mode comes first: structure before sentences.

#### Creator brief-specific
- Follow `${CLAUDE_PLUGIN_ROOT}/skills/content-formats/references/creator-brief-template.md`: its nine sections, guardrails, and the bar it sets. A creator should be able to deliver from it with no follow-up call.

---

## Step 5: Edit

The draft is finished. Editing is separate work, applied to a draft that already exists. Don't fold it back into drafting.

**Order: structure first, sentences last.** Big changes come before small ones, so nothing gets polished and then rewritten:

1. **5a. no-slops gate** (mandatory). Catch the tells before anything gets edited around them.
2. **5b. Schwartz re-angle** (optional). Changes the headline, lead, and structure, so it runs before anything that polishes them.
3. **5c. Ogilvy review** (default for some types). Promise, proof, and headline: what the piece says.
4. **5d. search-weave** (published web content). Works the keywords, questions, and citations into the structure.
5. **5e. red-pen** (anything going to publish). The line-level copyedit, last, once the structure has stopped moving.
6. **5f. Final sweep** (mandatory). no-slops's mechanical sweep again, because every rewrite is a fresh chance for a tell.

Skip any optional pass the piece doesn't need. Never reorder the ones that run.

### 5a. no-slops gate (mandatory, every piece)

Run the `no-slops` skill (`${CLAUDE_PLUGIN_ROOT}/skills/no-slops/SKILL.md`) against the draft. It scores five dimensions (directness, rhythm, trust, authenticity, density) out of 50, and 35 is the minimum to pass. Fix every violation, and re-audit anything under 35. This is verification. The rules were drafting constraints in Step 4, so a finding here means the draft wasn't built clean. Fix it, and note which pass let it through.

**For Light workflows** (social, short email): skip the scoring, but run the mechanical sweep for real. Short copy ships most often, which makes it the main leak. "It's just a tweet" is how tells get published.

### 5b. Schwartz re-angle (when the substance is right and the opening isn't)

Place the reader with `${CLAUDE_PLUGIN_ROOT}/skills/craft/references/schwartz-5x5-matrix.md`, then rewrite the headline, lead, and structure to fit that position. Show the new version next to the original. Most useful for blog posts and web copy. Rarely needed if the Step 2 diagnosis was done well. If only the headline is in question, use `headline-lab` instead.

### 5c. Ogilvy review (the persuasion edit)

**On by default for customer stories, sales enablement, landing and web copy, and ads. On request for everything else.** Run `ogilvy-copywriting` in review mode and ask its diagnostic questions of the finished draft. Is the positioning clear, and for whom? Is there one promise? Does the headline carry it, and the news if there is any? Where is the proof, and are the facts doing the work the adjectives claim? Is the news buried? Is the product the hero, or has the writing taken over? Fix what fails. Leave what works.

This is an edit, not a voice change. It applies on top of whatever voice the draft already has, including a team member's. On the default types, offer it after the gate. Elsewhere, run it when asked, or when the piece has to sell and doesn't.

### 5d. search-weave (keywords, questions, citations)

Every published blog post and web page goes through `search-weave` before the copyedit. It asks for the target keywords, the questions the piece should answer, and the citations to include (or pulls them from Insights, when that's installed and connected). Then it works them into the finished draft: question-shaped headers, answer-first sections, a definition block, attributed claims, liftable formats, an FAQ, and dated facts. It's a structural pass, not a rewrite. It never stuffs keywords, and voice and accuracy win every disagreement.

### 5e. red-pen (the copyedit, last)

For anything going to publish, or when the user asks to "tighten," "edit," "redline," or "check readability," hand the draft to `red-pen`. It runs last because line edits on a structure that's still moving get thrown away. red-pen owns the diagnostic lenses (lead, stress position, cohesion, rhythm, kicker, thought verbs, stance, claims and proof), the readability script against the reader's target band, and the numbered findings. Pick the mode that fits: the default verdict and reds; Developmental for a long draft whose structure is still open (run that before 5b instead); or Proofread-only for a finished piece. If red-pen keeps flagging the same lens, the fix belongs in drafting: reread the matching section of `${CLAUDE_PLUGIN_ROOT}/skills/craft/references/prose-craft.md`.

### 5f. Final sweep (mandatory)

Run no-slops's mechanical sweep on the final text. Rescore only if the edits changed more than a few sentences. If no optional pass ran, the gate in 5a already covered it, and this can be skipped.

---

## Step 6: Present

Deliver clean, ready-to-use copy:
- A suggested title or headline (sentence case for blog and long-form; adapt for other types)
- The full content, formatted
- A meta description under 160 characters for anything published on the web

The optional passes (the Schwartz re-angle, Ogilvy, search-weave, red-pen) were offered in Step 5. Don't offer them again unless the user asks.

**Export:** if the user wants a file, ask where it should go and in what format. A `.docx` through the `anthropic-skills:docx` skill is the usual choice. Use any local folder, synced cloud folder, or connected docs tool. If the destination needs a tool that isn't connected, save the file locally and say where. For Google Drive, upload the finished `.docx` rather than building a native Google Doc through a connector, which tends to lose formatting. Webinar packages can go to a connected team wiki instead (see Webinar-specific in Step 4).

---

## Other workflows

**Ideation** (research and strategy, no drafting): run `${CLAUDE_PLUGIN_ROOT}/skills/craft/references/ideation-workflow.md`. The promise still comes first, and the ideas hand off to the writing workflow.

**Draft revision** (tightening a draft that already exists, or updating published content, on requests like "revise this," "tighten this up," "simplify," or "check readability"): go to Step 5. red-pen owns the readability analysis against the reader's band and runs the script rather than estimating. Take its redline, re-run the no-slops gate, and present the revised draft with a before-and-after readability comparison.

**Google Doc as a template:** if the user gives a Google Doc URL as the template, export its text (append `/export?format=txt` to the base URL, before `/edit`), map its sections, draft each section to match its placeholders, and present the result section by section for review.

## SEO and AEO: inputs, not tools

craft doesn't pull data. SEO and AEO work runs on inputs: target keywords, the questions to answer, and the citations to use. search-weave asks for those in Step 5d and weaves them into the structure. Drafting follows `${CLAUDE_PLUGIN_ROOT}/skills/craft/references/SEO-GEO-drafting.md`, which is a writing rule rather than a tool.

If the Insights plugin is installed and wired, it can supply those inputs instead of the user. `seo-geo` provides the site's Search Console queries and traffic and its map of SEO tools. `aeo-insights` provides AI-answer visibility: named versus cited, term winnability, and the sub-questions engines asked. Both stay dormant when not connected. If one reports that it isn't connected, take that as the answer and work from what the user gives you. Never invent volumes, rankings, or citation figures, and skip any data step whose input the user already supplied.
