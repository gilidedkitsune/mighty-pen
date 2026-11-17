---
name: seo-geo
description: >
  Part of the Insights plugin, and dormant until connected. If Google Analytics 4 and Search
  Console aren't set up on this machine, it says so in one line and stops. Once set up, it reads
  the site's real traffic and search numbers (GA4 sessions by channel; Search Console clicks,
  impressions, CTR, and position by query or page) as the signed-in user, and it keeps a map of
  which SEO tools are connected and which are gated. Trigger on "how's our traffic", "traffic by
  channel", "top search queries", "what are we ranking for", "Search Console", "GSC", "GA4",
  "organic clicks", "impressions", "CTR", or when a report or content refresh needs real numbers.
  AI-answer visibility belongs to aeo-insights, not here. Not for writing or editing.
---

# seo-geo

Reads your site's real numbers and says what SEO data is and isn't connected. It runs through your own Google sign-in, read-only. It never fills a gap with an estimate.

## Check connection first

Before anything else, check whether this machine is set up. The check: `~/.config/claude-seo/token.json` exists, and `python3 ${CLAUDE_PLUGIN_ROOT}/skills/seo-geo/scripts/seo_pull.py ga4 --days 1` returns data.

- **Not set up:** say so in one line ("GA4 and Search Console aren't connected here, so I have no live numbers") and stop. Don't walk through setup unless asked, don't estimate, and don't hold up the task that called you. The writing skills carry on with whatever the user supplied.
- **Set up, sign-in expired:** say so, offer to run `auth`, and wait for the answer.
- **Set up and working:** continue below.

Other skills call this one only when Insights is installed. If a skill asks for data and this check fails, the answer is "not connected," never a number.

## What's connected, and what isn't

The rule: **if a source isn't connected, don't invent its output.** Skip the step and say so, or ask the user for the data. Never make up search volumes, difficulty scores, rankings, or traffic.

**Google, for your site (once set up).** Read-only, as the signed-in user.
- **GA4:** sessions, users, engagement rate, and page views by default channel group (organic search, direct, referral, and so on). Answers: how much traffic, from where, and how engaged.
- **Search Console:** impressions, clicks, CTR, and average position by query or by page. Answers: what the site ranks for, and how it performs in Google.

**AI-answer visibility** (named versus cited, per engine, competitors) is not this skill's job. It belongs to `aeo-insights`, which has its own connection check and its own rule against mixing numbers across tools.

**Not connected, keep gated:**
- **DataForSEO** (live SERP data, search volume, keyword difficulty). The data parts of `/keyword-research`, `/serp-analysis`, `/seo-cluster`, `/seo-content-brief`, `/seo-dataforseo`, `/competitor-analysis`, and `/seo-backlinks` need it.
- **Firecrawl** (full-site crawling): `/seo-firecrawl` and the crawl steps in `/seo-audit`.
- **PageSpeed and CrUX** (Core Web Vitals field data): not wired. The generic `/seo-google` skill covers these if it's installed; for GA4 and Search Console, this skill's puller is preferred.
- **Domain authority data:** `/domain-authority-auditor` needs an external authority source.

**Works with no backend** (judgment and logic, no live data): `/content-strategy`, `/meta-tags-optimizer`, `/schema-markup-generator`, `/internal-linking-optimizer`, and any trend scan done by web search. For AI-citation structure, fresh-ink's `search-weave` runs on the keywords and citations the user supplies, with no backend needed. AI-visibility measurement is `aeo-insights`. Social and email repurposing is fresh-ink's `socialize`.

Installing DataForSEO or Firecrawl is a one-time setup for whoever maintains the tools. It isn't a content task, so don't do it mid-draft.

---

## Pulling data

The puller is `${CLAUDE_PLUGIN_ROOT}/skills/seo-geo/scripts/seo_pull.py`. Run it with the system `python3`. Once `config.json` is set up, the commands need no arguments. Otherwise pass `--property` or `--site` on each call.

```bash
# GA4: traffic by channel, last 28 days (default)
python3 ${CLAUDE_PLUGIN_ROOT}/skills/seo-geo/scripts/seo_pull.py ga4
python3 ${CLAUDE_PLUGIN_ROOT}/skills/seo-geo/scripts/seo_pull.py ga4 --days 90

# Search Console: top queries, last 28 days (default)
python3 ${CLAUDE_PLUGIN_ROOT}/skills/seo-geo/scripts/seo_pull.py gsc
python3 ${CLAUDE_PLUGIN_ROOT}/skills/seo-geo/scripts/seo_pull.py gsc --dimension page --limit 50 --days 90

# List the GA4 properties this account can read (to find an ID)
python3 ${CLAUDE_PLUGIN_ROOT}/skills/seo-geo/scripts/seo_pull.py properties

# One-time, or when a pull fails with an auth error: sign in again
python3 ${CLAUDE_PLUGIN_ROOT}/skills/seo-geo/scripts/seo_pull.py auth
```

