# Prose craft: building the draft

The generative side of no-slops. no-slops's rules serve as pass 0 here, so they shape the draft from its first word. Its audit runs afterward as verification and should find little. Removing a tell from a finished sentence leaves a sentence built around the tell. Copy written clean from the start reads differently, and craft happens while drafting, not in cleanup.

Work the passes in order. Pass 0 is the set of constraints you write inside. Passes 1 through 8 cover the build itself: promise, lead, sentences, concreteness, rhythm, thread, ending, cut. Product examples are invented; don't reuse them as claims.

---

## 0. Before drafting: know the tells

A model writes whatever is most probable next, which favors the choice that suits the most readers and subjects. A person writes for one reader and one subject, so their choices come out uneven and specific. Each tell is a form of the probable default: a sentence announcing importance instead of adding a fact, rhythm applied by rule, an ordinary point presented as a revelation. A useful question while drafting: was this sentence chosen for this reader and this subject, or would it fit anywhere?

Open no-slops's rulebook before the first sentence. It's a set of constraints, not a checklist for later: the phrase catalog and Tier 1 vocabulary in `${CLAUDE_PLUGIN_ROOT}/skills/no-slops/references/banned.md`, the §0 artifacts and mechanical sweep in `${CLAUDE_PLUGIN_ROOT}/skills/no-slops/SKILL.md`, and the sentence shapes in `${CLAUDE_PLUGIN_ROOT}/skills/no-slops/references/structures.md`. Also read one pair from `${CLAUDE_PLUGIN_ROOT}/skills/no-slops/references/slop-vs-gold.md` so the bar is familiar before you start.

Write within those limits: no em dashes, and watch what replaces them (§5). No adverbs; if a verb needs help, pick a stronger verb (§3). No fingerprint openers, no inflated copulas, no recap closers (§7). No Tier 1 vocabulary in any voice, including a team member's.

No-slops still runs at the end, but as a check. If it finds something, the failure happened here.

## 1. The promise, written above the draft

Write one sentence, for yourself, at the top of the page: who this is for and what they'll walk away with. Not the topic. The takeaway. Craft's intake produces this sentence; here it becomes the test for every section.

- Topic: "This post is about AI prototyping for enterprise teams."
- Promise: "An enterprise PM leaves knowing the three approval gates that stall AI prototypes, and what to bring to each one."

If the sentence won't come, the piece has no thesis yet. Return to research, because drafting won't produce one. Once the sentence exists, every section gets checked against it, and anything that doesn't serve it is a favorite line that should be cut before drafting.

## 2. The lead

The opening sets the whole piece's direction and makes a promise about what kind of piece it is. The piece has to keep that promise.

**Start with the thing, not the topic.** Open on a specific fact, number, person, or scene. Don't open on a category, an era, or a landscape. An opening that names a subject without saying anything about it isn't a lead.

- Topic: "AI app builders are changing how enterprise teams think about prototyping."
- Thing: "A designer at an insurance company built in one afternoon what her engineering queue had estimated at six weeks."

**The first sentence has to be arguable or picturable.** If no reader could disagree with it and no reader can see it, it's a warm-up.

**Draft past the warm-up, then cut back to the start.** First drafts often clear their throat for a paragraph. That's thinking, and it's fine. Delete the opening paragraph and reread. Usually the piece still works without it, which means the real lead was in paragraph two.

**Keep the promise.** Don't open with a statistic the piece never returns to. Don't promise how and deliver why. If the lead and the body disagree, fix whichever one is wrong.

## 3. Sentence construction

Five rules, applied as you write.

**The doer is the subject, the action is the verb.** Nouns ending in -tion, -ment, -ness, or -ity are often verbs disguised as nouns, and they drag the sentence into abstraction. "The implementation of the migration produced improved build times" hides both the actor and the action. "We migrated, and builds got faster" hides nothing. red-pen catches these during edits; write them out in the first draft.

**Subject and verb in the first six words.** Qualify after you've said who did what. A sentence that opens with three clauses of hedging makes the reader wait for the point.

**End on the payload.** The last position before the period carries the most weight, so put the number, the name, or the claim there. "The new onboarding flow drove a 40% jump in signups" lands. "A 40% jump in signups followed from the new onboarding flow" trails off. Apply this to every sentence that matters: claims, openers, closers, headers.

**Use verbs a camera could record.** Cut, ship, stall, drain, break. If the verb can't be filmed, a stronger one is usually hiding in a noun or an adjective. "Provides acceleration for" is "speeds up" in formal dress.

**Limit the copulas.** Plain "is" is better than "serves as," and no-slops removes the costume forms. But three "is" sentences in a row mean the paragraph has no action in it. That's an action shortage, so find what actually happens and write it.

## 4. Concreteness

Abstract writing persuades no one. Each step down from the abstract to the specific buys belief:

