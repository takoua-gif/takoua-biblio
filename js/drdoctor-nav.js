/**
 * EyePros Strategic Playbook — DrDoctor-Inspired Navigation Engine
 * Injects the floating capsule header, mega-menus, mobile drawer, and active page detection.
 */

(function () {
  'use strict';

  const NAV_HTML = `
  <header class="drd-header-wrapper" id="drdHeaderWrapper">
    <nav class="drd-nav-capsule" id="drdNavCapsule">
      <!-- Brand Logo -->
      <a href="index.html" class="drd-brand">
        <div class="drd-brand-mark">👁</div>
        <div>
          <span>EyePros</span>
          <span class="drd-brand-sub">Playbook</span>
        </div>
      </a>

      <!-- Desktop Navigation Menu with Mega-Menus -->
      <ul class="drd-nav-menu">
        <!-- 1. Home -->
        <li class="drd-nav-item" data-nav="home">
          <a href="index.html" class="drd-nav-link">Home</a>
        </li>

        <!-- 2. Patient Pathways (Mega-Menu) -->
        <li class="drd-nav-item" data-nav="patient-pathways">
          <a href="patient-pathways.html" class="drd-nav-link">
            Patient Pathways
            <svg width="10" height="10" viewBox="0 0 12 12" fill="none">
              <path d="M2.5 4.5L6 8L9.5 4.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </a>
          
          <div class="drd-mega-dropdown" style="grid-template-columns: repeat(3, 1fr) 260px; width: 920px;">
            <div class="drd-mega-col">
              <h4>Surgical Pathways</h4>
              <ul class="drd-mega-list">
                <li class="drd-mega-item">
                  <a href="patient-pathways.html">
                    <span class="drd-mega-title">Archetype A · Cataracts</span>
                    <span class="drd-mega-desc">Volume surgery &amp; premium multifocal IOLs</span>
                  </a>
                </li>
                <li class="drd-mega-item">
                  <a href="patient-pathways.html">
                    <span class="drd-mega-title">Archetype C · Refractive</span>
                    <span class="drd-mega-desc">LASIK, SMILE &amp; implantable collamer lens</span>
                  </a>
                </li>
              </ul>
            </div>

            <div class="drd-mega-col">
              <h4>Chronic &amp; Wellness</h4>
              <ul class="drd-mega-list">
                <li class="drd-mega-item">
                  <a href="patient-pathways.html">
                    <span class="drd-mega-title">Archetype B · Glaucoma</span>
                    <span class="drd-mega-desc">Micro-stents (MIGS) &amp; care subscriptions</span>
                  </a>
                </li>
                <li class="drd-mega-item">
                  <a href="patient-pathways.html">
                    <span class="drd-mega-title">Archetype D · EyeSpa</span>
                    <span class="drd-mega-desc">Dry eye rehabilitation &amp; IPL therapy</span>
                  </a>
                </li>
                <li class="drd-mega-item">
                  <a href="patient-pathways.html">
                    <span class="drd-mega-title">Archetype E · Valeda AMD</span>
                    <span class="drd-mega-desc">Photobiomodulation for dry macula</span>
                  </a>
                </li>
              </ul>
            </div>

            <div class="drd-mega-col">
              <h4>Referral Tools</h4>
              <ul class="drd-mega-list">
                <li class="drd-mega-item">
                  <a href="patient-pathways.html">
                    <span class="drd-mega-title">5-Stage Patient Journey</span>
                    <span class="drd-mega-desc">Detection to shared care discharge</span>
                  </a>
                </li>
                <li class="drd-mega-item">
                  <a href="patient-pathways.html">
                    <span class="drd-mega-title">Optom Conversion Drivers</span>
                    <span class="drd-mega-desc">Overcoming NHS hospital queue friction</span>
                  </a>
                </li>
              </ul>
            </div>

            <!-- Featured Promo Box -->
            <a href="patient-pathways.html" class="drd-mega-featured">
              <div>
                <span class="drd-badge drd-badge-teal mb-2" style="font-size: 0.65rem;">Clinical Focus</span>
                <h5>Named Consultant Care</h5>
                <p>How Mr Ahmad Elsahn's substantive NHS credentials create the ultimate trust bridge.</p>
              </div>
              <span class="drd-link-arrow">Explore Pathways &rarr;</span>
            </a>
          </div>
        </li>

        <!-- 3. Market & Numbers (Mega-Menu) -->
        <li class="drd-nav-item" data-nav="market-numbers">
          <a href="market-numbers.html" class="drd-nav-link">
            Market &amp; Numbers
            <svg width="10" height="10" viewBox="0 0 12 12" fill="none">
              <path d="M2.5 4.5L6 8L9.5 4.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </a>

          <div class="drd-mega-dropdown" style="grid-template-columns: repeat(3, 1fr) 260px; width: 920px;">
            <div class="drd-mega-col">
              <h4>Demand &amp; Macro</h4>
              <ul class="drd-mega-list">
                <li class="drd-mega-item">
                  <a href="market-numbers.html">
                    <span class="drd-mega-title">Macro Demand KPIs</span>
                    <span class="drd-mega-desc">450k cataracts &amp; 7.11m backlog</span>
                  </a>
                </li>
                <li class="drd-mega-item">
                  <a href="market-numbers.html">
                    <span class="drd-mega-title">Regional Stakeholder Map</span>
                    <span class="drd-mega-desc">LOCs, ICBs &amp; Trust relationships</span>
                  </a>
                </li>
              </ul>
            </div>

            <div class="drd-mega-col">
              <h4>Competitive Strategy</h4>
              <ul class="drd-mega-list">
                <li class="drd-mega-item">
                  <a href="market-numbers.html">
                    <span class="drd-mega-title">5 Competitor Tiers</span>
                    <span class="drd-mega-desc">NHS volume hubs to private soloists</span>
                  </a>
                </li>
                <li class="drd-mega-item">
                  <a href="market-numbers.html">
                    <span class="drd-mega-title">Self-Pay Pricing Benchmarks</span>
                    <span class="drd-mega-desc">Procedure tariff comparison</span>
                  </a>
                </li>
              </ul>
            </div>

            <div class="drd-mega-col">
              <h4>Strategy Models</h4>
              <ul class="drd-mega-list">
                <li class="drd-mega-item">
                  <a href="market-numbers.html">
                    <span class="drd-mega-title">SWOT Analysis</span>
                    <span class="drd-mega-desc">Internal strengths vs corporate threats</span>
                  </a>
                </li>
                <li class="drd-mega-item">
                  <a href="market-numbers.html">
                    <span class="drd-mega-title">9-Box Business Model</span>
                    <span class="drd-mega-desc">Kingfisher House Hospital BMC</span>
                  </a>
                </li>
                <li class="drd-mega-item">
                  <a href="market-numbers.html">
                    <span class="drd-mega-title">Market Watchlist</span>
                    <span class="drd-mega-desc">Policy, competitor moves &amp; M&amp;A</span>
                  </a>
                </li>
              </ul>
            </div>

            <!-- Featured Promo Box -->
            <a href="market-numbers.html" class="drd-mega-featured">
              <div>
                <span class="drd-badge drd-badge-copper mb-2" style="font-size: 0.65rem;">Market Insight</span>
                <h5>898k Private Admissions</h5>
                <p>Self-pay cataract procedures grew +12.4% as NHS waits exceed 26 weeks.</p>
              </div>
              <span class="drd-link-arrow">View Analysis &rarr;</span>
            </a>
          </div>
        </li>

        <!-- 4. Business Plan EyePros (Mega-Menu) -->
        <li class="drd-nav-item" data-nav="business-plan">
          <a href="business-plan.html" class="drd-nav-link">
            Business Plan EyePros
            <svg width="10" height="10" viewBox="0 0 12 12" fill="none">
              <path d="M2.5 4.5L6 8L9.5 4.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </a>

          <div class="drd-mega-dropdown" style="grid-template-columns: repeat(3, 1fr) 260px; width: 920px;">
            <div class="drd-mega-col">
              <h4>Brand Strategy</h4>
              <ul class="drd-mega-list">
                <li class="drd-mega-item">
                  <a href="business-plan.html">
                    <span class="drd-mega-title">Brand Foundation</span>
                    <span class="drd-mega-desc">Vision, Mission &amp; "Back in Focus"</span>
                  </a>
                </li>
                <li class="drd-mega-item">
                  <a href="business-plan.html">
                    <span class="drd-mega-title">Ahmad Elsahn Anchor</span>
                    <span class="drd-mega-desc">Clinical Director PR &amp; leadership</span>
                  </a>
                </li>
              </ul>
            </div>

            <div class="drd-mega-col">
              <h4>Strategy Fit</h4>
              <ul class="drd-mega-list">
                <li class="drd-mega-item">
                  <a href="business-plan.html">
                    <span class="drd-mega-title">8 Strategic Priorities</span>
                    <span class="drd-mega-desc">Referrals, EyeSpa &amp; subscriptions</span>
                  </a>
                </li>
                <li class="drd-mega-item">
                  <a href="business-plan.html">
                    <span class="drd-mega-title">19 Audience Personas</span>
                    <span class="drd-mega-desc">13 Patients &amp; 6 Optom gatekeepers</span>
                  </a>
                </li>
              </ul>
            </div>

            <div class="drd-mega-col">
              <h4>Commercial Operations</h4>
              <ul class="drd-mega-list">
                <li class="drd-mega-item">
                  <a href="business-plan.html">
                    <span class="drd-mega-title">470 Practice Territory</span>
                    <span class="drd-mega-desc">Notts, Leics &amp; Derbys breakdown</span>
                  </a>
                </li>
                <li class="drd-mega-item">
                  <a href="business-plan.html">
                    <span class="drd-mega-title">6-Stage Referral Funnel</span>
                    <span class="drd-mega-desc">72 visits/mo conversion rhythm</span>
                  </a>
                </li>
                <li class="drd-mega-item">
                  <a href="business-plan.html">
                    <span class="drd-mega-title">HubSpot CRM Setup</span>
                    <span class="drd-mega-desc">Lean 8-field practice visit workflow</span>
                  </a>
                </li>
              </ul>
            </div>

            <!-- Featured Promo Box -->
            <a href="business-plan.html" class="drd-mega-featured">
              <div>
                <span class="drd-badge drd-badge-teal mb-2" style="font-size: 0.65rem;">Operations</span>
                <h5>Field Conversion Engine</h5>
                <p>3 field days/week delivering 6 practice visits/day across the 3 counties.</p>
              </div>
              <span class="drd-link-arrow">View Strategy &rarr;</span>
            </a>
          </div>
        </li>

        <!-- 5. Timeline -->
        <li class="drd-nav-item" data-nav="timeline">
          <a href="timeline.html" class="drd-nav-link">Timeline</a>
        </li>

        <!-- 6. Sources -->
        <li class="drd-nav-item" data-nav="sources">
          <a href="index.html#sources" class="drd-nav-link">Sources</a>
        </li>
      </ul>

      <!-- CTA Action Button -->
      <div class="d-flex align-items-center gap-2">
        <a href="timeline.html" class="drd-btn drd-btn-primary">
          <span>Internship Roadmap</span>
          <svg width="12" height="12" viewBox="0 0 16 16" fill="none">
            <path d="M3 8L13 8M13 8L8.5 3.5M13 8L8.5 12.5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </a>

        <!-- Mobile Burger -->
        <button class="drd-burger" id="drdBurgerBtn" aria-label="Toggle navigation">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
            <path d="M4 6H20M4 12H20M4 18H20" stroke="#121016" stroke-width="2" stroke-linecap="round"/>
          </svg>
        </button>
      </div>
    </nav>
  </header>

  <!-- Mobile Drawer Menu -->
  <div class="drd-mobile-drawer" id="drdMobileDrawer">
    <div class="d-flex justify-content-between align-items-center mb-2 pb-2 border-bottom">
      <span class="font-bold text-sm">Strategic Menu</span>
      <button id="drdCloseDrawerBtn" style="background:none;border:none;font-size:1.2rem;cursor:pointer;">&times;</button>
    </div>
    <a href="index.html" class="drd-btn drd-btn-secondary justify-content-start"><i class="fa fa-home"></i> Home</a>
    <a href="patient-pathways.html" class="drd-btn drd-btn-secondary justify-content-start"><i class="fa fa-users"></i> Patient Pathways (5 Archetypes)</a>
    <a href="market-numbers.html" class="drd-btn drd-btn-secondary justify-content-start"><i class="fa fa-bar-chart"></i> Market &amp; Numbers Intelligence</a>
    <a href="business-plan.html" class="drd-btn drd-btn-secondary justify-content-start"><i class="fa fa-briefcase"></i> Business Plan EyePros</a>
    <a href="timeline.html" class="drd-btn drd-btn-teal justify-content-start"><i class="fa fa-calendar-check-o"></i> 23-Week Internship Timeline</a>
    <a href="index.html#sources" class="drd-btn drd-btn-secondary justify-content-start"><i class="fa fa-bookmark"></i> Authoritative Sources</a>
  </div>
  `;

  function init() {
    // Inject header
    document.body.insertAdjacentHTML('afterbegin', NAV_HTML);

    // Scroll listener for sticky compact capsule
    const headerWrapper = document.getElementById('drdHeaderWrapper');
    window.addEventListener('scroll', function () {
      if (window.scrollY > 40) {
        headerWrapper.classList.add('scrolled');
      } else {
        headerWrapper.classList.remove('scrolled');
      }
    }, { passive: true });

    // Active page highlighting
    const currentPath = window.location.pathname.toLowerCase();
    const filename = currentPath.split('/').pop() || 'index.html';
    
    let activeKey = 'home';
    if (filename.includes('patient-pathways')) activeKey = 'patient-pathways';
    else if (filename.includes('market-numbers') || filename.includes('competitor') || filename.includes('stakeholder')) activeKey = 'market-numbers';
    else if (filename.includes('business-plan') || filename.includes('strategy') || filename.includes('persona') || filename.includes('partnership')) activeKey = 'business-plan';
    else if (filename.includes('timeline')) activeKey = 'timeline';

    document.querySelectorAll('.drd-nav-item').forEach(item => {
      if (item.getAttribute('data-nav') === activeKey) {
        item.classList.add('active');
      }
    });

    // Mobile Drawer Toggle
    const burger = document.getElementById('drdBurgerBtn');
    const drawer = document.getElementById('drdMobileDrawer');
    const closeBtn = document.getElementById('drdCloseDrawerBtn');

    if (burger && drawer) {
      burger.addEventListener('click', () => drawer.classList.toggle('open'));
    }
    if (closeBtn && drawer) {
      closeBtn.addEventListener('click', () => drawer.classList.remove('open'));
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
