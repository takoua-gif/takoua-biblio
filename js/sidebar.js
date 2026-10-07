/**
 * Longsighted — Sidebar Navigation Engine
 * Shared across all pages
 */
(function () {
  'use strict';

  /* ── Sidebar HTML Template ── */
  const SIDEBAR_HTML = `
    <aside class="site-sidebar" id="siteSidebar">
      <div class="sidebar-header">
        <a href="index.html" class="sidebar-brand" style="text-decoration:none;">
          <div class="sidebar-brand-icon">👁</div>
          <div>
            <div class="sidebar-brand-name">EyePros</div>
            <div class="sidebar-brand-sub">Strategic Playbook</div>
          </div>
        </a>
      </div>

      <nav class="sidebar-nav">
        <!-- Core Pillars -->
        <div class="nav-group" data-group="main">
          <div class="nav-group-header">
            <span class="group-label">🏛️ Strategic Playbook</span>
            <span class="chevron">▾</span>
          </div>
          <div class="nav-group-items">
            <a class="sidebar-link" href="index.html" data-page="home"><i class="fa fa-home"></i> 1. Home &amp; Intel</a>
            <a class="sidebar-link" href="patient-pathways.html" data-page="patient-pathways"><i class="fa fa-users"></i> 2. Patient Pathways</a>
            <a class="sidebar-link" href="market-numbers.html" data-page="market-numbers"><i class="fa fa-bar-chart"></i> 3. Market &amp; Numbers</a>
            <a class="sidebar-link" href="market-landscape.html" data-page="market-landscape"><i class="fa fa-globe"></i> 3b. Market &amp; Landscape</a>
            <a class="sidebar-link" href="business-plan.html" data-page="business-plan"><i class="fa fa-briefcase"></i> 4. Business Plan EyePros</a>
            <a class="sidebar-link" href="business-plan-deck.html" data-page="business-plan-deck"><i class="fa fa-television"></i> 4b. Pitch Deck Slides</a>
            <a class="sidebar-link" href="timeline.html" data-page="timeline"><i class="fa fa-calendar-check-o"></i> 5. Timeline</a>
            <a class="sidebar-link" href="index.html#sources" data-page="sources"><i class="fa fa-link"></i> 6. Sources</a>
          </div>
        </div>

        <!-- In-Page Jump Links for Home -->
        <div class="nav-group in-page-group" data-group="home-sections" style="margin-top: 15px;">
          <div class="nav-group-header">
            <span class="group-label">⚡ Home Sections</span>
            <span class="chevron">▾</span>
          </div>
          <div class="nav-group-items">
            <a class="sidebar-link sub-link" href="index.html#banner" data-section="banner"><i class="fa fa-dot-circle-o"></i> Hero Banner</a>
            <a class="sidebar-link sub-link" href="index.html#events-calendar" data-section="events-calendar"><i class="fa fa-calendar"></i> Events Calendar</a>
            <a class="sidebar-link sub-link" href="index.html#intel-carousel" data-section="intel-carousel"><i class="fa fa-rss"></i> Live Intel Feed</a>
            <a class="sidebar-link sub-link" href="index.html#acronyms" data-section="acronyms"><i class="fa fa-font"></i> Acronym Explorer</a>
            <a class="sidebar-link sub-link" href="index.html#sources" data-section="sources"><i class="fa fa-bookmark"></i> Sources</a>
          </div>
        </div>
      </nav>

      <div class="sidebar-footer">
        <span class="font-mono" style="font-size: 0.7rem; color: #94a3b8;"><i class="fa fa-shield text-teal"></i> Midlands Hub v2.5</span>
        <span class="sidebar-shortcut">⌘K</span>
      </div>
    </aside>

    <div class="sidebar-overlay" id="sidebarOverlay"></div>

    <button class="sidebar-toggle" id="sidebarToggle" aria-label="Toggle menu">
      <span></span><span></span><span></span>
    </button>
  `;

  /* ── Page-to-data-page mapping ── */
  const PAGE_MAP = {
    'index.html': 'home',
    'patient-pathways.html': 'patient-pathways',
    'market-numbers.html': 'market-numbers',
    'market-landscape.html': 'market-landscape',
    'business-plan.html': 'business-plan',
    'business-plan-deck.html': 'business-plan-deck',
    'timeline.html': 'timeline',
    'eyepros — internship timeline.html': 'timeline',
    'eyepros — persona boards.html': 'business-plan',
    'eyepros — business strategy.html': 'business-plan',
    'eyepros — competitor analysis.html': 'market-numbers',
    'eyepros — market intelligence.html': 'market-numbers',
    'eyepros — partnership intelligence.html': 'business-plan',
    'eyepros — stakeholder map.html': 'market-numbers'
  };

  /* ── Init ── */
  function init() {
    // Inject sidebar HTML
    document.body.insertAdjacentHTML('afterbegin', SIDEBAR_HTML);
    document.documentElement.classList.add('has-sidebar');

    const sidebar = document.getElementById('siteSidebar');
    const overlay = document.getElementById('sidebarOverlay');
    const toggle  = document.getElementById('sidebarToggle');

    // Mobile toggle
    if (toggle) {
      toggle.addEventListener('click', function () {
        sidebar.classList.toggle('open');
        overlay.classList.toggle('active');
        toggle.classList.toggle('active');
      });
    }
    if (overlay) {
      overlay.addEventListener('click', function () {
        sidebar.classList.remove('open');
        overlay.classList.remove('active');
        if (toggle) toggle.classList.remove('active');
      });
    }

    // Close sidebar on mobile when clicking a link
    sidebar.querySelectorAll('.sidebar-link').forEach(function (link) {
      link.addEventListener('click', function () {
        if (window.innerWidth <= 768) {
          sidebar.classList.remove('open');
          overlay.classList.remove('active');
          if (toggle) toggle.classList.remove('active');
        }
      });
    });

    // Group collapse/expand
    sidebar.querySelectorAll('.nav-group-header').forEach(function (header) {
      header.addEventListener('click', function () {
        this.parentElement.classList.toggle('collapsed');
      });
    });

    // Set active page
    setActivePage();

    // Scroll-spy for playbook sections (only on index/playbook page)
    var currentPage = getCurrentPageId();
    if (currentPage === 'playbook') {
      setupScrollSpy();
      // Convert playbook links to anchor-only (no page reload)
      sidebar.querySelectorAll('[data-section]').forEach(function (link) {
        link.setAttribute('href', '#' + link.getAttribute('data-section'));
      });
    }

    // Theme toggle in sidebar
    var themeBtn = document.getElementById('sidebarThemeToggle');
    if (themeBtn) {
      themeBtn.addEventListener('click', function () {
        // Try to use existing theme toggle if present
        var existingBtn = document.getElementById('themeToggleBtn');
        if (existingBtn) {
          existingBtn.click();
        } else {
          // Toggle manually
          var html = document.documentElement;
          var current = html.getAttribute('data-theme') || 'dark';
          var next = current === 'dark' ? 'light' : 'dark';
          html.setAttribute('data-theme', next);
          try { localStorage.setItem('theme', next); } catch(e) {}
        }
      });
    }
  }

  function getCurrentPageId() {
    var path = decodeURIComponent(window.location.pathname).toLowerCase();
    var filename = path.split('/').pop() || 'index.html';
    if (filename === '' || filename === '/') filename = 'index.html';
    return PAGE_MAP[filename] || 'playbook';
  }

  function setActivePage() {
    var pageId = getCurrentPageId();
    var sidebar = document.getElementById('siteSidebar');
    if (!sidebar) return;

    // Highlight the matching page link
    sidebar.querySelectorAll('.sidebar-link[data-page]').forEach(function (link) {
      if (link.getAttribute('data-page') === pageId) {
        link.classList.add('active');
        // Expand parent group
        var group = link.closest('.nav-group');
        if (group) group.classList.remove('collapsed');
      }
    });

    // If on home, highlight home by default and show home sections
    var isHomePage = (pageId === 'home');
    var inPageGroup = sidebar.querySelector('.in-page-group');
    if (inPageGroup) {
      inPageGroup.style.display = isHomePage ? 'block' : 'none';
    }

    // Keep main group open
    sidebar.querySelectorAll('.nav-group').forEach(function (group) {
      if (group.getAttribute('data-group') === 'main') {
        group.classList.remove('collapsed');
      }
    });
  }

  function setupScrollSpy() {
    var sections = [
      'banner', 'events-calendar', 'intel-carousel', 'acronyms', 'sources'
    ];

    var sectionLinks = {};
    var sidebar = document.getElementById('siteSidebar');
    sections.forEach(function (id) {
      var link = sidebar.querySelector('[data-section="' + id + '"]');
      if (link) sectionLinks[id] = link;
    });

    window.addEventListener('scroll', function () {
      var scrollPos = window.scrollY + 120;
      var current = '';

      sections.forEach(function (id) {
        var el = document.getElementById(id);
        if (el && scrollPos >= el.offsetTop) {
          current = id;
        }
      });

      // Update active states
      Object.keys(sectionLinks).forEach(function (id) {
        if (id === current) {
          sectionLinks[id].classList.add('active');
        } else {
          sectionLinks[id].classList.remove('active');
        }
      });
    }, { passive: true });
  }

  // Run on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
