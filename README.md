<h1 align="center">Hey, I'm Jay Lalkiya 👋</h1>

<p align="center">
  <a href="https://jaylalkiyaportfolio.vercel.app/">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=24&duration=3200&pause=900&color=E74C3C&center=true&vCenter=true&width=600&lines=Cyber+Security+Trainee+(NSQF+L4);I+build+honeypots%2C+detectors+and+attacks;SOC+Monitoring+%2B+VAPT+Fundamentals;BCA+Honours+%7C+84.09%25" alt="Typing SVG" />
  </a>
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=jaylalkiya&label=Profile%20Views&color=E74C3C&style=for-the-badge" alt="Profile views" />
  <img src="https://visitor-badge.laobi.icu/badge?page_id=jaylalkiya.jaylalkiya&title=Visitors&color=2C3E50" alt="Visitors" />
  <a href="https://github.com/jaylalkiya?tab=followers"><img src="https://img.shields.io/github/followers/jaylalkiya?label=Followers&style=for-the-badge&color=6f42c1&logo=github" alt="Followers" /></a>
</p>

---

## 🙋‍♂️ A bit about me

I'm a final-year **BCA (Honours)** student from **Gujarat**, currently working through a **300+ hour NSQF Level 4 Cyber Security program** at Adani Saksham — covering network foundations, firewalls & access control, audit & compliance, SOC monitoring/escalation, and VAPT fundamentals in controlled lab environments.

My background is in software development (React, Node.js, Java), which turned out to be a real advantage on the security side — I understand how applications are actually built, so I can reason about *why* a vulnerability exists, not just recognize that one does.