The output is JSON from Google's APIs. Read the numbers from it as they are; don't round or dress them up. A GA4 response has rows of channel → sessions, users, engagement rate, and page views. A Search Console response has rows of query or page → clicks, impressions, CTR, and position.

**Two things to know about the numbers:**
- **Search Console lags two to three days.** The `gsc` command already ends its window three days back, so "last 28 days" means the 28 days ending three days ago. Don't expect yesterday's search data.
- **A GA4 account can span several properties.** If the account can see more than one (a help center, a status page, staging), pass `--property` to pick the right one. Run `properties` to get the IDs.

If `ga4` or `gsc` returns an auth error, the sign-in has expired: run `auth` and retry. If it reports a missing client, the one-time setup hasn't been done.

### Feeding other skills

When a report, a content refresh, or a brief needs real traffic or search figures, pull them here first and pass the JSON along. For AI-answer figures, run `aeo-insights` and pass its numbers with their window. The point of a connected source is that downstream skills stop guessing.

For which SEO skill to run at which stage of a content project, see `${CLAUDE_PLUGIN_ROOT}/skills/seo-geo/references/seo-geo-toolkit.md`. This file says what's connected and how to pull it. The toolkit says what to run and when.

---

## One-time setup

Each person does this once, on their own machine, with their own Google account. It takes about ten minutes. For someone who isn't comfortable in a terminal, the assistant can run the commands and the person only clicks through Google's screens.

**Access first.** The account you sign in with has to see the site already: at least Viewer on the GA4 property and at least Full or Restricted in Search Console. Read access is enough, and this skill never writes. If the account can't see the data in the GA4 or Search Console web interfaces, fix that first.

1. **Create a Google Cloud project** at console.cloud.google.com (any name, for example `site-insights`).
2. **Enable three APIs** for that project: the Google Analytics Data API, the Google Analytics Admin API (needed for the `properties` command), and the Google Search Console API.
3. **Set up the OAuth consent screen.** User type External, with the signing-in account added as a test user. External with testing works; see the expiry note below.
4. **Create an OAuth client** of type Desktop app, and download its JSON.
5. **Save that file** as `~/.config/claude-seo/oauth_client.json`. Create the folder if it doesn't exist.
6. **Install the Python packages:** `pip install google-auth google-auth-oauthlib google-api-python-client`
7. **Sign in:** run `seo_pull.py auth`. A browser opens. Approve the read-only scopes. This writes `~/.config/claude-seo/token.json`.
8. **Set the property.** Create `~/.config/claude-seo/config.json` with `{"ga4_property": "properties/<id>", "gsc_site": "sc-domain:<your-domain>"}`. Run `properties` first to find the GA4 ID.

**Why sign in as the user rather than using a service account.** A service account would have to be added to the GA4 property and to Search Console with admin-level rights. Most people have Editor in GA4 and Full in Search Console, which is enough to read through the API but not enough to add a service account. Signing in as yourself uses the access you already have, with no admin changes.

**Sign-in expiry.** While the consent screen is in External and testing mode, Google expires the saved sign-in roughly every week. When a pull fails with an auth error, run `auth` again. If the Google Workspace admin allows it, moving the project to Internal removes the weekly expiry.

---

## Sharing and credentials

This skill can go to teammates or an agency. Keep it safe:

- **The skill has no secrets.** It contains `SKILL.md`, the puller, and the references. Credentials live in `~/.config/claude-seo/`, outside the skill, so copying the skill never copies a password.
- **Each person uses their own credentials.** Everyone runs the one-time setup with their own Google account, and that account needs access to the site's data. Nobody shares `token.json` or `oauth_client.json`.
- **Treat `oauth_client.json`, `token.json`, and `config.json` like passwords.** Don't paste them into chat, commit them to a repo, put them in the skill folder, or send them by email or chat. If one leaks, delete the OAuth client in Google Cloud Console and create a new one.
- **The IDs in `config.json` aren't secret** (a GA4 property number and a domain), but treat them as internal, because they show which site this points at.
