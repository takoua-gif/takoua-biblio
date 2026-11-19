import re
import base64
import io
from PIL import Image

def get_b64(path, max_w=900, q=75):
    im = Image.open(path)
    ratio = max_w / float(im.size[0])
    if ratio < 1.0:
        new_h = int(float(im.size[1]) * ratio)
        im = im.resize((max_w, new_h), Image.Resampling.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, format="JPEG", quality=q, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode("utf-8")

# Read new logo from images/synergy-logo-new.png
with open('images/synergy-logo-new.png', 'rb') as f_logo:
    logo_b64 = 'data:image/png;base64,' + base64.b64encode(f_logo.read()).decode('utf-8')

# Read current embed for base64 headshots if already embedded, or fallback
try:
    with open("synergy-wix-embed.html", "r", encoding="utf-8") as f:
        orig = f.read()
    ahmad_m = re.search(r'img src="(data:image/jpeg;base64,[A-Za-z0-9+/=]+)" alt="Mr Ahmad Elsahn', orig)
    yasmine_m = re.search(r'img src="(data:image/jpeg;base64,[A-Za-z0-9+/=]+)" alt="Ms Yasmine Abdalla', orig)
    pinders_m = re.search(r'img src="(data:image/png;base64,[A-Za-z0-9+/=]+)" alt="Pinders Opticians', orig)
    ahmad_b64 = ahmad_m.group(1) if ahmad_m else get_b64("images/elsahn-headshot.jpg", max_w=400, q=80)
    yasmine_b64 = yasmine_m.group(1) if yasmine_m else get_b64("images/abdalla-headshot.jpg", max_w=400, q=80)
    pinders_b64 = pinders_m.group(1) if pinders_m else "images/partner-pinders.png"
except Exception:
    ahmad_b64 = get_b64("images/elsahn-headshot.jpg", max_w=400, q=80)
    yasmine_b64 = get_b64("images/abdalla-headshot.jpg", max_w=400, q=80)
    pinders_b64 = "images/partner-pinders.png"

hero_b64 = get_b64('images/synergy-hero-secret.jpg', max_w=1024, q=80)
optom_b64 = get_b64('images/optometrist-partners.jpg', max_w=800, q=75)
surgery_b64 = get_b64('images/cataract-surgery.jpg', max_w=800, q=75)

def build_page(is_embed=True):
    l_src = logo_b64 if is_embed else "images/synergy-logo-new.png"
    hero_img = hero_b64 if is_embed else "images/synergy-hero-secret.jpg"
    optom_img = optom_b64 if is_embed else "images/optometrist-partners.jpg"
    surgery_img = surgery_b64 if is_embed else "images/cataract-surgery.jpg"
    a_src = ahmad_b64 if is_embed else "images/elsahn-headshot.jpg"
    y_src = yasmine_b64 if is_embed else "images/abdalla-headshot.jpg"
    p_src = pinders_b64 if is_embed else "images/partner-pinders.png"

    template = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EyePros Synergy — Consultant-Led Shared Care for UK Independent Opticians</title>
<meta name="description" content="Specialist eye care. A connected care partnership. EyePros Synergy connects UK independent optometry practices with substantive NHS consultant ophthalmologists. Flat £250 cataract co-management, guaranteed 7-day discharge, and dedicated Syndesis platform.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root {
  /* ═══ EyePros Navy, Teal & Cream Palette ═══ */
  --bg-page: #0C1E34;
  --bg-page-deep: #081524;
  --bg-section-alt: rgba(14, 34, 58, 0.55);

  /* Signature EyePros Teal */
  --ep-teal: #0D9488;
  --ep-teal-vibrant: #14B8A6;
  --ep-teal-bright: #2DD4BF;
  --ep-teal-dark: #0F766E;
  --ep-teal-glow: rgba(20, 184, 166, 0.35);
  --ep-teal-tint: rgba(20, 184, 166, 0.12);

  /* Soft Cream & Editorial Accents */
  --ep-cream: #F8F6F0;
  --ep-cream-subtle: #EBE6DA;
  --ep-cream-tint: rgba(248, 246, 240, 0.12);

  /* EyePros Blues & Cyan */
  --ep-navy: #0C1E34;
  --ep-navy-card: rgba(16, 37, 64, 0.75);
  --ep-blue-cerulean: #0284C7;
  --ep-blue-light: #38BDF8;
  --ep-blue-glow: rgba(2, 132, 199, 0.35);

  /* Typography Colors */
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
  --glass-border: rgba(255, 255, 255, 0.15);
  --glass-border-hover: rgba(45, 212, 191, 0.45);
  --glass-specular: inset 0 1px 1px 0 rgba(255, 255, 255, 0.20);
  --glass-shadow: 0 12px 36px rgba(0, 0, 0, 0.28);
  --glass-blur: blur(20px);

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
  scroll-padding-top:76px;
  overflow-x:hidden;
}
body{
  font-family:var(--font-sans);
  font-size:15px;
  line-height:1.6;
  color:var(--text-body);
  background-color:var(--bg-page);
  background-image:linear-gradient(180deg, #091728 0%, #0C1E34 25%, #0F2744 50%, #0C1E34 75%, #081524 100%);
  -webkit-font-smoothing:antialiased;
  overflow-x:hidden;
  position:relative;
  width:100%;
}
section,[id]{scroll-margin-top:76px}
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
.text-cream{
  color:var(--ep-cream);
  font-style:normal;
}

/* ═══ Ambient Aurora Mesh Background with Light Effects ═══ */
.aurora-bg {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  pointer-events: none;
  z-index: 0;
  overflow: hidden;
}
.aurora-blob {
  position: absolute;
  border-radius: 50%;
  filter: blur(100px);
  opacity: 0.30;
  will-change: transform;
}
.aurora-blob-1 {
  width: 600px;
  height: 600px;
  top: -120px;
  left: 10%;
  background: radial-gradient(circle, #0284C7 0%, rgba(2, 132, 199, 0) 70%);
  animation: auroraMove1 24s ease-in-out infinite alternate;
}
.aurora-blob-2 {
  width: 650px;
  height: 650px;
  top: 30%;
  right: -100px;
  background: radial-gradient(circle, #0D9488 0%, rgba(13, 148, 136, 0) 70%);
  animation: auroraMove2 28s ease-in-out infinite alternate;
}
.aurora-blob-3 {
  width: 550px;
  height: 550px;
  bottom: 15%;
  left: 5%;
  background: radial-gradient(circle, #38BDF8 0%, rgba(56, 189, 248, 0) 70%);
  animation: auroraMove3 32s ease-in-out infinite alternate;
}
.aurora-blob-4 {
  width: 500px;
  height: 500px;
  top: 70%;
  right: 15%;
  background: radial-gradient(circle, #8FBBB5 0%, rgba(143, 187, 181, 0) 70%);
  animation: auroraMove4 26s ease-in-out infinite alternate;
}
.aurora-mesh-overlay {
  position: absolute;
  inset: 0;
  background-image:
    radial-gradient(at 20% 15%, rgba(13, 148, 136, 0.12) 0px, transparent 50%),
    radial-gradient(at 80% 25%, rgba(2, 132, 199, 0.14) 0px, transparent 50%),
    radial-gradient(at 50% 65%, rgba(20, 184, 166, 0.10) 0px, transparent 50%),
    radial-gradient(at 85% 85%, rgba(56, 189, 248, 0.12) 0px, transparent 50%);
  pointer-events: none;
}
@keyframes auroraMove1 {
  0% { transform: translate(0, 0) scale(1); }
  50% { transform: translate(60px, 40px) scale(1.08); }
  100% { transform: translate(-40px, 70px) scale(0.95); }
}
@keyframes auroraMove2 {
  0% { transform: translate(0, 0) scale(1); }
  50% { transform: translate(-70px, -50px) scale(1.12); }
  100% { transform: translate(40px, 60px) scale(0.92); }
}
@keyframes auroraMove3 {
  0% { transform: translate(0, 0) scale(1); }
  50% { transform: translate(50px, -60px) scale(1.05); }
  100% { transform: translate(-50px, 40px) scale(1.10); }
}
@keyframes auroraMove4 {
  0% { transform: translate(0, 0) scale(1); }
  50% { transform: translate(-60px, 40px) scale(1.08); }
  100% { transform: translate(50px, -40px) scale(0.95); }
}

/* ═══ Layout Primitives ═══ */
.container {
  max-width: var(--max-w);
  margin: 0 auto;
  padding: 0 24px;
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
.btn svg {
  width: 15px;
  height: 15px;
  transition: transform 0.2s ease;
}
.btn:hover svg {
  transform: translateX(3px);
}
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

/* ═══ Sticky Frosted Navigation ═══ */
.nav {
  position: sticky;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  background: rgba(8, 20, 36, 0.82);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.12);
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.35);
  transition: all 0.3s var(--ease-smooth);
}
.nav.scrolled {
  background: rgba(8, 20, 36, 0.95);
  border-bottom-color: rgba(45, 212, 191, 0.35);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.50);
}
.nav-inner {
  height: 66px;
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
  padding: 5px 12px;
  border-radius: var(--radius-sm);
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
  height: 30px;
  width: auto;
  display: block;
}
.nav-links {
  display: flex;
  align-items: center;
  gap: 4px;
  list-style: none;
}
.nav-links a:not(.btn) {
  color: var(--text-body);
  font-size: 0.88rem;
  font-weight: 600;
  padding: 7px 11px;
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
  left: 11px;
  right: 11px;
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
  padding: 7px;
  align-items: center;
  justify-content: center;
  line-height: 1;
  transition: all 0.2s ease;
}
.nav-toggle:hover {
  background: rgba(255, 255, 255, 0.15);
  border-color: var(--ep-teal-bright);
}

/* ═══ STEP 2 — HERO COVER: FULL-WIDTH TORN-PAPER BACKGROUND ═══ */
.hero-cover {
  position: relative;
  min-height: 520px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 64px 0 56px;
  overflow: hidden;
  border-bottom: 1px solid rgba(255, 255, 255, 0.12);
  z-index: 2;
}
.hero-cover-bg {
  position: absolute;
  inset: 0;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  z-index: 1;
}
.hero-cover-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(8, 20, 36, 0.72) 0%, rgba(12, 30, 52, 0.58) 50%, rgba(8, 20, 36, 0.88) 100%);
  z-index: 2;
  pointer-events: none;
}
.hero-cover-card {
  position: relative;
  z-index: 3;
  max-width: 840px;
  margin: 0 auto;
  text-align: center;
  background: rgba(8, 20, 36, 0.62);
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
  border: 1px solid rgba(255, 255, 255, 0.16);
  border-radius: var(--radius-lg);
  padding: 36px 36px 30px;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.45), inset 0 1px 1px rgba(255, 255, 255, 0.20);
}
.hero-cover-logo-pill {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 12px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.12);
  padding: 5px 16px;
  border-radius: var(--radius-sm);
}
.hero-cover-logo-pill img {
  height: 28px;
  width: auto;
  display: block;
}
.hero-cover-title {
  font-family: var(--font-display);
  font-size: clamp(1.75rem, 3.2vw, 2.35rem);
  font-weight: 800;
  letter-spacing: -0.025em;
  line-height: 1.18;
  color: var(--text-white);
  margin-bottom: 8px;
}
.hero-cover-tagline {
  font-family: var(--font-display);
  font-size: 1.05rem;
  font-weight: 600;
  color: var(--ep-teal-bright);
  margin-bottom: 10px;
}
.hero-cover-desc {
  font-size: 0.90rem;
  color: var(--text-body);
  max-width: 620px;
  margin: 0 auto 18px;
  line-height: 1.55;
}
.hero-cover-ctas {
  display: flex;
  justify-content: center;
  gap: 12px;
  margin-bottom: 22px;
  flex-wrap: wrap;
}
.hero-cover-proof {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 14px;
  padding-top: 16px;
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
  justify-content: center;
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

/* ═══ STEP 3 & 4: VISUAL ACCENT IN BENEFITS SECTION ═══ */
.benefits-visual-accent {
  margin-bottom: 20px;
}
.visual-accent-card {
  display: grid;
  grid-template-columns: 0.85fr 1.15fr;
  background: var(--glass-bg);
  border: 1px solid var(--glass-border);
  backdrop-filter: var(--glass-blur);
  -webkit-backdrop-filter: var(--glass-blur);
  border-radius: var(--radius-md);
  overflow: hidden;
  box-shadow: var(--glass-shadow), var(--glass-specular);
  align-items: center;
}
.visual-accent-img-wrap img {
  width: 100%;
  height: 100%;
  min-height: 175px;
  max-height: 200px;
  object-fit: cover;
  display: block;
}
.visual-accent-caption {
  padding: 20px 24px;
}
.visual-accent-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 0.10em;
  text-transform: uppercase;
  color: var(--ep-teal-bright);
  margin-bottom: 6px;
}
.visual-accent-caption h4 {
  font-size: 1.05rem;
  color: var(--text-white);
  margin-bottom: 6px;
  line-height: 1.35;
}
.visual-accent-caption p {
  font-size: 0.84rem;
  color: var(--text-muted);
  line-height: 1.5;
}

