"""Generate the SOC-console style SVG panels for the GitHub profile. Usage: python gen_profile.py <outdir>"""
import sys, os, textwrap
OUT = sys.argv[1]
os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)

MONO = "ui-monospace,'JetBrains Mono','SF Mono','Cascadia Code',Consolas,monospace"
BG, PANEL, LINE = "#060b12", "#08111b", "#1d2a3a"
GREEN, RED, AMBER, BLUE, TEXT, MUTED, WHITE = "#4ade80", "#ff6b6b", "#ffb547", "#4f9bff", "#c6d4e3", "#6f87a3", "#ffffff"

def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def svg(w, h, label, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{esc(label)}">'
            f'<title>{esc(label)}</title>'
            f'<defs><clipPath id="c"><rect width="{w}" height="{h}" rx="12"/></clipPath></defs>'
            f'<g clip-path="url(#c)"><rect width="{w}" height="{h}" fill="{BG}"/>'
            + "".join(f'<line x1="{x}" y1="0" x2="{x}" y2="{h}" stroke="#0b1520"/>' for x in range(0, w, 40))
            + "".join(f'<line x1="0" y1="{y}" x2="{w}" y2="{y}" stroke="#0b1520"/>' for y in range(0, h, 40))
            + body +
            f'<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="12" fill="none" stroke="{LINE}"/></g></svg>')

def T(x, y, s, size=13, fill=TEXT, weight=400, extra=""):
    return f'<text x="{x}" y="{y}" font-family="{MONO}" font-size="{size}" font-weight="{weight}" fill="{fill}" {extra}>{s}</text>'

def led(x, y, color, dur="1.6s", r=4.5):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}"><animate attributeName="opacity" values="1;.2;1" dur="{dur}" repeatCount="indefinite"/></circle>')

def header(w, title, right, rcolor=GREEN):
    return (f'<rect width="{w}" height="44" fill="#0a121d"/><line x1="0" y1="44" x2="{w}" y2="44" stroke="{LINE}"/>'
            + T(24, 28, esc(title), 14, WHITE, 700, 'letter-spacing="2"')
            + led(w - 24 - len(right) * 9.4 - 14, 23, rcolor)
            + T(w - 24, 28, esc(right), 12, rcolor, 700, 'text-anchor="end" letter-spacing="2"'))

def write(name, content):
    open(os.path.join(OUT, "assets", name), "w", encoding="utf-8").write(content)

