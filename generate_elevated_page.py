import re

with open("synergy-wix-embed.html", "r", encoding="utf-8") as f:
    orig = f.read()

logo_m = re.search(r"img src=\"(data:image/jpeg;base64,[A-Za-z0-9+/=]+)\" alt=\"Synergy", orig)
ahmad_m = re.search(r"img src=\"(data:image/jpeg;base64,[A-Za-z0-9+/=]+)\" alt=\"Mr Ahmad Elsahn", orig)
yasmine_m = re.search(r"img src=\"(data:image/jpeg;base64,[A-Za-z0-9+/=]+)\" alt=\"Ms Yasmine Abdalla", orig)
pinders_m = re.search(r"img src=\"(data:image/png;base64,[A-Za-z0-9+/=]+)\" alt=\"Pinders Opticians", orig)

logo_b64 = logo_m.group(1) if logo_m else "images/synergy-logo-dark.jpg"
ahmad_b64 = ahmad_m.group(1) if ahmad_m else "images/elsahn-headshot.jpg"
yasmine_b64 = yasmine_m.group(1) if yasmine_m else "images/abdalla-headshot.jpg"
pinders_b64 = pinders_m.group(1) if pinders_m else "images/partner-pinders.png"

def make_html(is_embed=True):
    l_src = logo_b64 if is_embed else "images/synergy-logo-dark.jpg"
    a_src = ahmad_b64 if is_embed else "images/elsahn-headshot.jpg"
    y_src = yasmine_b64 if is_embed else "images/abdalla-headshot.jpg"
    p_src = pinders_b64 if is_embed else "images/partner-pinders.png"
    hero_img = "https://takoua-gif.github.io/takoua-biblio/images/optometrist-partners.jpg" if is_embed else "images/optometrist-partners.jpg"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EyePros Synergy &mdash; Consultant-Led Shared Care for UK Independent Opticians</title>
<meta name="description" content="Partner with EyePros Synergy: Named substantive NHS consultant ophthalmologists, &pound;250 flat cataract co-management fee, real-time Syndesis referral tracking, and guaranteed 7-day patient return to your independent practice.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root {{
  /* ═══ EyePros Luxury Medical Palette ═══ */
  --bg-canvas: #F8FAF9;
  --bg-canvas-warm: #FAF8F5;
  --bg-canvas-subtle: #F1F5F4;
  --bg-section-alt: rgba(240, 245, 244, 0.55);

  /* Signature EyePros Teal Green ("Tale Green") */
  --ep-teal: #0A7268;
  --ep-teal-vibrant: #0D8A7E;
  --ep-teal-dark: #074B44;
  --ep-teal-tint: rgba(10, 114, 104, 0.08);
  --ep-teal-tint-hover: rgba(10, 114, 104, 0.14);
  --ep-teal-glow: rgba(10, 114, 104, 0.28);

  /* Substantive British Ink Navy */
  --ep-navy: #111E2E;
  --ep-navy-soft: #1B2C42;
  --ep-navy-deep: #0B141F;
  --ep-navy-tint: rgba(17, 30, 46, 0.06);

  /* Luminous Ocean Blue & Sage Accents */
  --ep-blue: #0E7490;
  --ep-blue-light: rgba(14, 116, 144, 0.08);
  --ep-sage: #8FBBB5;
  --ep-sage-light: rgba(143, 187, 181, 0.18);
  --ep-gold: #D9822B;
  --ep-gold-light: rgba(217, 130, 43, 0.12);
  --ep-grey-border: rgba(226, 232, 240, 0.85);

  /* Typography */
  --text-heading: var(--ep-navy);
  --text-body: #334155;
  --text-muted: #64748B;
  --font-display: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
  --font-sans: 'Inter', system-ui, -apple-system, sans-serif;

  /* Frosted Glass & Surface Refinement */
  --glass-surface: rgba(255, 255, 255, 0.88);
  --glass-surface-hover: rgba(255, 255, 255, 0.98);
  --glass-surface-tint: linear-gradient(135deg, rgba(255, 255, 255, 0.92) 0%, rgba(246, 251, 250, 0.82) 100%);
  --glass-border: rgba(255, 255, 255, 0.95);
  --glass-outline: rgba(10, 114, 104, 0.12);
  --glass-outline-hover: rgba(10, 114, 104, 0.35);

  /* Depth & Shadows */
  --shadow-xs: 0 1px 3px rgba(17, 30, 46, 0.04);
  --shadow-sm: 0 4px 14px -2px rgba(17, 30, 46, 0.05);
  --shadow-md: 0 12px 28px -6px rgba(17, 30, 46, 0.08);
  --shadow-lg: 0 24px 50px -12px rgba(17, 30, 46, 0.12);
  --shadow-glow: 0 8px 30px var(--ep-teal-glow);
  --specular-inner: inset 0 1px 1px 0 rgba(255, 255, 255, 0.95);

  /* Geometry & Motion */
  --radius-sm: 8px;
  --radius-md: 14px;
  --radius-lg: 20px;
  --radius-xl: 28px;
  --radius-pill: 9999px;
  --max-w: 1180px;
  --ease-smooth: cubic-bezier(0.16, 1, 0.3, 1);
}}

*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
html{{scroll-behavior:smooth;-webkit-text-size-adjust:100%;scroll-padding-top:88px}}
body{{
  font-family:var(--font-sans);
  font-size:16px;
  line-height:1.65;
  color:var(--text-body);
  background-color:var(--bg-canvas);
  -webkit-font-smoothing:antialiased;
  overflow-x:hidden;
  position:relative;
}}
section,[id]{{scroll-margin-top:88px}}
img{{max-width:100%;display:block}}
a{{color:inherit;text-decoration:none}}
button{{font-family:inherit;cursor:pointer}}

/* Headings */
h1,h2,h3,h4,h5{{
  font-family:var(--font-display);
  color:var(--text-heading);
  line-height:1.2;
  font-weight:700;
  letter-spacing:-0.025em;
}}
h1{{font-size:clamp(2.35rem,4.5vw,3.6rem);font-weight:800;letter-spacing:-0.035em;line-height:1.12}}
h2{{font-size:clamp(1.85rem,3.2vw,2.5rem);font-weight:800;letter-spacing:-0.03em}}
h3{{font-size:1.28rem;font-weight:700}}
h4{{font-size:1.05rem;font-weight:700}}

.text-gradient{{
  background:linear-gradient(135deg, var(--ep-teal) 0%, var(--ep-blue) 100%);
  -webkit-background-clip:text;
  -webkit-text-fill-color:transparent;
}}

/* ═══ Ambient Aurora Mesh Background ═══ */
.aurora-bg {{
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  z-index: 0;
  pointer-events: none;
  overflow: hidden;
  contain: paint;
  max-width: 100vw;
  background-color: var(--bg-canvas);
  background-image:
    radial-gradient(at 0% 0%, rgba(10, 114, 104, 0.08) 0px, transparent 55%),
    radial-gradient(at 100% 15%, rgba(14, 116, 144, 0.07) 0px, transparent 50%),
    radial-gradient(at 50% 50%, var(--bg-canvas) 0px, transparent 80%);
}}

.aurora-blob {{
  position: absolute;
  border-radius: 50%;
  filter: blur(110px);
  -webkit-filter: blur(110px);
  opacity: 0.55;
  will-change: transform;
}}

.aurora-blob-1 {{
  width: 720px;
  height: 720px;
  background: radial-gradient(circle, rgba(10, 114, 104, 0.22) 0%, rgba(10, 114, 104, 0.06) 60%, transparent 80%);
  top: -180px;
  left: -120px;
  animation: auroraFloat1 32s var(--ease-smooth) infinite alternate;
}}

.aurora-blob-2 {{
  width: 780px;
  height: 780px;
  background: radial-gradient(circle, rgba(14, 116, 144, 0.18) 0%, rgba(14, 116, 144, 0.04) 55%, transparent 75%);
  top: 30%;
  right: -160px;
  animation: auroraFloat2 38s var(--ease-smooth) infinite alternate;
}}

.aurora-blob-3 {{
  width: 620px;
  height: 620px;
  background: radial-gradient(circle, rgba(217, 130, 43, 0.10) 0%, transparent 70%);
  bottom: 8%;
  left: 10%;
  animation: auroraFloat3 34s var(--ease-smooth) infinite alternate;
}}

.aurora-blob-4 {{
  width: 580px;
  height: 580px;
  background: radial-gradient(circle, rgba(143, 187, 181, 0.16) 0%, transparent 70%);
  top: 65%;
  right: 18%;
  animation: auroraFloat4 28s var(--ease-smooth) infinite alternate;
}}

.aurora-mesh-overlay {{
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse at 50% 20%, rgba(248, 250, 249, 0.35) 0%, rgba(248, 250, 249, 0.1) 100%);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
}}

@keyframes auroraFloat1 {{
  0% {{ transform: translate3d(0, 0, 0) scale(1); }}
  50% {{ transform: translate3d(80px, 60px, 0) scale(1.08); }}
  100% {{ transform: translate3d(-50px, 100px, 0) scale(0.95); }}
}}
@keyframes auroraFloat2 {{
  0% {{ transform: translate3d(0, 0, 0) scale(1); }}
  50% {{ transform: translate3d(-90px, -70px, 0) scale(1.06); }}
  100% {{ transform: translate3d(40px, -110px, 0) scale(0.96); }}
}}
@keyframes auroraFloat3 {{
  0% {{ transform: translate3d(0, 0, 0) scale(1); }}
  50% {{ transform: translate3d(60px, -50px, 0) scale(1.05); }}
  100% {{ transform: translate3d(-40px, 40px, 0) scale(0.94); }}
}}
@keyframes auroraFloat4 {{
  0% {{ transform: translate3d(0, 0, 0) scale(1); }}
  50% {{ transform: translate3d(-70px, 50px, 0) scale(1.08); }}
  100% {{ transform: translate3d(50px, -60px, 0) scale(0.95); }}
}}

@media (prefers-reduced-motion: reduce) {{
  .aurora-blob {{ animation: none !important; }}
}}

/* ═══ Layout Primitives ═══ */
.container {{
  max-width: var(--max-w);
  margin: 0 auto;
  padding: 0 28px;
  position: relative;
  z-index: 2;
}}
.section {{
  padding: 88px 0;
  position: relative;
  z-index: 2;
}}
.section-alt {{
  background: var(--bg-section-alt);
  border-top: 1px solid var(--ep-grey-border);
  border-bottom: 1px solid var(--ep-grey-border);
}}

