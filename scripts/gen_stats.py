#!/usr/bin/env python3
"""Render assets/activity.svg from the public events feed.

Runs on a schedule in GitHub Actions and commits the result when it changes,
so the card on the profile stays current without depending on a third-party
image service.
"""

import datetime as dt
import json
import os
import os.path as p
import sys
import urllib.request
from xml.sax.saxutils import escape

USER = os.environ.get("GH_USER", "leisurely-dev")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
API = "https://api.github.com"
OUT = p.join(p.dirname(p.dirname(p.abspath(__file__))), "assets", "activity.svg")

ACCENT = "#00c6ff"
MUTED = "#5b7183"
TEXT = "#c9d1d9"
CARD = "#0d1117"
EDGE = "#1f3547"


def get(path):
    req = urllib.request.Request(
        API + path,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": USER,
            **({"Authorization": "token " + TOKEN} if TOKEN else {}),
        },
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def ago(ts):
    then = dt.datetime.strptime(ts, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=dt.timezone.utc)
    secs = int((dt.datetime.now(dt.timezone.utc) - then).total_seconds())
    for unit, size in (("d", 86400), ("h", 3600), ("m", 60)):
        if secs >= size:
            return "%d%s ago" % (secs // size, unit)
    return "just now"


def describe(ev):
    kind = ev["type"]
    repo = ev.get("repo", {}).get("name", "")
    payload = ev.get("payload", {}) or {}
    if kind == "PushEvent":
        n = len(payload.get("commits", []) or [])
        return "pushed %d commit%s to %s" % (n, "" if n == 1 else "s", repo)
    if kind == "WatchEvent":
        return "starred " + repo
    if kind == "ForkEvent":
        return "forked " + repo
    if kind == "CreateEvent":
        ref_type = payload.get("ref_type", "repository")
        return "created %s %s" % (ref_type, repo or payload.get("ref", ""))
    if kind == "PullRequestEvent":
        return "%s a pull request in %s" % (payload.get("action", "opened"), repo)
    if kind == "IssuesEvent":
        return "%s an issue in %s" % (payload.get("action", "opened"), repo)
    if kind == "ReleaseEvent":
        return "published a release in " + repo
    return "%s in %s" % (kind.replace("Event", "").lower(), repo)


def build(items, stamp):
    h = 74 + 27 * (max(len(items), 1) - 1) + 32
    out = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="880" height="%d" viewBox="0 0 880 %d" '
        'role="img" aria-label="recent GitHub activity">' % (h, h),
        "  <defs>",
        '    <linearGradient id="edge" x1="0" y1="0" x2="1" y2="0">',
        '      <stop offset="0%%" stop-color="%s" stop-opacity="0.55"/>' % ACCENT,
        '      <stop offset="100%%" stop-color="%s" stop-opacity="0"/>' % ACCENT,
        "    </linearGradient>",
        "  </defs>",
        '  <rect x="0.5" y="0.5" width="879" height="%d" rx="10" fill="%s" stroke="%s"/>' % (h - 1, CARD, EDGE),
        '  <rect x="0.5" y="0.5" width="879" height="1.5" rx="1" fill="url(#edge)"/>',
        '  <g font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">',
        '    <text x="28" y="40" font-size="11" letter-spacing="2.2" fill="%s">RECENT ACTIVITY</text>' % MUTED,
        '    <text x="852" y="40" font-size="11" fill="%s" text-anchor="end">%s</text>' % (MUTED, escape(stamp)),
    ]
    y = 74
    for line, ts in items:
        out.append('    <circle cx="32" cy="%d" r="3" fill="%s"/>' % (y - 4, ACCENT))
        out.append('    <text x="50" y="%d" font-size="14" fill="%s">%s</text>' % (y, TEXT, escape(line)))
        out.append('    <text x="852" y="%d" font-size="11" fill="%s" text-anchor="end">%s</text>' % (y, MUTED, escape(ts)))
        y += 27
    if not items:
        out.append('    <text x="50" y="74" font-size="14" fill="%s">nothing public yet</text>' % MUTED)
    out.append("  </g>")
    out.append("</svg>")
    return "\n".join(out) + "\n"


def main():
    limit = int(os.environ.get("LIMIT", "5"))
    try:
        events = get("/users/%s/events/public?per_page=40" % USER)
    except Exception as exc:  # keep the previous card instead of shipping a broken one
        print("fetch failed: %s" % exc, file=sys.stderr)
        return 1

    seen, items = set(), []
    for ev in events:
        line = describe(ev)
        if line in seen:
            continue
        seen.add(line)
        items.append((line, ago(ev["created_at"])))
        if len(items) >= limit:
            break

    svg = build(items, "updated " + dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d"))
    old = open(OUT, encoding="utf-8").read() if p.exists(OUT) else ""
    if svg == old:
        print("no change")
        return 0
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(svg)
    print("wrote", OUT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