# ---------------------------------------------------------------- operator file
def operator():
    w, h = 1100, 380
    b = header(w, "OPERATOR FILE // whoami", "STATUS: OPEN TO WORK")
    rows = [("NAME", "Jay Lalkiya", WHITE), ("ROLE", "Cyber security intern · SOC / blue team", TEXT),
            ("BASE", "Ahmedabad, Gujarat, India", TEXT),
            ("EDUCATION", "BCA (Honours) · CGPA 8.48 · 84.09%", TEXT),
            ("TRAINING", "NSQF Level 4 Cyber Security · 300+ hrs · Adani Saksham", TEXT),
            ("CURRENT", "Red team intern @ CyArt Tech", TEXT),
            ("COMPLETED", "Cyber security intern @ CodeAlpha · certified + LOR", GREEN),
            ("FOCUS", "SOC monitoring · detection · web app security · IR", TEXT),
            ("ASK ME", "firewalls & access control, alert triage, OWASP", TEXT),
            ("SEEKING", "SOC analyst / cybersecurity roles · available now", AMBER)]
    y = 82
    for k, v, c in rows:
        b += T(32, y, k, 12, MUTED, 400, 'letter-spacing="2"') + T(170, y, esc(v), 15, c, 700 if c != TEXT else 400)
        y += 29
    # radar
    cx, cy, r = 905, 190, 112
    b += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#07131c" stroke="{LINE}"/>'
    for rr in (r * .33, r * .66):
        b += f'<circle cx="{cx}" cy="{cy}" r="{rr:.0f}" fill="none" stroke="#14283a"/>'
    b += f'<line x1="{cx-r}" y1="{cy}" x2="{cx+r}" y2="{cy}" stroke="#14283a"/><line x1="{cx}" y1="{cy-r}" x2="{cx}" y2="{cy+r}" stroke="#14283a"/>'
    b += (f'<g><path d="M{cx},{cy} L{cx+r},{cy} A{r},{r} 0 0 0 {cx+r*0.866:.1f},{cy-r*0.5:.1f} Z" fill="{GREEN}" fill-opacity=".22"/>'
          f'<line x1="{cx}" y1="{cy}" x2="{cx+r}" y2="{cy}" stroke="{GREEN}" stroke-width="2"/>'
          f'<animateTransform attributeName="transform" type="rotate" from="0 {cx} {cy}" to="-360 {cx} {cy}" dur="4s" repeatCount="indefinite"/></g>')
    for i, (dx, dy, c) in enumerate([(40, -50, RED), (-60, 30, AMBER), (20, 70, RED), (-30, -80, AMBER), (75, 25, RED)]):
        b += (f'<circle cx="{cx+dx}" cy="{cy+dy}" r="4" fill="{c}" opacity="0"><animate attributeName="opacity" values="0;1;0" dur="4s" begin="{i*0.8}s" repeatCount="indefinite"/></circle>')
    b += f'<circle cx="{cx}" cy="{cy}" r="5" fill="{GREEN}"/>'
    b += T(cx, cy + r + 26, "THREAT SCAN: ACTIVE", 11, MUTED, 400, 'text-anchor="middle" letter-spacing="2"')
    # stamp
    b += (f'<g transform="rotate(-11 700 330)"><rect x="610" y="306" width="190" height="44" fill="none" stroke="{RED}" stroke-width="3" rx="3"/>'
          + T(705, 337, "VERIFIED", 26, RED, 800, 'text-anchor="middle" letter-spacing="5"') + '</g>')
    write("operator.svg", svg(w, h, "Operator file: Jay Lalkiya, cyber security intern in Ahmedabad. BCA Honours, NSQF L4 cyber security trainee, red team intern at CyArt Tech, CodeAlpha certified, open to SOC analyst roles", b))

# ---------------------------------------------------------------- capability matrix
def skills():
    w = 1100
    cols = [("DETECT", GREEN, ["SOC monitoring", "Suricata IDS", "Detection engineering", "MITRE ATT&CK mapping", "Alert triage"]),
            ("DEFEND", BLUE, ["Firewalls & access control", "Networking fundamentals", "Audit & compliance", "Linux", "Incident response basics"]),
            ("ATTACK", RED, ["VAPT fundamentals", "Secure code review", "Web recon (nmap, nuclei)", "OWASP Top 10", "Honeypot design"]),
            ("BUILD", AMBER, ["Python security tooling", "Java · JavaScript", "React · Node.js", "MySQL · PostgreSQL", "Git"])]
    h = 44 + 30 + 46 + 5 * 34 + 24
    b = header(w, "CAPABILITY MATRIX", "ALL SYSTEMS ONLINE")
    cw = (w - 48 - 3 * 14) / 4
    for i, (name, c, items) in enumerate(cols):
        x = 24 + i * (cw + 14)
        b += f'<rect x="{x:.1f}" y="66" width="{cw:.1f}" height="{h-90}" rx="8" fill="{PANEL}" stroke="{LINE}"/>'
        b += f'<rect x="{x:.1f}" y="66" width="{cw:.1f}" height="4" rx="2" fill="{c}"/>'
        b += T(x + 16, 98, name, 15, c, 800, 'letter-spacing="3"')
        for j, it in enumerate(items):
            yy = 134 + j * 34
            b += led(x + 22, yy - 4, c, f"{1.2 + (i + j) % 4 * 0.35:.2f}s", 3.5)
            b += T(x + 36, yy, esc(it), 13, TEXT)
    write("skills.svg", svg(w, h, "Capability matrix. Detect: SOC monitoring, Suricata, detection engineering, ATT&CK mapping, alert triage. Defend: firewalls, networking, audit, Linux, incident response. Attack: VAPT, secure code review, web recon, OWASP Top 10, honeypot design. Build: Python, Java, JavaScript, React, Node.js, SQL, Git", b))