/* ═══ 4 Compact Benefit Bento Cards ═══ */
.simple-bento-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
}
.simple-bento-card {
  background: var(--glass-bg);
  border: 1px solid var(--glass-border);
  backdrop-filter: var(--glass-blur);
  -webkit-backdrop-filter: var(--glass-blur);
  border-radius: var(--radius-md);
  padding: 22px 22px;
  box-shadow: var(--glass-shadow), var(--glass-specular);
  transition: transform 0.3s var(--ease-smooth), border-color 0.3s ease, background 0.3s ease, box-shadow 0.3s ease;
  display: flex;
  flex-direction: column;
}
.simple-bento-card:hover {
  background: var(--glass-bg-hover);
  border-color: var(--glass-border-hover);
  transform: translateY(-3px);
  box-shadow: 0 14px 36px rgba(0, 0, 0, 0.35), 0 0 20px var(--ep-teal-glow), var(--glass-specular);
}
.card-icon-bubble {
  width: 38px;
  height: 38px;
  border-radius: 10px;
  background: var(--ep-teal-tint);
  border: 1px solid rgba(45, 212, 191, 0.30);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: var(--ep-teal-bright);
  margin-bottom: 12px;
}
.card-icon-bubble svg {
  width: 18px;
  height: 18px;
}
.card-tag {
  display: inline-block;
  font-size: 0.64rem;
  font-weight: 700;
  letter-spacing: 0.10em;
  text-transform: uppercase;
  color: var(--ep-teal-bright);
  margin-bottom: 6px;
}
.simple-bento-card h3 {
  font-size: 1.05rem;
  margin-bottom: 8px;
  color: var(--text-white);
}
.simple-bento-card p {
  font-size: 0.85rem;
  color: var(--text-body);
  line-height: 1.5;
}
.card-pill-row {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
  margin-top: 14px;
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
  width: 62px;
  height: 62px;
  border-radius: 12px;
  object-fit: cover;
  border: 2px solid var(--ep-teal-bright);
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.40);
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

