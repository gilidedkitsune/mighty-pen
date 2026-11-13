#!/usr/bin/env python3
"""Pull GA4 traffic and Google Search Console performance for one site, read-only.

Authentication is OAuth as the signed-in user. The user's own access in Analytics and
Search Console is what gets read; no service account has to be added anywhere.

Credentials and settings live in ~/.config/claude-seo/, outside the plugin:
  oauth_client.json   Desktop-app OAuth client downloaded from Google Cloud
  token.json          saved sign-in, written by the `auth` command
  config.json         {"ga4_property": "properties/<id>", "gsc_site": "sc-domain:<domain>"}

Nothing is hard-coded. Pass --property or --site on a call to override config.json.

Commands:
  auth          sign in once in the browser and save the token
  properties    list the GA4 properties this account can read
  ga4           sessions, users, engagement rate, and views by default channel group
  gsc           clicks, impressions, CTR, and position by query or page

Dependencies: pip install google-auth google-auth-oauthlib google-api-python-client
"""

import argparse
import json
import os
import sys
from datetime import date, timedelta
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse
import webbrowser

SETTINGS_DIR = os.path.expanduser("~/.config/claude-seo")
CLIENT_FILE = os.path.join(SETTINGS_DIR, "oauth_client.json")
TOKEN_FILE = os.path.join(SETTINGS_DIR, "token.json")
CONFIG_FILE = os.path.join(SETTINGS_DIR, "config.json")
AUTH_URL_FILE = os.path.join(SETTINGS_DIR, "auth_url.txt")

READ_ONLY_SCOPES = [
    "https://www.googleapis.com/auth/analytics.readonly",
    "https://www.googleapis.com/auth/webmasters.readonly",
]
CALLBACK_PORT = 8765
CALLBACK_URI = f"http://localhost:{CALLBACK_PORT}/"
SEARCH_CONSOLE_LAG_DAYS = 3  # Search Console data settles two to three days late


def read_settings():
    if not os.path.exists(CONFIG_FILE):
        return {}
    with open(CONFIG_FILE) as fh:
        return json.load(fh)


def setting(name):
    return read_settings().get(name)


def load_credentials():
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials

    if not os.path.exists(TOKEN_FILE):
        sys.exit("No saved sign-in yet. Run the `auth` command first.")
    creds = Credentials.from_authorized_user_file(TOKEN_FILE, READ_ONLY_SCOPES)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        with open(TOKEN_FILE, "w") as fh:
            fh.write(creds.to_json())
    return creds


def run_sign_in(_args):
    if not os.path.exists(CLIENT_FILE):
        sys.exit(
            f"No OAuth client found at {CLIENT_FILE}. Download a Desktop-app client from "
            "Google Cloud Console and save it there (setup steps are in SKILL.md)."
        )
    from google_auth_oauthlib.flow import Flow

    flow = Flow.from_client_secrets_file(CLIENT_FILE, scopes=READ_ONLY_SCOPES, redirect_uri=CALLBACK_URI)
    url, _ = flow.authorization_url(access_type="offline", prompt="consent", include_granted_scopes="true")
    with open(AUTH_URL_FILE, "w") as fh:
        fh.write(url)
    print("Open this link to sign in: " + url, flush=True)

    received = {}

    class CallbackHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            query = parse_qs(urlparse(self.path).query)
            if "code" in query:
                received["code"] = query["code"][0]
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h2>Signed in. You can close this tab.</h2>")

        def log_message(self, *_):
            return

    server = HTTPServer(("localhost", CALLBACK_PORT), CallbackHandler)
    try:
        webbrowser.open(url)
    except Exception:
        pass
    while "code" not in received:
        server.handle_request()
    flow.fetch_token(code=received["code"])
    with open(TOKEN_FILE, "w") as fh:
        fh.write(flow.credentials.to_json())
    print("Signed in. Token saved to " + TOKEN_FILE)


def list_properties(_args):
    from googleapiclient.discovery import build

    service = build("analyticsadmin", "v1beta", credentials=load_credentials(), cache_discovery=False)
    summaries = service.accountSummaries().list().execute()
    rows = []
    for account in summaries.get("accountSummaries", []):
        for prop in account.get("propertySummaries", []):
            rows.append({
                "property": prop.get("property"),
                "name": prop.get("displayName"),
                "account": account.get("displayName"),
            })
    print(json.dumps(rows, indent=2))


def traffic_by_channel(args):
    from googleapiclient.discovery import build

    prop = args.property or setting("ga4_property")
    if not prop:
        sys.exit("No GA4 property. Pass --property, or set ga4_property in config.json.")
    prop = prop if prop.startswith("properties/") else f"properties/{prop}"
    service = build("analyticsdata", "v1beta", credentials=load_credentials(), cache_discovery=False)
    request_body = {
        "dateRanges": [{"startDate": f"{args.days}daysAgo", "endDate": "yesterday"}],
        "dimensions": [{"name": "sessionDefaultChannelGroup"}],
        "metrics": [{"name": n} for n in ("sessions", "totalUsers", "engagementRate", "screenPageViews")],
        "orderBys": [{"metric": {"metricName": "sessions"}, "desc": True}],
    }
    report = service.properties().runReport(property=prop, body=request_body).execute()
    print(json.dumps(report, indent=2))


def search_performance(args):
    from googleapiclient.discovery import build

    site = args.site or setting("gsc_site")
    if not site:
        sys.exit("No Search Console property. Pass --site, or set gsc_site in config.json.")
    service = build("webmasters", "v3", credentials=load_credentials(), cache_discovery=False)
    end = date.today() - timedelta(days=SEARCH_CONSOLE_LAG_DAYS)
    start = end - timedelta(days=args.days)
    request_body = {
        "startDate": start.isoformat(),
        "endDate": end.isoformat(),
        "dimensions": [args.dimension],
        "rowLimit": args.limit,
    }
    result = service.searchanalytics().query(siteUrl=site, body=request_body).execute()
    print(json.dumps(result, indent=2))


def build_parser():
    parser = argparse.ArgumentParser(description="Read-only GA4 and Search Console pulls, signed in as the user.")
    commands = parser.add_subparsers(dest="command", required=True)

    commands.add_parser("auth", help="sign in once and save the token").set_defaults(run=run_sign_in)
    commands.add_parser("properties", help="list readable GA4 properties").set_defaults(run=list_properties)

    ga4 = commands.add_parser("ga4", help="traffic by channel")
    ga4.add_argument("--property", help="GA4 property, e.g. properties/123456789")
    ga4.add_argument("--days", type=int, default=28)
    ga4.set_defaults(run=traffic_by_channel)

    gsc = commands.add_parser("gsc", help="search performance")
    gsc.add_argument("--site", help="Search Console property, e.g. sc-domain:example.com")
    gsc.add_argument("--dimension", choices=["query", "page"], default="query")
    gsc.add_argument("--days", type=int, default=28)
    gsc.add_argument("--limit", type=int, default=25)
    gsc.set_defaults(run=search_performance)
    return parser


def main():
    args = build_parser().parse_args()
    args.run(args)


if __name__ == "__main__":
    main()