/* Section Header Typography */
.section-head {{
  text-align: center;
  max-width: 680px;
  margin: 0 auto 52px;
}}
.section-head.text-left {{
  text-align: left;
  margin: 0 0 44px;
}}
.eyebrow-pill {{
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 5px 14px;
  border-radius: var(--radius-pill);
  background: var(--ep-teal-tint);
  border: 1px solid rgba(10, 114, 104, 0.22);
  color: var(--ep-teal-dark);
  font-family: var(--font-display);
  font-size: 0.74rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  margin-bottom: 16px;
}}
.eyebrow-dot {{
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--ep-teal);
  box-shadow: 0 0 8px var(--ep-teal);
  animation: pulseDot 2.2s infinite;
}}
@keyframes pulseDot {{
  0%, 100% {{ opacity: 1; transform: scale(1); }}
  50% {{ opacity: 0.4; transform: scale(0.85); }}
}}
.section-lead {{
  margin-top: 14px;
  font-size: 1.05rem;
  color: var(--text-muted);
  line-height: 1.65;
}}

/* ═══ Buttons & Interactive Controls ═══ */
.btn {{
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  font-family: var(--font-display);
  font-size: 0.94rem;
  font-weight: 700;
  padding: 13px 24px;
  border-radius: var(--radius-pill);
  transition: all 0.25s var(--ease-smooth);
  cursor: pointer;
  white-space: nowrap;
  line-height: 1;
  text-decoration: none;
}}
.btn-primary,
.nav-links a.btn-primary {{
  background: linear-gradient(135deg, var(--ep-teal) 0%, var(--ep-teal-dark) 100%);
  color: #FFFFFF !important;
  border: 1px solid rgba(255, 255, 255, 0.25);
  box-shadow: 0 4px 18px var(--ep-teal-glow), inset 0 1px 0 rgba(255, 255, 255, 0.25);
}}
.btn-primary:hover,
.nav-links a.btn-primary:hover {{
  background: linear-gradient(135deg, var(--ep-teal-vibrant) 0%, var(--ep-teal) 100%);
  color: #FFFFFF !important;
  transform: translateY(-2px);
  box-shadow: 0 8px 24px var(--ep-teal-glow);
}}
.btn-secondary {{
  background: rgba(255, 255, 255, 0.9);
  color: var(--ep-navy);
  border: 1px solid var(--ep-grey-border);
  box-shadow: var(--shadow-xs);
  backdrop-filter: blur(12px);
}}
.btn-secondary:hover {{
  background: #FFFFFF;
  border-color: var(--ep-teal);
  color: var(--ep-teal-dark);
  transform: translateY(-2px);
  box-shadow: var(--shadow-sm);
}}
.btn-sm {{
  padding: 9px 18px;
  font-size: 0.85rem;
}}
.btn svg {{
  width: 16px;
  height: 16px;
  transition: transform 0.2s ease;
}}
.btn:hover svg {{
  transform: translateX(3px);
}}

/* ═══ Sticky Glass Navigation ═══ */
.nav {{
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(248, 250, 249, 0.88);
  border-bottom: 1px solid rgba(226, 232, 240, 0.85);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  box-shadow: 0 2px 10px rgba(17, 30, 46, 0.03);
}}
.nav-inner {{
  max-width: var(--max-w);
  margin: 0 auto;
  padding: 0 28px;
  height: 74px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}}
.nav-brand {{
  display: flex;
  align-items: center;
  gap: 12px;
}}
.nav-logo-pill {{
  background: var(--ep-navy);
  padding: 6px 14px;
  border-radius: 10px;
  display: inline-flex;
  align-items: center;
  border: 1px solid rgba(143, 187, 181, 0.35);
  box-shadow: 0 2px 8px rgba(17, 30, 46, 0.15);
  transition: transform 0.2s ease;
}}
.nav-logo-pill:hover {{
  transform: translateY(-1px);
}}
.nav-logo-pill img {{
  height: 28px;
  width: auto;
  display: block;
}}
.nav-links {{
  display: flex;
  align-items: center;
  gap: 6px;
  list-style: none;
}}
.nav-links a:not(.btn) {{
  color: var(--text-body);
  font-size: 0.90rem;
  font-weight: 600;
  padding: 7px 11px;
  border-radius: var(--radius-sm);
  transition: all 0.2s ease;
  white-space: nowrap;
}}
.nav-links a:not(.btn):hover {{
  color: var(--ep-teal-dark);
  background: var(--ep-teal-tint);
}}
.nav-actions {{
  display: flex;
  align-items: center;
  gap: 12px;
  flex-shrink: 0;
}}
.nav-helpline {{
  font-size: 0.80rem;
  font-weight: 700;
  color: #C2410C;
  background: rgba(194, 65, 12, 0.08);
  border: 1px solid rgba(194, 65, 12, 0.22);
  padding: 6px 12px;
  border-radius: var(--radius-pill);
  display: flex;
  align-items: center;
  gap: 6px;
  white-space: nowrap;
}}
.nav-toggle {{
  display: none;
  background: rgba(10, 114, 104, 0.08);
  border: 1px solid rgba(10, 114, 104, 0.22);
  color: var(--ep-teal-dark);
  border-radius: 8px;
  cursor: pointer;
  padding: 7px;
  align-items: center;
  justify-content: center;
  line-height: 1;
}}

/* ═══ Hero Section: Bespoke MedTech Showcase ═══ */
.hero {{
  padding: 68px 0 76px;
  position: relative;
  z-index: 2;
}}
.hero-grid {{
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 52px;
  align-items: center;
}}
.hero-content {{
  max-width: 620px;
}}
.hero h1 {{
  margin-bottom: 20px;
}}
.hero-sub {{
  font-size: 1.14rem;
  color: var(--text-body);
  margin-bottom: 32px;
  line-height: 1.7;
}}
.hero-ctas {{
  display: flex;
  align-items: center;
  gap: 16px;
  flex-wrap: wrap;
  margin-bottom: 38px;
}}

/* Hero Metric Proof Strip */
.hero-proof-strip {{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
  padding-top: 26px;
  border-top: 1px solid var(--ep-grey-border);
}}
.proof-stat {{
  display: flex;
  flex-direction: column;
}}
.proof-val {{
  font-family: var(--font-display);
  font-size: 1.45rem;
  font-weight: 800;
  color: var(--ep-navy);
  line-height: 1.1;
  display: flex;
  align-items: center;
  gap: 6px;
}}
.proof-val .stat-dot {{
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--ep-teal);
}}
.proof-lbl {{
  font-size: 0.74rem;
  color: var(--text-muted);
  line-height: 1.35;
  margin-top: 4px;
}}

/* Hero Visual Showcase with Floating Glass Cards */
.hero-visual-wrap {{
  position: relative;
}}
.hero-visual-frame {{
  position: relative;
  border-radius: var(--radius-xl);
  overflow: hidden;
  border: 3px solid #FFFFFF;
  box-shadow: var(--shadow-lg), 0 0 36px var(--ep-teal-glow);
  background: #FFFFFF;
}}
.hero-visual-frame img {{
  width: 100%;
  height: 440px;
  object-fit: cover;
  object-position: center 25%;
  transition: transform 0.6s var(--ease-smooth);
}}
.hero-visual-frame:hover img {{
  transform: scale(1.02);
}}

/* Floating Glass Cards */
.floating-glass-card {{
  position: absolute;
  background: rgba(255, 255, 255, 0.92);
  border: 1px solid #FFFFFF;
  border-radius: var(--radius-md);
  padding: 14px 18px;
  box-shadow: 0 16px 36px -6px rgba(17, 30, 46, 0.14);
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
  z-index: 3;
  transition: transform 0.3s ease;
}}
.floating-glass-card:hover {{
  transform: translateY(-3px);
}}
.float-card-top {{
  top: -18px;
  right: -18px;
  max-width: 270px;
}}
.float-card-bottom {{
  bottom: -22px;
  left: -20px;
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 16px 20px;
}}

.f-badge-head {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  margin-bottom: 6px;
}}
.f-status-pill {{
  font-size: 0.68rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  padding: 2px 8px;
  border-radius: var(--radius-pill);
  background: rgba(16, 185, 129, 0.12);
  color: #059669;
  display: inline-flex;
  align-items: center;
  gap: 5px;
}}
.f-status-dot {{
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: #10B981;
}}
.f-title {{
  font-size: 0.88rem;
  font-weight: 700;
  color: var(--ep-navy);
  line-height: 1.3;
}}
.f-timeline {{
  display: flex;
  align-items: center;
  gap: 6px;
  margin-top: 8px;
  font-size: 0.72rem;
  color: var(--ep-teal-dark);
  font-weight: 600;
}}
.f-timeline svg {{
  width: 12px;
  height: 12px;
  color: var(--ep-teal);
}}

.float-amount {{
  font-family: var(--font-display);
  font-size: 2.1rem;
  font-weight: 800;
  color: var(--ep-teal);
  line-height: 1;
}}
.float-desc strong {{
  display: block;
  font-size: 0.86rem;
  color: var(--ep-navy);
}}
.float-desc span {{
  font-size: 0.74rem;
  color: var(--text-muted);
}}

/* ═══ Bento Grid: Partnership Advantages ═══ */
.bento-grid {{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 22px;
}}
.bento-col-2 {{
  grid-column: span 2;
}}
.bento-col-1 {{
  grid-column: span 1;
}}
.bento-card {{
  background: var(--glass-surface);
  border: 1px solid var(--glass-border);
  outline: 1px solid var(--glass-outline);
  border-radius: var(--radius-lg);
  padding: 32px 30px;
  box-shadow: var(--shadow-sm);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  transition: all 0.28s var(--ease-smooth);
  display: flex;
  flex-direction: column;
  position: relative;
  overflow: hidden;
}}
.bento-card::before {{
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: linear-gradient(90deg, transparent, rgba(10, 114, 104, 0.4), transparent);
  opacity: 0;
  transition: opacity 0.3s ease;
}}
.bento-card:hover {{
  outline-color: var(--glass-outline-hover);
  background: var(--glass-surface-hover);
  transform: translateY(-3px);
  box-shadow: var(--shadow-md), 0 0 24px -6px var(--ep-teal-glow);
}}
.bento-card:hover::before {{
  opacity: 1;
}}

.bento-header {{
  display: flex;
  align-items: center;
  gap: 14px;
  margin-bottom: 18px;
}}
.bento-icon {{
  width: 44px;
  height: 44px;
  border-radius: 12px;
  background: var(--ep-teal-tint);
  border: 1px solid rgba(10, 114, 104, 0.22);
  color: var(--ep-teal);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}}
.bento-icon svg {{
  width: 22px;
  height: 22px;
}}
.bento-card h3 {{
  font-size: 1.22rem;
  color: var(--ep-navy);
}}
.bento-card p {{
  font-size: 0.94rem;
  color: var(--text-body);
  line-height: 1.6;
  margin-bottom: 20px;
}}