/* Governance Pillars & Visual Strip */
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
.gov-visual-strip {
  margin-top: 18px;
}
.gov-visual-card {
  position: relative;
  border-radius: var(--radius-md);
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.14);
  box-shadow: var(--glass-shadow);
  max-height: 160px;
}
.gov-visual-card img {
  width: 100%;
  height: 160px;
  object-fit: cover;
  display: block;
  filter: brightness(0.65);
}
.gov-visual-overlay {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 18px 24px;
  background: linear-gradient(90deg, rgba(8, 20, 36, 0.90) 0%, rgba(12, 30, 52, 0.65) 60%, transparent 100%);
}
.gov-visual-pill {
  display: inline-block;
  font-size: 0.62rem;
  font-weight: 700;
  letter-spacing: 0.10em;
  color: var(--ep-teal-bright);
  margin-bottom: 3px;
}
.gov-visual-overlay h4 {
  font-size: 1.02rem;
  color: var(--text-white);
  margin-bottom: 3px;
}
.gov-visual-overlay p {
  font-size: 0.80rem;
  color: var(--text-body);
  max-width: 520px;
}

/* ═══ Trusted Partners & Infinite Carousel ═══ */
.pinders-featured-card {
  max-width: 800px;
  margin: 0 auto 28px;
  background: var(--glass-bg);
  border: 1.5px solid rgba(45, 212, 191, 0.35);
  border-radius: var(--radius-lg);
  padding: 20px 24px;
  display: flex;
  align-items: center;
  gap: 20px;
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.35), var(--glass-specular);
  backdrop-filter: var(--glass-blur);
  -webkit-backdrop-filter: var(--glass-blur);
}
.pinders-logo-box {
  width: 110px;
  flex-shrink: 0;
  background: rgba(8, 20, 36, 0.85);
  padding: 10px 14px;
  border-radius: var(--radius-sm);
  border: 1px solid rgba(255, 255, 255, 0.18);
}
.pinders-featured-content h3 {
  font-size: 1.05rem;
  color: var(--text-white);
  margin-bottom: 6px;
}
.pinders-quote {
  font-size: 0.88rem;
  color: var(--text-body);
  line-height: 1.5;
  font-style: italic;
}
.partner-carousel-wrap {
  position: relative;
  width: 100%;
  overflow: hidden;
  mask-image: linear-gradient(90deg, transparent 0%, #000000 12%, #000000 88%, transparent 100%);
  -webkit-mask-image: linear-gradient(90deg, transparent 0%, #000000 12%, #000000 88%, transparent 100%);
}
.partner-carousel-track {
  display: flex;
  gap: 14px;
  width: max-content;
  animation: partnerMarquee 38s linear infinite;
}
.partner-carousel-track:hover {
  animation-play-state: paused;
}
@keyframes partnerMarquee {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}
.partner-card {
  min-width: 250px;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.14);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-radius: var(--radius-sm);
  padding: 10px 14px;
  display: flex;
  align-items: center;
  gap: 12px;
}
.partner-logo-pill {
  width: 44px;
  height: 32px;
  background: rgba(8, 20, 36, 0.85);
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid rgba(255, 255, 255, 0.15);
}
.partner-logo-pill img {
  max-width: 30px;
  max-height: 18px;
}
.partner-badge-icon {
  width: 34px;
  height: 34px;
  border-radius: 6px;
  background: var(--ep-teal-tint);
  border: 1px solid rgba(45, 212, 191, 0.30);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--ep-teal-bright);
}
.partner-meta strong {
  display: block;
  font-size: 0.82rem;
  color: var(--text-white);
}
.partner-meta span {
  font-size: 0.72rem;
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
.enquiry-header h2 {
  font-size: 1.35rem;
  margin-bottom: 4px;
}
.enquiry-header p {
  font-size: 0.82rem;
  color: var(--text-muted);
  margin-bottom: 18px;
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
  margin-bottom: 4px;
  color: var(--text-white);
}
.contact-card p {
  font-size: 0.80rem;
  color: var(--text-muted);
  margin-bottom: 16px;
}
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
  padding: 48px 0 32px;
  position: relative;
  z-index: 2;
}
.footer-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-bottom: 28px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.10);
  margin-bottom: 24px;
  flex-wrap: wrap;
  gap: 18px;
}
.footer-links {
  display: flex;
  gap: 18px;
  flex-wrap: wrap;
  list-style: none;
}
.footer-links a {
  font-size: 0.84rem;
  color: var(--text-muted);
  transition: color 0.2s ease;
}
.footer-links a:hover {
  color: var(--ep-teal-bright);
}
.footer-bottom {
  display: flex;
  justify-content: space-between;
  font-size: 0.78rem;
  color: var(--text-muted);
  flex-wrap: wrap;
  gap: 12px;
}

