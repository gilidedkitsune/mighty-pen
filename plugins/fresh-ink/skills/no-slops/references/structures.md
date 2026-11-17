# The structure catalog

The reference behind no-slops §2. Each entry is a sentence or paragraph shape that models produce far more often than people do. One instance can be a choice; a habit is a fingerprint. Entries are grouped by what the shape is trying to fake.

Every entry gives the shape, an example, and the repair. Examples are illustrative and invented.

---

## A. Fake drama

### Binary contrasts / negation-reframes
Building a wrong frame only to correct it.

| Shape | Example |
|---|---|
| It's not X, it's Y | "It's not a CRM. It's a relationship engine." |
| X isn't the problem, Y is | "Hiring isn't your bottleneck. Onboarding is." |
| The question isn't X, it's Y | "The question isn't whether to migrate. It's when." |
| Not because X, because Y | "Not because it's cheaper. Because it's calmer." |
| Seems like X, really Y | "It looks like a pricing problem. It's a packaging problem." |
| Stops being X, starts being Y | "Docs stop being a chore and start being a product." |
| Not just X, but Y | "Not just faster, but smarter." |
| Forget X / Less X, more Y | "Forget dashboards. Think decisions." "Less noise, more signal." |

**Repair:** state Y with its reason. "Onboarding is the bottleneck: new hires wait nine days for access."

### Negative listing
Several "not" items before the reveal. "It wasn't the price. It wasn't the timing. It was trust." **Repair:** say what it was and why.

### Dramatic fragmentation
Fragments used as drumbeats. "Built for speed. Built for scale. Built for you." "One login. Every tool. Zero friction." "That's it. That's the product." **Repair:** a full sentence carrying the actual claim.

### Rhetorical setups
Announcing an insight instead of delivering it. "What if everything you knew about churn was wrong?" "Let that framing settle for a second." "Here's the kicker:" "And honestly? That's fine." "You can't unsee it once you see it." "Aphorism as proof: what gets measured gets managed." **Repair:** make the point and let the reader react.

### Significance inflation
Treating routine events as history. "Marks a watershed moment for the category." "Cements its place in the story of..." "Plays an indispensable role in..." "Leaves a lasting legacy." **Repair:** what happened, with a number, a name, or a consequence. Real significance survives the plain version.

---

## B. Missing people

### False agency
Things doing what people do, so no one has to be named. "The backlog spoke for itself." "The pivot happened organically." "The numbers pushed us toward..." "The market punished the launch." **Repair:** name who acted ("Support flagged it; Dev fixed it Tuesday"), or use "you."

### Narrator-from-a-distance
Commentary from above the scene. "Organizations rarely plan for this." "There's a reason teams end up here." "Humans are wired to..." **Repair:** put the reader inside it: a named team, a real moment, "you."

### Passive defaults
"A decision was made." "It's been decided that." "Concerns were raised." **Repair:** who decided, who raised them. (Passive on purpose is fine; see no-slops §3.)

---

## C. Fake depth

### Superficial -ing analyses
A participle phrase tacked onto the end of a sentence to sound analytical. "The team shipped weekly, reflecting a deeper commitment to iteration." "Revenue doubled, signaling a shift in buyer priorities." **Repair:** stop at the fact. If the meaning is real, give it its own sentence with something checkable.

### False ranges
"From X to Y" with endpoints on no real scale. "From side projects to global banks." "Everything from onboarding to offboarding and beyond." **Repair:** name the actual set, or two real examples.

### Arguing with no one
Rebutting an objection the reader never raised, often a leftover from the writer's own thinking. "To be clear, this isn't a rewrite." "I'm not saying process is bad." "Some will call this overkill." "You might be tempted to just add a cache." **Repair:** delete the rebuttal and make the claim. Keep an objection only when a real person raised it and you answer it fully.

### Vague connection
A relationship asserted without being named. "Burnout is linked to on-call load." "She's associated with the Series B." **Repair:** say the relationship the source gives (caused, correlated in one survey, led, invested). If the source doesn't say, keep it vague and flag it rather than inventing a role.

