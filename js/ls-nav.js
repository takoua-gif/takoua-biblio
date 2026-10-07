/**
 * LONGSIGHTED Navigation Module
 * Klarna-inspired minimal sticky nav with Longsighted logo
 */

(function () {
  'use strict';

  const PAGES = [
    { label: 'Home',              href: 'index.html' },
    { label: 'Patient Pathways',  href: 'patient-pathways.html' },
    { label: 'Market & Numbers',  href: 'market-numbers.html' },
    { label: 'Market & Landscape', href: 'market-landscape.html' },
    { label: 'Business Plan Eyepros', href: 'business-plan.html' },
    { label: 'Pitch Deck Slides', href: 'business-plan-deck.html' },
    { label: 'Timeline',          href: 'timeline.html' },
  ];

  function getCurrentPage() {
    const path = window.location.pathname.split('/').pop() || 'index.html';
    return path;
  }

  function buildNav() {
    const current = getCurrentPage();

    const navEl = document.createElement('nav');
    navEl.className = 'ls-nav';
    navEl.id = 'ls-main-nav';
    navEl.setAttribute('aria-label', 'Main navigation');

    navEl.innerHTML = `
      <div class="ls-nav-inner">

        <!-- Logo -->
        <a href="index.html" class="ls-nav-logo" aria-label="Longsighted Home">
          <img src="images/longsighted-logo-horizontal.png" alt="Longsighted" onerror="this.src='images/longsighted-logo.png';">
        </a>

        <!-- Desktop links -->
        <ul class="ls-nav-links" role="list">
          ${PAGES.map(p => `
            <li>
              <a href="${p.href}"
                 class="ls-nav-link${current === p.href ? ' active' : ''}"
                 ${current === p.href ? 'aria-current="page"' : ''}>
                ${p.label}
              </a>
            </li>
          `).join('')}
        </ul>

        <!-- Right -->
        <div class="ls-nav-cta">
          <a href="timeline.html" class="ls-btn ls-btn-gold ls-btn-sm ls-hide-mobile">
            View Timeline
          </a>
          <!-- Mobile burger -->
          <button class="ls-burger" id="ls-burger-btn" aria-expanded="false" aria-controls="ls-mobile-drawer" aria-label="Open menu">
            <svg width="20" height="14" viewBox="0 0 20 14" fill="none">
              <path d="M0 1h20M0 7h20M0 13h14" stroke="currentColor" stroke-width="1.75" stroke-linecap="round"/>
            </svg>
          </button>
        </div>
      </div>
    `;

    // Mobile drawer
    const drawerBackdrop = document.createElement('div');
    drawerBackdrop.className = 'ls-mobile-overlay';
    drawerBackdrop.id = 'ls-mobile-overlay';
    drawerBackdrop.setAttribute('aria-hidden', 'true');

    const drawer = document.createElement('div');
    drawer.className = 'ls-mobile-drawer';
    drawer.id = 'ls-mobile-drawer';
    drawer.setAttribute('role', 'dialog');
    drawer.setAttribute('aria-label', 'Navigation menu');
    drawer.setAttribute('aria-modal', 'true');

    drawer.innerHTML = `
      <div style="display:flex; align-items:center; justify-content:space-between;">
        <a href="index.html" class="ls-nav-logo" aria-label="Longsighted Home">
          <img src="images/longsighted-logo-horizontal.png" alt="Longsighted" style="height:38px; max-width:220px;" onerror="this.src='images/longsighted-logo.png';">
        </a>
        <button id="ls-drawer-close" class="ls-burger" aria-label="Close menu">
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
            <path d="M1 1l14 14M15 1L1 15" stroke="currentColor" stroke-width="1.75" stroke-linecap="round"/>
          </svg>
        </button>
      </div>
      <nav class="ls-mobile-nav-links" aria-label="Mobile navigation">
        ${PAGES.map(p => `
          <a href="${p.href}" class="ls-mobile-nav-link${current === p.href ? ' active' : ''}"
             style="${current === p.href ? 'background: var(--ls-cream); color: var(--ls-navy);' : ''}"
             ${current === p.href ? 'aria-current="page"' : ''}>
            ${p.label}
          </a>
        `).join('')}
      </nav>
      <div style="margin-top: auto; padding-top: 32px;">
        <a href="timeline.html" class="ls-btn ls-btn-gold" style="width:100%;">View Timeline</a>
      </div>
    `;

    document.body.prepend(drawerBackdrop);
    document.body.prepend(drawer);
    document.body.prepend(navEl);

    // Push content below nav
    document.body.style.paddingTop = 'var(--nav-h)';

    // --- Scroll transparency on hero pages
    const hero = document.querySelector('.ls-hero');
    if (hero) {
      navEl.classList.add('transparent');
      const obs = new IntersectionObserver(
        ([entry]) => navEl.classList.toggle('transparent', entry.isIntersecting),
        { rootMargin: `-${72}px 0px 0px 0px` }
      );
      obs.observe(hero);
    }

    // --- Mobile interactions
    const burger = document.getElementById('ls-burger-btn');
    const closeBtn = document.getElementById('ls-drawer-close');
    const overlay = document.getElementById('ls-mobile-overlay');

    function openDrawer() {
      drawer.classList.add('open');
      overlay.classList.add('open');
      burger.setAttribute('aria-expanded', 'true');
      document.body.style.overflow = 'hidden';
    }

    function closeDrawer() {
      drawer.classList.remove('open');
      overlay.classList.remove('open');
      burger.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
    }

    if (burger) burger.addEventListener('click', openDrawer);
    if (closeBtn) closeBtn.addEventListener('click', closeDrawer);
    if (overlay) overlay.addEventListener('click', closeDrawer);

    // Esc key
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape' && drawer.classList.contains('open')) closeDrawer();
    });

    // Active link scroll spy (home page sections only)
    if (current === 'index.html' || current === '') {
      setupScrollSpy();
    }
  }

  function setupScrollSpy() {
    const sections = document.querySelectorAll('[data-spy]');
    const links = document.querySelectorAll('.ls-nav-link[data-spy-target]');
    if (!sections.length || !links.length) return;

    const obs = new IntersectionObserver(
      entries => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            const id = entry.target.dataset.spy;
            links.forEach(l => {
              l.classList.toggle('active', l.dataset.spyTarget === id);
            });
          }
        });
      },
      { rootMargin: '-30% 0px -60% 0px' }
    );

    sections.forEach(s => obs.observe(s));
  }

  // Scroll reveal
  function setupReveal() {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    const els = document.querySelectorAll('.ls-reveal, .ls-reveal-up');
    if (!els.length) return;

    const obs = new IntersectionObserver(
      entries => {
        entries.forEach(e => {
          if (e.isIntersecting) {
            e.target.classList.add('visible');
            obs.unobserve(e.target);
          }
        });
      },
      { rootMargin: '0px 0px -60px 0px', threshold: 0.1 }
    );

    els.forEach(el => obs.observe(el));
  }

  // Toast helper (global)
  window.lsToast = function (msg, duration = 2800) {
    let t = document.getElementById('ls-toast-global');
    if (!t) {
      t = document.createElement('div');
      t.className = 'ls-toast';
      t.id = 'ls-toast-global';
      document.body.appendChild(t);
    }
    t.textContent = msg;
    t.classList.add('show');
    clearTimeout(t._timer);
    t._timer = setTimeout(() => t.classList.remove('show'), duration);
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => { buildNav(); setupReveal(); });
  } else {
    buildNav();
    setupReveal();
  }
})();
