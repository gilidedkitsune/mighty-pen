# Slop vs. gold

Paired examples: the same job done by a model on autopilot and by a writer who knew something. Every pair is invented for teaching, across the kinds of work this stack does, so nothing here should be reused as a real claim. Each slop version is tagged with the tells it carries (names from `banned.md` and `structures.md`), so the pairs double as drills.

**Use it three ways:**
- **Before drafting:** read the pair closest to your content type to set the bar.
- **On a borderline score (30 to 35):** put your weakest sentence beside a pair. It's usually obvious which column it belongs in.
- **When teaching someone the filter:** this file first, then the three-rules test (tone-and-guidelines), then the catalogs.

---

## Pairs by content type

### Product page hero (developer tool)
**Slop:** "Unlock seamless deployments with our cutting-edge platform, empowering teams to ship with confidence across the modern software landscape."
**Gold:** "Push to main. Your preview URL is live in 40 seconds, and it disappears when the branch merges."
**Tells:** Tier 1 ×4 (unlock, seamless, cutting-edge, landscape) · hype verb · no number, no mechanism.
**What changed:** a mechanism you can picture, a number you can test, and a detail (it cleans up after itself) only this product would mention.

### Release note
**Slop:** "We're thrilled to announce a robust new feature that elevates your reporting experience and streamlines workflows."
**Gold:** "Reports now export to CSV. Filters carry over, so the file matches what you see on screen."
**Tells:** manufactured enthusiasm · Tier 1 (elevate) · Tier 2 pair (robust, streamline) · no feature named.
**What changed:** names the feature, then answers the one question a user would ask next.

### Cover letter line
**Slop:** "I am a passionate, results-driven content leader with a proven track record of driving impactful outcomes."
**Gold:** "At my last company I took the blog from 4,000 to 61,000 monthly readers in 18 months, with a team of two."
**Tells:** self-applied adjectives · Tier 1 (impactful) · no number, no scope, nothing checkable.
**What changed:** a result, a timeframe, and a constraint. The hiring manager can now believe something.

### LinkedIn post opening
**Slop:** "Here's something nobody talks about in content marketing. Let that sink in. 👇"
**Gold:** "We deleted 300 old blog posts last spring. Organic traffic went up 18%."
**Tells:** secret-knowledge hook · emphasis prop · emoji pointer · the post hasn't started yet.
**What changed:** the surprising fact goes first, so the reader has a reason to click "see more."

### Personal essay opening
**Slop:** "Growing up, I learned many valuable lessons about resilience that continue to shape who I am today."
**Gold:** "My father kept a jar of bent nails on the workbench, because he'd paid for them."
**Tells:** abstract noun (resilience) doing the work a scene should · Tier 3 (valuable) · could open any essay by anyone.
**What changed:** one object, one reason, and the reader already knows the father.

### Sales email
**Slop:** "I hope this email finds you well! I wanted to reach out because I believe our solution could add significant value to your organization."
**Gold:** "Your status page showed three incidents last week, all in the EU region. We cut EU failover for a team your size from 14 minutes to under one."
**Tells:** assistant manners · "solution" · Tier 3 (significant) · nothing about the recipient.
**What changed:** proof the sender looked, and a claim the recipient can check against their own week.

### Case study line
**Slop:** "The partnership marked a pivotal moment, enabling the client to achieve transformative results."
**Gold:** "Within a quarter, the client's support team closed tickets in 4 hours instead of 2 days, without adding headcount."
**Tells:** significance inflation · Tier 1 (pivotal) · Tier 2 (transformative) · no number.
**What changed:** before, after, a timeframe, and the constraint that makes it impressive.

### Technical blog intro
**Slop:** "In today's rapidly evolving tech landscape, observability plays a crucial role. In this post, we'll explore key strategies."
**Gold:** "Our p99 latency doubled every Tuesday at 2 a.m. It took us six weeks to learn it was a backup job."
**Tells:** boilerplate scaffolding · Tier 1 (landscape) · Tier 2 pair (crucial, key) · self-narration.
**What changed:** a mystery with a time stamp. The reader wants the answer, which is the definition of a lead.

---

## The three-rules scorecard

The gold lines pass all three questions from tone-and-guidelines' three-rules test; the slop lines fail all three.

| Line | Can you picture it? | Can you prove it true or false? | Could only this writer say it? |
|---|---|---|---|
| "Preview URL is live in 40 seconds" | the URL appearing | time it | one product's behavior |
| "4,000 to 61,000 monthly readers" | the chart | check the analytics | one person's record |
| "a jar of bent nails" | the jar | (memoir: it's testimony) | one family |
| "three incidents last week, all in the EU" | the status page | look it up | one sender who did the homework |
| "p99 doubled every Tuesday at 2 a.m." | the graph spike | read the dashboard | one team's bad month |
| *any slop line above* | ✗ | ✗ | ✗ |

---

## Gold that breaks the rules

The filter catches defaults, not decisions. Lines that trip a rule and should stay:

- **Avis, 1962: "We try harder."** Three words around an admission most brands would never make (the campaign's point was that Avis was number two). Short and fragment-adjacent, and it stays because it's a claim with a cost.
- **"Got milk?" (California Milk Processor Board, 1993).** A question as a headline, which the catalog flags in prose. It stays because the question is the whole idea: you only notice milk when it's gone.
- **Patagonia's 2011 Black Friday newspaper ad: "Don't buy this jacket."** A negation, the exact shape the catalog flags. It stays because the negation is the argument (buy less), and the brand backed it with specifics about the jacket's environmental cost.

The test for any rule-breaker: can you defend it the way you'd defend a claim, with intent and a reason? Then it stays. If the shape showed up because it's what the model reaches for, it goes. (Orwell's version: break any rule sooner than write something barbarous.)

---

## The repair drill

The pairs above run from slop to gold already. Here's the climb, step by step.

**Slop:** "Leveraging our innovative AI-powered platform, organizations can unlock actionable insights that drive meaningful outcomes across the customer journey."

1. **Delete what can be deleted.** "Across the customer journey" changes nothing. Gone.
2. **Plain verbs.** "Leveraging" is "using." "Unlock insights" is "see."
3. **Ask the questions the sentence avoids.** Which organizations? Which insights? What outcome, how big? If there are no answers, the real finding is that the sentence knows nothing; go find a fact.
4. **Rebuild from the fact.** (The numbers here are invented for the drill.)

**Gold:** "Support leads see which tickets will escalate before they do. Pilot teams cut escalations by a third in their first month."

**Practice line** (unrepaired): "Our holistic approach empowers stakeholders to navigate complexity and achieve sustainable growth in an ever-changing market."

---

## The pattern underneath

Slop removes three things: the specific (a number becomes "significant"), the falsifiable (a test becomes "proven"), and the particular (a confession becomes "excellence"). Then it adds atmosphere: landscape, journey, commitment, cutting-edge. When a draft starts leaning on those words, the repair is always the same: a name, a number, or a claim that could turn out to be wrong.
