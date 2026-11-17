# X

**Last checked:** November 2026. Tags: [platform] statement or published code, [study] third-party data with a sample, [reported] single or vendor source.

## Who's there and what they want
Tech, media, finance, and niche communities in real time. Fast, opinionated, allergic to marketing voice. Room for irreverence; the strongest posts sound like one sharp person, not a brand.

## How ranking works
X publishes its For You ranker as open source ([xai-org/x-algorithm](https://github.com/xai-org/x-algorithm)). The code shows **which** behaviors are scored, not their weights.
- [platform] The model predicts about 15 separate actions and sums them. Positive: like, reply, repost, quote, click into the post, **profile click**, **follow**, three kinds of **share (including via DM and copy link)**, photo expand, dwell (scored two ways), and video watch time above a minimum length.
- [platform] Predicted **"not interested," mute, block, and report** subtract from the score before anyone acts. Bait that looks like what people mute is penalized on sight.
- [platform] Muted keywords filter a post out **before** scoring.
- [platform] An author-diversity step decays each additional post from the same author in a feed, so back-to-back posts compete with each other.
- [platform] Posts and replies between mutual follows rank higher (July 2026).

What that means for writing: likes are the weakest lever. Write for the reply, the DM-forward ("would someone send this to a friend?"), the profile click, and the follow.

## What costs reach
- **Links,** for accounts without Premium. [study] Buffer has measured median engagement of 0% on non-Premium link posts since March 2025. Put the substance in the post and the link in the first reply or a quote post.
- **Bursts.** [reported] Space original posts about an hour apart.
- **Engagement bait and generic CTA phrases**, which are widely muted.

## Formats

### Single post
- **Limit:** 280 characters (Premium accounts can post up to 25,000; long posts truncate in the feed).
- **First 8 to 10 words:** the specific claim and the topic, by name. [reported] Topic routing depends on the model recognizing what the post is about; "Postgres" routes, "our database journey" doesn't.
- One idea. Specific nouns: tools, companies, numbers.
- No "🧵", no "A thread:", no hashtags beyond one or two, and usually none.

### Thread
Only when the material is a sequence (steps, a story, a teardown) of 4 to 8 posts.
- Post 1 stands alone and makes the promise; it's the only one most people see.
- Each post is one move and could be quoted on its own.
- No "1/" numbering unless it's a numbered list.
- The last post lands the point; the link goes in a reply after it.

### Reply
Inside the author's niche and mutual network beats cold replies under huge accounts. Add a fact, a counterexample, or a sharper version of the point.

### Quote post
[platform] Quotes earn engagement and click-throughs to the quoted post as two separate signals. Quote with an added insight rather than a bare repost.

### Video
[platform] Video only earns watch credit above a minimum duration ([reported] about 8 seconds). Captions on; most viewing is muted.

## Checklist
- [ ] Claim and topic in the first 8 to 10 words
- [ ] Specific nouns, no vague abstractions
- [ ] Written for a reply, a share, or a follow, not a like
- [ ] Link in a reply (unless the account has Premium and clicks are the goal)
- [ ] Under 280 characters per post
- [ ] Author can be around for the first 30 minutes to answer replies
