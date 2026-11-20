"""Phone versions (600px wide, big text) of every profile panel. README swaps them in with
<picture><source media="(max-width: 1011px)">. Usage: python scripts/gen_mobile.py <repo root>"""
import os, sys, textwrap
sys.path.insert(0, os.path.dirname(__file__))
from worldmap import LAND

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
A = os.path.join(ROOT, "assets")
MONO = "ui-monospace,'JetBrains Mono','SF Mono','Cascadia Code',Consolas,monospace"
BG, PANEL, LINE = "#060b12", "#08111b", "#1d2a3a"
GREEN, RED, AMBER, BLUE, TEXT, MUTED, WHITE = "#4ade80", "#ff6b6b", "#ffb547", "#4f9bff", "#c6d4e3", "#6f87a3", "#ffffff"
W = 600


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def T(x, y, s, size=18, fill=TEXT, weight=400, extra=""):
    return f'<text x="{x}" y="{y}" font-family="{MONO}" font-size="{size}" font-weight="{weight}" fill="{fill}" {extra}>{s}</text>'


def led(x, y, c, r=6, dur="1.4s"):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"><animate attributeName="opacity" values="1;.2;1" dur="{dur}" repeatCount="indefinite"/></circle>'


def svg(name, w, h, label, body):
    grid = "".join(f'<line x1="{x}" y1="0" x2="{x}" y2="{h}" stroke="#0b1520"/>' for x in range(0, w, 40))
    grid += "".join(f'<line x1="0" y1="{y}" x2="{w}" y2="{y}" stroke="#0b1520"/>' for y in range(0, h, 40))
    out = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{esc(label)}">'
           f'<title>{esc(label)}</title><defs><clipPath id="c"><rect width="{w}" height="{h}" rx="14"/></clipPath>'
           f'<radialGradient id="glow"><stop offset="0" stop-color="{GREEN}" stop-opacity=".55"/><stop offset="1" stop-color="{GREEN}" stop-opacity="0"/></radialGradient></defs>'
           f'<g clip-path="url(#c)"><rect width="{w}" height="{h}" fill="{BG}"/>{grid}{body}'
           f'<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="14" fill="none" stroke="{LINE}"/></g></svg>')
    open(os.path.join(A, name), "w", encoding="utf-8").write(out)


def head(title, sub, subc=GREEN):
    return (f'<rect width="{W}" height="76" fill="#0a121d"/><line x1="0" y1="76" x2="{W}" y2="76" stroke="{LINE}"/>'
            + T(24, 38, esc(title), 24, WHITE, 800, 'letter-spacing="2"') + T(24, 63, esc(sub), 15, subc, 700, 'letter-spacing="1"')
            + led(W - 32, 32, subc))