/* Mini UI Mockup inside Bento Card (Syndesis Platform) */
.syndesis-preview-card {{
  margin-top: auto;
  background: #FFFFFF;
  border: 1px solid var(--ep-grey-border);
  border-radius: var(--radius-md);
  padding: 14px 16px;
  box-shadow: var(--shadow-xs);
}}
.syndesis-row {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.8rem;
  margin-bottom: 8px;
}}
.syndesis-patient {{
  font-weight: 700;
  color: var(--ep-navy);
}}
.syndesis-status {{
  background: rgba(10, 114, 104, 0.1);
  color: var(--ep-teal-dark);
  font-weight: 700;
  font-size: 0.7rem;
  padding: 2px 8px;
  border-radius: 6px;
}}
.syndesis-steps {{
  display: flex;
  gap: 6px;
}}
.syndesis-step-bar {{
  flex: 1;
  height: 4px;
  border-radius: 2px;
  background: #E2E8F0;
}}
.syndesis-step-bar.done {{
  background: var(--ep-teal);
}}
.syndesis-step-bar.active {{
  background: #10B981;
}}
.syndesis-meta {{
  display: flex;
  justify-content: space-between;
  margin-top: 8px;
  font-size: 0.72rem;
  color: var(--text-muted);
}}

/* Quote callout inside Surgeon continuity card */
.bento-quote {{
  margin-top: auto;
  padding: 14px 16px;
  background: var(--bg-canvas-subtle);
  border-left: 3px solid var(--ep-teal);
  border-radius: 0 8px 8px 0;
  font-size: 0.86rem;
  color: var(--text-heading);
  font-style: italic;
}}

/* Badge cluster inside Bento */
.bento-pill-cluster {{
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-top: auto;
}}
.bento-pill {{
  font-size: 0.76rem;
  font-weight: 600;
  color: var(--ep-teal-dark);
  background: var(--ep-teal-tint);
  border: 1px solid rgba(10, 114, 104, 0.2);
  padding: 3px 10px;
  border-radius: var(--radius-pill);
}}

/* ═══ Referral Pathway: 5-Step Connected Care Loop ═══ */
.pathway-track {{
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 16px;
  position: relative;
  margin-top: 24px;
}}
.pathway-track::before {{
  content: '';
  position: absolute;
  top: 38px;
  left: 40px;
  right: 40px;
  height: 2px;
  background: linear-gradient(90deg, var(--ep-teal) 0%, var(--ep-blue) 50%, var(--ep-teal) 100%);
  z-index: 1;
  opacity: 0.35;
}}
.pathway-card {{
  background: var(--glass-surface);
  border: 1px solid var(--glass-border);
  outline: 1px solid var(--glass-outline);
  border-radius: var(--radius-lg);
  padding: 24px 20px;
  box-shadow: var(--shadow-sm);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  position: relative;
  z-index: 2;
  transition: all 0.25s var(--ease-smooth);
  display: flex;
  flex-direction: column;
}}
.pathway-card:hover {{
  transform: translateY(-4px);
  background: #FFFFFF;
  outline-color: var(--ep-teal);
  box-shadow: var(--shadow-md), 0 0 20px -5px var(--ep-teal-glow);
}}
.pathway-step-num {{
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: #FFFFFF;
  border: 2px solid var(--ep-teal);
  color: var(--ep-teal-dark);
  font-family: var(--font-display);
  font-size: 0.85rem;
  font-weight: 800;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 16px;
  box-shadow: var(--shadow-xs);
}}
.pathway-actor {{
  font-family: var(--font-display);
  font-size: 0.68rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  margin-bottom: 6px;
  display: block;
}}
.pathway-actor.optom {{
  color: var(--ep-teal);
}}
.pathway-actor.eyepros {{
  color: var(--ep-blue);
}}
.pathway-card h4 {{
  font-size: 0.98rem;
  margin-bottom: 8px;
  color: var(--ep-navy);
}}
.pathway-card p {{
  font-size: 0.82rem;
  color: var(--text-body);
  line-height: 1.5;
}}

/* ═══ Consultant Leadership & Governance ═══ */
.consultants-grid {{
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 28px;
}}
.consultant-card {{
  background: var(--glass-surface);
  border: 1px solid var(--glass-border);
  outline: 1px solid var(--glass-outline);
  border-radius: var(--radius-xl);
  padding: 36px 32px;
  box-shadow: var(--shadow-sm);
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
  transition: all 0.3s var(--ease-smooth);
  display: flex;
  flex-direction: column;
  position: relative;
}}
.consultant-card:hover {{
  outline-color: var(--ep-teal);
  box-shadow: var(--shadow-lg), 0 0 30px -8px var(--ep-teal-glow);
  transform: translateY(-3px);
  background: #FFFFFF;
}}
.consultant-header {{
  display: flex;
  align-items: center;
  gap: 22px;
  margin-bottom: 22px;
}}
.consultant-photo {{
  width: 104px;
  height: 104px;
  border-radius: 18px;
  object-fit: cover;
  object-position: top center;
  border: 2.5px solid var(--ep-teal);
  box-shadow: 0 8px 22px -4px rgba(10, 114, 104, 0.22);
  flex-shrink: 0;
}}
.consultant-title-group h3 {{
  font-size: 1.35rem;
  font-weight: 800;
  color: var(--ep-navy);
  margin-bottom: 4px;
}}
.consultant-role {{
  color: var(--ep-teal-dark);
  font-weight: 700;
  font-size: 0.92rem;
  margin-bottom: 10px;
}}
.consultant-credentials {{
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}}
.cred-badge {{
  background: var(--ep-teal-tint);
  border: 1px solid rgba(10, 114, 104, 0.24);
  color: var(--ep-navy);
  font-size: 0.72rem;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: 6px;
  letter-spacing: 0.02em;
}}
.consultant-bio {{
  font-size: 0.92rem;
  color: var(--text-body);
  line-height: 1.65;
  margin-bottom: 22px;
}}
.consultant-posts {{
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 10px;
  font-size: 0.86rem;
  color: var(--ep-navy);
  font-weight: 600;
  border-top: 1px solid var(--ep-grey-border);
  padding-top: 18px;
  margin-top: auto;
}}
.consultant-posts li {{
  display: flex;
  align-items: flex-start;
  gap: 10px;
}}
.consultant-posts svg {{
  width: 16px;
  height: 16px;
  color: var(--ep-teal);
  flex-shrink: 0;
  margin-top: 4px;
}}

/* 4 Clinical Commitments */
.gov-grid {{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 18px;
  margin-top: 36px;
}}
.gov-card {{
  background: rgba(255, 255, 255, 0.85);
  border: 1px solid #FFFFFF;
  outline: 1px solid var(--ep-grey-border);
  border-radius: var(--radius-md);
  padding: 22px 20px;
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  box-shadow: var(--shadow-xs);
  transition: all 0.2s ease;
}}
.gov-card:hover {{
  outline-color: var(--ep-teal);
  background: #FFFFFF;
  transform: translateY(-2px);
  box-shadow: var(--shadow-sm);
}}
.gov-card h4 {{
  font-size: 0.94rem;
  color: var(--ep-navy);
  margin-bottom: 6px;
  display: flex;
  align-items: center;
  gap: 8px;
}}
.gov-card h4 svg {{
  width: 16px;
  height: 16px;
  color: var(--ep-teal);
  flex-shrink: 0;
}}
.gov-card p {{
  font-size: 0.82rem;
  color: var(--text-muted);
  line-height: 1.5;
}}

/* ═══ Trusted By Section & Prominent Pinders Showcase ═══ */
.section-trusted {{
  background: linear-gradient(180deg, rgba(248, 250, 249, 0.5) 0%, rgba(240, 246, 245, 0.7) 50%, rgba(248, 250, 249, 0.5) 100%);
  border-top: 1px solid var(--ep-grey-border);
  border-bottom: 1px solid var(--ep-grey-border);
  position: relative;
  overflow: hidden;
  padding: 72px 0;
}}

/* Featured Partner Card: Pinders Opticians */
.pinders-featured-card {{
  max-width: 860px;
  margin: 0 auto 42px;
  background: #FFFFFF;
  border: 1.5px solid rgba(10, 114, 104, 0.25);
  border-radius: var(--radius-xl);
  padding: 32px 38px;
  box-shadow: var(--shadow-md), 0 0 30px var(--ep-teal-tint);
  display: flex;
  align-items: center;
  gap: 36px;
  position: relative;
}}
.pinders-featured-logo {{
  background: #FFFFFF;
  padding: 12px 20px;
  border-radius: 14px;
  border: 1px solid var(--ep-grey-border);
  box-shadow: var(--shadow-xs);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}}
.pinders-featured-logo img {{
  height: 48px;
  width: auto;
}}
.pinders-featured-meta strong {{
  font-family: var(--font-display);
  font-size: 1.25rem;
  color: var(--ep-navy);
  display: block;
  margin-bottom: 4px;
}}
.pinders-featured-meta .pinders-tag {{
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 0.78rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--ep-teal-dark);
  background: var(--ep-teal-tint);
  padding: 3px 10px;
  border-radius: var(--radius-pill);
  margin-bottom: 10px;
}}
.pinders-featured-meta p {{
  font-size: 0.92rem;
  color: var(--text-body);
  line-height: 1.6;
  font-style: italic;
}}

/* Smooth Infinite Partner Carousel */
.partner-carousel-wrap {{
  position: relative;
  width: 100%;
  overflow: hidden;
  mask-image: linear-gradient(90deg, transparent 0%, #000000 12%, #000000 88%, transparent 100%);
  -webkit-mask-image: linear-gradient(90deg, transparent 0%, #000000 12%, #000000 88%, transparent 100%);
}}
.partner-carousel-track {{
  display: flex;
  gap: 18px;
  width: max-content;
  animation: partnerMarquee 38s linear infinite;
}}
.partner-carousel-track:hover {{
  animation-play-state: paused;
}}
.partner-carousel-track:hover {{
  animation-play-state: paused;
}}
@keyframes partnerMarquee {{
  0% {{ transform: translateX(0); }}
  100% {{ transform: translateX(-50%); }}
}}

.partner-card {{
  min-width: 290px;
  background: var(--glass-surface);
  border: 1px solid var(--glass-border);
  outline: 1px solid var(--glass-outline);
  border-radius: var(--radius-md);
  padding: 14px 20px;
  display: flex;
  align-items: center;
  gap: 14px;
  box-shadow: var(--shadow-xs);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  transition: all 0.25s ease;
}}
.partner-card:hover {{
  outline-color: var(--ep-teal);
  box-shadow: var(--shadow-sm);
  background: #FFFFFF;
}}
.partner-logo-pill {{
  background: #FFFFFF;
  height: 38px;
  padding: 4px 12px;
  border-radius: 8px;
  border: 1px solid var(--ep-grey-border);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}}
.partner-logo-pill img {{
  height: 24px;
  width: auto;
}}
.partner-badge-icon {{
  width: 40px;
  height: 40px;
  border-radius: 10px;
  background: var(--ep-teal-tint);
  border: 1px solid rgba(10, 114, 104, 0.25);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--ep-teal);
  flex-shrink: 0;
}}
.partner-meta strong {{
  font-size: 0.92rem;
  color: var(--ep-navy);
  display: block;
}}
.partner-meta span {{
  font-size: 0.74rem;
  color: var(--text-muted);
  display: block;
}}
.partner-card-add {{
  border-style: dashed;
  outline: none;
  background: transparent;
  color: var(--ep-teal);
}}
.partner-card-add:hover {{
  background: var(--ep-teal-tint);
  border-color: var(--ep-teal);
}}

/* ═══ Remuneration & Practice Earnings Calculator ═══ */
.remuneration-layout {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 32px;
  align-items: stretch;
  margin-bottom: 36px;
}}

