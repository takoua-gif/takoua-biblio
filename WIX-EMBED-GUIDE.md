# EyePros Synergy — Wix Embed & Integration Guide

This guide provides step-by-step instructions for embedding and publishing the **Synergy by EyePros** B2B Shared Care Partnership page on your Wix website ([eyepros.co.uk](https://www.eyepros.co.uk)).

---

## 1. Quick Reference & Embed Assets

| Asset / Method | Value / Link | Description |
| :--- | :--- | :--- |
| **Embed Target URL** | `https://takoua-gif.github.io/takoua-biblio/synergy-wix-embed.html` | Optimized for iframes (hosted on GitHub Pages, upright dark logo, restored consultants) |
| **Standalone Page** | `https://takoua-gif.github.io/takoua-biblio/synergy-landing-page.html` | Full standalone landing page with local asset fallbacks |
| **Target Page on Wix** | `https://www.eyepros.co.uk/synergy` | Recommended URL slug on your domain |
| **Form Destination** | `practice@eyepros.co.uk` | Automated partner enquiry delivery |
| **Urgent Clinical Contact** | `0333 77 272 77 (Option 5)` | 24/7 escalation helpline featured in hero & footer |

---

## 2. Option A: "Embed a Site" (Recommended Method)

This is the cleanest and easiest method in Wix. Wix renders the hosted page inside a dedicated container with no code conflicts.

### Step 1: Create a Dedicated Page in Wix
1. Log into your **Wix Dashboard** and open the **Wix Editor**.
2. Click **Pages & Menu** (icon on left sidebar).
3. Click **+ Add Page** &rarr; select **Blank Page**.
4. Rename the page to **Synergy** (Page URL: `/synergy`).
5. Open the page **Settings** &rarr; **Layouts** tab &rarr; select **No Header & Footer** (this ensures the sleek dark-mode Synergy navigation and footer display without double headers).

### Step 2: Add the Embed Widget
1. Click **+ Add Elements** (top left of editor).
2. Navigate to **Embed Code** &rarr; **Embed a Site** (or **Website Address**).
3. Drag the widget onto your blank page.
4. Click **Enter Website Address** (or **Settings**).
5. Paste the exact URL:
   ```text
   https://takoua-gif.github.io/takoua-biblio/synergy-wix-embed.html
   ```
6. Click **Apply**.

### Step 3: Size the Container
1. Click the **Stretch** icon on the embed widget and select **Full Width**.
2. Drag the bottom resize handle down to expand the container height (recommended: `~4,500px` to fit all sections from Hero through FAQ without a nested scrollbar).
3. Click **Preview** to verify smooth scrolling, then **Publish**.

---

## 3. Option B: "HTML iframe / Code" (HTML Embed Snippet)

If you prefer using Wix’s **HTML Code** element (or if embedding on WordPress, Squarespace, or Webflow), use this snippet.

### Embed Code Snippet

```html
<!-- EyePros Synergy Shared Care Partnership Embed -->
<div style="width: 100%; min-height: 100vh; overflow: hidden; background: #1C192E;">
  <iframe 
    id="synergy-partnership-frame"
    src="https://takoua-gif.github.io/takoua-biblio/synergy-wix-embed.html" 
    title="Synergy by EyePros - Shared Care Partnership"
    width="100%" 
    height="4600px" 
    style="width: 100%; height: 4600px; border: none; display: block; overflow: hidden;" 
    loading="lazy"
    allow="clipboard-write">
  </iframe>
</div>
```

### Steps in Wix:
1. In the Wix Editor, click **+ Add Elements** &rarr; **Embed Code** &rarr; **Embed HTML**.
2. Click **Enter Code** and paste the snippet above into the code field.
3. Click **Update**.
4. Stretch the element to **Full Width** and adjust the height to match the frame.

---

## 4. Mobile Layout Optimization in Wix

Because Wix has a separate **Mobile Editor**, verify the mobile layout before final publishing:

1. Switch to the **Mobile Editor** (phone icon in top Wix toolbar).
2. Click on the embedded Synergy element.
3. Ensure the width is set to **100% of mobile width**.
4. Drag the bottom height handle down. On mobile, cards stack vertically, so the height required will be approximately `5,200px - 5,600px`.
5. Preview in mobile mode:
   - Check the **Synergy upright logo** in the header.
   - Check the **Mobile Sticky CTA Bar** ("Become Partner") at the bottom of the viewport.
   - Verify both consultant surgeon cards (**Mr Ahmad Elsahn** and **Ms Yasmine Abdalla**) stack cleanly.

---

## 5. Connecting Form Submissions to Your Inbox

The partner enquiry form at `#partner-enquiry` is pre-configured to deliver directly to:
**`practice@eyepros.co.uk`**

### First-Time Activation Step:
The form uses the secure `FormSubmit.co` AJAX gateway:
1. When the first enquiry is submitted from your live website, an activation email from FormSubmit is sent to `practice@eyepros.co.uk`.
2. Click the **"Activate Form"** link in that email once.
3. From then on, every partner submission will instantly arrive as a structured email table in your inbox, containing:
   - Full Name & Practice Name
   - Practice Postcode
   - Email Address & Phone Number
   - Number of Resident Optometrists
   - Message / Onboarding Request

---

## 6. How to Sync Local Updates to GitHub Pages

Whenever page content, styling, or logos are updated locally on your computer, push the changes to GitHub so the live Wix embed updates automatically:

### Method 1: VS Code (One-Click)
1. Open **VS Code**.
2. Click the **Source Control** icon on the left sidebar (shortcut: `Ctrl+Shift+G` or `Cmd+Shift+G`).
3. Click the blue **Sync Changes** (or **Push**) button.

### Method 2: Terminal Command
Run this command from the repository root:
```bash
git push origin main
```

> [!NOTE]
> GitHub Pages usually takes **30–60 seconds** to refresh the live site after a push. You can verify it immediately by visiting `https://takoua-gif.github.io/takoua-biblio/synergy-wix-embed.html` in an Incognito window.

---

## 7. Features Included in this Embed

- **Upright Synergy Dark Logo**: Matches the page background `#1C192E` with crisp inline base64 fallback.
- **Consultant Leadership Restored**: Complete cards with professional portraits for Managing Director **Mr Ahmad Elsahn** and Clinical Director **Ms Yasmine Abdalla**, subspecialties, and NHS appointments.
- **Simplified Agreement CTA**: Single clean button &mdash; **"Request a copy of the Partnership Agreement"** &mdash; that smoothly navigates to the enquiry form.
- **4-Card Fee Schedule**: Cataract (£250/eye), PMI (£100/procedure), MIGS (£100/procedure), and Laser (£90/eye).
- **Direct Consultant Escalation**: Dedicated urgent line `0333 77 272 77 (Option 5)` and Syndesis portal integration.
- **Interactive FAQ Accordion**: Instant answers to optometrist questions without page reload.