> faster iteration → prototype to stakeholder review in a day → she demoed on Tuesday what she scoped on Monday

**One breath, one anchor.** Any abstract claim touches something concrete in the same sentence or the next: a number, a name, an artifact, a date. A paragraph of pure principle gives the reader nothing to hold onto.

**The three-rules test while drafting.** Can the reader picture it? Can they count it or check it? Could it be false? That's the tone-and-guidelines test, applied at the moment of writing to headlines, claims, openers, and CTAs.

**Use the proper noun.** "Supabase migrations" beats "database tooling," which beats "infrastructure." A reader who knows the term trusts you more, and a reader who doesn't still trusts the precision.

**Let numbers carry belief.** A concrete figure needs no adjective around it. When a line turns abstract, don't decorate it; go find the specific.

## 5. Rhythm

Uniform sentence length makes clean copy sound lifeless. Vary it, and the sentences carry a sense of movement.

- **In any run of five sentences, at least one under eight words and one over twenty.** If three consecutive sentences are the same length, change one. Short sentences land points. A paragraph made only of short sentences reads like a drumbeat, though: readers start bracing for the next jab. Let one sentence run long and carry the argument, then stop.
- **Save the period for what matters.** A short sentence after a long build hits hardest. Don't spend it on filler.
- **Watch the substitution.** Without em dashes, drafts fill with colons and semicolons. no-slops §4 (punctuation displacement) sets the limit.
- **Read it aloud.** The ear catches a monotone the eye skips. no-slops does the same check at the end, and doing it while drafting is cheaper.

## 6. Paragraphs and flow

**One move per paragraph.** Make one claim, prove one claim, or turn the argument once. A paragraph that does all three is three paragraphs sharing a page. The topic sentence names the move, and the rest carries it out.

**Give each sentence a link backward.** Open each sentence with something the reader already holds (a word, a name, an idea from the last sentence) and close with the new thing. When a sentence opens on a subject nothing introduced, the reader feels a jolt, which is what people mean by "it doesn't flow." red-pen's cohesion check finds these in a finished draft; drafting with the link in place means there's nothing to find.

**Join with "but" or "therefore," not "and then."** If a paragraph could open with "additionally," it hasn't earned its spot. It should either push back on what came before (but) or follow from it (therefore, so). A run of "and then" paragraphs is a list dressed as an argument: either make each one a real turn or merge it into a neighbor.

**Let the weight be uneven.** Give the point you care about the long paragraph and the housekeeping a single line. Even coverage reads as generated. no-slops §6 asks for this texture after the fact, but it's cheaper to build it in.

Outlines follow the same rules, with sections in place of paragraphs: one move per section, but or therefore between sections, weight where it matters. craft's outline step applies them. An outline built from "and then" sections produces a list no matter how good the sentences are.

## 7. Endings

**End on a fact, an image, or a consequence, never a recap.** The reader has just read the piece. Recapping it is explaining a joke. The banned list already covers recap openers ("Ultimately...", "All in all..."). Land something new instead.

**The kicker is the second-best line.** The lead gets the best one. The kicker should be a specific with weight. If the last line could close any piece on the same topic, it doesn't close this one.

**Stop when the point is made.** The hardest rule: once you've made the point, end. If the final paragraph exists to tie things up, the piece really ended one paragraph earlier. Cut it and check.

**For conversion copy, the kicker sets up the ask.** The call to action isn't the ending; the line before it is. A call to action carries only as much weight as the sentence before it has earned.

## 8. The cut

After the draft is done, cut about a tenth of it. Then read it aloud once. The cuts, in the order they usually pay off:

1. **The opening paragraph** (see §2; it was likely a warm-up).
2. **Adverbs.** no-slops removes them anyway, so do it here first.
3. **"That"** wherever the sentence still works without it.
4. **Chains of prepositions.** "The utilization of this approach by the team" is a sentence with five prepositions that means "the team used it."
5. **Favorite lines.** Anything kept because it sounds good, and doesn't serve the promise from §1. It hurts to cut, and the piece improves.

Track the cut rate. Under 5% suggests the pass didn't really happen. Over 25% means the draft was loose; next time, write tighter from the start.

---

## Where this file fits

| File | Job | When |
|---|---|---|
| **prose-craft.md** (this file) | How to build the prose | Outline and draft |
| **no-slops** | What a tell looks like, plus the 35/50 gate | Before drafting (pass 0), and as the final check |
| **tone-and-guidelines** | Voice, house style, the three-rules test | Always |
| **slop-vs-gold.md** | The standard, shown by example | Before drafting |
| **red-pen** | The same principles, applied as diagnostics to a finished draft | Edit time |

red-pen's lenses (stress position, cohesion, thought verbs, stance) are these rules applied to a draft that already exists. If red-pen keeps flagging the same lens, reread the matching section here: the fix belongs in drafting.