/* Flagship Cataract Card */
.flagship-fee-card {{
  background: linear-gradient(135deg, #FFFFFF 0%, rgba(246, 252, 250, 0.9) 100%);
  border: 2px solid var(--ep-teal);
  border-radius: var(--radius-xl);
  padding: 40px 36px;
  box-shadow: var(--shadow-md), 0 0 32px var(--ep-teal-tint);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  position: relative;
}}
.flagship-badge {{
  position: absolute;
  top: 24px;
  right: 24px;
  background: var(--ep-teal);
  color: #FFFFFF;
  font-family: var(--font-display);
  font-size: 0.72rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  padding: 4px 12px;
  border-radius: var(--radius-pill);
}}
.fee-flagship-val {{
  font-family: var(--font-display);
  font-size: 3.5rem;
  font-weight: 800;
  color: var(--ep-navy);
  line-height: 1;
  letter-spacing: -0.04em;
  margin: 14px 0 6px;
}}
.fee-flagship-val span {{
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--ep-teal-dark);
  letter-spacing: normal;
}}
.flagship-features {{
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin: 24px 0;
  font-size: 0.92rem;
  color: var(--text-body);
}}
.flagship-features li {{
  display: flex;
  align-items: center;
  gap: 10px;
}}
.flagship-features svg {{
  width: 18px;
  height: 18px;
  color: var(--ep-teal);
  flex-shrink: 0;
}}

/* Interactive Practice Revenue Calculator Card */
.calc-card {{
  background: var(--glass-surface);
  border: 1px solid var(--glass-border);
  outline: 1px solid var(--glass-outline);
  border-radius: var(--radius-xl);
  padding: 40px 36px;
  box-shadow: var(--shadow-sm);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}}
.calc-card h3 {{
  font-size: 1.35rem;
  color: var(--ep-navy);
  margin-bottom: 6px;
}}
.calc-card p {{
  font-size: 0.9rem;
  color: var(--text-muted);
  margin-bottom: 24px;
}}
.slider-group {{
  margin-bottom: 28px;
}}
.slider-header {{
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-bottom: 12px;
}}
.slider-label {{
  font-weight: 700;
  font-size: 0.92rem;
  color: var(--ep-navy);
}}
.slider-value {{
  font-family: var(--font-display);
  font-size: 1.35rem;
  font-weight: 800;
  color: var(--ep-teal-dark);
}}
.calc-slider {{
  width: 100%;
  height: 8px;
  border-radius: 4px;
  background: #E2E8F0;
  outline: none;
  -webkit-appearance: none;
  cursor: pointer;
}}
.calc-slider::-webkit-slider-thumb {{
  -webkit-appearance: none;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: var(--ep-teal);
  box-shadow: 0 2px 8px var(--ep-teal-glow);
  cursor: pointer;
  border: 2px solid #FFFFFF;
}}

.calc-output-box {{
  background: var(--bg-canvas-subtle);
  border: 1px solid var(--ep-grey-border);
  border-radius: var(--radius-md);
  padding: 20px;
  text-align: center;
}}
.calc-output-label {{
  font-size: 0.78rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--text-muted);
  margin-bottom: 4px;
}}
.calc-output-val {{
  font-family: var(--font-display);
  font-size: 2.3rem;
  font-weight: 800;
  color: var(--ep-teal);
  line-height: 1.1;
  letter-spacing: -0.03em;
}}
.calc-output-note {{
  font-size: 0.76rem;
  color: var(--text-muted);
  margin-top: 6px;
}}

/* Categorized Fee Grid (Remaining 6 Fees) */
.fees-grid {{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
}}
.fee-card {{
  background: var(--glass-surface);
  border: 1px solid var(--glass-border);
  outline: 1px solid var(--glass-outline);
  border-radius: var(--radius-lg);
  padding: 24px 22px;
  box-shadow: var(--shadow-xs);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  transition: all 0.25s var(--ease-smooth);
  display: flex;
  flex-direction: column;
}}
.fee-card:hover {{
  outline-color: var(--ep-teal);
  background: #FFFFFF;
  transform: translateY(-3px);
  box-shadow: var(--shadow-sm);
}}
.fee-category {{
  font-family: var(--font-display);
  font-size: 0.72rem;
  font-weight: 800;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--ep-teal-dark);
  margin-bottom: 10px;
}}
.fee-amount-box {{
  margin-bottom: 8px;
}}
.fee-upto {{
  font-size: 0.7rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--text-muted);
  display: block;
  margin-bottom: 2px;
}}
.fee-upto-spacer {{
  font-size: 0.7rem;
  display: block;
  margin-bottom: 2px;
  visibility: hidden;
}}
.fee-val {{
  font-family: var(--font-display);
  font-size: 1.95rem;
  font-weight: 800;
  color: var(--ep-navy);
  line-height: 1;
  letter-spacing: -0.02em;
}}
.fee-cycle {{
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--text-muted);
}}
.fee-card h4 {{
  font-size: 0.95rem;
  color: var(--ep-navy);
  margin-top: 6px;
  margin-bottom: 4px;
}}
.fee-card p {{
  font-size: 0.8rem;
  color: var(--text-muted);
  line-height: 1.45;
}}

/* ═══ Shared Care Agreement Executive Callout ═══ */
.agreement-banner {{
  margin-top: 48px;
  background: linear-gradient(135deg, var(--ep-navy) 0%, var(--ep-navy-soft) 100%);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: var(--radius-xl);
  padding: 40px 44px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 32px;
  box-shadow: 0 16px 40px -10px rgba(17, 30, 46, 0.22);
  flex-wrap: wrap;
}}
.agreement-banner h3 {{
  font-size: 1.45rem;
  margin-bottom: 8px;
  color: #FFFFFF;
}}
.agreement-banner p {{
  font-size: 0.95rem;
  color: rgba(255, 255, 255, 0.82);
  margin: 0;
  max-width: 620px;
  line-height: 1.6;
}}
.agreement-actions {{
  display: flex;
  gap: 14px;
  flex-wrap: wrap;
}}
.agreement-banner .btn-primary {{
  background: #FFFFFF;
  color: var(--ep-teal-dark);
  border: none;
  font-weight: 700;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
}}
.agreement-banner .btn-primary:hover {{
  background: #F1F5F9;
  color: var(--ep-navy);
  transform: translateY(-2px);
}}
.agreement-banner .btn-outline-white {{
  background: transparent;
  color: #FFFFFF;
  border: 1.5px solid rgba(255, 255, 255, 0.35);
}}
.agreement-banner .btn-outline-white:hover {{
  background: rgba(255, 255, 255, 0.1);
  border-color: #FFFFFF;
}}

/* ═══ Partnership Registration Form & Contact ═══ */
.enquiry-layout {{
  display: grid;
  grid-template-columns: 1.25fr 0.75fr;
  gap: 38px;
  align-items: start;
}}
.enquiry-card {{
  background: #FFFFFF;
  border: 1px solid var(--ep-grey-border);
  border-radius: var(--radius-xl);
  padding: 40px 38px;
  box-shadow: var(--shadow-md);
}}
.form-grid {{
  display: flex;
  flex-direction: column;
  gap: 18px;
}}
.form-row {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}}
.form-group {{
  display: flex;
  flex-direction: column;
  gap: 6px;
}}
.form-group label {{
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--ep-navy);
}}
.form-group {{
  min-width: 0;
}}
.form-group input,
.form-group select,
.form-group textarea {{
  font-family: var(--font-sans);
  font-size: 0.94rem;
  padding: 12px 14px;
  border-radius: var(--radius-sm);
  border: 1.5px solid #CBD5E1;
  background: #FFFFFF;
  color: var(--text-body);
  transition: all 0.2s ease;
  width: 100%;
  min-width: 0;
  box-sizing: border-box;
}}
.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {{
  outline: none;
  border-color: var(--ep-teal);
  box-shadow: 0 0 0 3px var(--ep-teal-tint);
}}

.contact-card {{
  background: var(--glass-surface);
  border: 1px solid var(--glass-border);
  border-radius: var(--radius-xl);
  padding: 34px 30px;
  box-shadow: var(--shadow-sm);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
}}
.contact-card h4 {{
  font-size: 1.15rem;
  margin-bottom: 8px;
  color: var(--ep-navy);
}}
.contact-card p {{
  font-size: 0.88rem;
  color: var(--text-muted);
  line-height: 1.55;
  margin-bottom: 22px;
}}
.contact-list {{
  display: flex;
  flex-direction: column;
  gap: 16px;
}}
.contact-item {{
  display: flex;
  align-items: flex-start;
  gap: 12px;
  font-size: 0.88rem;
}}
.contact-item svg {{
  width: 20px;
  height: 20px;
  color: var(--ep-teal);
  flex-shrink: 0;
  margin-top: 2px;
}}
.contact-item strong {{
  color: var(--ep-navy);
  display: block;
}}

/* ═══ FAQ Accordion ═══ */
.faq-list {{
  max-width: 820px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 12px;
}}
.faq-item {{
  background: var(--glass-surface);
  border: 1px solid var(--glass-border);
  outline: 1px solid var(--glass-outline);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-xs);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  overflow: hidden;
  transition: all 0.2s ease;
}}
.faq-item:hover {{
  outline-color: var(--ep-teal);
  background: #FFFFFF;
}}
.faq-q {{
  width: 100%;
  text-align: left;
  background: none;
  border: none;
  padding: 20px 24px;
  font-family: var(--font-display);
  font-size: 1.02rem;
  font-weight: 700;
  color: var(--ep-navy);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}}
.faq-q svg {{
  width: 18px;
  height: 18px;
  color: var(--ep-teal);
  transition: transform 0.25s ease;
  flex-shrink: 0;
}}
.faq-item.open .faq-q svg {{
  transform: rotate(180deg);
}}
.faq-a {{
  display: none;
  padding: 0 24px 20px;
  font-size: 0.92rem;
  color: var(--text-body);
  line-height: 1.65;
}}
.faq-item.open .faq-a {{
  display: block;
}}

/* ═══ Footer ═══ */
.footer {{
  background: #FFFFFF;
  border-top: 1px solid var(--ep-grey-border);
  padding: 44px 0;
  position: relative;
  z-index: 2;
}}
.footer-row {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-bottom: 24px;
  border-bottom: 1px solid var(--ep-grey-border);
  margin-bottom: 20px;
  flex-wrap: wrap;
  gap: 20px;
}}
.footer-copy {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.82rem;
  color: var(--text-muted);
  gap: 16px;
  flex-wrap: wrap;
}}

