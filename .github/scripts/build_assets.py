"""Generate the animated SVG header and project cards used in README.md.

Run from the repo root:  python .github/scripts/build_assets.py
Edit PROJECTS below to add / change cards.
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path("assets")
OUT.mkdir(exist_ok=True)

SANS = "'Segoe UI', Inter, -apple-system, Helvetica, Arial, sans-serif"
MONO = "'JetBrains Mono', 'Fira Code', Consolas, 'Courier New', monospace"

# ------------------------------------------------------------------ header
ROLES = [
    "Full-Stack Developer",
    "React · Next.js · TypeScript",
    "Python · Django · REST APIs",
    "Turning ideas into products",
]


def header() -> str:
    step = 3  # seconds each role stays on screen
    total = step * len(ROLES)
    roles = []
    for i, text in enumerate(ROLES):
        a, b = i / len(ROLES), (i + 1) / len(ROLES)
        e = 0.35 / total  # fade duration as a fraction of the loop
        key_times = f"0;{max(a,0):.4f};{a+e:.4f};{b-e:.4f};{b:.4f};1"
        roles.append(f"""
    <text x="80" y="232" class="role" opacity="0">&gt; {escape(text)}<tspan fill="#a5b4fc">▍<animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/></tspan>
      <animate attributeName="opacity" dur="{total}s" repeatCount="indefinite"
               keyTimes="{key_times}" values="0;0;1;1;0;0"/>
    </text>""")
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="320" viewBox="0 0 1200 320" role="img" aria-label="Dinesh Kumar — Full-Stack Developer">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#070a13"/><stop offset="1" stop-color="#0d1222"/>
    </linearGradient>
    <linearGradient id="name" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#ffffff"/>
      <stop offset="0.5" stop-color="#a5b4fc"/>
      <stop offset="1" stop-color="#67e8f9"/>
      <animateTransform attributeName="gradientTransform" type="translate" values="-0.3 0;0.3 0;-0.3 0" dur="8s" repeatCount="indefinite"/>
    </linearGradient>
    <filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="60"/></filter>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M40 0H0V40" fill="none" stroke="#ffffff" stroke-opacity="0.045"/>
    </pattern>
    <linearGradient id="fade" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#fff" stop-opacity="0.9"/><stop offset="1" stop-color="#fff" stop-opacity="0.1"/>
    </linearGradient>
    <mask id="gridmask"><rect width="1200" height="320" fill="url(#fade)"/></mask>
    <clipPath id="card"><rect width="1200" height="320" rx="20"/></clipPath>
    <style>
      .name {{ font: 800 64px {SANS}; letter-spacing: -1.5px; }}
      .hi   {{ font: 500 20px {MONO}; fill: #8b95a7; }}
      .role {{ font: 500 24px {MONO}; fill: #c7d2fe; }}
      .pill {{ font: 600 14px {SANS}; fill: #bbf7d0; }}
      .code {{ font: 500 15px {MONO}; fill: #64748b; }}
    </style>
  </defs>

  <g clip-path="url(#card)">
    <rect width="1200" height="320" fill="url(#bg)"/>
    <g filter="url(#blur)" opacity="0.75">
      <circle cx="950" cy="80" r="150" fill="#4f46e5">
        <animate attributeName="cx" values="950;1030;900;950" dur="14s" repeatCount="indefinite"/>
        <animate attributeName="cy" values="80;150;60;80" dur="14s" repeatCount="indefinite"/>
      </circle>
      <circle cx="1080" cy="260" r="120" fill="#0891b2">
        <animate attributeName="cx" values="1080;980;1100;1080" dur="11s" repeatCount="indefinite"/>
      </circle>
      <circle cx="760" cy="300" r="90" fill="#9333ea" opacity="0.7">
        <animate attributeName="cy" values="300;240;300" dur="9s" repeatCount="indefinite"/>
      </circle>
    </g>
    <rect width="1200" height="320" fill="url(#grid)" mask="url(#gridmask)"/>

    <!-- floating code snippet -->
    <g opacity="0.9">
      <animateTransform attributeName="transform" type="translate" values="0 0;0 -8;0 0" dur="6s" repeatCount="indefinite"/>
      <rect x="830" y="92" width="290" height="136" rx="14" fill="#0b1020" fill-opacity="0.72" stroke="#ffffff" stroke-opacity="0.08"/>
      <circle cx="852" cy="112" r="5" fill="#f87171"/><circle cx="870" cy="112" r="5" fill="#fbbf24"/><circle cx="888" cy="112" r="5" fill="#34d399"/>
      <text x="852" y="146" class="code"><tspan fill="#c084fc">const</tspan> <tspan fill="#e2e8f0">dev</tspan> = {{</text>
      <text x="872" y="170" class="code">stack: <tspan fill="#67e8f9">"full"</tspan>,</text>
      <text x="872" y="194" class="code">ships: <tspan fill="#86efac">true</tspan>,</text>
      <text x="852" y="218" class="code">}};</text>
    </g>

    <text x="80" y="104" class="hi">Hi there, I'm</text>
    <text x="78" y="176" class="name" fill="url(#name)">Dinesh Kumar</text>
{''.join(roles)}

    <!-- status pill -->
    <rect x="80" y="258" width="196" height="32" rx="16" fill="#052e1a" stroke="#22c55e" stroke-opacity="0.45"/>
    <circle cx="100" cy="274" r="5" fill="#22c55e"/>
    <circle cx="100" cy="274" r="5" fill="none" stroke="#22c55e" stroke-width="2">
      <animate attributeName="r" values="5;12" dur="1.8s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.9;0" dur="1.8s" repeatCount="indefinite"/>
    </circle>
    <text x="114" y="279" class="pill">Available for work</text>
  </g>
</svg>
"""


