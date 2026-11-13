"""Build assets/activity.svg (desktop) and assets/activity-m.svg (phone) from REAL public GitHub activity.

Runs in GitHub Actions every day (see .github/workflows/activity.yml). Needs GITHUB_TOKEN in the env.
Usage: python scripts/activity.py [outdir]   (default: assets)
"""
import datetime as dt, json, os, sys, urllib.request

USER = os.environ.get("PROFILE_USER", "jaylalkiya")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
OUT = sys.argv[1] if len(sys.argv) > 1 else "assets"
IST = dt.timezone(dt.timedelta(hours=5, minutes=30))

MONO = "ui-monospace,'JetBrains Mono','SF Mono','Cascadia Code',Consolas,monospace"
BG, PANEL, LINE = "#060b12", "#08111b", "#1d2a3a"
GREEN, RED, AMBER, BLUE, TEXT, MUTED, WHITE = "#4ade80", "#ff6b6b", "#ffb547", "#4f9bff", "#c6d4e3", "#6f87a3", "#ffffff"


def api(url, data=None):
    req = urllib.request.Request(url, data=json.dumps(data).encode() if data else None,
                                 headers={"Accept": "application/vnd.github+json", "User-Agent": "profile-activity",
                                          **({"Authorization": f"Bearer {TOKEN}"} if TOKEN else {})})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def clip(t, n):
    return t if len(t) <= n else t[: n - 1] + "…"


def collect():
    q = """query($u:String!){user(login:$u){
      repositories(privacy:PUBLIC, ownerAffiliations:OWNER){totalCount}
      contributionsCollection{contributionCalendar{totalContributions weeks{contributionDays{date contributionCount}}}}}}"""
    u = api("https://api.github.com/graphql", {"query": q, "variables": {"u": USER}})["data"]["user"]
    cal = u["contributionsCollection"]["contributionCalendar"]
    days = [(d["date"], d["contributionCount"]) for w in cal["weeks"] for d in w["contributionDays"]]
    today = dt.datetime.now(IST).date().isoformat()
    days = [d for d in days if d[0] <= today]
    streak, i = 0, len(days) - 1
    if i >= 0 and days[i][1] == 0:
        i -= 1                      # today not over yet: count from yesterday
    while i >= 0 and days[i][1] > 0:
        streak += 1
        i -= 1

    commits = []
    for repo in api(f"https://api.github.com/users/{USER}/repos?sort=pushed&per_page=8"):
        try:
            for c in api(f"https://api.github.com/repos/{USER}/{repo['name']}/commits?author={USER}&per_page=4"):
                when = dt.datetime.fromisoformat(c["commit"]["author"]["date"].replace("Z", "+00:00")).astimezone(IST)
                msg = c["commit"]["message"].splitlines()[0].strip()
                commits.append((when, repo["name"], msg))
        except Exception as e:      # empty repo etc.
            print("skip", repo["name"], e)
    commits.sort(reverse=True)
    last = commits[0][0] if commits else None
    commits = [c for c in commits if c[1] != USER]   # hide profile-README housekeeping commits from the feed
    return {"total": cal["totalContributions"], "streak": streak, "repos": u["repositories"]["totalCount"],
            "days": days, "commits": commits[:9], "last": last, "now": dt.datetime.now(IST)}


def ago(now, when):
    s = (now - when).total_seconds()
    if s < 3600:
        return f"{max(1, int(s // 60))} min ago"
    if s < 86400:
        return f"{int(s // 3600)} hrs ago"
    return f"{int(s // 86400)} days ago"


def T(x, y, s, size=13, fill=TEXT, weight=400, extra=""):
    return f'<text x="{x}" y="{y}" font-family="{MONO}" font-size="{size}" font-weight="{weight}" fill="{fill}" {extra}>{s}</text>'


def led(x, y, c, r=4.5, dur="1.4s"):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"><animate attributeName="opacity" values="1;.2;1" dur="{dur}" repeatCount="indefinite"/></circle>'


def frame(w, h, body, label):
    grid = "".join(f'<line x1="{x}" y1="0" x2="{x}" y2="{h}" stroke="#0b1520"/>' for x in range(0, w, 40))
    grid += "".join(f'<line x1="0" y1="{y}" x2="{w}" y2="{y}" stroke="#0b1520"/>' for y in range(0, h, 40))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{esc(label)}">'
            f'<title>{esc(label)}</title><defs><clipPath id="c"><rect width="{w}" height="{h}" rx="12"/></clipPath></defs>'
            f'<g clip-path="url(#c)"><rect width="{w}" height="{h}" fill="{BG}"/>{grid}{body}'
            f'<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="12" fill="none" stroke="{LINE}"/></g></svg>')


def heat(days, x, y, weeks, cell, gap):
    days = days[-weeks * 7:]
    top = max([c for _, c in days] + [1])
    out = ""
    for i, (_, c) in enumerate(days):
        col, row = divmod(i, 7)
        if c == 0:
            fill, op = "#0f1d2b", 1
        else:
            fill, op = GREEN, 0.3 + 0.7 * c / top
        out += f'<rect x="{x + col * (cell + gap)}" y="{y + row * (cell + gap)}" width="{cell}" height="{cell}" rx="2" fill="{fill}" fill-opacity="{op:.2f}"/>'
    return out