/* ═══ Mobile Sticky Partnership CTA ═══ */
.mobile-sticky-cta {
  display: none;
}
@media (max-width: 768px) {
  body {
    padding-bottom: 60px;
  }
  .mobile-sticky-cta {
    display: block;
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    z-index: 990;
    background: rgba(8, 20, 36, 0.95);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border-top: 1px solid rgba(45, 212, 191, 0.35);
    padding: 10px 16px;
    box-shadow: 0 -8px 24px rgba(0, 0, 0, 0.45);
  }
  .mobile-sticky-inner {
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 500px;
    margin: 0 auto;
    gap: 12px;
  }
  .mobile-sticky-text strong {
    display: block;
    font-size: 0.82rem;
    color: var(--text-white);
    line-height: 1.2;
  }
  .mobile-sticky-text span {
    font-size: 0.70rem;
    color: var(--ep-teal-bright);
    line-height: 1.2;
  }
}

/* ═══ Responsive Breakpoints ═══ */
@media (max-width: 1024px) {
  .simple-bento-grid { grid-template-columns: 1fr; }
  .pathway-track { grid-template-columns: 1fr; }
  .consultants-grid { grid-template-columns: 1fr; }
  .gov-grid { grid-template-columns: repeat(2, 1fr); }
  .remuneration-layout { grid-template-columns: 1fr; }
  .fees-grid { grid-template-columns: repeat(2, 1fr); }
  .enquiry-layout { grid-template-columns: 1fr; }
  .visual-accent-card { grid-template-columns: 1fr; }
}

@media (max-width: 768px) {
  body { font-size: 14.5px; }
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
    padding: 18px 22px;
    box-shadow: 0 16px 40px rgba(0, 0, 0, 0.65);
    gap: 8px;
    transition: opacity 0.3s ease, transform 0.3s var(--ease-smooth);
  }
  .nav-links.active { display: flex !important; }
  .nav-links li { width: 100%; }
  .nav-links a:not(.btn) { display: block; width: 100%; padding: 9px 0; }
  .nav-links a.btn-primary { display: flex; width: 100%; justify-content: center; margin-top: 6px; }
  .nav-toggle { display: inline-flex !important; }

  .hero-cover { min-height: auto; padding: 42px 0 36px; }
  .hero-cover-card { padding: 26px 18px 22px; border-radius: var(--radius-md); }
  .hero-cover-proof { grid-template-columns: repeat(2, 1fr); gap: 12px; }
  .hero-cover-title { font-size: 1.5rem; }
  .hero-cover-tagline { font-size: 0.96rem; }

  .gov-grid { grid-template-columns: 1fr; }
  .fees-grid { grid-template-columns: 1fr; }
  .pinders-featured-card { flex-direction: column; text-align: center; padding: 18px 16px; }
  .agreement-banner { flex-direction: column; align-items: flex-start; padding: 20px 18px; }
  .enquiry-card { padding: 20px 16px; }
  .form-row { grid-template-columns: 1fr; }
}