# ------------------------------------------------------------------ cards
PROJECTS = [
    dict(slug="portfolio", title="Developer Portfolio", accent=("#6366f1", "#22d3ee"),
         kicker="FEATURED · LIVE",
         desc=["ATS-friendly portfolio with dark/light mode,",
               "Framer Motion animations and a JSON data layer."],
         tags=["React", "TypeScript", "Vite", "Tailwind"]),
    dict(slug="library", title="Library Seat Booking", accent=("#f59e0b", "#ef4444"),
         kicker="FULL-STACK · SAAS",
         desc=["Hourly study-seat booking with memberships,",
               "reviews, notifications and an analytics panel."],
         tags=["Next.js", "Django REST", "Zustand", "Framer"]),
    dict(slug="roomscholars", title="Room Scholars", accent=("#10b981", "#3b82f6"),
         kicker="FULL-STACK · PROPTECH",
         desc=["Student-housing platform for the UK — listings,",
               "advanced filters, enquiry & newsletter APIs."],
         tags=["Next.js 16", "TypeScript", "MySQL", "Tailwind"]),
    dict(slug="events", title="Event Directory", accent=("#ec4899", "#8b5cf6"),
         kicker="BACKEND · PLATFORM",
         desc=["Event management & social posting platform",
               "with auth, email/SMS blasts and admin dashboard."],
         tags=["Django", "Python", "HTML", "CSS"]),
    dict(slug="shining", title="Shi-ning Services", accent=("#0ea5e9", "#6366f1"),
         kicker="CLIENT · LIVE",
         desc=["Dynamic business website with a Django backend,",
               "responsive UI and integrated contact forms."],
         tags=["Django", "HTML", "CSS", "JavaScript"]),
    dict(slug="chess", title="Chess Game", accent=("#a3e635", "#14b8a6"),
         kicker="GAME · LIVE",
         desc=["Playable in-browser chess game with move",
               "handling, built with vanilla web tech."],
         tags=["JavaScript", "HTML", "CSS"]),
]


def card(p: dict) -> str:
    a1, a2 = p["accent"]
    x = 36
    pills, tx = [], x
    for t in p["tags"]:
        w = 18 + len(t) * 8.2
        pills.append(f'<rect x="{tx}" y="196" width="{w:.0f}" height="28" rx="14" fill="{a1}" fill-opacity="0.12" stroke="{a1}" stroke-opacity="0.35"/>'
                     f'<text x="{tx + w/2:.0f}" y="215" class="tag" text-anchor="middle">{escape(t)}</text>')
        tx += w + 8
    desc = "".join(f'<text x="{x}" y="{130 + i*26}" class="desc">{escape(l)}</text>' for i, l in enumerate(p["desc"]))
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="600" height="260" viewBox="0 0 600 260" role="img" aria-label="{escape(p['title'])}">
  <defs>
    <linearGradient id="border" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="600" y2="260">
      <stop offset="0" stop-color="{a1}"/><stop offset="0.5" stop-color="{a2}" stop-opacity="0.15"/><stop offset="1" stop-color="{a2}"/>
      <animateTransform attributeName="gradientTransform" type="rotate" values="0 300 130;360 300 130" dur="10s" repeatCount="indefinite"/>
    </linearGradient>
    <radialGradient id="glow" cx="1" cy="0" r="0.9">
      <stop offset="0" stop-color="{a2}" stop-opacity="0.28"/><stop offset="1" stop-color="{a2}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="title" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="{a2}"/>
    </linearGradient>
    <linearGradient id="shine" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="0.5" stop-color="#fff" stop-opacity="0.06"/><stop offset="1" stop-color="#fff" stop-opacity="0"/>
    </linearGradient>
    <clipPath id="c"><rect x="2" y="2" width="596" height="256" rx="18"/></clipPath>
    <style>
      .kick {{ font: 700 12px {MONO}; letter-spacing: 1.5px; fill: {a2}; }}
      .title {{ font: 700 30px {SANS}; letter-spacing: -0.5px; }}
      .desc {{ font: 400 16px {SANS}; fill: #9aa4b2; }}
      .tag {{ font: 600 12.5px {SANS}; fill: #e2e8f0; }}
    </style>
  </defs>
  <rect x="1" y="1" width="598" height="258" rx="19" fill="#0b0f19" stroke="url(#border)" stroke-width="2"/>
  <g clip-path="url(#c)">
    <rect width="600" height="260" fill="url(#glow)"/>
    <rect x="-300" y="0" width="240" height="260" fill="url(#shine)" transform="skewX(-20)">
      <animate attributeName="x" values="-300;900" dur="5s" begin="1s" repeatCount="indefinite"/>
    </rect>
  </g>
  <circle cx="{x+4}" cy="47" r="4" fill="{a2}">
    <animate attributeName="opacity" values="1;0.3;1" dur="2s" repeatCount="indefinite"/>
  </circle>
  <text x="{x+16}" y="52" class="kick">{escape(p['kicker'])}</text>
  <text x="{x}" y="94" class="title" fill="url(#title)">{escape(p['title'])}</text>
  {desc}
  {''.join(pills)}
  <text x="564" y="56" text-anchor="end" font-size="22" fill="#64748b" font-family="{SANS}">↗
    <animateTransform attributeName="transform" type="translate" values="0 0;3 -3;0 0" dur="2s" repeatCount="indefinite"/>
  </text>
</svg>
"""


(OUT / "header.svg").write_text(header(), encoding="utf-8")
for p in PROJECTS:
    (OUT / f"card-{p['slug']}.svg").write_text(card(p), encoding="utf-8")
print("wrote", len(PROJECTS) + 1, "files to", OUT)
