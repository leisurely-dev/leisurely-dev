#!/usr/bin/env python3
"""Render assets/activity.svg from the public API.

Runs on a schedule in GitHub Actions and commits the result when it changes,
so the card on the profile stays current without depending on a third-party
image service. Two blocks: recent public events, then the current public
repos sorted by last push.
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
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"

WIDTH = 880
LEFT = 32
TEXT_X = 50
RIGHT = WIDTH - 28
TOP = 40          # baseline of the first section label
LINE = 27         # event row spacing


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
    if not ts:
        return ""
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
        return "created %s %s" % (payload.get("ref_type", "repository"), repo)
    if kind == "PullRequestEvent":
        return "%s a pull request in %s" % (payload.get("action", "opened"), repo)
    if kind == "IssuesEvent":
        return "%s an issue in %s" % (payload.get("action", "opened"), repo)
    if kind == "ReleaseEvent":
        return "published a release in " + repo
    return "%s in %s" % (kind.replace("Event", "").lower(), repo)


def ellipsize(text, limit=58):
    return text if len(text) <= limit else text[: limit - 1] + "\u2026"


def build(events, repos, stamp):
    y = TOP + 34
    rows = []
    for line, when in events:
        rows.append((y, "event", line, when))
        y += LINE
    if not events:
        rows.append((y, "empty", "nothing public yet", ""))
        y += LINE

    repo_label_y = y + 12
    first_repo_y = repo_label_y + 30
    height = (first_repo_y + 26 * max(len(repos) - 1, 0) + 26) if repos else repo_label_y + 30

    out = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" '
        'role="img" aria-label="recent GitHub activity">' % (WIDTH, height, WIDTH, height),
        "  <defs>",
        '    <linearGradient id="edge" x1="0" y1="0" x2="1" y2="0">',
        '      <stop offset="0%%" stop-color="%s" stop-opacity="0.55"/>' % ACCENT,
        '      <stop offset="100%%" stop-color="%s" stop-opacity="0"/>' % ACCENT,
        "    </linearGradient>",
        "  </defs>",
        '  <rect x="0.5" y="0.5" width="%d" height="%d" rx="10" fill="%s" stroke="%s"/>'
        % (WIDTH - 1, height - 1, CARD, EDGE),
        '  <rect x="0.5" y="0.5" width="%d" height="1.5" rx="1" fill="url(#edge)"/>' % (WIDTH - 1),
        '  <g font-family="%s">' % MONO,
        '    <text x="%d" y="%d" font-size="11" letter-spacing="2.2" fill="%s">RECENT ACTIVITY</text>'
        % (LEFT - 4, TOP, MUTED),
        '    <text x="%d" y="%d" font-size="11" fill="%s" text-anchor="end">%s</text>'
        % (RIGHT, TOP, MUTED, escape(stamp)),
    ]

    for row in rows:
        if row[1] == "event":
            yy, _kind, line, when = row
            out.append('    <circle cx="%d" cy="%d" r="3" fill="%s"/>' % (LEFT, yy - 4, ACCENT))
            out.append('    <text x="%d" y="%d" font-size="14" fill="%s">%s</text>' % (TEXT_X, yy, TEXT, escape(line)))
            out.append('    <text x="%d" y="%d" font-size="11" fill="%s" text-anchor="end">%s</text>'
                       % (RIGHT, yy, MUTED, escape(when)))
        else:
            yy, _kind, line, _ = row
            out.append('    <text x="%d" y="%d" font-size="14" fill="%s">%s</text>' % (TEXT_X, yy, MUTED, escape(line)))

    out.append('    <text x="%d" y="%d" font-size="11" letter-spacing="2.2" fill="%s">PUBLIC REPOS</text>'
               % (LEFT - 4, repo_label_y, MUTED))

    for i, (name, lang, when) in enumerate(repos):
        yy = first_repo_y + i * 26
        out.append('    <circle cx="%d" cy="%d" r="2.5" fill="#2f6b8a"/>' % (LEFT, yy - 4))
        out.append('    <text x="%d" y="%d" font-size="14" fill="%s">%s</text>' % (TEXT_X, yy, TEXT, escape(name)))
        out.append('    <text x="%d" y="%d" font-size="11" fill="%s" text-anchor="end">%s \u00b7 %s</text>'
                   % (RIGHT, yy, MUTED, escape(lang), escape(when)))

    out.append("  </g>")
    out.append("</svg>")
    return "\n".join(out) + "\n"


def main():
    limit = int(os.environ.get("LIMIT", "5"))
    try:
        events = get("/users/%s/events/public?per_page=40" % USER)
        repos = get("/users/%s/repos?sort=pushed&per_page=6" % USER)
    except Exception as exc:  # keep the previous card rather than shipping a broken one
        print("fetch failed: %s" % exc, file=sys.stderr)
        return 1

    seen, picked = set(), []
    for ev in events:
        line = describe(ev)
        if line in seen:
            continue
        seen.add(line)
        picked.append((ellipsize(line), ago(ev["created_at"])))
        if len(picked) >= limit:
            break

    repo_rows = [(r["name"], r.get("language") or "mixed", ago(r.get("pushed_at")))
                 for r in repos if r["name"] != USER and not r.get("fork")]
    if not repo_rows:
        repo_rows = [(r["name"], r.get("language") or "mixed", ago(r.get("pushed_at")))
                     for r in repos if r["name"] != USER]

    svg = build(picked, repo_rows[:3], "updated " + dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d"))
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