@media (max-width: 640px) {
  .nav-logo-pill { padding: 4px 9px; }
  .nav-logo-pill img { height: 24px; }
  .hero-cover-ctas { flex-direction: column; width: 100%; }
  .hero-cover-ctas .btn { width: 100%; justify-content: center; }
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

<!-- Sticky Frosted Navigation -->
<header class="nav" id="mainNav">
  <div class="container">
    <div class="nav-inner">
      <a href="#hero" class="nav-brand" aria-label="EyePros Synergy">
        <div class="nav-logo-pill">
          <img src="__LOGO_SRC__" alt="Synergy by EyePros">
        </div>
      </a>
      <ul class="nav-links" id="navLinks">
        <li><a href="#benefits">Why EyePros</a></li>
        <li><a href="#journey">Patient Pathway</a></li>
        <li><a href="#consultants">Surgeons</a></li>
        <li><a href="#trusted">Partners</a></li>
        <li><a href="#remuneration">Fees &amp; Calculator</a></li>
        <li><a href="#faq">FAQ</a></li>
        <li><a href="#partner-enquiry" class="btn btn-primary btn-sm">Become a Partner</a></li>
      </ul>
      <button class="nav-toggle" id="navToggle" aria-label="Toggle navigation menu">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" style="width:20px;height:20px;display:block">
          <line x1="3" y1="12" x2="21" y2="12"></line>
          <line x1="3" y1="6" x2="21" y2="6"></line>
          <line x1="3" y1="18" x2="21" y2="18"></line>
        </svg>
      </button>
    </div>
  </div>
</header>

<!-- STEP 2 — HERO COVER: FULL-WIDTH TORN-PAPER TEAL & CREAM BACKGROUND -->
<section id="hero" class="hero-cover">
  <div class="hero-cover-bg" style="background-image: url('__HERO_IMG__');"></div>
  <div class="hero-cover-overlay"></div>
  <div class="container">
    <div class="hero-cover-card">
      <div class="hero-cover-logo-pill">
        <img src="__LOGO_SRC__" alt="Synergy by EyePros">
      </div>
      <div class="eyebrow-pill">
        <span class="eyebrow-dot"></span>
        UK INDEPENDENT OPTOMETRY SHARED CARE
      </div>
      <h1 class="hero-cover-title">Specialist eye care. <span class="text-cream">A connected care partnership.</span></h1>
      <p class="hero-cover-tagline">Better together. Closer to your patients.</p>
      <p class="hero-cover-desc">Substantive NHS consultant ophthalmologists partnering directly with independent optometry practices. Flat &pound;250 cataract co-management, dedicated Syndesis digital referral platform, and protected 7-day patient return.</p>
      <div class="hero-cover-ctas">
        <a href="#partner-enquiry" class="btn btn-primary">
          <span>Become a Partner</span>
          <svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd"/></svg>
        </a>
        <a href="#remuneration" class="btn btn-secondary">Explore Fee Schedule</a>
      </div>
      <div class="hero-cover-proof">
        <div class="proof-item">
          <span class="proof-num">&pound;250</span>
          <span class="proof-label">Flat Cataract Shared-Care</span>
        </div>
        <div class="proof-item">
          <span class="proof-num">7 Days</span>
          <span class="proof-label">Electronic Discharge to Practice</span>
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
  </div>
</section>

<!-- STEP 1 & 3: Why Independent Practices Partner with EyePros -->
<section id="benefits" class="section section-alt">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow-pill">
        <span class="eyebrow-dot"></span>
        PARTNERSHIP ARCHITECTURE
      </div>
      <h2>Built around the reality of independent practice</h2>
      <p class="section-lead">Corporate chains keep your patients. NHS lists test their patience. EyePros Synergy keeps the relationship right where it belongs: with you.</p>
    </div>

    <!-- Editorial Visual Accent Card -->
    <div class="benefits-visual-accent">
      <div class="visual-accent-card">
        <div class="visual-accent-img-wrap">
          <img src="__OPTOM_IMG__" alt="Consultant-Led Shared Care in Independent Practice" loading="lazy">
        </div>
        <div class="visual-accent-caption">
          <div class="visual-accent-badge">
            <span class="eyebrow-dot"></span>
            <span>CONNECTED OPHTHALMIC CARE</span>
          </div>
          <h4>Direct named-surgeon access without intermediate hospital call centres</h4>
          <p>Independent optometrists retain their patient relationship from primary triage through surgical co-management and 7-day electronic discharge.</p>
        </div>
      </div>
    </div>

    <div class="simple-bento-grid">
      <!-- Card 1: Direct Named-Surgeon Continuity & Access -->
      <div class="simple-bento-card">
        <div class="card-icon-bubble">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="8.5" cy="7" r="4"/><line x1="20" y1="8" x2="20" y2="14"/><line x1="23" y1="11" x2="17" y2="11"/></svg>
        </div>
        <span class="card-tag">DIRECT CONSULTANT LINE</span>
        <h3>Direct Named-Surgeon Continuity &amp; Access</h3>
        <p>Direct telephone and platform contact with the operating NHS consultant ophthalmologist for queries, triage, and patient continuity.</p>
        <div class="card-pill-row">
          <span class="card-pill">Named Consultant Access</span>
          <span class="card-pill">Direct Clinical Dialogue</span>
          <span class="card-pill">No Intermediaries</span>
        </div>
      </div>

      <!-- Card 2: Communication Through Dedicated Platform: Syndesis -->
      <div class="simple-bento-card">
        <div class="card-icon-bubble">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
        </div>
        <span class="card-tag">DEDICATED DIGITAL PLATFORM</span>
        <h3>Communication through a dedicated platform: Syndesis</h3>
        <p>Refer in under 2 minutes, upload scans securely, and track every patient milestone with real-time automated status updates.</p>
        <div class="card-pill-row">
          <span class="card-pill">Under 2-Min Submissions</span>
          <span class="card-pill">Real-Time Patient Tracker</span>
          <span class="card-pill">Secure Biometry &amp; OCT</span>
        </div>
      </div>

      <!-- Card 3: Complete Team Training & Support -->
      <div class="simple-bento-card">
        <div class="card-icon-bubble">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/></svg>
        </div>
        <span class="card-tag">PRACTICE EMPOWERMENT</span>
        <h3>Complete Team Training &amp; Support</h3>
        <p>Comprehensive 1-on-1 training for your optometrists and front-of-house team on using the Syndesis platform and tracking patients.</p>
        <div class="card-pill-row">
          <span class="card-pill">Practice Onboarding</span>
          <span class="card-pill">Front-of-House Triage</span>
          <span class="card-pill">1-on-1 Portal Demos</span>
        </div>
      </div>

      <!-- Card 4: Protected Patient Relationship & 7-Day Discharge -->
      <div class="simple-bento-card">
        <div class="card-icon-bubble">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
        </div>
        <span class="card-tag">PATIENT RETENTION GUARANTEE</span>
        <h3>Protected Patient Relationship &amp; 7-Day Discharge</h3>
        <p>Guaranteed electronic discharge within 7 days. Your patients return to your practice for post-op care, future refractions, and optical dispensing.</p>
        <div class="card-pill-row">
          <span class="card-pill">Electronic Discharge in 7 Days</span>
          <span class="card-pill">Post-op Biometry Shared</span>
          <span class="card-pill">Ongoing Optical Dispensing</span>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- STEP 3: 5-Step Connected Clinical Pathway -->
<section id="journey" class="section">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow-pill">
        <span class="eyebrow-dot"></span>
        CLINICAL PATHWAY
      </div>
      <h2>Five steps. Clear clinical boundaries.</h2>
      <p class="section-lead">A seamless co-management pathway designed so optometrists and consultant surgeons do exactly what each does best.</p>
    </div>

    <div class="pathway-track">
      <!-- Step 1 -->
      <div class="pathway-card">
        <div class="step-num">1</div>
        <div class="step-actor">YOUR PRACTICE</div>
        <h4>Patient Referral</h4>
        <p>Submit patient clinical details and biometry via the Syndesis portal in under 2 minutes.</p>
      </div>

      <!-- Step 2 -->
      <div class="pathway-card">
        <div class="step-num">2</div>
        <div class="step-actor">EYEPROS</div>
        <h4>Consultant Assessment</h4>
        <p>Pre-operative workup and informed consent conducted personally by the named surgeon.</p>
      </div>

      <!-- Step 3 -->
      <div class="pathway-card">
        <div class="step-num">3</div>
        <div class="step-actor">EYEPROS</div>
        <h4>Day-Case Surgery</h4>
        <p>Modern surgical episode performed in our surgical centre by your patient's named NHS consultant.</p>
      </div>

      <!-- Step 4 -->
      <div class="pathway-card">
        <div class="step-num">4</div>
        <div class="step-actor">EYEPROS &rarr; YOU</div>
        <h4>7-Day Discharge</h4>
        <p>Discharge summary, surgical notes, and medication plan transmitted securely within 7 days.</p>
      </div>

      <!-- Step 5 -->
      <div class="pathway-card">
        <div class="step-num">5</div>
        <div class="step-actor">YOUR PRACTICE</div>
        <h4>4-Week Co-Management</h4>
        <p>Conduct post-op review and new refraction. Submit completion report to receive your &pound;250 fee.</p>
      </div>
    </div>
  </div>
</section>

<!-- STEP 3: Consultant Leadership & Clinical Governance -->
<section id="consultants" class="section section-alt">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow-pill">
        <span class="eyebrow-dot"></span>
        CLINICAL LEADERSHIP &amp; GOVERNANCE
      </div>
      <h2>Led by substantive NHS Consultant Ophthalmologists</h2>
      <p class="section-lead">Direct named-surgeon continuity. You and your patient have direct contact with the operating consultant, underpinned by robust NHS clinical governance.</p>
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

      <!-- Ms Yasmine Abdalla: ROLE CHANGED TO MEDICAL DIRECTOR ONLY (CO-FOUNDER REMOVED) -->
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

    <!-- Governance Pillars -->
    <div class="gov-grid">
      <div class="gov-card">
        <h4>
          <svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
          Surgeon-Led Consent
        </h4>
        <p>Consent is taken personally by, or under direct supervision of, the operating consultant ophthalmologist.</p>
      </div>
      <div class="gov-card">
        <h4>
          <svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
          Named Consultant Contact
        </h4>
        <p>Direct communication channel with operating surgeons for clinical queries, triage, and patient updates.</p>
      </div>
      <div class="gov-card">
        <h4>
          <svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
          Substantive NHS Standards
        </h4>
        <p>All consultants hold active substantive NHS appointments with specialist royal college fellowship credentials.</p>
      </div>
      <div class="gov-card">
        <h4>
          <svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
          NOD Audit Governance
        </h4>
        <p>Full clinical adherence to National Ophthalmology Database audit standards and RCOphth clinical guidelines.</p>
      </div>
    </div>

    <!-- Governance Visual Strip -->
    <div class="gov-visual-strip">
      <div class="gov-visual-card">
        <img src="__SURGERY_IMG__" alt="State-of-the-art CQC Registered Surgical Facilities" loading="lazy">
        <div class="gov-visual-overlay">
          <span class="gov-visual-pill">SURGICAL GOVERNANCE</span>
          <h4>State-of-the-art day-case surgical facilities</h4>
          <p>CQC registered surgical centres compliant with the National Ophthalmology Database (NOD) audit and GMC Specialist Register standards.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- STEP 3: Trusted by Leading Independent Practices -->
<section id="trusted" class="section">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow-pill">
        <span class="eyebrow-dot"></span>
        ESTABLISHED PARTNERSHIPS
      </div>
      <h2>Trusted by Leading Independent Practices</h2>
      <p class="section-lead">Independent optometry practices across the East Midlands partner with EyePros to expand their clinical scope, preserve patient relationships, and deliver consultant-led surgical excellence.</p>
    </div>

    <!-- Pinders Featured Partner Card -->
    <div class="pinders-featured-card">
      <div class="pinders-logo-box">
        <img src="__PINDERS_SRC__" alt="Pinders Opticians Logo" loading="lazy">
      </div>
      <div class="pinders-featured-content">
        <div class="eyebrow-pill" style="margin-bottom:6px;padding:3px 9px;font-size:0.65rem">
          <span class="eyebrow-dot"></span>
          FOUNDING PARTNER PRACTICE
        </div>
        <h3>Pinders Opticians &mdash; Mansfield, Southwell &amp; Rufford</h3>
        <p class="pinders-quote">&ldquo;Partnering with EyePros Synergy has enabled our practice to offer our patients fast, consultant-led surgical care with the total certainty that they are discharged back to us for ongoing management. The &pound;250 co-management fee properly values our clinical chair time.&rdquo;</p>
      </div>
    </div>

    <!-- Smooth Infinite Logo Carousel -->
    <div class="partner-carousel-wrap">
      <div class="partner-carousel-track">
        <div class="partner-card">
          <div class="partner-logo-pill">
            <img src="__PINDERS_SRC__" alt="Pinders Opticians" loading="lazy">
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
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          </div>
          <div class="partner-meta">
            <strong>Nottinghamshire Eye Care</strong>
            <span>Accredited Practice Partner &bull; Nottingham</span>
          </div>
        </div>
        <div class="partner-card">
          <div class="partner-badge-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
          </div>
          <div class="partner-meta">
            <strong>Leicestershire Shared Care</strong>
            <span>Synergy Partner &bull; Leicester</span>
          </div>
        </div>
        <!-- Duplicated items for seamless marquee loop -->
        <div class="partner-card">
          <div class="partner-logo-pill">
            <img src="__PINDERS_SRC__" alt="Pinders Opticians" loading="lazy">
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
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          </div>
          <div class="partner-meta">
            <strong>Nottinghamshire Eye Care</strong>
            <span>Accredited Practice Partner &bull; Nottingham</span>
          </div>
        </div>
        <div class="partner-card">
          <div class="partner-badge-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
          </div>
          <div class="partner-meta">
            <strong>Leicestershire Shared Care</strong>
            <span>Synergy Partner &bull; Leicester</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- STEP 3: Transparent Remuneration & Interactive Calculator -->
<section id="remuneration" class="section section-alt">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow-pill">
        <span class="eyebrow-dot"></span>
        TRANSPARENT REMUNERATION
      </div>
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
              <span class="slider-value" id="calcSliderVal">4 patients / month</span>
            </div>
            <input type="range" min="1" max="20" value="4" class="calc-slider" id="cataractSlider" aria-label="Monthly Cataract Referrals">
          </div>

          <div class="calc-output-box">
            <div class="calc-output-label">ESTIMATED ANNUAL CO-MANAGEMENT FEES</div>
            <div class="calc-output-val" id="calcAnnualVal">&pound;12,000</div>
            <div class="calc-output-note">Direct shared-care revenue to your practice + 100% patient retention for eyewear.</div>
          </div>
        </div>
        <p style="font-size:0.74rem;color:var(--text-muted);text-align:center;margin-top:12px">Based on flat &pound;250/eye cataract co-management remuneration.</p>
      </div>
    </div>

    <!-- 6 Additional Fee Cards -->
    <div class="fees-grid">
      <!-- 1: Insurance Patients -->
      <div class="fee-card">
        <span class="fee-category">INSURANCE PATIENTS</span>
        <div class="fee-amount-box">
          <span class="fee-upto">UP TO</span>
          <span class="fee-val">&pound;100</span>
        </div>
        <h4>Private Medical Insurance</h4>
        <p>Covered under insurer fee schedules for insured episodes and post-operative assessment.</p>
      </div>

      <!-- 2: Glaucoma/MIGS -->
      <div class="fee-card">
        <span class="fee-category">GLAUCOMA / MIGS</span>
        <div class="fee-amount-box">
          <span class="fee-upto">UP TO</span>
          <span class="fee-val">&pound;100</span>
        </div>
        <h4>Minimally Invasive Glaucoma Surgery</h4>
        <p>Post-operative pressure checks and bleb monitoring for MIGS and iStent procedures.</p>
      </div>

      <!-- 3: Laser -->
      <div class="fee-card">
        <span class="fee-category">LASER TREATMENT</span>
        <div class="fee-amount-box">
          <span class="fee-upto-spacer">UP TO</span>
          <span class="fee-val">&pound;95</span>
        </div>
        <h4>YAG Capsulotomy &amp; SLT Laser</h4>
        <p>Flat fee per eye for YAG posterior capsulotomy, peripheral iridotomy, and SLT episodes.</p>
      </div>

      <!-- 4: Valeda Treatment -->
      <div class="fee-card">
        <span class="fee-category">DRY AMD THERAPY</span>
        <div class="fee-amount-box">
          <span class="fee-upto-spacer">UP TO</span>
          <span class="fee-val">&pound;150</span>
          <span class="fee-cycle">/course</span>
        </div>
        <h4>Valeda Photobiomodulation</h4>
        <p>Multi-session light therapy course for dry age-related macular degeneration (Dry AMD).</p>
      </div>

      <!-- 5: EyeSpa -->
      <div class="fee-card">
        <span class="fee-category">DRY EYE CLINIC</span>
        <div class="fee-amount-box">
          <span class="fee-upto-spacer">UP TO</span>
          <span class="fee-val">&pound;120</span>
          <span class="fee-cycle">/course</span>
        </div>
        <h4>EyeSpa Advanced Ocular Surface</h4>
        <p>Dedicated clinical course for meibomian gland dysfunction, blepharitis, and severe dry eye.</p>
      </div>

      <!-- 6: Lacryfill -->
      <div class="fee-card">
        <span class="fee-category">PUNCTAL OCCLUSION</span>
        <div class="fee-amount-box">
          <span class="fee-upto-spacer">UP TO</span>
          <span class="fee-val">&pound;60</span>
        </div>
        <h4>Lacryfill Cross-Linked HA</h4>
        <p>Advanced cross-linked hyaluronic acid punctal occlusion for chronic ocular surface disease.</p>
      </div>
    </div>

    <!-- Shared Care Agreement Banner -->
    <div class="agreement-banner">
      <div class="agreement-content">
        <h3>Receive a copy of our Shared Care Agreement</h3>
        <p>Review the full legal framework, clinical governance protocols, indemnities, and transparent payment schedules. Governed by English law.</p>
      </div>
      <div class="agreement-actions">
        <a href="#partner-enquiry" class="btn btn-agreement-white">Request Agreement Copy</a>
        <a href="tel:03337727277" class="btn btn-secondary">0333 77 272 77</a>
      </div>
    </div>
  </div>
</section>

<!-- STEP 3: Practice Registration Form & Direct Helpline -->
<section id="partner-enquiry" class="section">
  <div class="container">
    <div class="enquiry-layout">
      <!-- Registration Card -->
      <div class="enquiry-card">
        <div class="enquiry-header">
          <div class="eyebrow-pill">
            <span class="eyebrow-dot"></span>
            PRACTICE REGISTRATION
          </div>
          <h2>Become an EyePros Synergy Partner</h2>
          <p>Join independent optometry practices across the Midlands delivering consultant-led surgical excellence and protected patient continuity.</p>
        </div>

        <form id="partnerForm" class="form-grid">
          <div class="form-row">
            <div class="form-group">
              <label for="practiceName">Practice Name *</label>
              <input type="text" id="practiceName" name="practiceName" placeholder="e.g. Vision Care Opticians" required>
            </div>
            <div class="form-group">
              <label for="practicePostcode">Practice Postcode *</label>
              <input type="text" id="practicePostcode" name="practicePostcode" placeholder="e.g. NG1 1AA" required>
            </div>
          </div>

          <div class="form-row">
            <div class="form-group">
              <label for="contactName">Contact Name *</label>
              <input type="text" id="contactName" name="contactName" placeholder="Lead Optometrist / Practice Manager" required>
            </div>
            <div class="form-group">
              <label for="gocNumber">GOC Number (Optional)</label>
              <input type="text" id="gocNumber" name="gocNumber" placeholder="e.g. 01-12345">
            </div>
          </div>

          <div class="form-row">
            <div class="form-group">
              <label for="email">Email Address *</label>
              <input type="email" id="email" name="email" placeholder="practice@example.co.uk" required>
            </div>
            <div class="form-group">
              <label for="phone">Phone Number *</label>
              <input type="tel" id="phone" name="phone" placeholder="0115 ... or 07..." required>
            </div>
          </div>

          <div class="form-group">
            <label for="interests">Primary Clinical Interests</label>
            <select id="interests" name="interests" class="form-select">
              <option value="cataract">Cataract &amp; Premium Lens Co-Management (&pound;250 fee)</option>
              <option value="laser">YAG &amp; SLT Laser Co-Management (&pound;95 fee)</option>
              <option value="glaucoma">Glaucoma / MIGS Co-Management (&pound;100 fee)</option>
              <option value="dry-eye">Dry Eye Spa &amp; Valeda Photobiomodulation</option>
              <option value="all">Full Comprehensive Shared Care Portfolio</option>
            </select>
          </div>

          <div class="form-group">
            <label for="notes">Additional Comments or Questions</label>
            <textarea id="notes" name="notes" placeholder="Tell us about your practice, current patient volume, or Syndesis onboarding preferences..."></textarea>
          </div>

          <button type="submit" class="btn btn-primary" id="submitBtn" style="width:100%;padding:11px 20px">
            <span>Submit Partnership Enquiry &amp; Receive Agreement</span>
            <svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd"/></svg>
          </button>

          <div id="formSuccess" style="display:none;text-align:center;padding:24px 16px">
            <div style="width:46px;height:46px;border-radius:50%;background:var(--ep-teal-tint);color:var(--ep-teal-bright);display:flex;align-items:center;justify-content:center;margin:0 auto 12px">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="width:24px;height:24px"><polyline points="20 6 9 17 4 12"/></svg>
            </div>
            <h3 style="color:var(--text-white);margin-bottom:6px">Registration Received</h3>
            <p style="color:var(--text-body);font-size:0.86rem">Thank you. Our partnership team will review your practice details and send a copy of our Shared Care Agreement and Syndesis onboarding information within 1 business day.</p>
          </div>
        </form>
      </div>

      <!-- Direct Clinical Helpline Card -->
      <div class="contact-card">
        <h3>Direct Clinical Helpline</h3>
        <p>Speak directly with our partnership director or clinical lead regarding clinical protocols, patient suitability, and Syndesis onboarding.</p>

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
              <span>Option 5 (Clinician-to-Clinician)</span>
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

<!-- STEP 3: FAQ Accordion -->
<section id="faq" class="section section-alt">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow-pill">
        <span class="eyebrow-dot"></span>
        FREQUENTLY ASKED QUESTIONS
      </div>
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

<!-- STEP 5: Mobile Sticky Partnership CTA -->
<div class="mobile-sticky-cta" id="mobileStickyCta">
  <div class="mobile-sticky-inner">
    <div class="mobile-sticky-text">
      <strong>EyePros Synergy</strong>
      <span>&pound;250 Co-Management &bull; 7-Day Return</span>
    </div>
    <a href="#partner-enquiry" class="btn btn-primary btn-sm">Become a Partner</a>
  </div>
</div>

<script>
// Sticky Navbar scroll transition
var mainNav = document.getElementById('mainNav');
window.addEventListener('scroll', function() {
  if (window.scrollY > 25) {
    mainNav.classList.add('scrolled');
  } else {
    mainNav.classList.remove('scrolled');
  }
});

// Mobile Drawer Toggle
var navToggle = document.getElementById('navToggle');
var navLinks = document.getElementById('navLinks');
if (navToggle && navLinks) {
  navToggle.addEventListener('click', function(e) {
    e.stopPropagation();
    navLinks.classList.toggle('active');
  });
  document.addEventListener('click', function(e) {
    if (!navLinks.contains(e.target) && !navToggle.contains(e.target)) {
      navLinks.classList.remove('active');
    }
  });
  var links = navLinks.querySelectorAll('a');
  links.forEach(function(l) {
    l.addEventListener('click', function() {
      navLinks.classList.remove('active');
    });
  });
}

// Interactive Revenue Calculator (£250 * patients * 12 months)
var slider = document.getElementById('cataractSlider');
var sliderVal = document.getElementById('calcSliderVal');
var annualVal = document.getElementById('calcAnnualVal');
if (slider && sliderVal && annualVal) {
  slider.addEventListener('input', function() {
    var count = parseInt(this.value, 10);
    sliderVal.textContent = count + (count === 1 ? ' patient / month' : ' patients / month');
    var total = count * 250 * 12;
    annualVal.textContent = '£' + total.toLocaleString('en-GB');
  });
}

// Interactive FAQ Accordion
var faqItems = document.querySelectorAll('.faq-item');
faqItems.forEach(function(item) {
  var btn = item.querySelector('.faq-q');
  if (btn) {
    btn.addEventListener('click', function() {
      var isOpen = item.classList.contains('open');
      faqItems.forEach(function(other) { other.classList.remove('open'); });
      if (!isOpen) {
        item.classList.add('open');
      }
    });
  }
});

// Interactive Partner Registration Form Submission
var partnerForm = document.getElementById('partnerForm');
var formSuccess = document.getElementById('formSuccess');
var submitBtn = document.getElementById('submitBtn');
if (partnerForm && formSuccess && submitBtn) {
  partnerForm.addEventListener('submit', function(e) {
    e.preventDefault();
    submitBtn.disabled = true;
    submitBtn.innerHTML = 'Submitting Practice Details...';
    setTimeout(function() {
      partnerForm.reset();
      submitBtn.style.display = 'none';
      formSuccess.style.display = 'block';
    }, 700);
  });
}

// Active navigation highlight on scroll
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
}, { threshold: 0.25 });
sections.forEach(function(sec) { observer.observe(sec); });