/* ═══ Responsive Breakpoints ═══ */
@media (max-width: 1024px) {{
  .hero-grid {{ grid-template-columns: 1fr; gap: 40px; }}
  .bento-grid {{ grid-template-columns: 1fr; }}
  .bento-col-2, .bento-col-1 {{ grid-column: span 1; }}
  .pathway-track {{ grid-template-columns: 1fr; }}
  .pathway-track::before {{ display: none; }}
  .consultants-grid {{ grid-template-columns: 1fr; }}
  .gov-grid {{ grid-template-columns: repeat(2, 1fr); }}
  .remuneration-layout {{ grid-template-columns: 1fr; }}
  .fees-grid {{ grid-template-columns: repeat(2, 1fr); }}
  .enquiry-layout {{ grid-template-columns: 1fr; }}
}}

@media (max-width: 768px) {{
  body {{ font-size: 15px; }}
  .section {{ padding: 54px 0; }}
  .nav-inner {{ height: 62px; padding: 0 16px; }}
  .nav-links {{
    display: none;
    position: absolute;
    top: 62px;
    left: 0;
    right: 0;
    background: #FFFFFF;
    border-bottom: 1px solid var(--ep-grey-border);
    flex-direction: column;
    padding: 18px 24px;
    box-shadow: var(--shadow-lg);
    gap: 8px;
  }}
  .nav-links.active {{ display: flex !important; }}
  .nav-links li {{ width: 100%; }}
  .nav-links a:not(.btn) {{ display: block; width: 100%; padding: 10px 0; }}
  .nav-links a.btn-primary {{ display: flex; width: 100%; justify-content: center; margin-top: 8px; }}
  .nav-toggle {{ display: inline-flex !important; }}
  .nav-helpline {{ display: none; }}

  .hero {{ padding: 36px 0 44px; }}
  .hero-proof-strip {{ grid-template-columns: repeat(2, 1fr); gap: 14px; }}
  .hero-visual-frame img {{ height: 260px; }}
  .floating-glass-card {{ position: static; margin-top: 14px; width: 100%; }}
  .float-card-top, .float-card-bottom {{ margin: 12px 0 0; }}

  .gov-grid {{ grid-template-columns: 1fr; }}
  .fees-grid {{ grid-template-columns: 1fr; }}
  .pinders-featured-card {{ flex-direction: column; text-align: center; padding: 24px 18px; }}
  .agreement-banner {{ flex-direction: column; align-items: flex-start; padding: 28px 22px; }}
  .enquiry-card {{ padding: 28px 18px; }}
  .form-row {{ grid-template-columns: 1fr; }}
}}

@media (max-width: 640px) {{
  .hero-ctas {{
    flex-direction: column;
    width: 100%;
  }}
  .hero-ctas .btn {{
    width: 100%;
    justify-content: center;
  }}
}}
</style>
</head>
<body>

<!-- Ambient Aurora Mesh Background -->
<div class="aurora-bg">
  <div class="aurora-blob aurora-blob-1"></div>
  <div class="aurora-blob aurora-blob-2"></div>
  <div class="aurora-blob aurora-blob-3"></div>
  <div class="aurora-blob aurora-blob-4"></div>
  <div class="aurora-mesh-overlay"></div>
</div>

<!-- Sticky Glass Navigation -->
<header class="nav">
  <div class="nav-inner">
    <a href="#hero" class="nav-brand" aria-label="EyePros Synergy">
      <div class="nav-logo-pill">
        <img src="{l_src}" alt="Synergy by EyePros">
      </div>
    </a>
    <ul class="nav-links">
      <li><a href="#benefits">Why EyePros</a></li>
      <li><a href="#journey">Patient Pathway</a></li>
      <li><a href="#consultants">Surgeons</a></li>
      <li><a href="#trusted">Partners</a></li>
      <li><a href="#remuneration">Fees &amp; Calculator</a></li>
      <li><a href="#faq">FAQ</a></li>
      <li><a href="#partner-enquiry" class="btn btn-sm btn-primary">Become a Partner</a></li>
    </ul>
    <div class="nav-actions">
      <div class="nav-helpline">
        <svg viewBox="0 0 20 20" fill="currentColor" style="width:14px;height:14px"><path d="M2 3a1 1 0 011-1h2.153a1 1 0 01.986.836l.74 4.435a1 1 0 01-.54 1.06l-1.548.773a11.037 11.037 0 006.105 6.105l.774-1.548a1 1 0 011.059-.54l4.435.74a1 1 0 01.836.986V17a1 1 0 01-1 1h-2C7.82 18 2 12.18 2 4V3z"/></svg>
        <span>Urgent: Option 5</span>
      </div>
      <button class="nav-toggle" id="navToggle" aria-label="Toggle Navigation">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" style="width:22px;height:22px;display:block">
          <line x1="3" y1="6" x2="21" y2="6"></line>
          <line x1="3" y1="12" x2="21" y2="12"></line>
          <line x1="3" y1="18" x2="21" y2="18"></line>
        </svg>
      </button>
    </div>
  </div>
</header>

<!-- Hero Section: Bespoke MedTech Showcase -->
<section id="hero" class="hero">
  <div class="container">
    <div class="hero-grid">
      <div class="hero-content">
        <div class="eyebrow-pill">
          <span class="eyebrow-dot"></span>
          <span>UK INDEPENDENT OPTOMETRY SHARED CARE</span>
        </div>
        <h1>Expand your clinical scope. Retain your patients. <span class="text-gradient">Earn fair shared-care fees.</span></h1>
        <p class="hero-sub">The consultant-led shared care programme built specifically for UK independent optometry practices. Named substantive NHS surgeons, direct communication through the Syndesis platform, and guaranteed 7-day discharge back to your consulting room.</p>
        <div class="hero-ctas">
          <a href="#partner-enquiry" class="btn btn-primary">
            <span>Become a Partner</span>
            <svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd"/></svg>
          </a>
          <a href="#remuneration" class="btn btn-secondary">Explore Fee Schedule</a>
        </div>
        <div class="hero-proof-strip">
          <div class="proof-stat">
            <div class="proof-val"><span class="stat-dot"></span>&pound;250</div>
            <div class="proof-lbl">Flat Cataract Shared-Care Fee</div>
          </div>
          <div class="proof-stat">
            <div class="proof-val"><span class="stat-dot"></span>7 Days</div>
            <div class="proof-lbl">Electronic Discharge to Practice</div>
          </div>
          <div class="proof-stat">
            <div class="proof-val"><span class="stat-dot"></span>100%</div>
            <div class="proof-lbl">Substantive NHS Consultants</div>
          </div>
          <div class="proof-stat">
            <div class="proof-val"><span class="stat-dot"></span>0 Volume</div>
            <div class="proof-lbl">No Referral Minimums Ever</div>
          </div>
        </div>
      </div>

      <div class="hero-visual-wrap">
        <div class="hero-visual-frame">
          <img src="{hero_img}" alt="Consultant and Referring Optometrist in Clinical Co-Management" loading="eager">
        </div>

        <!-- Floating Glass Card: 7-Day Guarantee -->
        <div class="floating-glass-card float-card-top">
          <div class="f-badge-head">
            <span class="f-status-pill"><span class="f-status-dot"></span>Active Loop</span>
            <span style="font-size:0.75rem;color:var(--text-muted);font-weight:600">Protocol v2.6</span>
          </div>
          <div class="f-title">7-Day Patient Return Guarantee</div>
          <div class="f-timeline">
            <span>Referral</span>
            <svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd"/></svg>
            <span>Surgery</span>
            <svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd"/></svg>
            <strong style="color:var(--ep-teal)">Optom Review</strong>
          </div>
        </div>

        <!-- Floating Glass Card: £250 Fee -->
        <div class="floating-glass-card float-card-bottom">
          <div class="float-amount">&pound;250</div>
          <div class="float-desc">
            <strong>Flat Cataract Co-Management</strong>
            <span>Direct BACS settlement on 4-week review</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Bento Grid: Why Independent Practices Partner With EyePros -->
<section id="benefits" class="section section-alt">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow-pill">PARTNERSHIP ARCHITECTURE</div>
      <h2>Built around the reality of independent practice</h2>
      <p class="section-lead">Corporate hospital chains keep your patients. NHS waiting lists test their patience. EyePros Synergy keeps the relationship right where it belongs: with you.</p>
    </div>

    <div class="bento-grid">
      <!-- Bento 1: Direct Surgeon Continuity (2 cols) -->
      <div class="bento-card bento-col-2">
        <div class="bento-header">
          <div class="bento-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="8.5" cy="7" r="4"/><line x1="20" y1="8" x2="20" y2="14"/><line x1="23" y1="11" x2="17" y2="11"/></svg>
          </div>
          <div>
            <h3>Direct Named-Surgeon Continuity &amp; Access</h3>
            <span style="font-size:0.82rem;color:var(--ep-teal-dark);font-weight:700">NO CALL CENTRES &bull; NO INTERMEDIARIES</span>
          </div>
        </div>
        <p>You and your patient have direct contact with the named operating consultant ophthalmologist from first assessment through day-case surgery and discharge. If a clinical question arises, you speak directly with the surgeon who performed the operation.</p>
        <div class="bento-quote">
          &ldquo;True clinical shared care requires direct peer-to-peer dialogue between surgeon and optometrist. You always have direct access to us.&rdquo;
        </div>
      </div>

      <!-- Bento 2: Syndesis Platform (1 col) -->
      <div class="bento-card bento-col-1">
        <div class="bento-header">
          <div class="bento-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
          </div>
          <div>
            <h3>Dedicated Platform: Syndesis</h3>
            <span style="font-size:0.82rem;color:var(--ep-teal-dark);font-weight:700">REAL-TIME REFERRALS</span>
          </div>
        </div>
        <p>Refer in under 2 minutes, upload scans securely, and track your patient&rsquo;s clinical journey in real time with automated status alerts.</p>
        <div class="syndesis-preview-card">
          <div class="syndesis-row">
            <span class="syndesis-patient">Patient: J. Thompson</span>
            <span class="syndesis-status">Day 7 Discharged</span>
          </div>
          <div class="syndesis-steps">
            <div class="syndesis-step-bar done"></div>
            <div class="syndesis-step-bar done"></div>
            <div class="syndesis-step-bar done"></div>
            <div class="syndesis-step-bar active"></div>
          </div>
          <div class="syndesis-meta">
            <span>Cataract Right Eye</span>
            <strong style="color:var(--ep-teal)">&pound;250 Fee Ready</strong>
          </div>
        </div>
      </div>

      <!-- Bento 3: Comprehensive Team Training (1 col) -->
      <div class="bento-card bento-col-1">
        <div class="bento-header">
          <div class="bento-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
          </div>
          <div>
            <h3>Complete Team Training</h3>
            <span style="font-size:0.82rem;color:var(--ep-teal-dark);font-weight:700">SYNDESIS &amp; TRIAGE</span>
          </div>
        </div>
        <p>EyePros provides dedicated training for your optometrists, dispensing opticians, and front-of-house staff on using the Syndesis portal, managing patient enquiries, and tracking outcomes.</p>
        <div class="bento-pill-cluster">
          <span class="bento-pill">Practice Onboarding</span>
          <span class="bento-pill">Front-of-House Triage</span>
          <span class="bento-pill">1-on-1 Portal Demos</span>
        </div>
      </div>

      <!-- Bento 4: Protected Patient Relationship & 7-Day Discharge (2 cols) -->
      <div class="bento-card bento-col-2">
        <div class="bento-header">
          <div class="bento-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
          </div>
          <div>
            <h3>Protected Patient Relationship &amp; 7-Day Discharge</h3>
            <span style="font-size:0.82rem;color:var(--ep-teal-dark);font-weight:700">PATIENT RETENTION GUARANTEE</span>
          </div>
        </div>
        <p>Your patients remain your patients. We perform the surgical episode and return them to your care with full clinical handover within 7 days. You manage the post-operative review and continue all future spectacle dispensing and eye examinations.</p>
        <div class="bento-pill-cluster">
          <span class="bento-pill">&bull; Electronic Discharge in 7 Days</span>
          <span class="bento-pill">&bull; Post-op Biometry Data Shared</span>
          <span class="bento-pill">&bull; Ongoing Optical Dispensing Retained</span>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Referral Pathway: Connected 5-Step Care Loop -->
