# Synergy Landing Page — Developer Handoff (Aligned with Partner Deck v2.2)

## Repository
**https://github.com/takoua-gif/takoua-biblio**

The Synergy B2B landing page is located in `synergy-landing-page.html`. It is a self-contained, high-performance HTML/CSS/JS file designed for easy integration into Wix or hosting as a dedicated subdomain.

---

## File Structure

```
synergy-landing-page.html     ← Complete page (HTML + CSS + JS in one file)
images/
  optometrist-partners.jpg    ← Hero section
  partner-pinders.png         ← Trusted partner logo (Pinders Opticians)
  patient-exam.jpg            ← Slit lamp examination
  hero-clinic.jpg             ← Surgical theatre suite
  oct-scan.jpg                ← Diagnostic OCT scan
```

---

## Core Content & Clinical Governance (Exact Source of Truth)

The page has been completely rewritten to align with the **EyePros Synergy Shared Care Agreement v2.2**:

1. **The 3 Core Questions**:
   - *Will I know what happened?* Structured discharge letters within 48 hours via Syndesis.
   - *Can I reach the surgeon if I am worried?* Direct consultant access + 24/7 Urgent Clinical Helpline (`0333 77 272 77 Option 5`).
   - *Will my patient come back to me?* Protected 4-week review and un-tiered clinical shared care fee.
2. **The 5-Step Shared Care Pathway**:
   - Step 1: Your Practice — Assess (clinical workup and options counseling).
   - Step 2: Your Practice — Refer (Syndesis, GOS 18, practice software).
   - Step 3: EyePros — Consent & Treat (consultant-led consent, surgery, NOD audits).
   - Step 4: EyePros — Report Back (48h discharge letter, emergency number).
   - Step 5: Your Practice — Follow Up (4-week review within 5 working days, fee released).
3. **Transparent Remuneration**:
   - Self-pay & Finance (Cataract/Lens): Up to £250 per eye.
   - Private Medical Insurance: Up to £100 per procedure (subject to insurer schedule).
   - MIGS: Up to £100 per procedure.
   - YAG / SLT: Up to £90 per eye.
   - Safeguards: No tiers, not linked to volume. Patient choice comes first.
4. **Clinical Safety & Complications**:
   - EyePros retains full responsibility for managing surgical complications (including re-operation).
   - Clear red flags listed for immediate escalation.
5. **Locations**:
   - 4 Midlands locations: Loughborough, Nottingham, Leicester, Derby.
6. **Agreement Terms**:
   - 6 weeks written notice to step away (measured from last referral).

---

## How to Integrate into Wix (`eyepros.co.uk`)

### Method A: Standalone Subdomain (Recommended)
1. Enable **GitHub Pages** on this repo (Settings → Pages → Branch: `main` → `/ (root)`).
2. The page is immediately live at: `https://takoua-gif.github.io/takoua-biblio/synergy-landing-page.html`
3. Point `synergy.eyepros.co.uk` via DNS CNAME to the GitHub Pages URL, or add a 301 redirect in Wix from `/synergy` to this URL.

### Method B: Rebuild in Wix Editor (Native)
Use `synergy-landing-page.html` as the visual and copy blueprint. Copy each section's headlines, paragraphs, and tables into Wix components:
- **Navy**: `#0F2B4C` | `#0A1F38`
- **Teal**: `#0D9488` | `#0B7B72` | `#F0FDFA`
- **Font**: Inter (Google Fonts / Wix library)

### Method C: Wix Embed HTML
1. In Wix Editor, add a blank page at `/synergy`.
2. Add an **Embed HTML** component (set to 100% width and full height).
3. Paste the code or point to the hosted URL.

---

## Form Connection

The registration form on the page is currently hooked to a client-side success handler. To connect it to your CRM or backend:
- Find `id="partnerForm"`.
- Replace the inline submission handler with an AJAX POST or connect to Wix Forms / HubSpot / your practice endpoint (`practice@eyepros.co.uk`).