// Smooth scrolling with exact header offset
document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
  anchor.addEventListener('click', function (e) {
    var targetId = this.getAttribute('href');
    if (targetId === '#') return;
    var targetEl = document.querySelector(targetId);
    if (targetEl) {
      e.preventDefault();
      var navHeight = mainNav ? mainNav.offsetHeight : 70;
      var elPos = targetEl.getBoundingClientRect().top + window.pageYOffset;
      window.scrollTo({
        top: elPos - navHeight - 12,
        behavior: 'smooth'
      });
    }
  });
});
</script>
</body>
</html>"""

    html = template
    html = html.replace('__LOGO_SRC__', l_src)
    html = html.replace('__HERO_IMG__', hero_img)
    html = html.replace('__OPTOM_IMG__', optom_img)
    html = html.replace('__SURGERY_IMG__', surgery_img)
    html = html.replace('__AHMAD_SRC__', a_src)
    html = html.replace('__YASMINE_SRC__', y_src)
    html = html.replace('__PINDERS_SRC__', p_src)
    return html

# Generate synergy-wix-embed.html (fully self-contained with base64 for Wix iframe)
with open("synergy-wix-embed.html", "w", encoding="utf-8") as f:
    f.write(build_page(is_embed=True))

# Generate synergy-landing-page.html (standalone relative image links)
with open("synergy-landing-page.html", "w", encoding="utf-8") as f:
    f.write(build_page(is_embed=False))

print("Successfully regenerated synergy-wix-embed.html and synergy-landing-page.html with Hero Cover & updated branding!")