<section id="journey" class="section">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow-pill">CLINICAL PATHWAY</div>
      <h2>Five steps. Clear clinical boundaries.</h2>
      <p class="section-lead">A seamless co-management pathway designed so optometrists and consultant surgeons do exactly what each does best.</p>
    </div>

    <div class="pathway-track">
      <!-- Step 1 -->
      <div class="pathway-card">
        <div class="pathway-step-num">1</div>
        <span class="pathway-actor optom">YOUR PRACTICE</span>
        <h4>Patient Referral</h4>
        <p>Submit patient clinical details and biometry via the Syndesis portal in under 2 minutes with instant confirmation.</p>
      </div>

      <!-- Step 2 -->
      <div class="pathway-card">
        <div class="pathway-step-num">2</div>
        <span class="pathway-actor eyepros">EYEPROS</span>
        <h4>Consultant Assessment</h4>
        <p>Comprehensive pre-op diagnostic workup and surgeon-led informed consent conducted personally by the operating consultant.</p>
      </div>

      <!-- Step 3 -->
      <div class="pathway-card">
        <div class="pathway-step-num">3</div>
        <span class="pathway-actor eyepros">EYEPROS</span>
        <h4>Day-Case Surgery</h4>
        <p>State-of-the-art procedure performed in our modern surgical suite by your patient&rsquo;s named NHS consultant ophthalmologist.</p>
      </div>

      <!-- Step 4 -->
      <div class="pathway-card">
        <div class="pathway-step-num">4</div>
        <span class="pathway-actor eyepros">EYEPROS &rarr; YOU</span>
        <h4>7-Day Discharge</h4>
        <p>Electronic discharge letter, surgical notes, and post-op medication plan securely sent to your practice within 7 days.</p>
      </div>

      <!-- Step 5 -->
      <div class="pathway-card">
        <div class="pathway-step-num">5</div>
        <span class="pathway-actor optom">YOUR PRACTICE</span>
        <h4>4-Week Co-Management</h4>
        <p>Conduct the post-operative review and new refraction. Submit completion report via Syndesis to receive your &pound;250 fee.</p>
      </div>
    </div>
  </div>
</section>

<!-- Consultant Leadership Section -->
<section id="consultants" class="section section-alt">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow-pill">CLINICAL LEADERSHIP &amp; GOVERNANCE</div>
      <h2>Led by substantive NHS Consultant Ophthalmologists</h2>
      <p class="section-lead">Direct named-surgeon continuity. You and your patient have direct contact with the operating consultant, underpinned by robust NHS clinical governance and national audit compliance.</p>
    </div>

    <div class="consultants-grid">
      <!-- Mr Ahmad Elsahn -->
      <div class="consultant-card">
        <div class="consultant-header">
          <img src="{a_src}" alt="Mr Ahmad Elsahn" class="consultant-photo" loading="lazy">
          <div class="consultant-title-group">
            <h3>Mr Ahmad Elsahn</h3>
            <p class="consultant-role">Managing Director &amp; Founder, EyePros</p>
            <div class="consultant-credentials">
              <span class="cred-badge">MBBCh</span>
              <span class="cred-badge">PhD</span>
              <span class="cred-badge">FRCS</span>
              <span class="cred-badge">FRCOphth</span>
              <span class="cred-badge">FHEA</span>
              <span class="cred-badge">FWCRS</span>
              <span class="cred-badge">CertLRS</span>
            </div>
          </div>
        </div>
        <p class="consultant-bio">Specialist in complex and premium cataract surgery, laser vision correction, MIGS glaucoma surgery, and anterior segment reconstruction with over two decades of international and NHS surgical leadership.</p>
        <ul class="consultant-posts">
          <li>
            <svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
            <span>Consultant Ophthalmic Surgeon and Head of Service for Ophthalmology, Sherwood Forest Hospitals NHS Foundation Trust</span>
          </li>
          <li>
            <svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
            <span>Honorary Assistant Professor of Ophthalmology, University of Nottingham</span>
          </li>
        </ul>
      </div>

      <!-- Ms Yasmine Abdalla -->
      <div class="consultant-card">
        <div class="consultant-header">
          <img src="{y_src}" alt="Ms Yasmine Abdalla" class="consultant-photo" loading="lazy">
          <div class="consultant-title-group">
            <h3>Ms Yasmine Abdalla</h3>
            <p class="consultant-role">Medical Director, EyePros</p>
            <div class="consultant-credentials">
              <span class="cred-badge">MBBCh</span>
              <span class="cred-badge">MSc</span>
              <span class="cred-badge">FRCOphth</span>
              <span class="cred-badge">Retina Fellow</span>
            </div>
          </div>
        </div>
        <p class="consultant-bio">Specialist in diabetic eye disease, age-related macular degeneration (AMD), inflammatory eye conditions (uveitis), intravitreal injections, retinal &amp; macular laser, and complex cataract surgery with over two decades of clinical experience.</p>
        <ul class="consultant-posts">
          <li>
            <svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
            <span>Consultant Ophthalmologist &amp; Uveitis Service Lead, University Hospitals of Derby and Burton NHS Foundation Trust</span>
          </li>
          <li>
            <svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
            <span>Royal College Tutor, Royal Derby Hospital (supervising ophthalmology registrars)</span>
          </li>
        </ul>
      </div>
    </div>

    <!-- 4 Clinical Commitments -->
    <div class="gov-grid">
      <div class="gov-card">
        <h4><svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>Surgeon-Led Consent</h4>
        <p>Consent is taken personally by, or under direct supervision of, the operating consultant ophthalmologist.</p>
      </div>
      <div class="gov-card">
        <h4><svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>Named Consultant Contact</h4>
        <p>Direct communication channel with operating surgeons for clinical queries, triage, and patient updates.</p>
      </div>
      <div class="gov-card">
        <h4><svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>Substantive NHS Standards</h4>
        <p>All consultants hold active substantive NHS appointments with specialist royal college fellowship credentials.</p>
      </div>
      <div class="gov-card">
        <h4><svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>NOD Audit Governance</h4>
        <p>Full clinical adherence to National Ophthalmology Database audit standards and RCOphth clinical guidelines.</p>
      </div>
    </div>
  </div>
</section>

<!-- Trusted By Section: Prominent Pinders Opticians & Sliding Carousel -->
<section id="trusted" class="section-trusted">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow-pill">ESTABLISHED PARTNERSHIPS</div>
      <h2>Trusted by Leading Independent Practices</h2>
      <p class="section-lead">Independent optometry practices across the East Midlands partner with EyePros to expand their clinical scope, preserve patient relationships, and deliver consultant-led surgical excellence.</p>
    </div>

    <!-- Featured Partner Spotlight: Pinders Opticians -->
    <div class="pinders-featured-card">
      <div class="pinders-featured-logo">
        <img src="{p_src}" alt="Pinders Opticians">
      </div>
      <div class="pinders-featured-meta">
        <span class="pinders-tag">&bull; Founding Partner Practice</span>
        <strong>Pinders Opticians &mdash; Mansfield, Southwell &amp; Rufford</strong>
        <p>&ldquo;Partnering with EyePros Synergy has enabled our practice to offer our patients fast, consultant-led surgical care with the total certainty that they are discharged back to us for ongoing management. The &pound;250 co-management fee properly values our clinical chair time.&rdquo;</p>
      </div>
    </div>

    <!-- Smooth Infinite Carousel for Additional Practices -->
    <div class="partner-carousel-wrap">
      <div class="partner-carousel-track">
        <!-- Card 1 -->
        <div class="partner-card">
          <div class="partner-logo-pill">
            <img src="{p_src}" alt="Pinders Opticians">
          </div>
          <div class="partner-meta">
            <strong>Pinders Opticians</strong>
            <span>Founding Partner &bull; Mansfield &amp; Southwell</span>
          </div>
        </div>
        <!-- Card 2 -->
        <div class="partner-card">
          <div class="partner-badge-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
          </div>
          <div class="partner-meta">
            <strong>Derbyshire Optical Practice</strong>
            <span>Shared Care Partner &bull; Derby &amp; Chesterfield</span>
          </div>
        </div>
        <!-- Card 3 -->
        <div class="partner-card">
          <div class="partner-badge-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>
          </div>
          <div class="partner-meta">
            <strong>Nottinghamshire Eye Care</strong>
            <span>Accredited Practice Partner &bull; Nottingham</span>
          </div>
        </div>
        <!-- Card 4 -->
        <div class="partner-card">
          <div class="partner-badge-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
          </div>
          <div class="partner-meta">
            <strong>Leicestershire Independent Eyecare</strong>
            <span>Synergy Partner &bull; Leicester &amp; Loughborough</span>
          </div>
        </div>
        <!-- Card 5: Apply Slot -->
        <div class="partner-card partner-card-add">
          <div class="partner-badge-icon" style="background:var(--ep-teal-tint)">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
          </div>
          <div class="partner-meta">
            <strong>Your Practice Here</strong>
            <span><a href="#partner-enquiry" style="color:var(--ep-teal);font-weight:700">Apply to become a partner &rarr;</a></span>
          </div>
        </div>

        <!-- Duplicated items for seamless marquee loop -->
        <div class="partner-card">
          <div class="partner-logo-pill">
            <img src="{p_src}" alt="Pinders Opticians">
          </div>
          <div class="partner-meta">
            <strong>Pinders Opticians</strong>
            <span>Founding Partner &bull; Mansfield &amp; Southwell</span>
          </div>
        </div>
        <div class="partner-card">
          <div class="partner-badge-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
          </div>
          <div class="partner-meta">
            <strong>Derbyshire Optical Practice</strong>
            <span>Shared Care Partner &bull; Derby &amp; Chesterfield</span>
          </div>
        </div>
        <div class="partner-card">
          <div class="partner-badge-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>
          </div>
          <div class="partner-meta">
            <strong>Nottinghamshire Eye Care</strong>
            <span>Accredited Practice Partner &bull; Nottingham</span>
          </div>
        </div>
        <div class="partner-card">
          <div class="partner-badge-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
          </div>
          <div class="partner-meta">
            <strong>Leicestershire Independent Eyecare</strong>
            <span>Synergy Partner &bull; Leicester &amp; Loughborough</span>
          </div>
        </div>
        <div class="partner-card partner-card-add">
          <div class="partner-badge-icon" style="background:var(--ep-teal-tint)">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
          </div>
          <div class="partner-meta">
            <strong>Your Practice Here</strong>
            <span><a href="#partner-enquiry" style="color:var(--ep-teal);font-weight:700">Apply to become a partner &rarr;</a></span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Remuneration & Practice Earnings Calculator -->