### Wisdom-shaped closers on every paragraph
Each paragraph ends with a line that could be a poster. "And that's the whole game." "Simple, but not easy." **Repair:** end some paragraphs on the plain last fact.

---

## D. Mechanical repetition

### Repeated sentence openings
Three sentences in a row starting with the same subject ("The tool syncs. The tool flags. The tool fixes.") or three paragraphs opening "Our team...". **Repair:** merge, change the subject, or lead with the action. Deliberate anaphora in a speech is craft.

### Heading restated by its first sentence
> **Security**
>
> Security is a priority.

**Repair:** delete the echo; open on the content.

### Synonym cycling
Rotating names for one thing to avoid repeating it: customers, then clients, then users, then members. **Repair:** pick the right term and keep it. Repetition of the correct word is clarity.

### Crutch openers
"What makes this work is...", "The thing about X is...", "So," to open a paragraph, "Look," anywhere. **Repair:** start with the subject or the verb.

---

## E. Endings

### Stock conclusions
"Despite the hurdles, the team remains committed to..." "As the space matures, X will only grow in importance." A last paragraph that summarizes the piece. **Repair:** end on the strongest specific point. Long reports that need a summary should summarize the argument, not the table of contents.

### Soft hedged reassurance
"Not always. Not perfectly. But often enough." **Repair:** give the real frequency or condition.

---

## F. Rhythm and word habits

| Habit | Repair |
|---|---|
| Lists of three by default | Two, or the real number |
| A question answered in the very next sentence | Ask only questions you'll let breathe, or cut the question |
| Every paragraph closes on a zinger | Vary the endings |
| More than two short punchy sentences in a row | Combine or lengthen one |
| Sweeping quantifiers (always, never, everyone, nobody, every single) | The real scope |
| Adverbs of any kind | Cut; fix the verb (banned.md, Part 4) |
| A hyphenated compound kept after the noun ("the plan is long-term") | Hyphenate before the noun (a long-term plan), not after (the plan is long term). A slip alone; a pattern in bulk |
| Em dashes | Comma, period, colon, semicolon, or parentheses |

---

## G. Formatting reflexes

Prose only; social platforms have their own conventions (no-slops §9).

| Reflex | Repair |
|---|---|
| Every bullet starts with a bolded label and a colon | One such list per piece, only for truly parallel items; otherwise prose |
| Bold sprinkled through paragraphs with no rule | Bold a defined term or one real emphasis, rarely |
| Emoji or arrows as bullets or header decoration | Remove outside social |
| A colon-hinged sentence in every paragraph | One per paragraph at most |
| Lists doing a paragraph's job, several per screen | Write the paragraph |
| Curly quotes inside code, commands, JSON, or config | Straight quotes; curly ones break the code |

---

## H. Writing about the document instead of the subject

| Shape | Example | Repair |
|---|---|---|
| Narrating edits in reference docs | "This endpoint was added to support exports." | "This endpoint exports..." (changelogs excepted) |
| Describing the page instead of using it | "The table below shows the differences." | Put a plain one-line lead-in only if it adds meaning; otherwise let the table speak |
| Then-and-now framing where only "now" matters | "Previously this required a restart; now it doesn't." | "Changes apply without a restart." |

---

## I. Register breaks

Word-level mixing (a technical term beside a casual one) is good texture (no-slops §6). The tell is different: a whole section that suddenly turns formal or chatty for no reason, as if pasted from another document. **Repair:** read the piece aloud in one sitting and smooth any seam the content doesn't explain (a quote, a disclaimer, a change of speaker).

---

## J. Context-dependent: question-shaped headers

| Context | Call |
|---|---|
| Ordinary blog sections, essays, docs | A tell. "So, Why Does This Matter?" does less than a stated header ("What a delay costs"). |
| Pieces built for search and AI answers (search-weave) | Correct and intended: headers phrased as the reader's question are what engines match and lift. |

Check the content type before flagging.
