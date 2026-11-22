import re
import base64

# Read current embed for base64 assets
with open("synergy-wix-embed.html", "r", encoding="utf-8") as f:
    orig = f.read()

# Load new synergy logo as PNG base64
with open('images/synergy-logo-new.png', 'rb') as f_logo:
    logo_b64 = 'data:image/png;base64,' + base64.b64encode(f_logo.read()).decode('utf-8')

# Load square consultant headshots for perfect framing & eye-level alignment
with open('images/elsahn-headshot-square.jpg', 'rb') as f_ahmad:
    ahmad_b64 = 'data:image/jpeg;base64,' + base64.b64encode(f_ahmad.read()).decode('utf-8')
with open('images/abdalla-headshot-square.jpg', 'rb') as f_yasmine:
    yasmine_b64 = 'data:image/jpeg;base64,' + base64.b64encode(f_yasmine.read()).decode('utf-8')

with open('images/partner-pinders.png', 'rb') as f_pinders:
    pinders_b64 = 'data:image/png;base64,' + base64.b64encode(f_pinders.read()).decode('utf-8')
with open('images/partner-optique-collingham.png', 'rb') as f_optique_col:
    optique_col_b64 = 'data:image/png;base64,' + base64.b64encode(f_optique_col.read()).decode('utf-8')
with open('images/partner-optique-southwell.png', 'rb') as f_optique_sow:
    optique_sow_b64 = 'data:image/png;base64,' + base64.b64encode(f_optique_sow.read()).decode('utf-8')
with open('images/partner-diblow.png', 'rb') as f_diblow:
    diblow_b64 = 'data:image/png;base64,' + base64.b64encode(f_diblow.read()).decode('utf-8')
with open('images/partner-oakwood.png', 'rb') as f_oakwood:
    oakwood_b64 = 'data:image/png;base64,' + base64.b64encode(f_oakwood.read()).decode('utf-8')
with open('images/partner-alvaston.png', 'rb') as f_alvaston:
    alvaston_b64 = 'data:image/png;base64,' + base64.b64encode(f_alvaston.read()).decode('utf-8')
with open('images/partner-kimberley.png', 'rb') as f_kimberley:
    kimberley_b64 = 'data:image/png;base64,' + base64.b64encode(f_kimberley.read()).decode('utf-8')
with open('images/partner-sumpton.png', 'rb') as f_sumpton:
    sumpton_b64 = 'data:image/png;base64,' + base64.b64encode(f_sumpton.read()).decode('utf-8')
with open('images/synergy-hero-secret.jpg', 'rb') as f_img:
    hero_b64 = 'data:image/jpeg;base64,' + base64.b64encode(f_img.read()).decode('utf-8')