# ------------------------------------------------------------------ monitor
def monitor():
    MX, MY, MW = 24, 250, 552
    LON0, LON1, LAT0, LAT1 = -170, 180, 80, -58
    K = MW / (LON1 - LON0)
    MH = (LAT0 - LAT1) * K
    xy = lambda la, lo: (MX + (lo - LON0) * K, MY + (LAT0 - la) * K)
    b = f'<rect width="{W}" height="214" fill="#0a121d"/><line x1="0" y1="214" x2="{W}" y2="214" stroke="{LINE}"/>'
    NAME = f'font-family="{MONO}" font-size="56" font-weight="800" letter-spacing="3"'
    for col, vals in (("#ff2e63", "0 0;-4 1;3 -1;0 0;0 0;-2 0;0 0"), ("#08d9d6", "0 0;4 -1;-3 1;0 0;0 0;2 1;0 0")):
        b += (f'<text x="24" y="78" {NAME} fill="{col}" opacity=".8">JAY LALKIYA<animateTransform attributeName="transform" type="translate" '
              f'values="{vals}" keyTimes="0;.04;.08;.12;.7;.73;1" calcMode="discrete" dur="3s" repeatCount="indefinite"/></text>')
    b += f'<text x="24" y="78" {NAME} fill="{WHITE}">JAY LALKIYA</text>'
    b += T(26, 116, "CYBER SECURITY INTERN", 21, GREEN, 700, 'letter-spacing="1.5"')
    b += T(26, 144, "SOC · BLUE TEAM · RED TEAM", 18, GREEN, 400, 'letter-spacing="1"')
    b += led(34, 182, "#ff4d4d", 8, "1s") + T(52, 189, "LIVE", 20, RED, 800, 'letter-spacing="3"')
    b += (f'<rect x="130" y="166" width="230" height="32" rx="5" fill="#2a0d10" stroke="#ff4d4d"><animate attributeName="stroke-opacity" values="1;.2;1" dur=".8s" repeatCount="indefinite"/></rect>'
          + T(245, 188, "THREAT LEVEL: HIGH", 16, RED, 800, 'text-anchor="middle" letter-spacing="1"'))
    b += T(576, 189, "AHMEDABAD", 15, MUTED, 400, 'text-anchor="end" letter-spacing="1"')
    b += T(24, 240, "INCOMING ATTACKS · DEMO FEED", 14, MUTED, 400, 'letter-spacing="2"')
    lat = LAT0
    while lat >= LAT1:
        lon = LON0
        while lon <= LON1:
            row = int(round(lat / 5) * 5)
            if any(a <= lon <= c for a, c in LAND.get(row, [])):
                x, y = xy(lat, lon)
                b += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2" fill="#1e3a57"/>'
            lon += 4
        lat -= 4
    hx, hy = xy(23.0, 72.6)
    src = [(55.7, 37.6), (39.9, 116.4), (-23.5, -46.6), (40.7, -74), (52.4, 4.9), (6.5, 3.4), (37.5, 127), (-6.2, 106.8),
           (34, -118), (-33.9, 151.2), (51.5, -0.1), (35.7, 139.7), (19.4, -99.1), (-1.3, 36.8), (41.9, -87.6), (-12, -77)]
    cols = [RED, AMBER, "#ff7a45"]
    for i, (la, lo) in enumerate(src):
        sx, sy = xy(la, lo)
        mx, my = (sx + hx) / 2, min(sy, hy) - abs(sx - hx) * .28 - 16
        p = f"M{sx:.1f},{sy:.1f} Q{mx:.1f},{my:.1f} {hx:.1f},{hy:.1f}"
        c, dur, beg = cols[i % 3], 1.5 + (i % 5) * .3, (i * .37) % 3
        b += f'<path d="{p}" fill="none" stroke="{c}" stroke-opacity=".18" stroke-width="1.4"/>'
        b += (f'<path d="{p}" fill="none" stroke="{c}" stroke-width="3" stroke-linecap="round" pathLength="100" stroke-dasharray="12 100" stroke-dashoffset="12" opacity="0">'
              f'<animate attributeName="stroke-dashoffset" values="12;-100" dur="{dur}s" begin="{beg:.2f}s" repeatCount="indefinite"/>'
              f'<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.05;.85;1" dur="{dur}s" begin="{beg:.2f}s" repeatCount="indefinite"/></path>')
        b += f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="3.5" fill="{c}"/>'
    for k in range(3):
        b += (f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="6" fill="none" stroke="{GREEN}" stroke-width="2"><animate attributeName="r" values="6;34" dur="2.4s" begin="{k*.8}s" repeatCount="indefinite"/>'
              f'<animate attributeName="opacity" values=".9;0" dur="2.4s" begin="{k*.8}s" repeatCount="indefinite"/></circle>')
    b += f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="26" fill="url(#glow)"/><circle cx="{hx:.1f}" cy="{hy:.1f}" r="7" fill="{GREEN}"/>'
    pops = ["BLOCKED: SSH brute force", "BLOCKED: SQL injection", "TRAPPED: telnet bot", "BLOCKED: port scan"]
    n = len(pops)
    for k, t in enumerate(pops):
        vis = ";".join("1" if m == k else "0" for m in range(n)) + ";" + ("1" if k == 0 else "0")
        kt = ";".join(f"{m/n:.3f}" for m in range(n)) + ";1"
        b += (f'<g opacity="{1 if k == 0 else 0}"><animate attributeName="opacity" values="{vis}" keyTimes="{kt}" calcMode="discrete" dur="{n*1.2}s" repeatCount="indefinite"/>'
              f'<rect x="{hx-250:.1f}" y="{hy+30:.1f}" width="300" height="34" rx="5" fill="#2a0d10" stroke="#ff4d4d"/>'
              + T(f"{hx-238:.1f}", f"{hy+53:.1f}", "! " + t, 16, "#ff8080", 800) + '</g>')
    y = MY + MH + 22
    stats = [("ATTEMPTS CAUGHT", "1,3xx", WHITE), ("DECOY SERVICES", "7", WHITE), ("ATT&amp;CK MAPPED", "100%", GREEN), ("REAL SYSTEMS HIT", "0", GREEN)]
    for i, (lab, v, c) in enumerate(stats):
        x, yy = 24 + (i % 2) * 282, y + (i // 2) * 100
        b += f'<rect x="{x}" y="{yy:.1f}" width="270" height="88" rx="10" fill="{PANEL}" stroke="{LINE}"/>'
        b += T(x + 18, f"{yy+30:.1f}", lab, 14, MUTED, 400, 'letter-spacing="1"')
        if i == 0:
            vals = ["1,284", "1,291", "1,297", "1,304", "1,312", "1,319"]
            for k, vv in enumerate(vals):
                vis = ";".join("1" if m == k else "0" for m in range(6)) + ";" + ("1" if k == 0 else "0")
                kt = ";".join(f"{m/6:.3f}" for m in range(6)) + ";1"
                b += (f'<text x="{x+18}" y="{yy+72:.1f}" font-family="{MONO}" font-size="32" font-weight="800" fill="{c}" opacity="{1 if k == 0 else 0}">{vv}'
                      f'<animate attributeName="opacity" values="{vis}" keyTimes="{kt}" calcMode="discrete" dur="9s" repeatCount="indefinite"/></text>')
        else:
            b += T(x + 18, f"{yy+72:.1f}", v, 32, c, 800)
    y += 200 + 20
    b += T(24, f"{y:.1f}", "&#9656; CodeAlpha certified", 17, TEXT) + T(24, f"{y+28:.1f}", "&#9656; Red team intern @ CyArt Tech", 17, TEXT)
    b += T(24, f"{y+62:.1f}", "OPEN TO SOC ANALYST ROLES", 21, WHITE, 800)
    b += (f'<rect x="354" y="{y+44:.1f}" width="12" height="22" fill="{GREEN}"><animate attributeName="opacity" values="1;0;1" dur="1s" calcMode="discrete" repeatCount="indefinite"/></rect>')
    b += (f'<rect x="0" y="-160" width="{W}" height="160" fill="{GREEN}" fill-opacity=".05"><animate attributeName="y" values="-160;{y+90:.0f}" dur="6s" repeatCount="indefinite"/></rect>')
    svg("live-monitor-m.svg", W, int(y + 90), "Live security monitor: Jay Lalkiya, cyber security intern. Demo attacks are caught by the GullakTrap honeypot in Ahmedabad", b)


# ------------------------------------------------------------------ operator file
def operator():
    rows = [("NAME", "Jay Lalkiya", WHITE), ("ROLE", "Cyber security intern", TEXT), ("BASE", "Ahmedabad, Gujarat", TEXT),
            ("EDUCATION", "BCA (Hons) · CGPA 8.48", TEXT), ("TRAINING", "NSQF L4 · 300+ hrs · Adani", TEXT),
            ("CURRENT", "Red team intern @ CyArt", TEXT), ("COMPLETED", "CodeAlpha · cert + LOR", GREEN),
            ("FOCUS", "SOC · detection · web sec", TEXT), ("SEEKING", "SOC analyst roles · now", AMBER)]
    b = head("OPERATOR FILE", "STATUS: OPEN TO WORK")
    y = 120
    for k, v, c in rows:
        b += T(24, y, k, 15, MUTED, 400, 'letter-spacing="2"') + T(24, y + 30, esc(v), 23, c, 800 if c != TEXT else 400)
        y += 66
    b += (f'<g transform="rotate(-11 470 140)"><rect x="390" y="112" width="170" height="46" fill="none" stroke="{RED}" stroke-width="3" rx="3"/>'
          + T(475, 145, "VERIFIED", 26, RED, 800, 'text-anchor="middle" letter-spacing="4"') + '</g>')
    svg("operator-m.svg", W, y - 10, "Operator file: Jay Lalkiya, cyber security intern, open to SOC analyst roles", b)


# ------------------------------------------------------------------ skills
def skills():
    groups = [("DETECT", GREEN, ["SOC monitoring", "Suricata IDS", "Detection eng.", "ATT&CK mapping", "Alert triage"]),
              ("DEFEND", BLUE, ["Firewalls & ACLs", "Networking", "Audit & compliance", "Linux", "Incident response"]),
              ("ATTACK", RED, ["VAPT basics", "Secure code review", "Web recon", "OWASP Top 10", "Honeypot design"]),
              ("BUILD", AMBER, ["Python tooling", "Java · JS", "React · Node.js", "MySQL · Postgres", "Git"])]
    b = head("CAPABILITY MATRIX", "ALL SYSTEMS ONLINE")
    y = 96
    for name, c, items in groups:
        rows = (len(items) + 1) // 2
        hgt = 56 + rows * 38 + 8
        b += f'<rect x="24" y="{y}" width="552" height="{hgt}" rx="10" fill="{PANEL}" stroke="{LINE}"/><rect x="24" y="{y}" width="6" height="{hgt}" rx="3" fill="{c}"/>'
        b += T(46, y + 36, name, 22, c, 800, 'letter-spacing="3"')
        for j, it in enumerate(items):
            x, yy = 46 + (j % 2) * 268, y + 76 + (j // 2) * 38
            b += led(x + 6, yy - 6, c, 5, f"{1.2 + j * .3:.1f}s") + T(x + 22, yy, esc(it), 19, TEXT)
        y += hgt + 14
    svg("skills-m.svg", W, y + 10, "Capability matrix: detect, defend, attack and build skills", b)


# ------------------------------------------------------------------ project cards (shown 2 per row, so ~176px wide on a phone)
CARDS = [("card-sentinelids-m.svg", "DETECTION", "SentinelIDS", "Network IDS that blocks attackers", "41 tests", GREEN),
         ("card-codereview-m.svg", "APPSEC", "Code Review", "Flask app audit: exploit, fix, retest", "12 vulns", BLUE),
         ("card-packetsentry-m.svg", "NETWORK", "PacketSentry", "Sniffer that flags plaintext logins", "CLI + GUI", BLUE),
         ("card-phishguard-m.svg", "AWARENESS", "PhishGuard", "Phishing training site with a quiz", "8 modules", AMBER),
         ("card-gullaktrap-m.svg", "DETECTION", "GullakTrap", "Honeypot that logs every attacker", "7 services", GREEN),
         ("card-wifisentry-m.svg", "DETECTION", "Wifi-Sentry", "Catches fake (evil twin) WiFi", "passive", GREEN),
         ("card-scopestorm-m.svg", "OFFENSIVE", "ScopeStorm", "Load tester locked to permission", "RoE gated", RED),
         ("card-reconraptor-m.svg", "OFFENSIVE", "ReconRaptor", "One-click web recon with report", "8 tools", RED),
         ("card-stegovault-m.svg", "CRYPTO", "StegoVault", "Hides encrypted text in images", "AES-256", BLUE),
         ("card-mitmtracker-m.svg", "DETECTION", "MITM Tracker", "Detects and undoes MITM attacks", "ARP + DHCP", GREEN)]


def cards():
    w, h = 300, 300
    for fname, kind, title, desc, stat, c in CARDS:
        b = f'<rect width="{w}" height="8" fill="{c}"/>' + T(18, 42, kind, 17, c, 800, 'letter-spacing="2"') + led(w - 24, 36, c, 7)
        size = 32 if len(title) <= 11 else 28
        b += T(18, 90, esc(title), size, WHITE, 800)
        for i, line in enumerate(textwrap.wrap(desc, 22)[:3]):
            b += T(18, 130 + i * 28, esc(line), 21, TEXT)
        b += f'<rect x="18" y="222" width="{len(stat)*13+28}" height="40" rx="20" fill="{PANEL}" stroke="{c}"/>' + T(32, 249, esc(stat), 21, c, 800)
        b += T(w - 18, 252, "&#9656;", 28, MUTED, 800, 'text-anchor="end"')
        svg(fname, w, h, f"{title}: {desc}", b)


# ------------------------------------------------------------------ ATT&CK
def attack():
    tiles = [("T1110", "Brute Force", "GullakTrap", RED), ("T1105", "Ingress Tool Transfer", "GullakTrap", AMBER),
             ("T1557", "Adversary-in-the-Middle", "Wifi-Sentry", RED), ("T1557.004", "Evil Twin", "Wifi-Sentry", RED),
             ("T1498", "Network DoS", "Wifi-Sentry", AMBER)]
    b = head("MITRE ATT&CK", "5 TECHNIQUES DETECTED", RED)
    y = 96
    for i, (tid, name, tool, c) in enumerate(tiles):
        b += f'<rect x="24" y="{y}" width="552" height="96" rx="10" fill="{PANEL}" stroke="{c}" stroke-opacity=".5"/>'
        b += (f'<rect x="24" y="{y}" width="552" height="96" rx="10" fill="{c}" opacity="0"><animate attributeName="opacity" values="0;.12;0" dur="3s" begin="{i*.6}s" repeatCount="indefinite"/></rect>')
        b += T(44, y + 40, tid, 26, c, 800) + T(44, y + 76, esc(name), 21, WHITE, 700)
        b += T(556, y + 40, "&#9656; " + tool, 17, GREEN, 700, 'text-anchor="end"')
        y += 110
    svg("attack-m.svg", W, y + 6, "MITRE ATT&CK coverage: T1110, T1105, T1557, T1557.004, T1498", b)


# ------------------------------------------------------------------ timeline
def timeline():
    items = [("OCT 2026 - NOW", "Red Team Intern", "CyArt Tech", "ACTIVE", AMBER),
             ("OCT - NOV 2026", "Cyber Security Intern", "CodeAlpha · cert + LOR", "DONE", GREEN),
             ("2026 - NOW", "NSQF L4 Cyber Security", "Adani Saksham · 300+ hrs", "ACTIVE", AMBER),
             ("DEC 2025 - JAN 2026", "React & Node.js Intern", "TechRover Solutions", "DONE", GREEN)]
    b = head("ACCESS LOG", "EXPERIENCE & TRAINING")
    y = 110
    b += f'<line x1="40" y1="{y}" x2="40" y2="{y + len(items) * 124 - 60}" stroke="{LINE}" stroke-width="3"/>'
    for d, role, org, st, c in items:
        b += f'<circle cx="40" cy="{y+12}" r="10" fill="{BG}" stroke="{c}" stroke-width="3"/>'
        if st == "ACTIVE":
            b += (f'<circle cx="40" cy="{y+12}" r="10" fill="none" stroke="{c}" stroke-width="2"><animate attributeName="r" values="10;22" dur="1.8s" repeatCount="indefinite"/>'
                  f'<animate attributeName="opacity" values="1;0" dur="1.8s" repeatCount="indefinite"/></circle>')
        b += T(70, y + 18, d, 16, MUTED, 700, 'letter-spacing="1"')
        b += f'<rect x="{W-24-96}" y="{y-4}" width="96" height="30" rx="15" fill="{PANEL}" stroke="{c}"/>' + T(W - 24 - 48, y + 16, st, 15, c, 800, 'text-anchor="middle" letter-spacing="1"')
        b += T(70, y + 52, esc(role), 23, WHITE, 800) + T(70, y + 82, esc(org), 19, c, 700)
        y += 124
    svg("timeline-m.svg", W, y - 10, "Experience: CyArt Tech red team intern, CodeAlpha cyber security intern, Adani Saksham NSQF L4, TechRover developer intern", b)


# ------------------------------------------------------------------ mode banners
def modes():
    h = 104
    for name, bg, fg, c, t1, t2 in [("mode-dark-m.svg", BG, WHITE, BLUE, "MODE: DEFENDER", "switch to light mode to see my attacker side"),
                                    ("mode-light-m.svg", "#fff4f2", "#3a0d08", "#d0301f", "MODE: ATTACKER", "switch to dark mode to see my defender side")]:
        b = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}" role="img" aria-label="{t1}">'
             f'<rect width="{W}" height="{h}" rx="14" fill="{bg}" stroke="{c}" stroke-opacity=".5"/><rect width="10" height="{h}" rx="5" fill="{c}"/>'
             + led(44, 42, c, 9, "1s") + T(68, 52, t1, 30, c, 800, 'letter-spacing="3"') + T(30, 86, t2, 17, fg, 400, 'opacity=".8"') + '</svg>')
        open(os.path.join(A, name), "w", encoding="utf-8").write(b)


for f in (monitor, operator, skills, cards, attack, timeline, modes):
    f()
print("mobile ok")
