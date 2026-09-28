# Synergy Landing Page — Developer Handoff

## Repository
**https://github.com/takoua-gif/takoua-biblio**

The Synergy B2B landing page is in `synergy-landing-page.html` (single file, self-contained).

---

## File Structure

```
synergy-landing-page.html     ← Complete page (HTML + CSS + JS in one file)
images/
  optometrist-partners.jpg    ← Hero section
  patient-exam.jpg            ← Positioning section
  elsahn-headshot.jpg         ← Consultant card (placeholder — needs real photo)
  abdalla-headshot.jpg        ← Consultant card (placeholder — needs real photo)
  hero-clinic.jpg             ← Treatments banner
  oct-scan.jpg                ← Form sidebar
  partner-pinders.png         ← Partner logo (Pinders)
```

---

## What the Developer Needs To Do

### 1. Replace Placeholders `[CONFIRM ...]`

Search the file for `[CONFIRM` — there are **11 placeholders** that need real content before launch:

| Placeholder | Line | What's needed |
|---|---|---|
| `[CONFIRM TEAM LOGINS]` | ~567 | Confirm if Syndesis supports multi-user team access |
| `[CONFIRM SHARED CARE PROTOCOL]` | ~631 | Link to downloadable shared care protocol PDF |
| `[CONFIRM PRIVATE MEDICAL RETINA SERVICES]` | ~714 | List of private medical retina services offered |
| `[CONFIRM LEICESTER VENUE]` | ~753 | Confirm the Leicester clinic venue name |
| `[CONFIRM URGENT CONTACT ROUTE]` | ~803 | How optometrists reach the consultant urgently |
| `[CONFIRM SYNDESIS FEATURES]` | ~823 | Specific Syndesis features to highlight |
| `[CONFIRM TIMING]` | ~901 | Response time after form submission (e.g. "within 48 hours") |
| `[CONFIRM CONTACT NAME]` | ~920 | Name of the Synergy contact person |
| `[CONFIRM ROLE]` | ~921 | Their job title |
| `[CONFIRM PHONE]` | ~922 | Contact phone number |
| `[CONFIRM SYNERGY EMAIL]` | ~923 | Contact email address |

### 2. Connect the Partner Form

The form at the bottom (id: `partnerForm`) currently uses a **demo stub** that simulates submission. 

**Find this function** (~line 1182):
```js
function submitToBackend(data) { ... }
```

**Replace it** with a real API call to your CRM/email endpoint:
```js
function submitToBackend(data) {
  return fetch('https://your-api.eyepros.co.uk/synergy-partner', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  }).then(function(r) { if (!r.ok) throw new Error(r.status); return r.json(); });
}
```

### 3. Connect Analytics

Search for `track(` — there are analytics stubs throughout the JS. Connect them to your analytics provider (GA4, GTM, etc.):

```js
// Current stub (~line 976):
function track(event, data) {
  console.log('[SYNERGY ANALYTICS]', event, data || '');
}

// Replace with e.g.:
function track(event, data) {
  gtag('event', event, data || {});
}
```

**Events tracked:** `nav_click`, `hero_cta_click`, `faq_toggle`, `partner_form_submit`, `partner_form_success`, `partner_form_error`, `partner_form_validation_error`

### 4. Replace Placeholder Images

- `elsahn-headshot.jpg` — Replace with real photo of Mr Ahmad Elsahn
- `abdalla-headshot.jpg` — Replace with real photo of Ms Yasmine Abdalla
- All other images are stock/generated — replace with branded EyePros photography if available

### 5. Links to Update

- **Privacy policy link** (~line 894): Currently `href="#"` — point to real privacy policy
- **Partner login button** (~line 571): Currently `href="#"` — point to Syndesis login URL
- **Footer links** (~lines 942-962): "Syndesis Login", "Shared Care Protocol" etc. need real URLs

---

## Integration into Wix (eyepros.co.uk)

The EyePros website is built on **Wix**. There are three ways to add this page:

### Option A: Embed via HTML iframe (Simplest)
1. Host `synergy-landing-page.html` and the `images/` folder on any static host (GitHub Pages, Netlify, Vercel, or Wix's own file hosting)
2. In the Wix Editor, add a **new blank page** at `/synergy`
3. Add an **"Embed HTML"** element (Add → Embed → HTML iframe)
4. Set it to **full width and full height** of the page
5. Point the iframe `src` to the hosted HTML file
6. Hide Wix's default header/footer on this page if the Synergy page has its own

> **Pros**: Zero code conflicts, page works exactly as built.  
> **Cons**: Separate scroll context inside iframe, SEO is limited.

### Option B: Custom Code via Wix Velo
1. In the Wix Editor, create a new page at `/synergy`
2. Go to **Dev Mode → Turn on Velo**
3. In the page's `masterPage.js` or a custom element, paste the full HTML
4. Use Wix's **Custom Element** or **HtmlComponent** API to render the page
5. Move CSS and JS into Wix's code panel

> **Pros**: Native Wix page, better SEO, shared header/footer.  
> **Cons**: Requires Velo experience, potential CSS conflicts with Wix styles.

### Option C: External Landing Page (Recommended)
1. Deploy `synergy-landing-page.html` to **GitHub Pages, Netlify, or Vercel** as a standalone site
2. Set up a **subdomain**: `synergy.eyepros.co.uk` pointing to the hosted page
3. Or use Wix's **URL redirect**: `/synergy` → external hosted URL

> **Pros**: Fully independent, no Wix limitations, fastest performance, clean URL.  
> **Cons**: Separate from main site (but this is a standalone B2B landing page, so that's fine).

### How to Enable GitHub Pages (Free Hosting)
1. Go to **https://github.com/takoua-gif/takoua-biblio/settings/pages**
2. Source: **Deploy from a branch**
3. Branch: **main**, folder: **/ (root)**
4. Click **Save**
5. Page will be live at: `https://takoua-gif.github.io/takoua-biblio/synergy-landing-page.html`
6. Optionally point `synergy.eyepros.co.uk` to this via DNS CNAME

---

## Technical Notes

- **No dependencies** — pure HTML, CSS, vanilla JS. No frameworks, no build step.
- **Font**: Inter (loaded from Google Fonts CDN)
- **Responsive breakpoints**: 1024px (tablet), 768px (mobile)
- **Accessibility**: ARIA attributes on FAQ, form validation, focus-visible styles, reduced-motion support
- **Print styles**: Nav/footer hidden, dark backgrounds removed
- **Form validation**: Client-side with inline error messages
- **Scroll animations**: IntersectionObserver-based reveal with staggered children

---

## Business Logic — Important

**There are NO referral fees.** The Synergy model is:
1. Optometrist refers a patient via Syndesis
2. EyePros consultant treats the patient
3. If additional diagnostics are needed from the optometrist, **EyePros covers the cost for the patient**
4. Patient returns to the optometrist for the post-op
5. Optometrist uploads post-op findings and feedback to Syndesis
6. The optometrist can track the full patient journey through Syndesis

The value to the optometrist is **clinical involvement, patient retention, and visibility** — not payment.