# ---------------------------------------------------------------- project cards
def card(fname, num, kind, title, desc, chips, color, status="ONLINE"):
    w, h = 540, 270
    b = f'<rect width="{w}" height="6" fill="{color}"/>'
    b += T(22, 36, f"MODULE {num:02d} · {kind}", 11, color, 700, 'letter-spacing="2.5"')
    b += led(w - 92, 31, color) + T(w - 22, 36, status, 11, color, 700, 'text-anchor="end" letter-spacing="2"')
    b += T(22, 76, esc(title), 28, WHITE, 800)
    for i, line in enumerate(textwrap.wrap(desc, 58)[:4]):
        b += T(22, 108 + i * 20, esc(line), 13, TEXT)
    x = 22
    for ch in chips:
        cw = len(ch) * 7.4 + 20
        b += f'<rect x="{x:.1f}" y="196" width="{cw:.1f}" height="26" rx="13" fill="{PANEL}" stroke="{color}" stroke-opacity=".6"/>'
        b += T(x + 10, 213, esc(ch), 12, color, 700)
        x += cw + 8
    b += f'<line x1="22" y1="238" x2="{w-22}" y2="238" stroke="{LINE}"/>'
    b += T(22, 258, "&#9656; OPEN REPOSITORY", 12, MUTED, 700, 'letter-spacing="2"')
    b += (f'<rect x="{w-22-46}" y="248" width="46" height="4" rx="2" fill="{LINE}"/>'
          f'<rect x="{w-22-46}" y="248" width="10" height="4" rx="2" fill="{color}"><animate attributeName="x" values="{w-22-46};{w-22-10};{w-22-46}" dur="2.4s" repeatCount="indefinite"/></rect>')
    write(fname, svg(w, h, f"{title}: {desc}", b))

CARDS = [
 ("card-sentinelids.svg", 1, "DETECTION", "SentinelIDS", "Suricata 7 network IDS with 18 custom rules, a response engine that can block attackers, and a live dashboard.", ["18 rules", "41 tests", "auto-block"], GREEN),
 ("card-codereview.svg", 2, "APPSEC", "Secure Code Review", "Audit of a deliberately vulnerable Flask app. Each bug gets a working exploit, a fix, and a retest.", ["12 vulns", "CWE + OWASP", "Bandit"], BLUE),
 ("card-packetsentry.svg", 3, "NETWORK", "PacketSentry", "Packet sniffer with a CLI and a Wireshark-style GUI. Flags plaintext credentials and unencrypted protocols.", ["ARP/TCP/UDP/DNS", ".pcap", "GUI"], BLUE),
 ("card-phishguard.svg", 4, "AWARENESS", "PhishGuard", "Eight-module phishing training site: spot red flags, inspect URLs, play Phish or Legit, pass the final quiz.", ["8 modules", "live site", "quiz"], AMBER),
 ("card-gullaktrap.svg", 5, "DETECTION", "GullakTrap", "Multi-protocol honeypot. Seven decoy services log every password tried and every command run, mapped to ATT&CK.", ["7 services", "SSH replay", "ATT&CK"], GREEN),
 ("card-wifisentry.svg", 6, "DETECTION", "Wifi-Sentry", "Passive evil-twin detector. Baselines real access points and alerts when a known SSID appears from a new BSSID.", ["no monitor mode", "T1557", "passive"], GREEN),
 ("card-mitmtracker.svg", 7, "DETECTION", "MITM Tracker", "Windows defence console. Fingerprints the trusted network, tells ARP spoofing, rogue DHCP and evil twins apart, and undoes each.", ["ARP spoofing", "rogue DHCP", "T1557.002"], GREEN),
 ("card-scopestorm.svg", 8, "OFFENSIVE", "ScopeStorm", "Authorized load-testing console. Refuses to run without a rules-of-engagement file and logs to a hash-chained audit log.", ["RoE gated", "auto-abort", "SHA-256 log"], RED),
 ("card-reconraptor.svg", 9, "OFFENSIVE", "ReconRaptor", "Chains nmap, whatweb, nikto, nuclei and more into one authorized run with a severity-ranked HTML report.", ["nmap", "nuclei", "HTML report"], RED),
 ("card-stegovault.svg", 10, "CRYPTO", "StegoVault", "Hides AES-256-GCM encrypted messages in PNG images, then detects hidden data with RS steganalysis.", ["AES-256-GCM", "PBKDF2", "RS analysis"], BLUE),
]