<section id="remuneration" class="section">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow-pill">TRANSPARENT REMUNERATION</div>
      <h2>Flat shared-care fee schedule</h2>
      <p class="section-lead">Fair, transparent remuneration recognising your clinical expertise and chair time. Fees are flat and never volume-dependent.</p>
    </div>

    <!-- Flagship Cataract Fee + Practice Revenue Calculator -->
    <div class="remuneration-layout">
      <!-- Flagship Card -->
      <div class="flagship-fee-card">
        <span class="flagship-badge">FLAGSHIP CO-MANAGEMENT</span>
        <div>
          <span class="fee-category">PRIMARY SURGICAL EPISODE</span>
          <div class="fee-flagship-val">&pound;250 <span>/ eye</span></div>
          <h3 style="margin-top:6px;font-size:1.3rem">Cataract &amp; Premium Lens Surgery</h3>
          <p style="color:var(--text-muted);font-size:0.92rem;margin-top:6px">Applies to all Self-Pay &amp; Patient Finance cataract episodes. Paid upon submission of the 4-week post-op assessment via Syndesis.</p>
        </div>
        <ul class="flagship-features">
          <li>
            <svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
            <span><strong>Prompt Settlement:</strong> Direct BACS transfer on review sign-off</span>
          </li>
          <li>
            <svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
            <span><strong>Zero Referral Quotas:</strong> Co-manage 1 or 20 patients &mdash; fee remains &pound;250</span>
          </li>
          <li>
            <svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
            <span><strong>Full Optical Retention:</strong> You dispense future spectacles and contact lenses</span>
          </li>
        </ul>
        <a href="#partner-enquiry" class="btn btn-primary" style="width:100%">Register for Cataract Shared Care</a>
      </div>

      <!-- Interactive Calculator Card -->
      <div class="calc-card">
        <div>
          <h3>Annual Practice Revenue Estimator</h3>
          <p>Estimate the co-management revenue retained directly by your practice based on your monthly cataract referrals.</p>
          <div class="slider-group">
            <div class="slider-header">
              <span class="slider-label">Monthly Cataract Referrals:</span>
              <span class="slider-value" id="calcPatientVal">4 patients / month</span>
            </div>
            <input type="range" min="1" max="20" value="4" class="calc-slider" id="calcSlider" aria-label="Monthly Cataract Referrals Slider">
          </div>
        </div>

        <div class="calc-output-box">
          <div class="calc-output-label">ESTIMATED ANNUAL CO-MANAGEMENT FEES</div>
          <div class="calc-output-val" id="calcAnnualFee">&pound;12,000</div>
          <div class="calc-output-note">Direct shared-care revenue to your practice + 100% patient retention for eyewear.</div>
        </div>

        <div style="font-size:0.8rem;color:var(--text-muted);text-align:center;margin-top:14px">
          Based on flat &pound;250/eye cataract co-management remuneration.
        </div>
      </div>
    </div>

    <!-- Remaining 6 Transparent Fee Cards -->
    <div class="fees-grid">
      <!-- 2. Insurance Patients -->
      <div class="fee-card">
        <span class="fee-category">INSURANCE PATIENTS</span>
        <div class="fee-amount-box">
          <span class="fee-upto">Up to</span>
          <div class="fee-val">&pound;100</div>
        </div>
        <h4>Private Medical Insurance</h4>
        <p>Covered under insurer fee schedules for insured episodes and post-operative assessment.</p>
      </div>

      <!-- 3. Glaucoma / MIGS -->
      <div class="fee-card">
        <span class="fee-category">GLAUCOMA / MIGS</span>
        <div class="fee-amount-box">
          <span class="fee-upto">Up to</span>
          <div class="fee-val">&pound;100</div>
        </div>
        <h4>Minimally Invasive Glaucoma Surgery</h4>
        <p>Post-operative pressure checks and bleb monitoring for MIGS and iStent procedures.</p>
      </div>

      <!-- 4. Laser Treatment -->
      <div class="fee-card">
        <span class="fee-category">LASER TREATMENT</span>
        <div class="fee-amount-box">
          <span class="fee-upto-spacer">&nbsp;</span>
          <div class="fee-val">&pound;95</div>
        </div>
        <h4>YAG Capsulotomy &amp; SLT Laser</h4>
        <p>Flat fee per eye for YAG posterior capsulotomy, peripheral iridotomy, and SLT episodes.</p>
      </div>

      <!-- 5. Valeda Treatment -->
      <div class="fee-card">
        <span class="fee-category">DRY AMD THERAPY</span>
        <div class="fee-amount-box">
          <span class="fee-upto-spacer">&nbsp;</span>
          <div class="fee-val">&pound;150<span class="fee-cycle">/course</span></div>
        </div>
        <h4>Valeda Photobiomodulation</h4>
        <p>Multi-session light therapy course for dry age-related macular degeneration (Dry AMD).</p>
      </div>

      <!-- 6. EyeSpa Treatment -->
      <div class="fee-card">
        <span class="fee-category">DRY EYE CLINIC</span>
        <div class="fee-amount-box">
          <span class="fee-upto-spacer">&nbsp;</span>
          <div class="fee-val">&pound;120<span class="fee-cycle">/course</span></div>
        </div>
        <h4>EyeSpa Advanced Ocular Surface</h4>
        <p>Dedicated clinical course for meibomian gland dysfunction, blepharitis, and severe dry eye.</p>
      </div>

      <!-- 7. Lacryfill -->
      <div class="fee-card">
        <span class="fee-category">PUNCTAL OCCLUSION</span>
        <div class="fee-amount-box">
          <span class="fee-upto-spacer">&nbsp;</span>
          <div class="fee-val">&pound;60</div>
        </div>
        <h4>Lacryfill Cross-Linked HA</h4>
        <p>Advanced cross-linked hyaluronic acid punctal occlusion for chronic ocular surface disease.</p>
      </div>
    </div>

    <!-- Shared Care Agreement Callout Banner -->
    <div class="agreement-banner">
      <div>
        <h3>Receive a copy of our Shared Care Agreement</h3>
        <p>Review the full legal framework, clinical governance protocols, indemnities, and transparent payment schedules. Governed by English law.</p>
      </div>
      <div class="agreement-actions">
        <a href="#partner-enquiry" class="btn btn-primary">Request Agreement Copy</a>
        <a href="tel:03337727277" class="btn btn-outline-white">0333 77 272 77</a>
      </div>
    </div>
  </div>
</section>

<!-- Partnership Enquiry & Registration Form -->
<section id="partner-enquiry" class="section section-alt">
  <div class="container">
    <div class="section-head text-left">
      <div class="eyebrow-pill">PRACTICE REGISTRATION</div>
      <h2>Become an EyePros Synergy Partner</h2>
      <p class="section-lead">Join independent optometry practices across the Midlands delivering consultant-led surgical excellence and protected patient continuity.</p>
    </div>

    <div class="enquiry-layout">
      <!-- Registration Form -->
      <div class="enquiry-card">
        <form id="partnerForm">
          <div class="form-grid">
            <div class="form-row">
              <div class="form-group">
                <label for="practiceName">Practice Name *</label>
                <input type="text" id="practiceName" name="practice_name" placeholder="e.g. Vision Care Opticians" required>
              </div>
              <div class="form-group">
                <label for="postcode">Practice Postcode *</label>
                <input type="text" id="postcode" name="practice_postcode" placeholder="e.g. NG1 1AA" required>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="leadName">Contact Name *</label>
                <input type="text" id="leadName" name="contact_name" placeholder="Lead Optometrist / Practice Manager" required>
              </div>
              <div class="form-group">
                <label for="gocNumber">GOC Number (Optional)</label>
                <input type="text" id="gocNumber" name="goc_number" placeholder="e.g. 01-12345">
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="email">Email Address *</label>
                <input type="email" id="email" name="contact_email" placeholder="practice@example.co.uk" required>
              </div>
              <div class="form-group">
                <label for="phone">Phone Number *</label>
                <input type="tel" id="phone" name="contact_phone" placeholder="0115 ... or 07..." required>
              </div>
            </div>

            <div class="form-group">
              <label for="interest">Primary Clinical Interests</label>
              <select id="interest" name="clinical_interests">
                <option value="cataract">Cataract &amp; Premium Lens Co-Management (&pound;250 fee)</option>
                <option value="glaucoma">Glaucoma / MIGS Shared Care</option>
                <option value="laser">YAG / SLT Laser Episodes</option>
                <option value="dryeye">Dry Eye / Valeda &amp; EyeSpa Courses</option>
                <option value="all">Comprehensive Full-Scope Partnership</option>
              </select>
            </div>

            <div class="form-group">
              <label for="notes">Additional Comments or Questions</label>
              <textarea id="notes" name="notes" rows="3" placeholder="Tell us about your practice, current patient volume, or Syndesis onboarding preferences..."></textarea>
            </div>

            <button type="submit" id="submitBtn" class="btn btn-primary" style="width:100%;padding:15px">
              <span>Submit Partnership Enquiry &amp; Receive Agreement</span>
              <svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd"/></svg>
            </button>
          </div>
        </form>

        <div id="formSuccess" style="display:none;text-align:center;padding:32px 16px">
          <div style="width:52px;height:52px;border-radius:50%;background:rgba(10,114,104,0.12);color:var(--ep-teal);display:inline-flex;align-items:center;justify-content:center;margin-bottom:14px">
            <svg viewBox="0 0 20 20" fill="currentColor" style="width:28px;height:28px"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
          </div>
          <h3 style="color:var(--ep-navy);margin-bottom:8px">Thank you for your enquiry</h3>
          <p style="color:var(--text-body);font-size:0.95rem">Our clinical directorship team will contact you within one working day with your onboarding pack and a copy of the Shared Care Agreement.</p>
        </div>
      </div>

      <!-- Contact Details Card -->
      <div class="contact-card">
        <h4>Direct Clinical Helpline</h4>
        <p>Speak directly with our partnership director or clinical lead regarding clinical protocols, patient suitability, and Syndesis onboarding.</p>
        
        <div class="contact-list">
          <div class="contact-item">
            <svg viewBox="0 0 20 20" fill="currentColor"><path d="M2 3a1 1 0 011-1h2.153a1 1 0 01.986.836l.74 4.435a1 1 0 01-.54 1.06l-1.548.773a11.037 11.037 0 006.105 6.105l.774-1.548a1 1 0 011.059-.54l4.435.74a1 1 0 01.836.986V17a1 1 0 01-1 1h-2C7.82 18 2 12.18 2 4V3z"/></svg>
            <div>
              <strong>Practice Enquiries</strong>
              <a href="tel:03337727277" style="color:var(--ep-teal);font-weight:700">0333 77 272 77</a>
              <div style="font-size:0.75rem;color:var(--text-muted)">Mon &ndash; Fri &bull; 8:30am &ndash; 6:00pm</div>
            </div>
          </div>

          <div class="contact-item">
            <svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd"/></svg>
            <div>
              <strong>Urgent Optometrist Line</strong>
              <span style="color:#C2410C;font-weight:700">Option 5 (Priority Clinical Triage)</span>
            </div>
          </div>

          <div class="contact-item">
            <svg viewBox="0 0 20 20" fill="currentColor"><path d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z"/><path d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z"/></svg>
            <div>
              <strong>Direct Partner Desk</strong>
              <a href="mailto:practice@eyepros.co.uk" style="color:var(--ep-teal);font-weight:600">practice@eyepros.co.uk</a>
            </div>
          </div>

          <div class="contact-item">
            <svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd"/></svg>
            <div>
              <strong>Surgical Locations</strong>
              <span>East Midlands Surgical Centres (Nottinghamshire, Derbyshire, Leicestershire)</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Frequently Asked Questions -->
