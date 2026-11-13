# Third-party notices

Mighty Pen's text is original, but some of its ideas, data, and reference points come from
outside sources. This file lists them, what each one contributed, and its license or terms.
It's a record, not legal advice. If you publish or sell anything built on this repo, check each
source's current terms yourself.

## Data

**Concreteness norms** (`plugins/red-pen/skills/red-pen/scripts/concreteness.csv`)
- Source: Brysbaert, M., Warriner, A. B., & Kuperman, V. (2014). Concreteness ratings for 40 thousand generally known English word lemmas. *Behavior Research Methods*, 46(3).
- Used for: the concreteness score in red-pen's readability script.
- Terms: the file's own header says "CC-derived, research use." Confirm the dataset's current license before any commercial use.

## Reference catalogs and frameworks

**AI-writing tells** (`plugins/fresh-ink/skills/no-slops/`)
- Wikipedia, "Signs of AI writing," maintained by WikiProject AI Cleanup. Content is licensed CC BY-SA 4.0. The catalog structure and some entries started from this page. Attribution and share-alike terms apply to material taken from it; the wording in no-slops is rewritten, but the derivation is real.
- blader/humanizer (v3.0.0), MIT License. Cross-checked for coverage.
- Aboudjem/humanizer-skill, MIT License. Cross-checked for coverage.

**Social platform guidance** (`plugins/fresh-ink/skills/socialize/`)
- coreyhaines31/marketingskills, `skills/social`, MIT License (© Corey Haines). Structure and ideas for platform references and the content-atom model.
- aaaronmiller/create-viral-content, license MIT as stated in its skill metadata. Brief-first workflow, platform rules, and the change log for mid-2026 platform updates.
- charlie947/social-media-skills, `skills/post-writer`, MIT License (© Charlie Hills). Angle selection before drafting and code-block output.
- heyashishsaini/writing-post-skills, MIT (per its README badge). Separate LinkedIn and X skills that verify news facts before drafting.
- Full list and links: `plugins/fresh-ink/skills/socialize/references/sources.md`.

**Advertising and persuasion** (`plugins/fresh-ink/skills/craft/references/`, `plugins/fresh-ink/skills/ogilvy-copywriting/`)
- David Ogilvy, *Confessions of an Advertising Man* (1963), *How to Create Advertising That Sells* (1972), and *Ogilvy on Advertising* (1983). Principles are paraphrased; no passages are quoted at length.
- Eugene Schwartz, *Breakthrough Advertising* (1966). The awareness and market-sophistication framework is paraphrased and reorganized.

**Search and AI-answer writing** (`plugins/fresh-ink/skills/craft/references/SEO-GEO-drafting.md`)
- Aggarwal et al., generative-engine optimization study, KDD 2024 (arXiv 2311.09735). Source of the citation-lever ranking; the figures are cited as directional.
- Google Search Central guidance on helpful content and expertise.

**Platform mechanics** (`plugins/insights/`, socialize references)
- X's open-sourced ranking code, xai-org/x-algorithm, used as a reference for what the ranker scores. The weights are not published there.

## Public facts and examples

Historical campaign examples used in teaching material (for instance in no-slops' slop-vs-gold file) are paraphrased and cited by name and year. They're public record, but the lines themselves belong to their owners and aren't reproduced at length.

## Tools this repo calls at runtime

These aren't bundled. Users connect them themselves: Google Analytics, Google Search Console, and Cairrot (AI-answer visibility). Each has its own terms of service.