# ---------------------------------------------------------------- ATT&CK coverage
def attack():
    w = 1100
    tiles = [("T1110", "Brute Force", "Credential Access", "GullakTrap", RED),
             ("T1105", "Ingress Tool Transfer", "Command and Control", "GullakTrap", AMBER),
             ("T1557", "Adversary-in-the-Middle", "Credential Access", "Wifi-Sentry", RED),
             ("T1557.002", "ARP Cache Poisoning", "Credential Access", "MITM Tracker", RED),
             ("T1557.003", "DHCP Spoofing", "Credential Access", "MITM Tracker", RED),
             ("T1557.004", "Evil Twin", "Credential Access", "Wifi-Sentry", RED),
             ("T1498", "Network Denial of Service", "Impact", "Wifi-Sentry", AMBER)]
    rows = -(-len(tiles) // 3)
    h = 44 + 24 + rows * 112 + (rows - 1) * 14 + 22
    b = header(w, "MITRE ATT&CK // DETECTION COVERAGE", f"{len(tiles)} TECHNIQUES", RED)
    tw = (w - 48 - 2 * 14) / 3
    for i, (tid, name, tac, tool, c) in enumerate(tiles):
        r, col = divmod(i, 3)
        x, y = 24 + col * (tw + 14), 68 + r * 126
        b += f'<rect x="{x:.1f}" y="{y}" width="{tw:.1f}" height="112" rx="8" fill="{PANEL}" stroke="{c}" stroke-opacity=".5"/>'
        b += (f'<rect x="{x:.1f}" y="{y}" width="{tw:.1f}" height="112" rx="8" fill="{c}" opacity="0">'
              f'<animate attributeName="opacity" values="0;.12;0" dur="3s" begin="{i*0.6}s" repeatCount="indefinite"/></rect>')
        b += T(x + 16, y + 30, tid, 20, c, 800)
        b += T(x + 16, y + 56, esc(name), 15, WHITE, 700)
        b += T(x + 16, y + 78, esc(tac.upper()), 11, MUTED, 400, 'letter-spacing="1.5"')
        b += T(x + 16, y + 99, "DETECTED BY &#9656; " + tool, 11, GREEN, 700, 'letter-spacing="1"')
    used = len(tiles) % 3
    if used:   # the note fills whatever is left of the last row
        x, y = 24 + used * (tw + 14), 68 + (rows - 1) * 126
        fw = (3 - used) * tw + (2 - used) * 14
        b += f'<rect x="{x:.1f}" y="{y}" width="{fw:.1f}" height="112" rx="8" fill="none" stroke="{LINE}" stroke-dasharray="6 6"/>'
        if used == 2:
            b += T(x + fw / 2, y + 50, "EVERY TILE IS BACKED", 12, MUTED, 700, 'text-anchor="middle" letter-spacing="1.5"')
            b += T(x + fw / 2, y + 72, "BY TESTED CODE", 12, MUTED, 700, 'text-anchor="middle" letter-spacing="1.5"')
        else:
            b += T(x + fw / 2, y + 61, "EVERY TILE IS BACKED BY TESTED CODE", 12, MUTED, 700, 'text-anchor="middle" letter-spacing="1.5"')
    write("attack.svg", svg(w, h, "MITRE ATT&CK coverage: T1110 Brute Force and T1105 Ingress Tool Transfer detected by GullakTrap; T1557 Adversary-in-the-Middle, T1557.004 Evil Twin and T1498 Network Denial of Service detected by Wifi-Sentry; T1557.002 ARP Cache Poisoning and T1557.003 DHCP Spoofing detected by MITM Tracker", b))

# ---------------------------------------------------------------- experience timeline
def timeline():
    w = 1100
    items = [("OCT 2026 - NOW", "Intern, Red Teaming", "CyArt Tech", "Four-month internship in the red teaming domain.", "ACTIVE", AMBER),
             ("OCT - NOV 2026", "Cyber Security Intern", "CodeAlpha", "Shipped a network IDS, a secure code review, a packet sniffer and a phishing course. Certificate + LOR.", "COMPLETE", GREEN),
             ("2026 - NOW", "Cyber Security Program, NSQF L4", "Adani Saksham, Ahmedabad", "300+ hrs: networks, firewalls, audit, SOC monitoring and escalation, VAPT in lab environments.", "ACTIVE", AMBER),
             ("DEC 2025 - JAN 2026", "React.js & Node.js Developer Intern", "TechRover Solutions", "120 hrs building a full app: auth, REST APIs, PostgreSQL schema design.", "COMPLETE", GREEN)]
    rowh = 92
    h = 44 + 24 + len(items) * rowh + 10
    b = header(w, "ACCESS LOG // experience & training", f"{len(items)} ENTRIES")
    lx = 214
    b += f'<line x1="{lx}" y1="72" x2="{lx}" y2="{h-30}" stroke="{LINE}" stroke-width="2"/>'
    for i, (d, role, org, desc, st, c) in enumerate(items):
        y = 72 + i * rowh
        b += T(lx - 22, y + 24, d, 12, MUTED, 700, 'text-anchor="end" letter-spacing="1"')
        b += f'<circle cx="{lx}" cy="{y+20}" r="7" fill="{BG}" stroke="{c}" stroke-width="2.5"/>'
        if st == "ACTIVE":
            b += (f'<circle cx="{lx}" cy="{y+20}" r="7" fill="none" stroke="{c}" stroke-width="2"><animate attributeName="r" values="7;16" dur="1.8s" repeatCount="indefinite"/>'
                  f'<animate attributeName="opacity" values="1;0" dur="1.8s" repeatCount="indefinite"/></circle>')
        b += T(lx + 26, y + 25, esc(role), 17, WHITE, 800) + T(lx + 26 + len(role) * 10.4 + 10, y + 25, "@ " + esc(org), 14, c, 700)
        b += T(lx + 26, y + 50, esc(desc), 13, TEXT)
        b += f'<rect x="{w-24-96}" y="{y+8}" width="96" height="24" rx="12" fill="{PANEL}" stroke="{c}"/>'
        b += T(w - 24 - 48, y + 25, st, 11, c, 700, 'text-anchor="middle" letter-spacing="2"')
    write("timeline.svg", svg(w, h, "Experience: red team intern at CyArt Tech (active); cyber security intern at CodeAlpha, Oct to Nov 2026 (complete, certificate and LOR); NSQF L4 cyber security program at Adani Saksham (active); React and Node.js developer intern at TechRover Solutions, Dec 2025 to Jan 2026", b))

# ---------------------------------------------------------------- mode banners (dark = defender, light = attacker)
def modes():
    w, h = 1100, 74
    for name, bg, fg, c, t1, t2 in [("mode-dark.svg", BG, WHITE, BLUE, "MODE: DEFENDER", "you're viewing in dark mode. switch GitHub to light mode to see the attacker side."),
                                    ("mode-light.svg", "#fff4f2", "#3a0d08", "#d0301f", "MODE: ATTACKER", "you're viewing in light mode. switch GitHub to dark mode to see the defender side.")]:
        b = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{t1}">'
             f'<rect width="{w}" height="{h}" rx="12" fill="{bg}" stroke="{c}" stroke-opacity=".5"/>'
             f'<rect x="0" y="0" width="8" height="{h}" rx="4" fill="{c}"/>'
             + led(40, 37, c, "1s", 7)
             + T(62, 45, t1, 24, c, 800, 'letter-spacing="4"')
             + T(w - 24, 45, t2, 13, fg, 400, 'text-anchor="end" opacity=".75"') + '</svg>')
        write(name, b)

operator(); skills(); attack(); timeline(); modes()
for c in CARDS:
    card(*c)
print("ok", sorted(os.listdir(os.path.join(OUT, "assets"))))