def build_page(is_embed=True):
    l_src = logo_b64 if is_embed else "images/synergy-logo-new.png"
    a_src = ahmad_b64 if is_embed else "images/elsahn-headshot-square.jpg"
    y_src = yasmine_b64 if is_embed else "images/abdalla-headshot-square.jpg"
    p_src = pinders_b64 if is_embed else "images/partner-pinders.png"
    o_col_src = optique_col_b64 if is_embed else "images/partner-optique-collingham.png"
    o_sow_src = optique_sow_b64 if is_embed else "images/partner-optique-southwell.png"
    di_src = diblow_b64 if is_embed else "images/partner-diblow.png"
    oak_src = oakwood_b64 if is_embed else "images/partner-oakwood.png"
    alv_src = alvaston_b64 if is_embed else "images/partner-alvaston.png"
    kim_src = kimberley_b64 if is_embed else "images/partner-kimberley.png"
    sump_src = sumpton_b64 if is_embed else "images/partner-sumpton.png"
    hero_img = hero_b64 if is_embed else "images/synergy-hero-secret.jpg"

    template = """
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EyePros Synergy — Consultant-Led Shared Care for UK Independent Opticians</title>
<meta name="description" content="EyePros Synergy connects UK independent optometry practices with substantive NHS consultant ophthalmologists. Flat £250 cataract co-management fee, guaranteed 7-day discharge, and dedicated Syndesis platform.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root {
  /* ═══ EyePros Blue Canvas & Medical Palette ═══ */
  --bg-page: #0C1E34;
  --bg-page-deep: #081524;
  --bg-section-alt: rgba(14, 34, 58, 0.55);

  /* Signature EyePros Tale Green (Teal) */
  --ep-teal: #0D9488;
  --ep-teal-vibrant: #14B8A6;
  --ep-teal-bright: #2DD4BF;
  --ep-teal-dark: #0F766E;
  --ep-teal-glow: rgba(20, 184, 166, 0.35);
  --ep-teal-tint: rgba(20, 184, 166, 0.12);

  /* EyePros Blues & Cyan */
  --ep-navy: #0C1E34;
  --ep-navy-card: rgba(16, 37, 64, 0.75);
  --ep-blue-cerulean: #0284C7;
  --ep-blue-light: #38BDF8;
  --ep-blue-glow: rgba(2, 132, 199, 0.35);
  --ep-sage: #8FBBB5;
  --ep-sage-light: rgba(143, 187, 181, 0.18);
  --ep-gold: #F59E0B;

  /* Typography Colors on Blue Canvas */
  --text-white: #FFFFFF;
  --text-heading: #FFFFFF;
  --text-body: #E2E8F0;
  --text-muted: #94A3B8;
  --text-dim: #64748B;
  --font-display: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
  --font-sans: 'Inter', system-ui, -apple-system, sans-serif;

  /* Authentic Frosted Glassmorphism */
  --glass-bg: rgba(255, 255, 255, 0.07);
  --glass-bg-hover: rgba(255, 255, 255, 0.12);
  --glass-border: rgba(255, 255, 255, 0.16);
  --glass-border-hover: rgba(45, 212, 191, 0.45);
  --glass-specular: inset 0 1px 1px 0 rgba(255, 255, 255, 0.22);
  --glass-shadow: 0 14px 40px rgba(0, 0, 0, 0.28);
  --glass-blur: blur(24px);

  /* Geometry & Motion */
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 14px;
  --radius-xl: 18px;
  --radius-pill: 9999px;
  --max-w: 1140px;
  --ease-smooth: cubic-bezier(0.16, 1, 0.3, 1);
}

*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{
  scroll-behavior:smooth;
  -webkit-text-size-adjust:100%;
  scroll-padding-top:84px;
  overflow-x:hidden;
}
body{
  font-family:var(--font-sans);
  font-size:16px;
  line-height:1.65;
  color:var(--text-body);
  background-color:var(--bg-page);
  background-image:linear-gradient(180deg, #091728 0%, #0C1E34 25%, #0F2744 50%, #0C1E34 75%, #081524 100%);
  -webkit-font-smoothing:antialiased;
  position:relative;
  width:100%;
  max-width:100%;
  padding-top:74px;
  overflow-x:hidden;
}
section,[id]{scroll-margin-top:84px}
img{max-width:100%;display:block}
a{color:inherit;text-decoration:none}
button{font-family:inherit;cursor:pointer}

/* Headings */
h1,h2,h3,h4,h5{
  font-family:var(--font-display);
  color:var(--text-white);
  line-height:1.2;
  font-weight:700;
  letter-spacing:-0.02em;
}
h1{font-size:clamp(1.75rem,2.8vw,2.35rem);font-weight:800;letter-spacing:-0.03em;line-height:1.15}
h2{font-size:clamp(1.35rem,2.0vw,1.75rem);font-weight:700;letter-spacing:-0.025em}
h3{font-size:1.08rem;font-weight:700}
h4{font-size:0.92rem;font-weight:700}

.text-gradient{
  background:linear-gradient(135deg, #2DD4BF 0%, #38BDF8 100%);
  -webkit-background-clip:text;
  -webkit-text-fill-color:transparent;
}

/* ═══ Ambient Aurora Mesh Background with Light Effects ═══ */
.aurora-bg {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  z-index: 0;
  pointer-events: none;
  overflow: hidden;
  contain: paint;
  max-width: 100%;
}
.aurora-blob {
  position: absolute;
  border-radius: 50%;
  filter: blur(120px);
  -webkit-filter: blur(120px);
  opacity: 0.60;
  will-change: transform;
}
.aurora-blob-1 {
  width: 720px;
  height: 720px;
  background: radial-gradient(circle, rgba(2, 132, 199, 0.32) 0%, rgba(2, 132, 199, 0.08) 60%, transparent 80%);
  top: -160px;
  left: -100px;
  animation: auroraFloat1 32s var(--ease-smooth) infinite alternate;
}
.aurora-blob-2 {
  width: 760px;
  height: 760px;
  background: radial-gradient(circle, rgba(13, 148, 136, 0.30) 0%, rgba(13, 148, 136, 0.06) 55%, transparent 75%);
  top: 30%;
  right: -140px;
  animation: auroraFloat2 38s var(--ease-smooth) infinite alternate;
}
.aurora-blob-3 {
  width: 640px;
  height: 640px;
  background: radial-gradient(circle, rgba(56, 189, 248, 0.22) 0%, transparent 70%);
  bottom: 8%;
  left: 10%;
  animation: auroraFloat3 34s var(--ease-smooth) infinite alternate;
}
.aurora-blob-4 {
  width: 580px;
  height: 580px;
  background: radial-gradient(circle, rgba(143, 187, 181, 0.20) 0%, transparent 70%);
  top: 65%;
  right: 15%;
  animation: auroraFloat4 28s var(--ease-smooth) infinite alternate;
}
.aurora-mesh-overlay {
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse at 50% 20%, rgba(12, 30, 52, 0.25) 0%, rgba(8, 21, 36, 0.45) 100%);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
}

@keyframes auroraFloat1 {
  0% { transform: translate3d(0, 0, 0) scale(1); }
  50% { transform: translate3d(70px, 50px, 0) scale(1.06); }
  100% { transform: translate3d(-40px, 90px, 0) scale(0.96); }
}
@keyframes auroraFloat2 {
  0% { transform: translate3d(0, 0, 0) scale(1); }
  50% { transform: translate3d(-80px, -60px, 0) scale(1.05); }
  100% { transform: translate3d(35px, -100px, 0) scale(0.95); }
}
@keyframes auroraFloat3 {
  0% { transform: translate3d(0, 0, 0) scale(1); }
  50% { transform: translate3d(50px, -40px, 0) scale(1.04); }
  100% { transform: translate3d(-35px, 35px, 0) scale(0.95); }
}
@keyframes auroraFloat4 {
  0% { transform: translate3d(0, 0, 0) scale(1); }
  50% { transform: translate3d(-60px, 45px, 0) scale(1.06); }
  100% { transform: translate3d(45px, -50px, 0) scale(0.96); }
}

@media (prefers-reduced-motion: reduce) {
  .aurora-blob { animation: none !important; }
}

/* ═══ Layout Primitives ═══ */
.container {
  max-width: var(--max-w);
  margin: 0 auto;
  padding: 0 28px;
  position: relative;
  z-index: 2;
}
.section {
  padding: 56px 0;
  position: relative;
  z-index: 2;
}
.section-alt {
  background: var(--bg-section-alt);
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

/* Section Header Typography */
.section-head {
  text-align: center;
  max-width: 620px;
  margin: 0 auto 32px;
}
.section-head.text-left {
  text-align: left;
  margin: 0 0 28px;
}
.eyebrow-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 11px;
  border-radius: var(--radius-pill);
  background: var(--ep-teal-tint);
  border: 1px solid rgba(45, 212, 191, 0.30);
  color: var(--ep-teal-bright);
  font-family: var(--font-display);
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  margin-bottom: 10px;
}
.eyebrow-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--ep-teal-bright);
  box-shadow: 0 0 8px var(--ep-teal-bright);
  animation: pulseDot 2.2s infinite;
}
@keyframes pulseDot {
  0%, 100% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.4; transform: scale(0.85); }
}
.section-lead {
  margin-top: 8px;
  font-size: 0.90rem;
  color: var(--text-body);
  line-height: 1.55;
}

/* ═══ Buttons & Interactive Controls ═══ */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  font-family: var(--font-display);
  font-size: 0.88rem;
  font-weight: 700;
  padding: 10px 20px;
  border-radius: var(--radius-pill);
  transition: all 0.25s var(--ease-smooth);
  cursor: pointer;
  white-space: nowrap;
  line-height: 1;
  text-decoration: none;
}
.btn-primary {
  background: linear-gradient(135deg, #0D9488 0%, #0F766E 100%);
  color: #FFFFFF !important;
  border: 1px solid rgba(255, 255, 255, 0.25);
  box-shadow: 0 3px 14px var(--ep-teal-glow), inset 0 1px 0 rgba(255, 255, 255, 0.25);
}
.btn-primary:hover {
  background: linear-gradient(135deg, #14B8A6 0%, #0D9488 100%);
  color: #FFFFFF !important;
  transform: translateY(-2px);
  box-shadow: 0 6px 20px var(--ep-teal-glow);
}
.btn-secondary {
  background: rgba(255, 255, 255, 0.10);
  color: #FFFFFF !important;
  border: 1px solid rgba(255, 255, 255, 0.22);
  box-shadow: 0 3px 12px rgba(0, 0, 0, 0.20);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
}
.btn-secondary:hover {
  background: rgba(255, 255, 255, 0.18);
  border-color: var(--ep-teal-bright);
  color: #FFFFFF !important;
  transform: translateY(-2px);
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.30);
}
.btn-sm {
  padding: 7px 14px;
  font-size: 0.80rem;
}
.btn-outline-white {
  background: rgba(255, 255, 255, 0.08);
  color: #FFFFFF !important;
  border: 1.5px solid rgba(255, 255, 255, 0.40);
  backdrop-filter: blur(8px);
}
.btn-outline-white:hover {
  background: rgba(255, 255, 255, 0.18);
  border-color: #FFFFFF;
  transform: translateY(-2px);
}
.btn svg {
  width: 16px;
  height: 16px;
  transition: transform 0.2s ease;
}
.btn:hover svg {
  transform: translateX(3px);
}

/* ═══ Fixed Glass Navigation with Smooth Transitions ═══ */
.nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  width: 100%;
  z-index: 1000;
  background: rgba(12, 30, 52, 0.88);
  border-bottom: 1px solid rgba(255, 255, 255, 0.10);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  box-shadow: 0 4px 18px rgba(0, 0, 0, 0.32);
  transition: background 0.3s var(--ease-smooth), border-color 0.3s ease, box-shadow 0.3s ease;
}
.nav.scrolled {
  background: rgba(9, 23, 40, 0.96);
  border-bottom-color: rgba(45, 212, 191, 0.30);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.55);
}
.nav-inner {
  max-width: var(--max-w);
  margin: 0 auto;
  padding: 0 28px;
  height: 74px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.nav-brand {
  display: flex;
  align-items: center;
  gap: 12px;
}
.nav-logo-pill {
  background: rgba(8, 20, 36, 0.65);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  padding: 6px 14px;
  border-radius: 10px;
  display: inline-flex;
  align-items: center;
  border: 1px solid rgba(255, 255, 255, 0.14);
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.35);
  transition: transform 0.25s var(--ease-smooth), border-color 0.25s ease, background 0.25s ease;
}
.nav-logo-pill:hover {
  transform: translateY(-1px);
  border-color: rgba(45, 212, 191, 0.5);
  background: rgba(12, 30, 52, 0.85);
}
.nav-logo-pill img {
  height: 32px;
  width: auto;
  display: block;
}
.nav-links {
  display: flex;
  align-items: center;
  gap: 6px;
  list-style: none;
}
.nav-links a:not(.btn) {
  color: var(--text-body);
  font-size: 0.90rem;
  font-weight: 600;
  padding: 8px 12px;
  border-radius: var(--radius-sm);
  transition: all 0.25s var(--ease-smooth);
  white-space: nowrap;
  position: relative;
}
.nav-links a:not(.btn):hover,
.nav-links a:not(.btn).active {
  color: var(--ep-teal-bright);
  background: rgba(45, 212, 191, 0.12);
}
.nav-links a:not(.btn)::after {
  content: '';
  position: absolute;
  bottom: 2px;
  left: 12px;
  right: 12px;
  height: 2px;
  background: var(--ep-teal-bright);
  border-radius: 2px;
  transform: scaleX(0);
  transition: transform 0.25s var(--ease-smooth);
}
.nav-links a:not(.btn):hover::after,
.nav-links a:not(.btn).active::after {
  transform: scaleX(1);
}
.nav-toggle {
  display: none;
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.20);
  color: var(--text-white);
  border-radius: 8px;
  cursor: pointer;
  padding: 8px;
  align-items: center;
  justify-content: center;
  line-height: 1;
  transition: all 0.2s ease;
}
.nav-toggle:hover {
  background: rgba(255, 255, 255, 0.15);
  border-color: var(--ep-teal-bright);
}

/* ═══ Hero Section: Bespoke MedTech Showcase ═══ */
.hero {
  padding: 44px 0 48px;
  position: relative;
  z-index: 2;
}
.hero-grid {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 36px;
  align-items: center;
}
.hero-content {
  max-width: 580px;
}
.hero h1 {
  margin-bottom: 8px;
}
.hero-tagline {
  font-family: var(--font-display);
  font-style: italic;
  font-weight: 700;
  font-size: clamp(1.25rem, 1.8vw, 1.55rem);
  margin: 4px 0 16px;
  letter-spacing: -0.01em;
  line-height: 1.3;
  display: block;
}
.hero-sub {
  font-size: 0.96rem;
  color: var(--text-body);
  margin-bottom: 20px;
  line-height: 1.55;
}
.hero-ctas {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 24px;
  flex-wrap: wrap;
}
.hero-proof-strip {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 14px;
  padding-top: 18px;
  border-top: 1px solid rgba(255, 255, 255, 0.12);
}
.proof-item {
  display: flex;
  flex-direction: column;
  gap: 3px;
}
.proof-num {
  font-family: var(--font-display);
  font-size: 1.12rem;
  font-weight: 800;
  color: var(--text-white);
  display: flex;
  align-items: center;
  gap: 5px;
}
.proof-num::before {
  content: '';
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: var(--ep-teal-bright);
}
.proof-label {
  font-size: 0.72rem;
  color: var(--text-muted);
  line-height: 1.35;
}

/* Hero Visual Showcase */
.hero-visual {
  position: relative;
}
.hero-visual-frame {
  position: relative;
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: 0 16px 44px rgba(0, 0, 0, 0.45), 0 0 30px rgba(13, 148, 136, 0.20);
  border: 1.5px solid rgba(45, 212, 191, 0.35);
  background: rgba(8, 20, 36, 0.85);
  transition: transform 0.3s var(--ease-smooth), box-shadow 0.3s ease;
}
.hero-visual-frame:hover {
  transform: translateY(-2px);
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.50), 0 0 40px rgba(45, 212, 191, 0.25);
}
.hero-visual-frame img {
  width: 100%;
  height: auto;
  aspect-ratio: 16 / 9;
  object-fit: cover;
  display: block;
}

/* ═══ Simple & Elegant 4-Card Bento Grid with Glass Effect ═══ */
.simple-bento-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 14px;
}
.simple-bento-card {
  background: var(--glass-bg);
  border: 1px solid var(--glass-border);
  backdrop-filter: var(--glass-blur);
  -webkit-backdrop-filter: var(--glass-blur);
  border-radius: var(--radius-md);
  padding: 16px 18px;
  box-shadow: var(--glass-shadow), var(--glass-specular);
  transition: transform 0.3s var(--ease-smooth), border-color 0.3s ease, background 0.3s ease, box-shadow 0.3s ease;
  display: flex;
  flex-direction: column;
  gap: 0;
  justify-content: space-between;
}
.simple-bento-card:hover {
  background: var(--glass-bg-hover);
  border-color: var(--glass-border-hover);
  transform: translateY(-3px);
  box-shadow: 0 14px 36px rgba(0, 0, 0, 0.35), 0 0 20px var(--ep-teal-glow), var(--glass-specular);
}
/* Icon + tag on same row */
.card-header-row {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 2px;
}
.card-icon-bubble {
  width: 34px;
  height: 34px;
  border-radius: 9px;
  background: var(--ep-teal-tint);
  border: 1px solid rgba(45, 212, 191, 0.30);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: var(--ep-teal-bright);
  flex-shrink: 0;
}
.card-icon-bubble svg {
  width: 16px;
  height: 16px;
}
.card-tag {
  display: inline-block;
  font-size: 0.62rem;
  font-weight: 700;
  letter-spacing: 0.10em;
  text-transform: uppercase;
  color: var(--ep-teal-bright);
}
.simple-bento-card h3 {
  font-size: 0.97rem;
  margin: 0 0 4px;
  color: var(--text-white);
  line-height: 1.3;
}
.simple-bento-card p {
  font-size: 0.82rem;
  color: var(--text-body);
  line-height: 1.45;
  margin: 0;
}
/* card-top grows to fill card, pushing pills to bottom */
.card-top {
  display: flex;
  flex-direction: column;
  gap: 6px;
  flex-grow: 1;
}
.card-pill-row {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
  margin-top: 10px;
}
.card-pill {
  font-size: 0.70rem;
  font-weight: 600;
  padding: 3px 8px;
  border-radius: var(--radius-pill);
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.14);
  color: var(--text-body);
}
.card-btn-action {
  margin-top: 16px;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(45, 212, 191, 0.12);
  color: var(--ep-teal-bright) !important;
  border: 1px solid rgba(45, 212, 191, 0.35);
  padding: 8px 14px;
  border-radius: var(--radius-sm);
  font-family: inherit;
  font-size: 0.80rem;
  font-weight: 600;
  text-decoration: none;
  width: fit-content;
  cursor: pointer;
  transition: all 0.25s var(--ease-smooth);
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.20);
}
.card-btn-action:hover {
  background: var(--ep-teal-bright);
  color: #081424 !important;
  border-color: var(--ep-teal-bright);
  transform: translateY(-2px);
  box-shadow: 0 4px 16px var(--ep-teal-glow);
}
.card-btn-action svg {
  width: 14px;
  height: 14px;
  flex-shrink: 0;
  fill: currentColor;
  transition: transform 0.2s ease;
}
.card-btn-action:hover svg {
  transform: scale(1.15);
}

/* ═══ Video Walkthrough Native Dialog Modal ═══ */
dialog.video-modal-dialog {
  border: 1px solid rgba(45, 212, 191, 0.40);
  border-radius: 16px;
  background: #081524;
  box-shadow: 0 24px 70px rgba(0, 0, 0, 0.85), 0 0 40px rgba(20, 184, 166, 0.25);
  padding: 0;
  max-width: 880px;
  width: calc(100vw - 32px);
  margin: auto;
  color: #FFFFFF;
  overflow: hidden;
  box-sizing: border-box;
}
dialog.video-modal-dialog::backdrop {
  background: rgba(8, 20, 36, 0.82);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  overflow: hidden;
  overscroll-behavior: contain;
}
dialog:modal {
  overscroll-behavior: contain;
}
.video-modal-content {
  width: 100%;
  display: flex;
  flex-direction: column;
}
.video-modal-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 12px 16px;
  background: rgba(12, 30, 52, 0.95);
  border-bottom: 1px solid rgba(255, 255, 255, 0.10);
  width: 100%;
  box-sizing: border-box;
}
.video-modal-title {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.88rem;
  font-weight: 700;
  color: #FFFFFF;
  min-width: 0;
  flex: 1 1 0%;
  overflow: hidden;
}
.video-modal-title span {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  min-width: 0;
}
.video-modal-close-btn {
  background: rgba(255, 255, 255, 0.10);
  border: 1px solid rgba(255, 255, 255, 0.15);
  color: #E2E8F0;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
  font-family: inherit;
  padding: 0;
  flex-shrink: 0;
}
.video-modal-close-btn:hover {
  background: rgba(239, 68, 68, 0.30);
  border-color: rgba(239, 68, 68, 0.60);
  color: #FFFFFF;
  transform: scale(1.05);
}
.video-responsive-wrap {
  position: relative;
  width: 100%;
  padding-top: 56.25%; /* 16:9 Aspect Ratio */
  background: #000000;
}
.video-responsive-wrap iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border: 0;
}

/* ═══ 5-Step Connected Clinical Pathway ═══ */
.pathway-track {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 12px;
  position: relative;
}
.pathway-card {
  background: var(--glass-bg);
  border: 1px solid var(--glass-border);
  backdrop-filter: var(--glass-blur);
  -webkit-backdrop-filter: var(--glass-blur);
  border-radius: var(--radius-md);
  padding: 16px 14px;
  box-shadow: var(--glass-shadow), var(--glass-specular);
  transition: transform 0.3s var(--ease-smooth), border-color 0.3s ease;
  display: flex;
  flex-direction: column;
}
.pathway-card:hover {
  transform: translateY(-2px);
  border-color: var(--ep-teal-bright);
}
.step-num {
  width: 26px;
  height: 26px;
  border-radius: 50%;
  background: rgba(8, 20, 36, 0.85);
  border: 1.5px solid var(--ep-teal-bright);
  color: var(--ep-teal-bright);
  font-family: var(--font-display);
  font-size: 0.76rem;
  font-weight: 800;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 8px;
}
.step-actor {
  font-size: 0.60rem;
  font-weight: 700;
  letter-spacing: 0.10em;
  text-transform: uppercase;
  color: var(--ep-teal-bright);
  margin-bottom: 4px;
}
.pathway-card h4 {
  font-size: 0.88rem;
  margin-bottom: 5px;
  color: var(--text-white);
}
.pathway-card p {
  font-size: 0.78rem;
  color: var(--text-muted);
  line-height: 1.45;
}

/* ═══ Consultant Leadership Cards ═══ */
.consultants-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 18px;
  margin-bottom: 24px;
}
.consultant-card {
  background: var(--glass-bg);
  border: 1px solid var(--glass-border);
  backdrop-filter: var(--glass-blur);
  -webkit-backdrop-filter: var(--glass-blur);
  border-radius: var(--radius-lg);
  padding: 22px 22px;
  box-shadow: var(--glass-shadow), var(--glass-specular);
  transition: transform 0.3s var(--ease-smooth), border-color 0.3s ease;
}
.consultant-card:hover {
  transform: translateY(-2px);
  border-color: var(--ep-teal-bright);
}
.consultant-header {
  display: flex;
  gap: 14px;
  align-items: center;
  margin-bottom: 14px;
}
.consultant-photo {
  width: 72px;
  height: 72px;
  border-radius: 14px;
  object-fit: cover;
  object-position: center;
  border: 2px solid var(--ep-teal-bright);
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.40);
  flex-shrink: 0;
}
.consultant-title-group h3 {
  font-size: 1.10rem;
  color: var(--text-white);
}
.consultant-role {
  font-size: 0.78rem;
  color: var(--ep-teal-bright);
  font-weight: 600;
  margin: 2px 0 6px;
}
.consultant-credentials {
  display: flex;
  gap: 5px;
  flex-wrap: wrap;
}
.cred-badge {
  font-size: 0.66rem;
  font-weight: 700;
  padding: 2px 6px;
  border-radius: 4px;
  background: rgba(255, 255, 255, 0.10);
  border: 1px solid rgba(255, 255, 255, 0.16);
  color: var(--text-body);
}
.consultant-bio {
  font-size: 0.82rem;
  color: var(--text-body);
  margin-bottom: 14px;
  line-height: 1.5;
}
.consultant-posts {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 6px;
  padding-top: 12px;
  border-top: 1px solid rgba(255, 255, 255, 0.12);
}
.consultant-posts li {
  display: flex;
  gap: 8px;
  font-size: 0.78rem;
  color: var(--text-muted);
  line-height: 1.45;
}
.consultant-posts li svg {
  width: 15px;
  height: 15px;
  flex-shrink: 0;
  color: var(--ep-teal-bright);
  margin-top: 2px;
}

/* Governance Pillars */
.gov-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
}
.gov-card {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.12);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-radius: var(--radius-sm);
  padding: 14px 14px;
}
.gov-card h4 {
  font-size: 0.82rem;
  display: flex;
  align-items: center;
  gap: 6px;
  color: var(--text-white);
  margin-bottom: 4px;
}
.gov-card h4 svg {
  width: 14px;
  height: 14px;
  color: var(--ep-teal-bright);
}
.gov-card p {
  font-size: 0.75rem;
  color: var(--text-muted);
  line-height: 1.4;
}

/* ═══ Trusted Partners & Infinite Carousel ═══ */
.partner-carousel-wrap {
  position: relative;
  width: 100%;
  max-width: 100%;
  overflow: hidden;
  contain: paint;
  mask-image: linear-gradient(90deg, transparent 0%, #000000 12%, #000000 88%, transparent 100%);
  -webkit-mask-image: linear-gradient(90deg, transparent 0%, #000000 12%, #000000 88%, transparent 100%);
}
.partner-carousel-track {
  display: flex;
  gap: 18px;
  width: max-content;
  animation: partnerMarquee 45s linear infinite;
}
.partner-carousel-track:hover {
  animation-play-state: paused;
}
@keyframes partnerMarquee {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}
.partner-card {
  min-width: 325px;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.14);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-radius: var(--radius-md);
  padding: 14px 18px;
  display: flex;
  align-items: center;
  gap: 14px;
}
.partner-logo-pill {
  width: 110px;
  height: 52px;
  background: #FFFFFF;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid rgba(0, 0, 0, 0.08);
  overflow: hidden;
  padding: 6px 10px;
  flex-shrink: 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.18);
}
.partner-logo-pill--dark {
  background: #0C1E34;
  border: 1px solid rgba(255,255,255,0.15);
}
/* Circle logos — minimal padding so they fill the pill */
.partner-logo-pill--circle {
  padding: 2px;
}
.partner-logo-pill--circle img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 8px;
}
.partner-logo-pill img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}
.partner-badge-icon {
  width: 40px;
  height: 40px;
  border-radius: 8px;
  background: var(--ep-teal-tint);
  border: 1px solid rgba(45, 212, 191, 0.30);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--ep-teal-bright);
}
.partner-meta strong {
  display: block;
  font-size: 0.88rem;
  color: var(--text-white);
}
.partner-meta span {
  font-size: 0.76rem;
  color: var(--text-muted);
}

/* ═══ Remuneration & Calculator ═══ */
.remuneration-layout {
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  gap: 16px;
  margin-bottom: 20px;
}
.flagship-fee-card {
  background: linear-gradient(135deg, rgba(13, 148, 136, 0.16) 0%, rgba(12, 30, 52, 0.85) 100%);
  border: 1.5px solid rgba(45, 212, 191, 0.45);
  border-radius: var(--radius-lg);
  padding: 22px 22px;
  box-shadow: 0 12px 36px rgba(0, 0, 0, 0.40), var(--glass-specular);
  backdrop-filter: var(--glass-blur);
  -webkit-backdrop-filter: var(--glass-blur);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.flagship-badge {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  background: linear-gradient(135deg, #0D9488 0%, #0F766E 100%);
  color: #FFFFFF;
  font-size: 0.65rem;
  font-weight: 800;
  letter-spacing: 0.10em;
  padding: 3px 10px;
  border-radius: var(--radius-pill);
  width: fit-content;
  margin-bottom: 10px;
}
.fee-flagship-val {
  font-family: var(--font-display);
  font-size: 2.2rem;
  font-weight: 800;
  color: var(--ep-teal-bright);
  line-height: 1;
  margin: 4px 0 8px;
}
.fee-flagship-val span {
  font-size: 0.88rem;
  color: var(--text-muted);
  font-weight: 600;
}
.flagship-features {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin: 14px 0 18px;
}
.flagship-features li {
  display: flex;
  gap: 8px;
  font-size: 0.82rem;
  color: var(--text-body);
}
.flagship-features li svg {
  width: 15px;
  height: 15px;
  flex-shrink: 0;
  color: var(--ep-teal-bright);
  margin-top: 1px;
}

/* Interactive Calculator */
.calc-card {
  background: var(--glass-bg);
  border: 1px solid var(--glass-border);
  backdrop-filter: var(--glass-blur);
  -webkit-backdrop-filter: var(--glass-blur);
  border-radius: var(--radius-lg);
  padding: 22px 20px;
  box-shadow: var(--glass-shadow), var(--glass-specular);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.calc-card h3 {
  font-size: 1.05rem;
  margin-bottom: 4px;
  color: var(--text-white);
}
.calc-card p {
  font-size: 0.78rem;
  color: var(--text-muted);
  margin-bottom: 14px;
}
.slider-group {
  margin-bottom: 14px;
}
.slider-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
}
.slider-label {
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--text-white);
}
.slider-value {
  font-family: var(--font-display);
  font-size: 0.95rem;
  font-weight: 800;
  color: var(--ep-teal-bright);
}
.calc-slider {
  width: 100%;
  height: 6px;
  border-radius: 3px;
  background: rgba(255, 255, 255, 0.15);
  outline: none;
  -webkit-appearance: none;
}
.calc-slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: var(--ep-teal-bright);
  cursor: pointer;
  box-shadow: 0 0 10px var(--ep-teal-bright);
  border: 2px solid #FFFFFF;
}
.calc-output-box {
  background: rgba(8, 20, 36, 0.85);
  border: 1px solid rgba(45, 212, 191, 0.35);
  border-radius: var(--radius-sm);
  padding: 12px;
  text-align: center;
}
.calc-output-label {
  font-size: 0.66rem;
  font-weight: 700;
  letter-spacing: 0.10em;
  text-transform: uppercase;
  color: var(--text-muted);
  margin-bottom: 2px;
}
.calc-output-val {
  font-family: var(--font-display);
  font-size: 1.65rem;
  font-weight: 800;
  color: var(--ep-teal-bright);
  margin-bottom: 2px;
}
.calc-output-note {
  font-size: 0.74rem;
  color: var(--text-body);
}

/* Remaining 6 Fee Cards */
.fees-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
  margin-bottom: 20px;
}
.fee-card {
  background: var(--glass-bg);
  border: 1px solid var(--glass-border);
  backdrop-filter: var(--glass-blur);
  -webkit-backdrop-filter: var(--glass-blur);
  border-radius: var(--radius-md);
  padding: 14px 14px;
  box-shadow: var(--glass-shadow), var(--glass-specular);
  transition: transform 0.3s var(--ease-smooth), border-color 0.3s ease;
}
.fee-card:hover {
  transform: translateY(-2px);
  border-color: var(--ep-teal-bright);
}
.fee-category {
  font-size: 0.60rem;
  font-weight: 700;
  letter-spacing: 0.10em;
  text-transform: uppercase;
  color: var(--ep-teal-bright);
  display: block;
  margin-bottom: 4px;
}
.fee-amount-box {
  display: flex;
  align-items: baseline;
  gap: 3px;
  margin-bottom: 4px;
}
.fee-upto {
  font-size: 0.60rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--text-muted);
}
.fee-upto-spacer {
  font-size: 0.60rem;
  visibility: hidden;
}
.fee-val {
  font-family: var(--font-display);
  font-size: 1.35rem;
  font-weight: 800;
  color: var(--text-white);
  line-height: 1;
}
.fee-cycle {
  font-size: 0.72rem;
  font-weight: 600;
  color: var(--text-muted);
}
.fee-card h4 {
  font-size: 0.85rem;
  margin-bottom: 4px;
  color: var(--text-white);
}
.fee-card p {
  font-size: 0.74rem;
  color: var(--text-muted);
  line-height: 1.4;
}

/* Shared Care Agreement Banner */
.agreement-banner {
  background: linear-gradient(135deg, rgba(8, 20, 36, 0.95) 0%, rgba(14, 38, 66, 0.90) 100%);
  border: 1.5px solid rgba(45, 212, 191, 0.35);
  border-radius: var(--radius-lg);
  padding: 20px 24px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 18px;
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.40), var(--glass-specular);
  backdrop-filter: var(--glass-blur);
  -webkit-backdrop-filter: var(--glass-blur);
}
.agreement-banner h3 {
  font-size: 1.08rem;
  margin-bottom: 4px;
  color: var(--text-white);
}
.agreement-banner p {
  color: var(--text-body);
  max-width: 600px;
  font-size: 0.82rem;
  line-height: 1.5;
}
.agreement-actions {
  display: flex;
  gap: 10px;
  flex-shrink: 0;
}
/* Fix white button with dark navy text so it is 100% visible */
.btn-agreement-white {
  background: #FFFFFF !important;
  color: #0C1E34 !important;
  font-weight: 700 !important;
  border: 1px solid #FFFFFF !important;
  box-shadow: 0 4px 18px rgba(255, 255, 255, 0.25) !important;
}
.btn-agreement-white:hover {
  background: #F1F5F9 !important;
  color: #0C1E34 !important;
  transform: translateY(-2px);
}

/* ═══ Practice Enquiry Form & Helpline ═══ */
.enquiry-layout {
  display: grid;
  grid-template-columns: 1.25fr 0.75fr;
  gap: 24px;
  align-items: start;
}
.enquiry-card {
  background: var(--glass-bg);
  border: 1px solid var(--glass-border);
  backdrop-filter: var(--glass-blur);
  -webkit-backdrop-filter: var(--glass-blur);
  border-radius: var(--radius-lg);
  padding: 24px 26px;
  box-shadow: var(--glass-shadow), var(--glass-specular);
}
.form-grid {
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}
.form-group {
  display: flex;
  flex-direction: column;
  gap: 4px;
  min-width: 0;
}
.form-group label {
  font-size: 0.74rem;
  font-weight: 700;
  color: var(--text-white);
}
.form-group input,
.form-group select,
.form-group textarea {
  font-family: var(--font-sans);
  font-size: 0.86rem;
  padding: 9px 12px;
  border-radius: var(--radius-sm);
  border: 1px solid rgba(255, 255, 255, 0.20);
  background: rgba(8, 20, 36, 0.75);
  color: #FFFFFF;
  transition: all 0.2s ease;
  width: 100%;
  min-width: 0;
  box-sizing: border-box;
}
.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
  outline: none;
  border-color: var(--ep-teal-bright);
  box-shadow: 0 0 0 3px rgba(45, 212, 191, 0.25);
}
.form-group textarea {
  resize: vertical;
  min-height: 70px;
}

/* Direct Clinical Helpline Card */
.contact-card {
  background: var(--glass-bg);
  border: 1px solid var(--glass-border);
  backdrop-filter: var(--glass-blur);
  -webkit-backdrop-filter: var(--glass-blur);
  border-radius: var(--radius-lg);
  padding: 22px 20px;
  box-shadow: var(--glass-shadow), var(--glass-specular);
}
.contact-card h3 {
  font-size: 1.05rem;
  margin-bottom: 14px;
  color: var(--text-white);
  display: flex;
  align-items: center;
  gap: 8px;
}
/* Info tooltip icon */
.info-tip {
  position: relative;
  display: inline-flex;
  align-items: center;
  cursor: default;
  flex-shrink: 0;
}
.info-tip svg {
  width: 15px;
  height: 15px;
  color: var(--ep-teal-bright);
  opacity: 0.7;
  transition: opacity 0.2s;
}
.info-tip:hover svg { opacity: 1; }
.info-tip-bubble {
  display: none;
  position: absolute;
  left: 50%;
  bottom: calc(100% + 8px);
  transform: translateX(-50%);
  background: rgba(8, 20, 36, 0.97);
  border: 1px solid rgba(45, 212, 191, 0.3);
  border-radius: 8px;
  padding: 9px 12px;
  width: 230px;
  font-size: 0.75rem;
  color: var(--text-body);
  line-height: 1.4;
  z-index: 50;
  pointer-events: none;
  box-shadow: 0 8px 24px rgba(0,0,0,0.4);
}
.info-tip:hover .info-tip-bubble { display: block; }
.contact-links {
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.contact-row {
  display: flex;
  gap: 12px;
}
.contact-icon {
  width: 36px;
  height: 36px;
  border-radius: 8px;
  background: var(--ep-teal-tint);
  border: 1px solid rgba(45, 212, 191, 0.30);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--ep-teal-bright);
  flex-shrink: 0;
}
.contact-icon svg {
  width: 17px;
  height: 17px;
}
.contact-text strong {
  display: block;
  font-size: 0.82rem;
  color: var(--text-white);
}
.contact-text a, .contact-text span {
  font-size: 0.88rem;
  color: var(--ep-teal-bright);
  font-weight: 600;
}
.contact-text small {
  display: block;
  font-size: 0.70rem;
  color: var(--text-muted);
  margin-top: 2px;
}

/* ═══ FAQ Accordion ═══ */
.faq-list {
  max-width: 800px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.faq-item {
  background: var(--glass-bg);
  border: 1px solid var(--glass-border);
  backdrop-filter: var(--glass-blur);
  -webkit-backdrop-filter: var(--glass-blur);
  border-radius: var(--radius-sm);
  overflow: hidden;
  box-shadow: var(--glass-shadow), var(--glass-specular);
  transition: border-color 0.25s ease;
  margin-bottom: 8px;
}
.faq-item:hover {
  border-color: rgba(45, 212, 191, 0.35);
}
.faq-q {
  width: 100%;
  padding: 13px 18px;
  background: none;
  border: none;
  display: flex;
  justify-content: space-between;
  align-items: center;
  text-align: left;
  font-family: var(--font-display);
  font-size: 0.90rem;
  font-weight: 700;
  color: var(--text-white);
  cursor: pointer;
  gap: 12px;
}
.faq-icon {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.10);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  color: var(--ep-teal-bright);
  transition: transform 0.3s var(--ease-smooth);
}
.faq-item.open .faq-icon {
  transform: rotate(45deg);
}
.faq-a {
  padding: 0 18px 13px;
  display: none;
  font-size: 0.82rem;
  color: var(--text-body);
  line-height: 1.5;
}
.faq-item.open .faq-a {
  display: block;
}

/* ═══ Footer ═══ */
.footer {
  border-top: 1px solid rgba(255, 255, 255, 0.10);
  background: #081524;
  padding: 60px 0 36px;
  position: relative;
  z-index: 2;
}
.footer-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-bottom: 34px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.10);
  margin-bottom: 30px;
  flex-wrap: wrap;
  gap: 20px;
}
.footer-links {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
  list-style: none;
}
.footer-links a {
  font-size: 0.88rem;
  color: var(--text-muted);
  transition: color 0.2s ease;
}
.footer-links a:hover {
  color: var(--ep-teal-bright);
}
.footer-bottom {
  display: flex;
  justify-content: space-between;
  font-size: 0.80rem;
  color: var(--text-muted);
  flex-wrap: wrap;
  gap: 14px;
}

/* ═══ Responsive Breakpoints ═══ */
@media (max-width: 1024px) {
  .hero-grid { grid-template-columns: 1fr; gap: 40px; }
  .simple-bento-grid { grid-template-columns: 1fr; }
  .pathway-track { grid-template-columns: 1fr; }
  .consultants-grid { grid-template-columns: 1fr; }
  .gov-grid { grid-template-columns: repeat(2, 1fr); }
  .remuneration-layout { grid-template-columns: 1fr; }
  .fees-grid { grid-template-columns: repeat(2, 1fr); }
  .enquiry-layout { grid-template-columns: 1fr; }
}

@media (max-width: 768px) {
  body { font-size: 15px; padding-top: 58px; }
  .section { padding: 42px 0; }
  .nav-inner { height: 58px; padding: 0 16px; }
  .nav-links {
    display: none;
    position: absolute;
    top: 58px;
    left: 0;
    right: 0;
    background: #091728;
    border-bottom: 1px solid rgba(45, 212, 191, 0.25);
    flex-direction: column;
    padding: 20px 24px;
    box-shadow: 0 16px 40px rgba(0, 0, 0, 0.65);
    gap: 8px;
    transition: opacity 0.3s ease, transform 0.3s var(--ease-smooth);
  }
  .nav-links.active { display: flex !important; }
  .nav-links li { width: 100%; }
  .nav-links a:not(.btn) { display: block; width: 100%; padding: 10px 0; }
  .nav-links a.btn-primary { display: flex; width: 100%; justify-content: center; margin-top: 8px; }
  .nav-toggle { display: inline-flex !important; }

  .hero { padding: 36px 0 44px; }
  .hero-proof-strip { grid-template-columns: repeat(2, 1fr); gap: 14px; }
  .hero-visual-frame img { height: auto; }

  .gov-grid { grid-template-columns: 1fr; }
  .fees-grid { grid-template-columns: 1fr; }
  .agreement-banner { flex-direction: column; align-items: flex-start; padding: 20px 18px; }
  .enquiry-card { padding: 20px 16px; }
  .form-row { grid-template-columns: 1fr; }
}

@media (max-width: 640px) {
  .nav-logo-pill {
    padding: 5px 10px;
  }
  .nav-logo-pill img {
    height: 25px;
  }
  .hero-ctas {
    flex-direction: column;
    width: 100%;
  }
  .hero-ctas .btn {
    width: 100%;
    justify-content: center;
  }
  /* Larger, more visible partner logo pills on mobile */
  .partner-card {
    min-width: 240px;
    padding: 12px 14px;
    gap: 12px;
  }
  .partner-logo-pill {
    width: 90px;
    height: 70px;
    padding: 4px 6px;
  }
  .partner-logo-pill--circle {
    padding: 2px;
  }
  .partner-logo-pill img {
    max-width: 100%;
    max-height: 100%;
  }
  .partner-meta strong {
    font-size: 0.82rem;
  }
  .partner-meta span {
    font-size: 0.70rem;
  }

  /* Fix agreement banner button row overflow */
  .agreement-actions {
    flex-direction: column;
    width: 100%;
  }
  .agreement-actions .btn {
    width: 100%;
    text-align: center;
    justify-content: center;
    white-space: normal;
    word-break: break-word;
  }

  /* Fix form select/input overflow */
  .form-group select,
  .form-group input,
  .form-group textarea {
    max-width: 100%;
    box-sizing: border-box;
  }

  /* Fix submit button overflow */
  #submitBtn {
    width: 100% !important;
    white-space: normal !important;
    word-break: break-word;
    text-align: center;
    box-sizing: border-box !important;
  }

  /* Enquiry card: prevent overflow on mobile */
  .enquiry-card {
    padding: 16px 14px;
    overflow: hidden;
  }

  /* Prevent any horizontal overflow */
  html, body {
    overflow-x: hidden;
    max-width: 100%;
  }
  .container {
    padding: 0 16px;
    max-width: 100%;
    box-sizing: border-box;
    overflow: hidden;
  }
  section, .section {
    overflow-x: hidden;
    max-width: 100vw;
  }
  /* Universal overflow guard for all block elements */
  h1, h2, h3, h4, h5, p, span, div, li {
    max-width: 100%;
    overflow-wrap: break-word;
    word-break: break-word;
  }
  /* Fix flex children that expand beyond viewport */
  .flagship-features li span,
  .fee-card p,
  .fee-card h4,
  .calc-output-note,
  .flagship-features li {
    min-width: 0;
    overflow-wrap: break-word;
    word-break: break-word;
    flex-shrink: 1;
  }
  .slider-label,
  .slider-value {
    min-width: 0;
    overflow-wrap: break-word;
  }
  /* Allow buttons to wrap text on small screens */
  .btn {
    white-space: normal;
    text-align: center;
  }
  /* Calculator label: allow wrapping */
  .calc-output-label {
    letter-spacing: 0.03em;
    white-space: normal;
    word-break: break-word;
    font-size: 0.58rem;
  }
  .slider-header {
    flex-wrap: wrap;
    gap: 4px;
  }
  /* Flagship fee card: contain content on mobile */
  .flagship-fee-card {
    overflow: hidden;
    padding: 16px 14px;
  }
  /* Section headings: ensure they don't overflow */
  .section-head h2,
  .section-head p {
    overflow-wrap: break-word;
    word-break: break-word;
  }
}
</style>
</head>
<body>

<!-- Ambient Aurora Mesh Background with Light Effects -->
<div class="aurora-bg" aria-hidden="true">
  <div class="aurora-blob aurora-blob-1"></div>
  <div class="aurora-blob aurora-blob-2"></div>
  <div class="aurora-blob aurora-blob-3"></div>
  <div class="aurora-blob aurora-blob-4"></div>
  <div class="aurora-mesh-overlay"></div>
</div>

<!-- Sticky Frosted Navigation (No Urgent Button) -->
<header class="nav" id="mainNav">
  <div class="nav-inner">
    <a href="#hero" class="nav-brand" aria-label="EyePros Synergy">
      <div class="nav-logo-pill">
        <img src="__LOGO_SRC__" alt="Synergy by EyePros">
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
    <button class="nav-toggle" id="navToggle" aria-label="Toggle Navigation">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" style="width:22px;height:22px;display:block">
        <line x1="3" y1="6" x2="21" y2="6"></line>
        <line x1="3" y1="12" x2="21" y2="12"></line>
        <line x1="3" y1="18" x2="21" y2="18"></line>
      </svg>
    </button>
  </div>
</header>

<!-- Hero Section: Bespoke MedTech Showcase -->
<section id="hero" class="hero">
  <div class="container">
    <div class="hero-grid">
      <div class="hero-content">
        <h1>Beyond Referrals. Towards Partnership.</h1>
        <div class="hero-tagline text-gradient">Better together.</div>
        <p class="hero-sub">A shared-care partnership for independent optometrists.</p>
        <div class="hero-ctas">
          <a href="#partner-enquiry" class="btn btn-primary">
            <span>Become a partner</span>
            <svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd"/></svg>
          </a>
          <a href="#remuneration" class="btn btn-secondary">Explore fee schedule</a>
        </div>
        <div class="hero-proof-strip">
          <div class="proof-item">
            <span class="proof-num">&pound;250</span>
            <span class="proof-label">Flat Cataract Shared-Care Fee</span>
          </div>
          <div class="proof-item">
            <span class="proof-num">7 Days</span>
            <span class="proof-label">Electronic Review to Practice</span>
          </div>
          <div class="proof-item">
            <span class="proof-num">100%</span>
            <span class="proof-label">Substantive NHS Consultants</span>
          </div>
          <div class="proof-item">
            <span class="proof-num">0 Volume</span>
            <span class="proof-label">No Referral Minimums Ever</span>
          </div>
        </div>
      </div>

      <!-- Hero Visual Showcase -->
      <div class="hero-visual">
        <div class="hero-visual-frame">
          <img src="__HERO_IMG__" alt="EyePros Synergy &mdash; The Secret? It's not just the referral... It's what happens after." loading="eager">
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Why Independent Practices Partner with EyePros: Simple 4-Card Bento Grid with Glass Effect -->
<section id="benefits" class="section section-alt">
  <div class="container">
    <div class="section-head">
      <h2>Built around the reality of independent practice</h2>
      <p class="section-lead">Corporate hospital chains keep your patients. NHS waiting lists test their patience. EyePros Synergy keeps the relationship right where it belongs: with you.</p>
    </div>

    <div class="simple-bento-grid">
      <!-- Card 1: Direct Named-Surgeon Continuity & Access -->
      <div class="simple-bento-card">
        <div class="card-top">
          <div class="card-header-row">
            <div class="card-icon-bubble">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="8.5" cy="7" r="4"/><line x1="20" y1="8" x2="20" y2="14"/><line x1="23" y1="11" x2="17" y2="11"/></svg>
            </div>
            <span class="card-tag">NO CALL CENTRES &bull; NO INTERMEDIARIES</span>
          </div>
          <h3>Direct Named-Surgeon Access</h3>
          <p>You and your patient have direct contact with the named operating consultant, from first assessment through surgery and discharge. Clinical questions go straight to the surgeon who operated.</p>
        </div>
        <div class="card-pill-row">
          <span class="card-pill">Named Consultant Access</span>
          <span class="card-pill">Direct Clinical Dialogue</span>
          <span class="card-pill">Dedicated Case Line</span>
        </div>
      </div>

      <!-- Card 2: Syndesis Platform -->
      <div class="simple-bento-card">
        <div class="card-top">
          <div class="card-header-row">
            <div class="card-icon-bubble">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
            </div>
            <span class="card-tag">DEDICATED DIGITAL PLATFORM</span>
          </div>
          <h3>Refer via Syndesis in under 2 minutes</h3>
          <p>Upload scans securely, track your patient's journey in real time, and receive automated status alerts. No paperwork, no friction.</p>
        </div>
        <div>
          <div class="card-pill-row">
            <span class="card-pill">Under 2-Min Submissions</span>
            <span class="card-pill">Real-Time Patient Tracker</span>
            <span class="card-pill">Secure Biometry &amp; OCT Uploads</span>
          </div>
          <button type="button" class="card-btn-action" id="openVideoBtn" aria-haspopup="dialog" aria-controls="videoModal" aria-label="Watch video: Explore how to refer with Syndesis">
            <svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
            <span>Explore how to refer with Syndesis</span>
          </button>
        </div>
      </div>

      <!-- Card 3: Complete Team Training -->
      <div class="simple-bento-card">
        <div class="card-top">
          <div class="card-header-row">
            <div class="card-icon-bubble">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/></svg>
            </div>
            <span class="card-tag">PRACTICE EMPOWERMENT</span>
          </div>
          <h3>Complete Team Training &amp; Support</h3>
          <p>Dedicated onboarding for your whole team: optometrists, dispensing opticians, and front-of-house. Includes 1-on-1 Syndesis walkthroughs and triage protocols.</p>
        </div>
        <div class="card-pill-row">
          <span class="card-pill">Practice Onboarding</span>
          <span class="card-pill">Front-of-House Triage</span>
          <span class="card-pill">1-on-1 Portal Demos</span>
        </div>
      </div>

      <!-- Card 4: Protected Patient Relationship & 7-Day Review -->
      <div class="simple-bento-card">
        <div class="card-top">
          <div class="card-header-row">
            <div class="card-icon-bubble">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            </div>
            <span class="card-tag">PATIENT RETENTION GUARANTEE</span>
          </div>
          <h3>Protected Patient Relationship &amp; 7-Day Review</h3>
          <p>Your patients stay yours. We perform the surgery and return them with full clinical handover within 7 days. You manage post-op review and all future dispensing.</p>
        </div>
        <div class="card-pill-row">
          <span class="card-pill">Electronic Review in 7 Days</span>
          <span class="card-pill">Post-op Biometry Shared</span>
          <span class="card-pill">Ongoing Optical Dispensing</span>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Clinical Pathway -->
<section id="journey" class="section">
  <div class="container">
    <div class="section-head">
      <h2>Five steps. Clear clinical boundaries.</h2>
      <p class="section-lead">A seamless co-management pathway designed so optometrists and consultant surgeons do exactly what each does best.</p>
    </div>

    <div class="pathway-track">
      <!-- Step 1 -->
      <div class="pathway-card">
        <div class="step-num">1</div>
        <div class="step-actor">YOUR PRACTICE</div>
        <h4>Patient Referral</h4>
        <p>Submit patient clinical details and biometry via the Syndesis portal in under 2 minutes with instant confirmation.</p>
      </div>

      <!-- Step 2 -->
      <div class="pathway-card">
        <div class="step-num">2</div>
        <div class="step-actor">EYEPROS</div>
        <h4>Consultant Assessment</h4>
        <p>Comprehensive pre-op diagnostic workup and surgeon-led informed consent conducted personally by the operating consultant.</p>
      </div>

      <!-- Step 3 -->
      <div class="pathway-card">
        <div class="step-num">3</div>
        <div class="step-actor">EYEPROS</div>
        <h4>Day-Case Surgery</h4>
        <p>State-of-the-art procedure performed in our modern surgical suite by your patient's named NHS consultant ophthalmologist.</p>
      </div>

      <!-- Step 4 -->
      <div class="pathway-card">
        <div class="step-num">4</div>
        <div class="step-actor">EYEPROS &rarr; YOU</div>
        <h4>7-Day Review</h4>
        <p>Electronic discharge letter, surgical notes, and post-op medication plan securely sent to your practice within 7 days.</p>
      </div>

      <!-- Step 5 -->
      <div class="pathway-card">
        <div class="step-num">5</div>
        <div class="step-actor">YOUR PRACTICE</div>
        <h4>4-Week Co-Management</h4>
        <p>Conduct the post-operative review and new refraction. Submit completion report via Syndesis to receive your &pound;250 fee.</p>
      </div>
    </div>
  </div>
</section>

<!-- Clinical Leadership & Governance -->
<section id="consultants" class="section section-alt">
  <div class="container">
    <div class="section-head">
      <h2>Led by substantive NHS Consultant Ophthalmologists</h2>
      <p class="section-lead">Direct named-surgeon continuity. You and your patient have direct contact with the operating consultant, underpinned by robust NHS clinical governance and national audit compliance.</p>
    </div>

    <div class="consultants-grid">
      <!-- Mr Ahmad Elsahn -->
      <div class="consultant-card">
        <div class="consultant-header">
          <img src="__AHMAD_SRC__" alt="Mr Ahmad Elsahn" class="consultant-photo" loading="lazy">
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
          <img src="__YASMINE_SRC__" alt="Ms Yasmine Abdalla" class="consultant-photo" loading="lazy">
          <div class="consultant-title-group">
            <h3>Ms Yasmine Abdalla</h3>
            <p class="consultant-role">Medical Director, EyePros</p>
            <div class="consultant-credentials">
              <span class="cred-badge">MBBCh</span>
              <span class="cred-badge">MSc</span>
              <span class="cred-badge">FRCOphth</span>
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
        <p>All consultants hold active substantive NHS appointments with specialist Fellowship training.</p>
      </div>
      <div class="gov-card">
        <h4><svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>NOD Audit Governance</h4>
        <p>Full clinical adherence to National Ophthalmology Database audit standards and RCOphth clinical guidelines.</p>
      </div>
    </div>
  </div>
</section>

<!-- Trusted Partners Section: Partners who trust Us -->
<section id="trusted" class="section">
  <div class="container">
    <div class="section-head">
      <h2>Partners who trust Us</h2>
      <p class="section-lead">Independent optometry practices across the Midlands partnering with EyePros to expand clinical scope, preserve patient continuity, and deliver consultant-led excellence.</p>
    </div>

    <!-- Infinite Carousel Marquee -->
    <div class="partner-carousel-wrap">
      <div class="partner-carousel-track">
        <!-- Set 1 (8 Partner Practices + Join Card) -->
        <div class="partner-card">
          <div class="partner-logo-pill">
            <img src="__SUMPTON_SRC__" alt="Sumpton Opticians" loading="lazy">
          </div>
          <div class="partner-meta">
            <strong>Sumpton Opticians</strong>
            <span>Practice Partner &bull; Nottinghamshire</span>
          </div>
        </div>

        <div class="partner-card">
          <div class="partner-logo-pill partner-logo-pill--dark">
            <img src="__PINDERS_SRC__" alt="Pinders Opticians" loading="lazy">
          </div>
          <div class="partner-meta">
            <strong>Pinders Opticians</strong>
            <span>Founding Partner &bull; Mansfield &amp; Southwell</span>
          </div>
        </div>

        <div class="partner-card">
          <div class="partner-logo-pill partner-logo-pill--circle">
            <img src="__OPTIQUE_COL_SRC__" alt="Optique of Collingham" loading="lazy">
          </div>
          <div class="partner-meta">
            <strong>Optique of Collingham</strong>
            <span>Practice Partner &bull; Collingham, Nottinghamshire</span>
          </div>
        </div>

        <div class="partner-card">
          <div class="partner-logo-pill partner-logo-pill--circle">
            <img src="__OPTIQUE_SOW_SRC__" alt="Optique of Southwell" loading="lazy">
          </div>
          <div class="partner-meta">
            <strong>Optique of Southwell</strong>
            <span>Practice Partner &bull; Southwell, Nottinghamshire</span>
          </div>
        </div>

        <div class="partner-card">
          <div class="partner-logo-pill">
            <img src="__DIBLOW_SRC__" alt="D.I. Blow Opticians" loading="lazy">
          </div>
          <div class="partner-meta">
            <strong>D.I. Blow Opticians</strong>
            <span>Practice Partner &bull; Nottinghamshire &amp; Derbyshire</span>
          </div>
        </div>

        <div class="partner-card">
          <div class="partner-logo-pill">
            <img src="__OAKWOOD_SRC__" alt="Oakwood Eyecare" loading="lazy">
          </div>
          <div class="partner-meta">
            <strong>Oakwood Eyecare</strong>
            <span>Practice Partner &bull; Oakwood, Derby</span>
          </div>
        </div>

        <div class="partner-card">
          <div class="partner-logo-pill">
            <img src="__ALVASTON_SRC__" alt="Alvaston Opticians" loading="lazy">
          </div>
          <div class="partner-meta">
            <strong>Alvaston Opticians</strong>
            <span>Practice Partner &bull; Alvaston, Derby</span>
          </div>
        </div>

        <div class="partner-card">
          <div class="partner-logo-pill">
            <img src="__KIMBERLEY_SRC__" alt="Kimberley Opticians" loading="lazy">
          </div>
          <div class="partner-meta">
            <strong>Kimberley Opticians</strong>
            <span>Practice Partner &bull; Kimberley, Nottinghamshire</span>
          </div>
        </div>

        <div class="partner-card partner-card-add">
          <div class="partner-badge-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width:20px;height:20px"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
          </div>
          <div class="partner-meta">
            <strong>Join Our Network</strong>
            <span><a href="#partner-enquiry" style="color:var(--ep-teal-bright);text-decoration:underline">Become a Partner Practice &rarr;</a></span>
          </div>
        </div>

        <!-- Set 2 (Exact duplicate for seamless continuous loop) -->
        <div class="partner-card">
          <div class="partner-logo-pill">
            <img src="__SUMPTON_SRC__" alt="Sumpton Opticians" loading="lazy">
          </div>
          <div class="partner-meta">
            <strong>Sumpton Opticians</strong>
            <span>Practice Partner &bull; Nottinghamshire</span>
          </div>
        </div>

        <div class="partner-card">
          <div class="partner-logo-pill partner-logo-pill--dark">
            <img src="__PINDERS_SRC__" alt="Pinders Opticians" loading="lazy">
          </div>
          <div class="partner-meta">
            <strong>Pinders Opticians</strong>
            <span>Founding Partner &bull; Mansfield &amp; Southwell</span>
          </div>
        </div>

        <div class="partner-card">
          <div class="partner-logo-pill partner-logo-pill--circle">
            <img src="__OPTIQUE_COL_SRC__" alt="Optique of Collingham" loading="lazy">
          </div>
          <div class="partner-meta">
            <strong>Optique of Collingham</strong>
            <span>Practice Partner &bull; Collingham, Nottinghamshire</span>
          </div>
        </div>

        <div class="partner-card">
          <div class="partner-logo-pill partner-logo-pill--circle">
            <img src="__OPTIQUE_SOW_SRC__" alt="Optique of Southwell" loading="lazy">
          </div>
          <div class="partner-meta">
            <strong>Optique of Southwell</strong>
            <span>Practice Partner &bull; Southwell, Nottinghamshire</span>
          </div>
        </div>

        <div class="partner-card">
          <div class="partner-logo-pill">
            <img src="__DIBLOW_SRC__" alt="D.I. Blow Opticians" loading="lazy">
          </div>
          <div class="partner-meta">
            <strong>D.I. Blow Opticians</strong>
            <span>Practice Partner &bull; Nottinghamshire &amp; Derbyshire</span>
          </div>
        </div>

        <div class="partner-card">
          <div class="partner-logo-pill">
            <img src="__OAKWOOD_SRC__" alt="Oakwood Eyecare" loading="lazy">
          </div>
          <div class="partner-meta">
            <strong>Oakwood Eyecare</strong>
            <span>Practice Partner &bull; Oakwood, Derby</span>
          </div>
        </div>

        <div class="partner-card">
          <div class="partner-logo-pill">
            <img src="__ALVASTON_SRC__" alt="Alvaston Opticians" loading="lazy">
          </div>
          <div class="partner-meta">
            <strong>Alvaston Opticians</strong>
            <span>Practice Partner &bull; Alvaston, Derby</span>
          </div>
        </div>

        <div class="partner-card">
          <div class="partner-logo-pill">
            <img src="__KIMBERLEY_SRC__" alt="Kimberley Opticians" loading="lazy">
          </div>
          <div class="partner-meta">
            <strong>Kimberley Opticians</strong>
            <span>Practice Partner &bull; Kimberley, Nottinghamshire</span>
          </div>
        </div>

        <div class="partner-card partner-card-add">
          <div class="partner-badge-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width:20px;height:20px"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
          </div>
          <div class="partner-meta">
            <strong>Join Our Network</strong>
            <span><a href="#partner-enquiry" style="color:var(--ep-teal-bright);text-decoration:underline">Become a Partner Practice &rarr;</a></span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Transparent Remuneration Section -->
<section id="remuneration" class="section section-alt">
  <div class="container">
    <div class="section-head">
      <h2>Flat shared-care fee schedule</h2>
      <p class="section-lead">Fair, transparent remuneration recognising your clinical expertise and chair time. Fees are flat and never volume-dependent.</p>
    </div>

    <!-- Flagship Cataract Fee + Practice Revenue Calculator -->
    <div class="remuneration-layout">
      <!-- Flagship Card -->
      <div class="flagship-fee-card">
        <div>
          <span class="flagship-badge">FLAGSHIP CO-MANAGEMENT</span>
          <span class="fee-category">PRIMARY SURGICAL EPISODE</span>
          <div class="fee-flagship-val">&pound;250 <span>/ eye</span></div>
          <h3 style="margin-top:4px;font-size:1.08rem">Cataract &amp; Premium Lens Surgery</h3>
          <p style="color:var(--text-body);font-size:0.84rem;margin-top:4px">Applies to all Self-Pay &amp; Patient Finance cataract episodes. Paid upon submission of the 4-week post-op assessment via Syndesis.</p>
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
        <h4>EyeSpa Dry Eye Protocols</h4>
        <p>Dedicated clinical course for meibomian gland dysfunction, blepharitis, and severe dry eye.</p>
      </div>

      <!-- 7. Lacryfill -->
      <div class="fee-card">
        <span class="fee-category">PUNCTAL OCCLUSION</span>
        <div class="fee-amount-box">
          <span class="fee-upto-spacer">&nbsp;</span>
          <div class="fee-val">&pound;60</div>
        </div>
        <h4>Lacryfill Injections</h4>
        <p>Advanced cross-linked hyaluronic acid punctal occlusion for chronic ocular surface disease.</p>
      </div>
    </div>

    <!-- Shared Care Agreement Callout Banner (With 100% visible dark navy text on white pill button) -->
    <div class="agreement-banner">
      <div>
        <h3>Receive a copy of our Shared Care Agreement</h3>
        <p>Review the full legal framework, clinical governance protocols, indemnities, and transparent payment schedules. Governed by English law.</p>
      </div>
      <div class="agreement-actions">
        <a href="#partner-enquiry" class="btn btn-agreement-white">Request Agreement Copy</a>
        <a href="tel:03337727277" class="btn btn-outline-white">0333 77 272 77</a>
      </div>
    </div>
  </div>
</section>

<!-- Practice Registration Section -->
<section id="partner-enquiry" class="section">
  <div class="container">
    <div class="section-head">
      <h2>Become an EyePros Synergy Partner</h2>
      <p class="section-lead">Join independent optometry practices across the Midlands delivering consultant-led surgical excellence and protected patient continuity.</p>
    </div>

    <div class="enquiry-layout">
      <!-- Form Card -->
      <div class="enquiry-card">
        <form id="partnerForm" class="form-grid">
          <div class="form-row">
            <div class="form-group">
              <label for="practiceName">Practice Name *</label>
              <input type="text" id="practiceName" name="practiceName" required placeholder="e.g. Vision Care Opticians">
            </div>
            <div class="form-group">
              <label for="practicePostcode">Practice Postcode *</label>
              <input type="text" id="practicePostcode" name="practicePostcode" required placeholder="e.g. NG1 1AA">
            </div>
          </div>

          <div class="form-row">
            <div class="form-group">
              <label for="contactName">Contact Name *</label>
              <input type="text" id="contactName" name="contactName" required placeholder="Lead Optometrist / Practice Manager">
            </div>
            <div class="form-group">
              <label for="gocNumber">GOC Number (Optional)</label>
              <input type="text" id="gocNumber" name="gocNumber" placeholder="e.g. 01-12345">
            </div>
          </div>

          <div class="form-row">
            <div class="form-group">
              <label for="email">Email Address *</label>
              <input type="email" id="email" name="email" required placeholder="practice@example.co.uk">
            </div>
            <div class="form-group">
              <label for="phone">Phone Number *</label>
              <input type="tel" id="phone" name="phone" required placeholder="0115 ... or 07...">
            </div>
          </div>

          <div class="form-group">
            <label for="clinicalInterests">Primary Clinical Interests</label>
            <select id="clinicalInterests" name="clinicalInterests">
              <option value="cataract">Cataract &amp; Premium Lens Co-Management (&pound;250 fee)</option>
              <option value="glaucoma">Glaucoma / MIGS Shared Care (Up to &pound;100)</option>
              <option value="laser">YAG &amp; SLT Laser Procedures (&pound;95 fee)</option>
              <option value="dry-amd">Valeda Photobiomodulation for Dry AMD (&pound;150 fee)</option>
              <option value="dry-eye">EyeSpa Dry Eye Clinic (&pound;120 fee)</option>
              <option value="full-portfolio">Full Shared Care &amp; Co-Management Portfolio</option>
            </select>
          </div>

          <div class="form-group">
            <label for="comments">Additional Comments or Questions</label>
            <textarea id="comments" name="comments" rows="3" placeholder="Tell us about your practice, current patient volume, or Syndesis onboarding preferences..."></textarea>
          </div>

          <button type="submit" class="btn btn-primary" id="submitBtn" style="width:100%;padding:11px 20px;box-sizing:border-box;white-space:normal">
            <span>Submit Partnership Enquiry &amp; Receive Agreement</span>
            <svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd"/></svg>
          </button>
        </form>

        <div id="formSuccess" style="display:none;text-align:center;padding:32px 20px">
          <div style="width:54px;height:54px;border-radius:50%;background:var(--ep-teal-tint);color:var(--ep-teal-bright);display:flex;align-items:center;justify-content:center;margin:0 auto 16px">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="width:28px;height:28px"><polyline points="20 6 9 17 4 12"/></svg>
          </div>
          <h3 style="color:var(--text-white);margin-bottom:8px">Enquiry Received</h3>
          <p style="color:var(--text-body);font-size:0.86rem">Thank you. Our partnership team will review your practice details and send a copy of our Shared Care Agreement within 1 business day.</p>
        </div>
      </div>

      <!-- Direct Clinical Helpline Card -->
      <div class="contact-card">
        <h3>Direct Clinical Helpline
          <span class="info-tip" aria-label="About this helpline" tabindex="0">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
            <span class="info-tip-bubble">Speak directly with our partnership director or clinical lead regarding clinical protocols, patient suitability, and Syndesis onboarding.</span>
          </span>
        </h3>
        <div class="contact-links">
          <div class="contact-row">
            <div class="contact-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 16.92z"/></svg>
            </div>
            <div class="contact-text">
              <strong>Practice Enquiries</strong>
              <a href="tel:03337727277">0333 77 272 77</a>
              <small>Mon &ndash; Fri &bull; 8:30am &ndash; 6:00pm</small>
            </div>
          </div>

          <div class="contact-row">
            <div class="contact-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/></svg>
            </div>
            <div class="contact-text">
              <strong>Priority Clinical Line</strong>
              <span style="color:var(--ep-teal-bright)">Option 5 (Clinician-to-Clinician)</span>
              <small>Direct access for triage and post-op queries</small>
            </div>
          </div>

          <div class="contact-row">
            <div class="contact-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
            </div>
            <div class="contact-text">
              <strong>Direct Partner Desk</strong>
              <a href="mailto:practice@eyepros.co.uk">practice@eyepros.co.uk</a>
              <small>Direct liaison for accreditation &amp; SLAs</small>
            </div>
          </div>

          <div class="contact-row">
            <div class="contact-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>
            </div>
            <div class="contact-text">
              <strong>Surgical Locations</strong>
              <span style="color:var(--text-white)">East Midlands Surgical Centres</span>
              <small>(Nottinghamshire, Derbyshire, Leicestershire)</small>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- FAQ Accordion -->
<section id="faq" class="section section-alt">
  <div class="container">
    <div class="section-head">
      <h2>Partnership clarity for your practice</h2>
      <p class="section-lead">Straightforward answers on clinical governance, payment terms, and co-management protocols.</p>
    </div>

    <div class="faq-list">
      <!-- FAQ 1 -->
      <div class="faq-item">
        <button class="faq-q">
          <span>How does the &pound;250 Cataract Co-Management fee work and when is it paid?</span>
          <span class="faq-icon">+</span>
        </button>
        <div class="faq-a">
          The &pound;250 fee is paid per eye for managing the 4-week post-operative review and refractive assessment of private and self-pay cataract patients. Upon submitting your clinical assessment findings via the Syndesis portal, payment is settled directly to your practice bank account via BACS. There are no volume minimums or quotas to qualify.
        </div>
      </div>

      <!-- FAQ 2 -->
      <div class="faq-item">
        <button class="faq-q">
          <span>Are my referred patients guaranteed to return to my practice?</span>
          <span class="faq-icon">+</span>
        </button>
        <div class="faq-a">
          Yes, absolutely. Our Shared Care Agreement legally protects your patient relationship. EyePros exclusively provides the surgical episode and returns the patient to your consulting room within 7 days for post-op care. We do not provide primary optometric services, spectacles, or contact lenses &mdash; all future dispensing remains 100% with your practice.
        </div>
      </div>

      <!-- FAQ 3 -->
      <div class="faq-item">
        <button class="faq-q">
          <span>What clinical support and team training does EyePros provide?</span>
          <span class="faq-icon">+</span>
        </button>
        <div class="faq-a">
          We provide complete training for your practice team on using the Syndesis digital referral platform, submitting scans, and tracking patient milestones. Additionally, partner optometrists have direct telephone access to the operating consultant ophthalmologist for clinical queries, patient triage, and peer-to-peer discussion.
        </div>
      </div>

      <!-- FAQ 4 -->
      <div class="faq-item">
        <button class="faq-q">
          <span>What happens if a patient experiences an unexpected complication?</span>
          <span class="faq-icon">+</span>
        </button>
        <div class="faq-a">
          EyePros retains full surgical indemnity and acute post-operative medical responsibility. If you or your patient has any clinical concerns, you have direct priority telephone access to the named consultant surgeon who performed the operation, with emergency same-day review at our surgical centre if required.
        </div>
      </div>

      <!-- FAQ 5 -->
      <div class="faq-item">
        <button class="faq-q">
          <span>What accreditation or equipment does my practice need to join?</span>
          <span class="faq-icon">+</span>
        </button>
        <div class="faq-a">
          Any GOC-registered optometrist in an independent practice can participate. Standard diagnostic equipment (slit lamp, applanation tonometry, visual field analyser) is sufficient for post-operative reviews. An OCT is beneficial but not mandatory. Our clinical team provides a straightforward induction on post-op assessment protocols.
        </div>
      </div>

      <!-- FAQ 6 -->
      <div class="faq-item">
        <button class="faq-q">
          <span>How do I receive a copy of the Shared Care Agreement?</span>
          <span class="faq-icon">+</span>
        </button>
        <div class="faq-a">
          Simply complete the practice enquiry form above or call our partnership desk on 0333 77 272 77. We will send the full legal agreement, clinical governance schedule, and onboarding documentation for your review within one business day.
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Footer -->
<footer class="footer">
  <div class="container">
    <div class="footer-top">
      <div class="nav-brand">
        <div class="nav-logo-pill">
          <img src="__LOGO_SRC__" alt="Synergy by EyePros">
        </div>
      </div>
      <ul class="footer-links">
        <li><a href="#benefits">Why EyePros</a></li>
        <li><a href="#journey">Patient Pathway</a></li>
        <li><a href="#consultants">Surgeons</a></li>
        <li><a href="#trusted">Partners</a></li>
        <li><a href="#remuneration">Fees &amp; Calculator</a></li>
        <li><a href="#faq">FAQ</a></li>
        <li><a href="#partner-enquiry">Partner Registration</a></li>
      </ul>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 EyePros Synergy. Consultant-led ophthalmic shared care for UK independent optometry. All rights reserved.</p>
      <p>CQC Registered Surgical Centres &bull; National Ophthalmology Database Audit Compliant &bull; GMC Specialist Register</p>
    </div>
  </div>
</footer>

<!-- Syndesis Walkthrough Video Modal -->
<dialog id="videoModal" class="video-modal-dialog" closedby="any" aria-labelledby="videoModalTitle">
  <div class="video-modal-content">
    <div class="video-modal-header">
      <div class="video-modal-title" id="videoModalTitle">
        <svg viewBox="0 0 24 24" style="width:20px;height:20px;fill:var(--ep-teal-bright)"><path d="M8 5v14l11-7z"/></svg>
        <span>Syndesis: Step by Step Refer in Under 2 Minutes</span>
      </div>
      <button type="button" class="video-modal-close-btn" id="closeVideoBtn" aria-label="Close video walkthrough">
        <svg viewBox="0 0 24 24" style="width:18px;height:18px;stroke:currentColor;fill:none;stroke-width:2.2;stroke-linecap:round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>
    </div>
    <div class="video-responsive-wrap">
      <iframe id="videoIframe" src="" title="Syndesis: Step by Step Refer in under 2 minutes" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    </div>
  </div>
</dialog>

<script>
// Sticky Navbar scroll transition
var mainNav = document.getElementById('mainNav');
window.addEventListener('scroll', function() {
  if (window.scrollY > 25) {
    mainNav.classList.add('scrolled');
  } else {
    mainNav.classList.remove('scrolled');
  }
}, { passive: true });

// Mobile navigation toggle
var navToggle = document.getElementById('navToggle');
var navLinks = document.querySelector('.nav-links');
if (navToggle && navLinks) {
  navToggle.addEventListener('click', function(e) {
    e.stopPropagation();
    navLinks.classList.toggle('active');
  });
  document.addEventListener('click', function(e) {
    if (!navToggle.contains(e.target) && !navLinks.contains(e.target)) {
      navLinks.classList.remove('active');
    }
  });
}

// In-page smooth scrolling with navbar offset, scrollIntoView and Wix cross-frame message
function scrollToSection(targetId) {
  var inIframe = false;
  try { inIframe = (window.self !== window.top); } catch(e) { inIframe = true; }

  if (!targetId || targetId === '#' || targetId === '#hero') {
    try { window.scrollTo({ top: 0, behavior: 'smooth' }); } catch(e) {}
    try { if (document.body) document.body.scrollIntoView({ behavior: 'smooth', block: 'start' }); } catch(e) {}
    if (inIframe) {
      try {
        window.parent.postMessage({ type: 'synergyScroll', action: 'scroll', target: '#hero', offsetTop: 0 }, '*');
        window.parent.postMessage({ type: 'scrollToSection', target: 'hero', offsetTop: 0 }, '*');
      } catch(err) {}
    }
    if (history.pushState) history.pushState(null, null, ' ');
    return;
  }

  var cleanId = targetId.replace(/^#/, '');
  var target = document.getElementById(cleanId) || document.querySelector(targetId);
  if (!target) {
    try { window.location.hash = targetId; } catch(e) {}
    return;
  }

  var nav = document.querySelector('.nav');
  var navHeight = nav ? nav.offsetHeight : 74;
  var targetRect = target.getBoundingClientRect();
  var currentY = window.pageYOffset || document.documentElement.scrollTop || 0;
  var targetY = Math.max(0, Math.round(targetRect.top + currentY - navHeight - 12));

  // 1. Scroll the current window/frame
  try {
    window.scrollTo({ top: targetY, behavior: 'smooth' });
  } catch(e) {
    try { window.scrollTo(0, targetY); } catch(e2) {}
  }

  // 2. If inside iframe, bubble scroll to outer parent window and broadcast postMessage
  if (inIframe) {
    try {
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    } catch(e) {
      try { target.scrollIntoView(true); } catch(e2) {}
    }

    try {
      window.parent.postMessage({
        type: 'synergyScroll',
        action: 'scroll',
        target: targetId,
        hash: targetId,
        cleanId: cleanId,
        offsetTop: targetY
      }, '*');
      window.parent.postMessage({
        type: 'scrollToSection',
        target: cleanId,
        offsetTop: targetY
      }, '*');
    } catch(err) {}
  }

  // 3. Update URL hash without forcing abrupt browser jump
  try {
    if (history.pushState) {
      history.pushState(null, null, targetId);
    } else {
      window.location.hash = targetId;
    }
  } catch(e) {}
}

document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
  anchor.addEventListener('click', function(e) {
    var href = this.getAttribute('href');
    if (!href) return;
    e.preventDefault();
    if (navLinks) navLinks.classList.remove('active');
    scrollToSection(href);
  });
});

// ScrollSpy to highlight active link
if ('IntersectionObserver' in window) {
  var sections = document.querySelectorAll('section[id]');
  var navAnchors = document.querySelectorAll('.nav-links a:not(.btn)');
  var observer = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
      if (entry.isIntersecting) {
        var id = entry.target.getAttribute('id');
        navAnchors.forEach(function(a) {
          if (a.getAttribute('href') === '#' + id) {
            a.classList.add('active');
          } else {
            a.classList.remove('active');
          }
        });
      }
    });
  }, { rootMargin: '-20% 0px -60% 0px' });
  sections.forEach(function(s) { observer.observe(s); });
}

// Initial hash check
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', function() {
    if (window.location.hash) {
      setTimeout(function() { scrollToSection(window.location.hash); }, 250);
    }
  });
} else {
  if (window.location.hash) {
    setTimeout(function() { scrollToSection(window.location.hash); }, 250);
  }
}

// Interactive Practice Revenue Calculator
var calcSlider = document.getElementById('calcSlider');
var calcPatientVal = document.getElementById('calcPatientVal');
var calcAnnualFee = document.getElementById('calcAnnualFee');

if (calcSlider && calcPatientVal && calcAnnualFee) {
  calcSlider.addEventListener('input', function() {
    var pts = parseInt(this.value, 10);
    calcPatientVal.innerText = pts + (pts === 1 ? ' patient / month' : ' patients / month');
    var annual = pts * 12 * 250;
    calcAnnualFee.innerText = '£' + annual.toLocaleString('en-GB');
  });
}

// FAQ Accordion
document.querySelectorAll('.faq-q').forEach(function(button) {
  button.addEventListener('click', function() {
    this.parentElement.classList.toggle('open');
  });
});

// Enquiry form submission
var partnerForm = document.getElementById('partnerForm');
if (partnerForm) {
  partnerForm.addEventListener('submit', function(e) {
    e.preventDefault();
    var submitBtn = document.getElementById('submitBtn');
    submitBtn.innerText = 'Submitting...';
    submitBtn.disabled = true;

    var formData = new FormData(partnerForm);
    var payload = {};
    formData.forEach(function(value, key) { payload[key] = value; });

    fetch('https://formsubmit.co/ajax/practice@eyepros.co.uk', {
      method: 'POST',
      headers: {'Content-Type': 'application/json', 'Accept': 'application/json'},
      body: JSON.stringify(payload)
    })
    .then(function() {
      partnerForm.style.display = 'none';
      document.getElementById('formSuccess').style.display = 'block';
    })
    .catch(function() {
      partnerForm.submit();
    });
  });
}

// Video Walkthrough Modal (Plays inline in native dialog without tab redirect)
var videoModal = document.getElementById('videoModal');
var openVideoBtn = document.getElementById('openVideoBtn');
var closeVideoBtn = document.getElementById('closeVideoBtn');
var videoIframe = document.getElementById('videoIframe');
var youtubeEmbedUrl = 'https://www.youtube.com/embed/ehPeRm3tENM?autoplay=1&rel=0';

if (videoModal && openVideoBtn && videoIframe) {
  openVideoBtn.addEventListener('click', function(e) {
    e.preventDefault();
    videoIframe.src = youtubeEmbedUrl;
    videoModal.showModal();
  });

  function stopAndCloseVideo() {
    videoModal.close();
    videoIframe.src = '';
  }

  if (closeVideoBtn) {
    closeVideoBtn.addEventListener('click', function(e) {
      e.preventDefault();
      stopAndCloseVideo();
    });
  }

  videoModal.addEventListener('close', function() {
    videoIframe.src = '';
  });

  // Light-dismiss fallback for browsers without native closedby support
  if (!('closedBy' in HTMLDialogElement.prototype)) {
    videoModal.addEventListener('click', function(event) {
      if (event.target !== videoModal) return;
      var rect = videoModal.getBoundingClientRect();
      var isInside = (
        rect.top <= event.clientY &&
        event.clientY <= rect.top + rect.height &&
        rect.left <= event.clientX &&
        event.clientX <= rect.left + rect.width
      );
      if (!isInside) {
        stopAndCloseVideo();
      }
    });
  }
}
</script>
</body>
</html>"""

    html = template
    html = html.replace('__LOGO_SRC__', l_src)
    html = html.replace('__AHMAD_SRC__', a_src)
    html = html.replace('__YASMINE_SRC__', y_src)
    html = html.replace('__PINDERS_SRC__', p_src)
    html = html.replace('__OPTIQUE_COL_SRC__', o_col_src)
    html = html.replace('__OPTIQUE_SOW_SRC__', o_sow_src)
    html = html.replace('__DIBLOW_SRC__', di_src)
    html = html.replace('__OAKWOOD_SRC__', oak_src)
    html = html.replace('__ALVASTON_SRC__', alv_src)
    html = html.replace('__KIMBERLEY_SRC__', kim_src)
    html = html.replace('__SUMPTON_SRC__', sump_src)
    html = html.replace('__HERO_IMG__', hero_img)
    return html


# Generate both files
embed_html = build_page(is_embed=True)
with open("synergy-wix-embed.html", "w", encoding="utf-8") as f:
    f.write(embed_html)

landing_html = build_page(is_embed=False)
with open("synergy-landing-page.html", "w", encoding="utf-8") as f:
    f.write(landing_html)

print("Generated both synergy-wix-embed.html and synergy-landing-page.html with EyePros Blue & Glassmorphism!")
