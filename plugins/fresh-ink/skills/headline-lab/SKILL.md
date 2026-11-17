---
name: headline-lab
description: >
  Generates about 10 headline, title, or subject-line variants for a piece, each built on a
  different angle, then scores them against Ogilvy's headline rules and, for anything that
  has to be found in search or AI answers, search-weave's term winnability rule. Returns a ranked
  shortlist with the reasoning. Trigger on "headline options", "headline variants", "title
  ideas", "give me headlines", "subject line options", "what should I call this", "headline
  lab", or when craft or blog needs a headline tested. Works on a finished draft, an outline,
  or a one-sentence promise. Does not write or edit the body.
---

# Headline Lab

Ten honest attempts at the headline, scored, so the choice is a decision instead of a vibe. The headline carries most of the piece's reach: Ogilvy's rule is that five times as many people read it as read the body. It deserves more than one draft.

## Inputs

Ask only for what the request doesn't already give you:
1. **The piece or its promise.** A draft, an outline, or the one-sentence promise (craft Step 1). Without a promise there's nothing to headline; ask for it.
2. **Where it runs.** Blog or web page (search and AI answers matter), email subject line, LinkedIn or X post, ad, landing page hero, op-ed or pitch subject, or a personal essay.
3. **Who it's for**, and the register (tone-and-guidelines, "Choosing a register").
4. **The target query**, if the piece is search- or AEO-led.

## Generate: about 10 variants, one per angle

Each variant takes a different angle, so the shortlist is a real choice and not ten rewordings of one idea. Cover at least seven of these:

| Angle | What it does | Example shape |
|---|---|---|
| Promise | States the benefit plainly | "Cut your deploy time in half without touching your CI" |
| News | Leads with what's new | "Postgres 18 changes how you should index JSON" |
| Number | A specific figure carries it | "We cut 40% of our cloud bill in one sprint. Here's the list." |
| Question | The reader's own question, in their words | "Why did my credits run out so fast?" |
| How-to | The method, named | "How to migrate off a monolith one endpoint at a time" |
| Audience flag | Names the reader first | "For platform teams drowning in YAML" |
| Contrarian | Takes a position someone would argue with | "Your onboarding flow is too short" |
| Specific story | A person, place, or moment | "The night our pager went off 212 times" |
| Answer-first | Defines or answers the target query directly | "What is a feature flag? A switch you can flip without a deploy." |
| Curiosity | Opens a gap the body closes | Use sparingly, and only if the body pays it off in the first paragraph |

Draft inside no-slops's rules from the start: no Tier 1 vocabulary, no fingerprint openers ("Unlocking," "The ultimate guide to," "Everything you need to know"), no em dashes, no colon-subtitle reflex on every option.

## Score

Score each variant out of 10 on the checks that apply to where it runs.

**Ogilvy (every headline, 6 points).** From `${CLAUDE_PLUGIN_ROOT}/skills/ogilvy-copywriting/SKILL.md`, Headlines:
- Promises a benefit or carries news (2)
- Plain language: telegraphs the message, no decoding (1)
- Flags the audience, or doesn't need to (1)
- Specific: a number, a name, a mechanism, a scene (1)
- No negative framing, and any curiosity it opens, the body pays off (1)

**Findability (search, web, and AEO pieces, 4 points).** From `${CLAUDE_PLUGIN_ROOT}/skills/search-weave/SKILL.md`, pass 1 (the term), using aeo-insights's verdict if Insights is wired:
- Contains the target term or the reader's phrasing of it (1)
- The term is winnable: greenfield, or scoped to the entity, not a head-on run at an owned term (2)
- Works as a lifted answer: an engine could quote it and it would still make sense (1)

**Fit (everything else, 4 points)** replaces Findability when search doesn't matter:
- Fits the channel's length (email subject lines 30 to 50 characters, X under about 100, LinkedIn's first line before "see more") (2)
- Matches the register and the voice (2)

## Present

1. **The top three**, ranked, each with its score and one line on why it wins.
2. **The full table:** every variant, its angle, score, and the one check it failed, if any.
3. **A pick**, with the tradeoff stated ("#2 is safer in search; #1 will get more clicks from people who already know the product").

Offer to combine the best parts of two variants, or to run a second round on one angle. For an email subject line, also offer an A/B pair: the two strongest variants from different angles.

The writer picks. Never swap a headline into a draft without asking.