- 🎓 BCA (Hons), CGPA **8.48** / **84.09%** — Bhakta Kavi Narsinh Mehta University
- 🔐 In progress: NSQF L4 Cyber Security — networking, firewalls, SOC workflows, VAPT
- 🧠 Interested in: web app security, threat detection, incident response basics
- 🌐 Portfolio: **[jaylalkiyaportfolio.vercel.app](https://jaylalkiyaportfolio.vercel.app/)**
- 💬 Ask me about firewalls & access control, SOC alert triage, or OWASP basics
- 📫 Reach me at **jaylalkiya02@gmail.com** — open to SOC analyst / cybersecurity internship roles

<br />

<p align="center">
  <img src="https://img.shields.io/badge/Location-Ahmedabad,%20India-2C3E50?style=for-the-badge&logo=googlemaps&logoColor=white" />
  <img src="https://img.shields.io/badge/Open%20To-Security%20Internships-E74C3C?style=for-the-badge&logo=handshake&logoColor=white" />
  <img src="https://img.shields.io/badge/Availability-Immediate-16A085?style=for-the-badge&logo=clockify&logoColor=white" />
</p>

---

## 🛡️ Security Skills

![Networking](https://img.shields.io/badge/Networking%20Fundamentals-1D63ED?style=for-the-badge&logo=cisco&logoColor=white)
![Firewalls](https://img.shields.io/badge/Firewalls%20%26%20Access%20Control-16A085?style=for-the-badge&logo=cloudflare&logoColor=white)
![SOC](https://img.shields.io/badge/SOC%20Monitoring-E74C3C?style=for-the-badge&logo=splunk&logoColor=white)
![VAPT](https://img.shields.io/badge/VAPT%20Fundamentals-2C3E50?style=for-the-badge&logo=kalilinux&logoColor=white)
![Load Testing](https://img.shields.io/badge/Load%20%26%20Resilience%20Testing-D35400?style=for-the-badge&logo=apachejmeter&logoColor=white)
![Audit](https://img.shields.io/badge/Audit%20%26%20Compliance-8E44AD?style=for-the-badge&logo=readthedocs&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Python](https://img.shields.io/badge/Python%20Security%20Tooling-3776AB?style=for-the-badge&logo=python&logoColor=white)

**Supporting technical background** (used to understand what I'm defending)

![Java](https://img.shields.io/badge/Java-007396?style=for-the-badge&logo=openjdk&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

---

## 📌 Security projects

Four tools built during the program, newest first. Each one implements the
defensive side *and* the offensive side, because building the attack is what
taught me where the detection has to go.

### 🌩️ ScopeStorm — Authorized Load & Resilience Console
`Python` `Tkinter` `Threading` `SHA-256 Audit Chain`

Generates controlled HTTP load — but refuses to fire until a Rules-of-Engagement
file authorizes the exact target, the concurrency / RPS ceilings, and the time
window, and it aborts itself the moment error rate or p95 latency crosses the
configured thresholds. Every run is written to a tamper-evident, hash-chained
audit log that verifies on read, so any later edit or deletion breaks the chain
and the whole engagement can be proven after the fact. The project was really
about the guardrails: building a load tool that physically can't be pointed
somewhere it wasn't cleared for.

[![Repo](https://img.shields.io/badge/Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/jaylalkiya/ScopeStorm)
![Stars](https://img.shields.io/github/stars/jaylalkiya/ScopeStorm?style=flat-square&color=f7dc6f)
![Last commit](https://img.shields.io/github/last-commit/jaylalkiya/ScopeStorm?style=flat-square&color=2ea44f)

<br />

### 🍯 GullakTrap — Multi-Protocol Honeypot
`Python` `Flask` `Paramiko` `SQLite` `MITRE ATT&CK`

Seven decoy services — HTTP, FTP, SSH, Telnet, SMB, SMTP, SNMP — that log every
credential tried and every command run. The SSH sensor serves a fake filesystem
and records inter-keystroke timing, so a session replays at the speed it was
typed. Each event is scored and mapped to an ATT&CK technique, and a bundled
red-team simulator speaks all seven protocols so the detection chain can be
proven end to end.

[![Repo](https://img.shields.io/badge/Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/jaylalkiya/gullaktrap)
![Stars](https://img.shields.io/github/stars/jaylalkiya/gullaktrap?style=flat-square&color=f7dc6f)
![Last commit](https://img.shields.io/github/last-commit/jaylalkiya/gullaktrap?style=flat-square&color=2ea44f)

<br />

### 📡 Wifi-Sentry — Rogue Access Point Monitor
`Python` `Windows` `MITRE ATT&CK T1557 / T1498`

Detects evil-twin access points without monitor mode or Npcap, by reading the
beacon metadata Windows already collects. An attacker can clone an SSID in five
seconds, but not the BSSID behind it — so the tool baselines the real radios and
alerts on a name broadcast from a MAC that was never there. Passive only: never
transmits, never deauthenticates, never captures traffic.

[![Repo](https://img.shields.io/badge/Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/jaylalkiya/Wifi-Sentry)
![Stars](https://img.shields.io/github/stars/jaylalkiya/Wifi-Sentry?style=flat-square&color=f7dc6f)
![Last commit](https://img.shields.io/github/last-commit/jaylalkiya/Wifi-Sentry?style=flat-square&color=2ea44f)

<br />

### 🖼️ StegoVault — Steganography & Steganalysis
`Python` `AES-256-GCM` `PBKDF2` `RS Analysis`

Hides an encrypted message in the low bit of a PNG, then detects it. The
passphrase goes through PBKDF2 at 200,000 iterations; a wrong key or a single
flipped bit is refused rather than silently mangled. The detector implements RS
Analysis (Fridrich, Goljan & Du, 2001) and scores any image 0–100 — including
images produced by other tools, which is how I know it isn't just recognising
its own output.

[![Repo](https://img.shields.io/badge/Code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/jaylalkiya/StegoVault)
![Stars](https://img.shields.io/github/stars/jaylalkiya/StegoVault?style=flat-square&color=f7dc6f)
![Last commit](https://img.shields.io/github/last-commit/jaylalkiya/StegoVault?style=flat-square&color=2ea44f)

---

## 💻 Development background

Before security I built applications, which is why I can reason about *why* a
vulnerability exists rather than only spotting that one does.

**[CodeShelf](https://github.com/jaylalkiya/CodeShelf)** — `Java` `JSP` `MySQL`
`Tomcat` · multi-module web app built with authentication and role-based access
control as first-class concerns: session management, MVC structure, and a schema
designed around least privilege.

**[Weather Application](https://github.com/jaylalkiya/WeatherApp)** —
`JavaScript` `REST API` · [live demo](https://weather-app-eight-plum-25.vercel.app)
· small project, useful practice in validating untrusted API responses and
failing cleanly on malformed input.

---

## 💼 Experience & Training

**Cyber Security Program, NSQF Level 4** — Adani Saksham, Ahmedabad · *2026 – Present*
300+ hours covering network foundations, firewalls and access control, audit & compliance, SOC monitoring and escalation, and VAPT in controlled environments.

**React.js and Node.js Developer Intern** — TechRover Solutions · *Dec 2025 – Jan 2026*
120 hours building a full application (auth, REST APIs, PostgreSQL schema design). Included here because understanding how apps are built end-to-end directly informs how I think about where they break.

---

## 📫 Say hi

<p align="center">
  <a href="mailto:jaylalkiya02@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" /></a>
  <a href="https://www.linkedin.com/in/jay-lalkiya-527149302/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
  <a href="https://github.com/jaylalkiya"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" /></a>
  <a href="https://jaylalkiyaportfolio.vercel.app/"><img src="https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=vercel&logoColor=white" /></a>
</p>

<br />

<p align="center">
  <i>"Understand how it's built to understand how it breaks."</i>
</p>