def stats_of(d):
    last = ago(d["now"], d["last"]) if d["last"] else "n/a"
    return [("CONTRIBUTIONS · 1 YR", f'{d["total"]:,}', WHITE), ("CURRENT STREAK", f'{d["streak"]} day' + ("" if d["streak"] == 1 else "s"), GREEN),
            ("PUBLIC REPOS", str(d["repos"]), WHITE), ("LAST COMMIT", last, AMBER)]


def desktop(d):
    w, h = 1100, 400
    stamp = d["now"].strftime("%d %b %Y · %H:%M IST").upper()
    b = f'<rect width="{w}" height="44" fill="#0a121d"/><line x1="0" y1="44" x2="{w}" y2="44" stroke="{LINE}"/>'
    b += T(24, 28, "LIVE FEED // REAL GITHUB ACTIVITY", 14, WHITE, 700, 'letter-spacing="2"')
    b += led(w - 24 - 250, 23, GREEN) + T(w - 24, 28, "SYNCED " + stamp, 12, GREEN, 700, 'text-anchor="end" letter-spacing="1"')
    # commit log
    b += f'<rect x="24" y="60" width="660" height="{h-84}" rx="8" fill="{PANEL}" stroke="{LINE}"/>'
    b += T(40, 84, "LATEST COMMITS", 11, MUTED, 400, 'letter-spacing="2"')
    for i, (when, repo, msg) in enumerate(d["commits"]):
        y = 114 + i * 30
        b += ('<g>' + T(40, y, when.strftime("%d %b %H:%M").upper(), 12, MUTED)
              + T(160, y, esc(clip(repo, 22)), 12, BLUE, 700)
              + T(352, y, esc(clip(msg, 42)), 12, TEXT) + '</g>')
    if not d["commits"]:
        b += T(40, 120, "no public commits found", 12, MUTED)
    # stats
    for i, (lab, val, c) in enumerate(stats_of(d)):
        col, row = i % 2, i // 2
        x, y = 700 + col * 194, 60 + row * 96
        b += f'<rect x="{x}" y="{y}" width="182" height="84" rx="8" fill="{PANEL}" stroke="{LINE}"/>'
        b += T(x + 14, y + 26, lab, 10.5, MUTED, 400, 'letter-spacing="1.2"') + T(x + 14, y + 62, esc(val), 24, c, 800)
    b += T(700, 268, "LAST 21 WEEKS", 11, MUTED, 400, 'letter-spacing="2"')
    b += heat(d["days"], 700, 280, 21, 14, 4)
    if d["commits"]:
        b += f'<rect x="666" y="{114 - 11}" width="8" height="13" fill="{GREEN}"><animate attributeName="opacity" values="1;0;1" dur="1s" calcMode="discrete" repeatCount="indefinite"/></rect>'
    # note: heat block is 16*24 = 384 wide -> 700..1076
    return frame(w, h, b, f'Real GitHub activity for {USER}: {d["total"]} contributions in the last year, {d["streak"]} day streak, {d["repos"]} public repos')


def phone(d):
    w = 600
    commits = d["commits"][:5]
    h = 70 + 2 * 112 + 40 + len(commits) * 66 + 30 + 7 * 25 + 36
    stamp = d["now"].strftime("%d %b · %H:%M IST").upper()
    b = f'<rect width="{w}" height="70" fill="#0a121d"/><line x1="0" y1="70" x2="{w}" y2="70" stroke="{LINE}"/>'
    b += T(24, 34, "LIVE FEED", 24, WHITE, 800, 'letter-spacing="3"') + led(w - 34, 28, GREEN, 7)
    b += T(24, 58, "REAL GITHUB ACTIVITY · " + stamp, 14, GREEN, 700)
    y0 = 86
    for i, (lab, val, c) in enumerate(stats_of(d)):
        col, row = i % 2, i // 2
        x, y = 24 + col * 282, y0 + row * 112
        b += f'<rect x="{x}" y="{y}" width="270" height="100" rx="10" fill="{PANEL}" stroke="{LINE}"/>'
        b += T(x + 18, y + 32, lab, 15, MUTED, 400) + T(x + 18, y + 78, esc(val), 34, c, 800)
    y = y0 + 2 * 112 + 20
    b += T(24, y, "LATEST COMMITS", 16, MUTED, 400, 'letter-spacing="2"')
    for when, repo, msg in commits:
        y += 66
        b += T(24, y - 30, esc(clip(repo, 26)), 19, BLUE, 700) + T(w - 24, y - 30, when.strftime("%d %b").upper(), 16, MUTED, 400, 'text-anchor="end"')
        b += T(24, y - 4, esc(clip(msg, 40)), 18, TEXT)
    y += 34
    b += T(24, y, "LAST 21 WEEKS", 16, MUTED, 400, 'letter-spacing="2"')
    b += heat(d["days"], 24, y + 12, 21, 21, 4.6)
    return frame(w, h, b, f'Real GitHub activity for {USER}: {d["total"]} contributions in the last year, {d["streak"]} day streak')


if __name__ == "__main__":
    data = collect()
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, "activity.svg"), "w", encoding="utf-8").write(desktop(data))
    open(os.path.join(OUT, "activity-m.svg"), "w", encoding="utf-8").write(phone(data))
    print("total", data["total"], "streak", data["streak"], "repos", data["repos"], "commits", len(data["commits"]))