<section id="faq" class="section">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow-pill">FREQUENTLY ASKED QUESTIONS</div>
      <h2>Partnership clarity for your practice</h2>
      <p class="section-lead">Straightforward answers on clinical governance, payment terms, and co-management protocols.</p>
    </div>

    <div class="faq-list">
      <div class="faq-item">
        <button class="faq-q">
          <span>How and when is the &pound;250 cataract co-management fee settled?</span>
          <svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd"/></svg>
        </button>
        <div class="faq-a">
          The &pound;250 flat fee is paid directly to your practice via BACS upon completion and submission of the 4-week post-operative review through the Syndesis portal. Payments are processed promptly and do not depend on referral volume.
        </div>
      </div>

      <div class="faq-item">
        <button class="faq-q">
          <span>How does EyePros guarantee my practice retains the patient?</span>
          <svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd"/></svg>
        </button>
        <div class="faq-a">
          Our Shared Care Agreement explicitly guarantees that EyePros acts strictly as the surgical provider. We never dispense optical appliances or compete for general eye examinations. Patients are formally discharged back to your practice within 7 days of surgery with full biometry notes for their post-op refraction and future spectacle dispensing.
        </div>
      </div>

      <div class="faq-item">
        <button class="faq-q">
          <span>What is the Syndesis platform and how is my team trained?</span>
          <svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd"/></svg>
        </button>
        <div class="faq-a">
          Syndesis is EyePros&rsquo; secure digital referral and patient tracking portal. It allows you to submit referrals in under two minutes, attach diagnostic scans, and see real-time updates as your patient completes consultation, surgery, and discharge. EyePros provides full, complimentary 1-on-1 and team training for your optometrists, dispensing staff, and practice managers.
        </div>
      </div>

      <div class="faq-item">
        <button class="faq-q">
          <span>Who conducts the surgery and patient consent?</span>
          <svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd"/></svg>
        </button>
        <div class="faq-a">
          All surgical procedures and informed consent are carried out directly by substantive NHS Consultant Ophthalmologists (Mr Ahmad Elsahn, Ms Yasmine Abdalla, and team). We never delegate surgical consent to non-consultant staff or technicians.
        </div>
      </div>

      <div class="faq-item">
        <button class="faq-q">
          <span>Are there any minimum referral quotas or exclusivity clauses?</span>
          <svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd"/></svg>
        </button>
        <div class="faq-a">
          None whatsoever. You retain complete clinical autonomy. You refer whenever it is in your patient&rsquo;s best clinical interest, whether that is one patient a month or twenty. Fees and support remain identical.
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Footer -->
<footer class="footer">
  <div class="container">
    <div class="footer-row">
      <a href="#hero" class="nav-brand">
        <div class="nav-logo-pill">
          <img src="{l_src}" alt="Synergy by EyePros" style="height:28px;width:auto">
        </div>
      </a>
      <div style="display:flex;gap:20px;align-items:center;flex-wrap:wrap">
        <a href="#partner-enquiry" style="color:var(--ep-teal-dark);font-weight:700">Receive a copy of our Shared Care Agreement</a>
        <a href="tel:03337727277" style="color:var(--ep-navy);font-weight:600">0333 77 272 77</a>
        <span style="color:#C2410C;font-weight:700">Urgent Helpline: Option 5</span>
      </div>
    </div>
    <div class="footer-copy">
      <div>&copy; 2026 EyePros. Shared Care Partnership Programme. Governed by English law.</div>
      <div>Managing Director: Mr Ahmad Elsahn &middot; Medical Director: Ms Yasmine Abdalla</div>
    </div>
  </div>
</footer>

<script>
// Mobile navigation toggle
var navToggle = document.getElementById('navToggle');
var navLinks = document.querySelector('.nav-links');
if (navToggle && navLinks) {{
  navToggle.addEventListener('click', function(e) {{
    e.stopPropagation();
    navLinks.classList.toggle('active');
  }});
  document.addEventListener('click', function(e) {{
    if (!navToggle.contains(e.target) && !navLinks.contains(e.target)) {{
      navLinks.classList.remove('active');
    }}
  }});
}}

// In-page smooth scrolling with navbar offset, scrollIntoView and Wix cross-frame message
function scrollToSection(targetId) {{
  var inIframe = false;
  try {{ inIframe = (window.self !== window.top); }} catch(e) {{ inIframe = true; }}

  if (!targetId || targetId === '#' || targetId === '#hero') {{
    try {{ window.scrollTo({{ top: 0, behavior: 'smooth' }}); }} catch(e) {{}}
    try {{ if (document.body) document.body.scrollIntoView({{ behavior: 'smooth', block: 'start' }}); }} catch(e) {{}}
    if (inIframe) {{
      try {{
        window.parent.postMessage({{ type: 'synergyScroll', action: 'scroll', target: '#hero', offsetTop: 0 }}, '*');
        window.parent.postMessage({{ type: 'scrollToSection', target: 'hero', offsetTop: 0 }}, '*');
      }} catch(err) {{}}
    }}
    if (history.pushState) history.pushState(null, null, ' ');
    return;
  }}

  var cleanId = targetId.replace(/^#/, '');
  var target = document.getElementById(cleanId) || document.querySelector(targetId);
  if (!target) {{
    try {{ window.location.hash = targetId; }} catch(e) {{}}
    return;
  }}

  var nav = document.querySelector('.nav');
  var navHeight = nav ? nav.offsetHeight : 74;
  var targetRect = target.getBoundingClientRect();
  var currentY = window.pageYOffset || document.documentElement.scrollTop || 0;
  var targetY = Math.max(0, Math.round(targetRect.top + currentY - navHeight - 12));

  // 1. Scroll the current window/frame
  try {{
    window.scrollTo({{ top: targetY, behavior: 'smooth' }});
  }} catch(e) {{
    try {{ window.scrollTo(0, targetY); }} catch(e2) {{}}
  }}

  // 2. If inside iframe, bubble scroll to outer parent window and broadcast postMessage
  if (inIframe) {{
    try {{
      target.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
    }} catch(e) {{
      try {{ target.scrollIntoView(true); }} catch(e2) {{}}
    }}

    try {{
      window.parent.postMessage({{
        type: 'synergyScroll',
        action: 'scroll',
        target: targetId,
        hash: targetId,
        cleanId: cleanId,
        offsetTop: targetY
      }}, '*');
      window.parent.postMessage({{
        type: 'scrollToSection',
        target: cleanId,
        offsetTop: targetY
      }}, '*');
    }} catch(err) {{}}
  }}

  // 3. Update URL hash without forcing abrupt browser jump
  try {{
    if (history.pushState) {{
      history.pushState(null, null, targetId);
    }} else {{
      window.location.hash = targetId;
    }}
  }} catch(e) {{}}
}}

document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {{
  anchor.addEventListener('click', function(e) {{
    var href = this.getAttribute('href');
    if (!href) return;
    e.preventDefault();
    if (navLinks) navLinks.classList.remove('active');
    scrollToSection(href);
  }});
}});

if (document.readyState === 'loading') {{
  document.addEventListener('DOMContentLoaded', function() {{
    if (window.location.hash) {{
      setTimeout(function() {{ scrollToSection(window.location.hash); }}, 250);
    }}
  }});
}} else {{
  if (window.location.hash) {{
    setTimeout(function() {{ scrollToSection(window.location.hash); }}, 250);
  }}
}}

// Interactive Practice Revenue Calculator
var calcSlider = document.getElementById('calcSlider');
var calcPatientVal = document.getElementById('calcPatientVal');
var calcAnnualFee = document.getElementById('calcAnnualFee');

if (calcSlider && calcPatientVal && calcAnnualFee) {{
  calcSlider.addEventListener('input', function() {{
    var pts = parseInt(this.value, 10);
    calcPatientVal.innerText = pts + (pts === 1 ? ' patient / month' : ' patients / month');
    var annual = pts * 12 * 250;
    calcAnnualFee.innerText = '£' + annual.toLocaleString('en-GB');
  }});
}}

// FAQ Accordion
document.querySelectorAll('.faq-q').forEach(function(button) {{
  button.addEventListener('click', function() {{
    this.parentElement.classList.toggle('open');
  }});
}});

// Enquiry form submission
var partnerForm = document.getElementById('partnerForm');
if (partnerForm) {{
  partnerForm.addEventListener('submit', function(e) {{
    e.preventDefault();
    var submitBtn = document.getElementById('submitBtn');
    submitBtn.innerText = 'Submitting...';
    submitBtn.disabled = true;

    var formData = new FormData(partnerForm);
    var payload = {{}};
    formData.forEach(function(value, key) {{ payload[key] = value; }});

    fetch('https://formsubmit.co/ajax/practice@eyepros.co.uk', {{
      method: 'POST',
      headers: {{'Content-Type': 'application/json', 'Accept': 'application/json'}},
      body: JSON.stringify(payload)
    }})
    .then(function() {{
      partnerForm.style.display = 'none';
      document.getElementById('formSuccess').style.display = 'block';
    }})
    .catch(function() {{
      partnerForm.submit();
    }});
  }});
}}
</script>

</body>
</html>
"""

# Write files
with open("synergy-wix-embed.html", "w", encoding="utf-8") as f:
    f.write(make_html(is_embed=True))

with open("synergy-landing-page.html", "w", encoding="utf-8") as f:
    f.write(make_html(is_embed=False))

print("Both synergy-wix-embed.html and synergy-landing-page.html regenerated successfully!")
