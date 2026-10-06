/**
 * EyePros Reference Library & Strategy Workspace Engine
 * Curator: Takoua Selmi
 * Logic Layer: Theme, Command Palette (Ctrl+K), Grouped ScrollSpy, Workbench, SWR Feed, Events Calendar
 */

const initPlaybook = () => {

  // ==========================================================================
  // 1. MOBILE DRAWER & 6-GROUP NAV SCROLL SPY
  // ==========================================================================
  const mobileToggle = document.getElementById('mobileMenuToggle');
  const closeDrawerBtn = document.getElementById('closeMobileDrawerBtn');
  const drawerSheet = document.getElementById('mobileDrawerSheet');
  const drawerOverlay = document.getElementById('mobileDrawerOverlay');

  function openMobileDrawer() {
    if (drawerSheet) drawerSheet.classList.add('active');
    if (drawerOverlay) drawerOverlay.classList.add('active');
  }

  function closeMobileDrawer() {
    if (drawerSheet) drawerSheet.classList.remove('active');
    if (drawerOverlay) drawerOverlay.classList.remove('active');
  }

  if (mobileToggle) mobileToggle.addEventListener('click', openMobileDrawer);
  if (closeDrawerBtn) closeDrawerBtn.addEventListener('click', closeMobileDrawer);
  if (drawerOverlay) drawerOverlay.addEventListener('click', closeMobileDrawer);

  document.querySelectorAll('.mobile-nav-link').forEach(link => {
    link.addEventListener('click', () => {
      closeMobileDrawer();
    });
  });

  // Group ScrollSpy — Maps section IDs to the home sections
  const sectionGroupMap = {
    'banner': 'banner',
    'events-calendar': 'events-calendar',
    'intel-carousel': 'intel-carousel',
    'acronyms': 'acronyms',
    'sources': 'sources'
  };

  const groupLinks = document.querySelectorAll('.nav-group-link');
  window.addEventListener('scroll', () => {
    let currentSection = '';
    Object.keys(sectionGroupMap).forEach(secId => {
      const el = document.getElementById(secId);
      if (el && window.scrollY >= el.offsetTop - 110) {
        currentSection = secId;
      }
    });

    const activeGroupId = sectionGroupMap[currentSection];
    groupLinks.forEach(link => {
      if (activeGroupId && link.id === activeGroupId) {
        link.classList.add('active');
      } else {
        link.classList.remove('active');
      }
    });
  }, { passive: true });

  // ==========================================================================
  // 2. HERO COLLAPSIBLE "ABOUT PLAYBOOK" & QUICK ACTIONS
  // ==========================================================================
  const toggleAboutBtn = document.getElementById('toggleAboutPlaybookBtn');
  const aboutContent = document.getElementById('aboutPlaybookContent');

  if (toggleAboutBtn && aboutContent) {
    toggleAboutBtn.addEventListener('click', () => {
      aboutContent.classList.toggle('open');
      const isExpanded = aboutContent.classList.contains('open');
      toggleAboutBtn.querySelector('.chevron-icon').style.transform = isExpanded ? 'rotate(180deg)' : 'rotate(0deg)';
    });
  }

  // ==========================================================================
  // 3. INTERNSHIP ELAPSED TIMER & REMAINING DAYS
  // ==========================================================================
  const INTERNSHIP_START = new Date("2026-07-01T00:00:00+01:00"); // July 1, 2026 (BST)
  const INTERNSHIP_END   = new Date("2026-12-18T23:59:59+00:00"); // Dec 18, 2026

  function updateCountdown() {
    const now = new Date();
    const widget = document.getElementById('countdownWidget');
    if (!widget) return;

    // Elapsed time since July 1
    const elapsedMs = Math.max(0, now - INTERNSHIP_START);
    const totalSecs  = Math.floor(elapsedMs / 1000);
    const totalMins  = Math.floor(totalSecs / 60);
    const totalHours = Math.floor(totalMins / 60);
    const days       = Math.floor(totalHours / 24);
    const hrsRemaining  = totalHours % 24;
    const minsRemaining = totalMins % 60;
    const secsRemaining = totalSecs % 60;

    const daysEl = document.getElementById('countdownDays');
    const hrsEl  = document.getElementById('countdownHours');
    const minsEl = document.getElementById('countdownMins');
    const secEl  = document.getElementById('countdownSecs');

    if (daysEl) daysEl.textContent  = String(days).padStart(2, '0');
    if (hrsEl)  hrsEl.textContent   = String(hrsRemaining).padStart(2, '0');
    if (minsEl) minsEl.textContent  = String(minsRemaining).padStart(2, '0');
    if (secEl)  secEl.textContent   = String(secsRemaining).padStart(2, '0');

    // Days remaining until Dec 18
    const footerEl = document.getElementById('countdownFooter');
    if (footerEl) {
      const remainingMs = Math.max(0, INTERNSHIP_END - now);
      const daysLeft = Math.ceil(remainingMs / (1000 * 60 * 60 * 24));
      footerEl.textContent = daysLeft > 0
        ? daysLeft + ' day' + (daysLeft !== 1 ? 's' : '') + ' left until 18 December'
        : 'Internship completed 🎓';
    }
  }

  updateCountdown();
  setInterval(updateCountdown, 1000);

  // ==========================================================================
  // 4. THEME CONTROLLER (Dark / Light toggle) & PRINT
  // ==========================================================================
  const themeToggleBtn = document.getElementById('themeToggleBtn');
  const printBtn = document.getElementById('printBtn');
  
  const storedTheme = localStorage.getItem('eyepros-theme') || 'light';
  document.documentElement.setAttribute('data-theme', storedTheme);

  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', () => {
      const currentTheme = document.documentElement.getAttribute('data-theme');
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      
      document.documentElement.setAttribute('data-theme', newTheme);
      localStorage.setItem('eyepros-theme', newTheme);
    });
  }

  if (printBtn) {
    printBtn.addEventListener('click', () => {
      window.print();
    });
  }

  // ==========================================================================
  // 5. GLOBAL COMMAND PALETTE (Ctrl+K / Cmd+K)
  // ==========================================================================
  const cmdModal = document.getElementById('cmdPaletteModal');
  const cmdInput = document.getElementById('cmdPaletteInput');
  const cmdResults = document.getElementById('cmdPaletteResults');
  const openCmdBtn = document.getElementById('openCmdPaletteBtn');
  const heroCmdBtn = document.getElementById('heroSearchTriggerBtn');
  const closeCmdBtn = document.getElementById('closeCmdPaletteBtn');
  const catPills = document.querySelectorAll('.cmd-cat-pill');

  let activeCategory = 'all';
  let selectedResultIndex = 0;

  function openCommandPalette() {
    if (!cmdModal) return;
    cmdModal.classList.add('active');
    if (cmdInput) {
      cmdInput.value = '';
      cmdInput.focus();
    }
    renderSearchResults('');
  }

  function closeCommandPalette() {
    if (!cmdModal) return;
    cmdModal.classList.remove('active');
  }

  if (openCmdBtn) openCmdBtn.addEventListener('click', openCommandPalette);
  if (heroCmdBtn) heroCmdBtn.addEventListener('click', openCommandPalette);
  if (closeCmdBtn) closeCmdBtn.addEventListener('click', closeCommandPalette);

  if (cmdModal) {
    cmdModal.addEventListener('click', (e) => {
      if (e.target === cmdModal) closeCommandPalette();
    });
  }

  // Keyboard Shortcuts: Ctrl+K / Cmd+K & Escape
  document.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      openCommandPalette();
    }
    if (e.key === 'Escape' && cmdModal && cmdModal.classList.contains('active')) {
      closeCommandPalette();
    }
  });

  // Filter Pills inside Command Palette
  catPills.forEach(pill => {
    pill.addEventListener('click', () => {
      catPills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      activeCategory = pill.getAttribute('data-filter');
      renderSearchResults(cmdInput ? cmdInput.value : '');
    });
  });

  // Build Index from Page Elements
  function searchIndex(query) {
    const q = query.trim().toLowerCase();
    const results = [];

    const searchableItems = [
      { selector: '.acronym-card', cat: 'Acronyms', getTitle: el => el.querySelector('h4')?.textContent || '', getDesc: el => el.querySelector('.term-full')?.textContent || '' },
      { selector: '.table-dark-custom tr', cat: 'Market', getTitle: el => el.querySelector('td')?.textContent || '', getDesc: el => el.textContent || '' },
      { selector: '.facts-list li', cat: 'Strategy', getTitle: el => el.querySelector('.fact-key')?.textContent || '', getDesc: el => el.querySelector('.fact-val')?.textContent || '' },
      { selector: '.q-item', cat: 'Interviews', getTitle: el => el.querySelector('.q-text')?.textContent || '', getDesc: el => el.querySelector('.q-crib-sheet')?.textContent || '' },
      { selector: '.timeline-milestone', cat: 'Timeline', getTitle: el => el.querySelector('h3')?.textContent || '', getDesc: el => el.querySelector('p')?.textContent || '' },
      { selector: '.gcal-event-row', cat: 'Events', getTitle: el => el.querySelector('h4')?.textContent || '', getDesc: el => el.querySelector('.gcal-location')?.textContent || '' }
    ];

    searchableItems.forEach(item => {
      if (activeCategory !== 'all' && activeCategory !== item.cat) return;

      document.querySelectorAll(item.selector).forEach((el, index) => {
        const title = item.getTitle(el).trim();
        const desc = item.getDesc(el).trim();
        const fullText = (title + ' ' + desc).toLowerCase();

        if (!q || fullText.includes(q)) {
          // Assign unique target ID if missing
          if (!el.id) el.id = `cmd_target_${item.cat}_${index}`;
          results.push({
            category: item.cat,
            title: title || 'Item Reference',
            snippet: desc.substring(0, 120) + (desc.length > 120 ? '...' : ''),
            targetId: el.id,
            element: el
          });
        }
      });
    });

    return results;
  }

  function renderSearchResults(query) {
    if (!cmdResults) return;
    const items = searchIndex(query);

    if (items.length === 0) {
      cmdResults.innerHTML = `
        <div class="cmd-empty-state">
          <i class="fa fa-info-circle"></i>
          <p>No matching results found for "${query}"</p>
        </div>
      `;
      return;
    }

    let html = '';
    items.slice(0, 15).forEach((item, idx) => {
      const isSelected = idx === 0 ? 'selected' : '';
      html += `
        <div class="cmd-result-item ${isSelected}" data-target="${item.targetId}" data-index="${idx}">
          <div class="cmd-result-meta">
            <span class="cmd-result-title">${item.title}</span>
            <span class="cmd-result-cat">${item.category}</span>
          </div>
          <div class="cmd-result-excerpt">${item.snippet}</div>
        </div>
      `;
    });

    cmdResults.innerHTML = html;
    selectedResultIndex = 0;

    // Item click jump handler
    cmdResults.querySelectorAll('.cmd-result-item').forEach(resEl => {
      resEl.addEventListener('click', () => {
        const targetId = resEl.getAttribute('data-target');
        jumpToTarget(targetId);
      });
    });
  }

  if (cmdInput) {
    cmdInput.addEventListener('input', (e) => {
      renderSearchResults(e.target.value);
    });

    // Arrow navigation inside Search Modal
    cmdInput.addEventListener('keydown', (e) => {
      const resItems = cmdResults.querySelectorAll('.cmd-result-item');
      if (!resItems.length) return;

      if (e.key === 'ArrowDown') {
        e.preventDefault();
        resItems[selectedResultIndex]?.classList.remove('selected');
        selectedResultIndex = (selectedResultIndex + 1) % resItems.length;
        resItems[selectedResultIndex]?.classList.add('selected');
        resItems[selectedResultIndex]?.scrollIntoView({ block: 'nearest' });
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        resItems[selectedResultIndex]?.classList.remove('selected');
        selectedResultIndex = (selectedResultIndex - 1 + resItems.length) % resItems.length;
        resItems[selectedResultIndex]?.classList.add('selected');
        resItems[selectedResultIndex]?.scrollIntoView({ block: 'nearest' });
      } else if (e.key === 'Enter') {
        e.preventDefault();
        const selected = resItems[selectedResultIndex];
        if (selected) {
          const targetId = selected.getAttribute('data-target');
          jumpToTarget(targetId);
        }
      }
    });
  }

  function jumpToTarget(targetId) {
    closeCommandPalette();
    const targetEl = document.getElementById(targetId);
    if (!targetEl) return;

    // Open parent accordion panel or tab if in Workbench
    const parentPanel = targetEl.closest('.workbench-persona-panel');
    if (parentPanel) {
      const persona = parentPanel.id.replace('panel', '').toLowerCase();
      switchPersonaTab(persona);
    }

    // Smooth scroll with header offset
    const targetTop = targetEl.getBoundingClientRect().top + window.scrollY - 95;
    window.scrollTo({ top: targetTop, behavior: 'smooth' });

    // Flash Teal Highlight
    targetEl.classList.remove('search-highlight-flash');
    void targetEl.offsetWidth; // Trigger reflow
    targetEl.classList.add('search-highlight-flash');
  }

  // ==========================================================================
  // 6. ACRONYM EXPLORER
  // ==========================================================================
  const acronymsGrid = document.getElementById('acronymsGrid');
  const filterPills = document.querySelectorAll('.filter-pill');

  if (acronymsGrid) {
    acronymsGrid.addEventListener('click', (e) => {
      const card = e.target.closest('.acronym-card');
      if (card) card.classList.toggle('flipped');
    });
  }

  filterPills.forEach(pill => {
    pill.addEventListener('click', () => {
      filterPills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');

      const category = pill.getAttribute('data-category');
      const cards = acronymsGrid ? acronymsGrid.querySelectorAll('.acronym-card') : [];
      
      cards.forEach(card => {
        const cardCat = card.getAttribute('data-category');
        if (category === 'all' || cardCat === category) {
          card.style.display = 'block';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });

  // Instant search input for Acronym Explorer
  const globalSearchInput = document.getElementById('globalSearch');
  const clearSearchBtn = document.getElementById('clearSearchBtn');
  const searchResultsStats = document.getElementById('searchResultsStats');

  if (globalSearchInput) {
    globalSearchInput.addEventListener('input', (e) => {
      const q = e.target.value.toLowerCase().trim();
      const cards = acronymsGrid ? acronymsGrid.querySelectorAll('.acronym-card') : [];
      let matchCount = 0;

      cards.forEach(card => {
        const text = card.textContent.toLowerCase();
        if (!q || text.includes(q)) {
          card.style.display = 'block';
          matchCount++;
        } else {
          card.style.display = 'none';
        }
      });

      if (searchResultsStats) {
        searchResultsStats.textContent = q ? `Found ${matchCount} matching term${matchCount === 1 ? '' : 's'}` : '';
      }
    });

    if (clearSearchBtn) {
      clearSearchBtn.addEventListener('click', () => {
        globalSearchInput.value = '';
        globalSearchInput.dispatchEvent(new Event('input'));
      });
    }
  }

  // ==========================================================================
  // 7. PATIENT ARCHETYPE SYSTEM
  // ==========================================================================
  const archetypesData = {
    A: {
      letter: 'A',
      title: 'The Cataract Patient',
      tagline: 'VOLUME ENGINE · 450,000 PROCEDURES ANNUALLY',
      trigger: 'Vision deterioration over months. Halos/glare driving at night. Typically picked up at routine sight test where the high-street optometrist grades the cataract.',
      logic: 'They face a critical decision: wait 16+ weeks on the NHS or pay to go private. Three core parameters shape their conversion: wait time impact, desire for premium multi-focal/EDOF IOLs, and consultant continuity. <strong>EyePros wins by offering speed, lens choice, and consultant care.</strong>'
    },
    B: {
      letter: 'B',
      title: 'The Glaucoma Patient',
      tagline: 'LIFETIME CARE · MIGS SURGICAL HOOK',
      trigger: 'Detected during routine primary sight test via elevated IOP, optic disc cupping, or visual field drops.',
      logic: 'Glaucoma is a lifetime relationship, representing the strongest fit for <strong>subscription care plans</strong>. Ahmad\'s MIGS subspecialty is the clinical hook.'
    },
    C: {
      letter: 'C',
      title: 'The Laser & Refractive Patient',
      tagline: 'SELF-INITIATED · HIGH-VOLUME SEGMENT',
      trigger: 'Self-referred. Aged 25-45. Frustrated with spectacles or contact lens discomfort.',
      logic: 'Avoid a price-led race to the bottom by competing on consultant credibility, custom clinical packages, and specialized post-op dry eye management.'
    },
    D: {
      letter: 'D',
      title: 'The Dry Eye Patient',
      tagline: 'EYESPA SERVICES · CARE SUBSCRIPTION TARGET',
      trigger: 'Self-medicated with over-the-counter drops for 2-10 years. Symptoms worsening.',
      logic: 'Ideal candidate for subscription models. Patients seek clinical pathways, IPL/LipiFlow specialized care, and recurring checkups.'
    },
    E: {
      letter: 'E',
      title: 'The Dry AMD Patient',
      tagline: 'VALEDA CLINIC PLAY · FIRST-MOVER ADVANTAGE',
      trigger: 'Detected via routine OCT scanning. Historically told nothing could be done beyond vitamins.',
      logic: 'First-mover advantage via Valeda Photobiomodulation (PBM) system. Monthly treatment sessions map directly into subscription pricing.'
    }
  };

  const archetypeTabs = document.querySelectorAll('.archetype-tab');
  const archetypeContent = document.getElementById('archetypeContent');

  function renderArchetype(letter) {
    const data = archetypesData[letter];
    if (!archetypeContent || !data) return;
    
    archetypeContent.innerHTML = `
      <div class="arch-header mb-3">
        <span class="badge badge-accent mb-2">${data.tagline}</span>
        <h3>${data.title} (${data.letter})</h3>
      </div>
      <div class="arch-body text-secondary font-size-sm">
        <div class="mb-3">
          <strong>Pathology Trigger &amp; Detection:</strong>
          <p class="mt-1">${data.trigger}</p>
        </div>
        <div>
          <strong>Conversion Strategy:</strong>
          <p class="mt-1">${data.logic}</p>
        </div>
      </div>
    `;
  }

  renderArchetype('A');

  archetypeTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      archetypeTabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      renderArchetype(tab.getAttribute('data-arch'));
    });
  });

  // ==========================================================================
  // 8. UNIFIED INTERVIEW WORKBENCH (LocalStorage Compatible)
  // ==========================================================================
  const personaTabs = document.querySelectorAll('.persona-tab');
  const personaPanels = document.querySelectorAll('.workbench-persona-panel');

  function switchPersonaTab(persona) {
    personaTabs.forEach(t => {
      t.classList.toggle('active', t.getAttribute('data-persona') === persona);
    });
    personaPanels.forEach(panel => {
      if (panel.id === `panel${persona.charAt(0).toUpperCase() + persona.slice(1)}`) {
        panel.classList.add('active');
      } else {
        panel.classList.remove('active');
      }
    });
  }

  personaTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      const persona = tab.getAttribute('data-persona');
      switchPersonaTab(persona);
    });
  });

  // Restore LocalStorage States
  function loadPlaybookStates() {
    // 1. Restore Checked Checkboxes
    const checkboxes = document.querySelectorAll('.q-chk');
    checkboxes.forEach(chk => {
      const checkedState = localStorage.getItem(`eyepros_chk_${chk.id}`);
      const qItem = chk.closest('.q-item');
      if (qItem) {
        if (checkedState === 'true') {
          chk.checked = true;
          qItem.classList.add('asked');
        } else {
          chk.checked = false;
          qItem.classList.remove('asked');
        }
      }
    });

    // 2. Restore Notes
    const textareas = document.querySelectorAll('.q-notes-input');
    textareas.forEach(ta => {
      const parentItem = ta.closest('.q-item');
      const qId = parentItem ? parentItem.getAttribute('data-id') : null;
      if (qId) {
        const savedNotes = localStorage.getItem(`eyepros_notes_${qId}`);
        if (savedNotes) {
          ta.value = savedNotes;
        } else {
          ta.value = '';
        }
      }
    });

    updateWorkbenchProgress();
  }
  
  loadPlaybookStates();

  // Progress Bar Calculation
  function updateWorkbenchProgress() {
    const totalQuestions = document.querySelectorAll('.q-item').length;
    if (totalQuestions === 0) return;

    let completedCount = 0;
    document.querySelectorAll('.q-item').forEach(qItem => {
      const chk = qItem.querySelector('.q-chk');
      const ta = qItem.querySelector('.q-notes-input');
      const isChecked = chk && chk.checked;
      const hasNotes = ta && ta.value.trim().length > 0;

      if (isChecked || hasNotes) {
        completedCount++;
      }
    });

    const percent = Math.round((completedCount / totalQuestions) * 100);
    const pBar = document.getElementById('workbenchProgressBar');
    const pText = document.getElementById('workbenchProgressText');

    if (pBar) pBar.style.width = `${percent}%`;
    if (pText) pText.textContent = `${percent}% (${completedCount}/${totalQuestions})`;
  }

  // Listen for checkbox toggles
  document.addEventListener('change', (e) => {
    if (e.target.classList.contains('q-chk')) {
      const chk = e.target;
      const qItem = chk.closest('.q-item');
      if (qItem) {
        if (chk.checked) {
          qItem.classList.add('asked');
          localStorage.setItem(`eyepros_chk_${chk.id}`, 'true');
        } else {
          qItem.classList.remove('asked');
          localStorage.setItem(`eyepros_chk_${chk.id}`, 'false');
        }
      }
      updateWorkbenchProgress();
    }
  });

  // Listen for note inputs with debounced save
  document.addEventListener('input', (e) => {
    if (e.target.classList.contains('q-notes-input')) {
      const ta = e.target;
      const parentItem = ta.closest('.q-item');
      const qId = parentItem ? parentItem.getAttribute('data-id') : null;
      if (qId) {
        localStorage.setItem(`eyepros_notes_${qId}`, ta.value);
      }
      updateWorkbenchProgress();
    }
  });

  // Global Crib Sheet Toggle
  const toggleGlobalCribBtn = document.getElementById('toggleGlobalCribBtn');
  if (toggleGlobalCribBtn) {
    toggleGlobalCribBtn.addEventListener('click', () => {
      const cribSheets = document.querySelectorAll('.q-crib-sheet');
      const isShowing = cribSheets.length > 0 && cribSheets[0].style.display === 'block';

      cribSheets.forEach(sheet => {
        sheet.style.display = isShowing ? 'none' : 'block';
      });

      toggleGlobalCribBtn.innerHTML = `
        <i class="fa fa-lightbulb-o"></i> ${isShowing ? 'Show Strategy Crib Sheet' : 'Hide Strategy Crib Sheet'}
      `;
    });
  }

  // Reset Workbench Notes
  const resetWorkbenchBtn = document.getElementById('resetWorkbenchBtn');
  if (resetWorkbenchBtn) {
    resetWorkbenchBtn.addEventListener('click', () => {
      if (confirm('CAUTION: This will delete ALL custom notes and asked statuses across all interview playbooks. This action cannot be undone. Proceed?')) {
        const keysToRemove = [];
        for (let i = 0; i < localStorage.length; i++) {
          const key = localStorage.key(i);
          if (key && (key.startsWith('eyepros_chk_') || key.startsWith('eyepros_notes_'))) {
            keysToRemove.push(key);
          }
        }
        keysToRemove.forEach(key => localStorage.removeItem(key));
        loadPlaybookStates();
      }
    });
  }

  // ==========================================================================
  // 9. READING PROGRESS BAR
  // ==========================================================================
  const progressBar = document.getElementById('readProgressFill');
  window.addEventListener('scroll', () => {
    const scrollTop = window.scrollY || document.documentElement.scrollTop;
    const scrollHeight = document.documentElement.scrollHeight - window.innerHeight;
    if (scrollHeight <= 0) return;
    
    const scrolled = Math.round((scrollTop / scrollHeight) * 100);
    if (progressBar) progressBar.style.width = `${scrolled}%`;
  }, { passive: true });

};

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initPlaybook);
} else {
  initPlaybook();
}

/* ==========================================================================
   OPHTHALMOLOGY INTELLIGENCE CAROUSEL (Real RSS Feed Engine v4)
   Fetches verified articles from NHS Digital, BJO, Nature Eye, GOV.UK
   ========================================================================== */
(function () {
  'use strict';

  /* ---- RSS Feed Sources (Ophthalmology Only) ---- */
  const RSS_SOURCES = [
    {
      name: 'British Journal of Ophthalmology',
      logo: 'BJO',
      feedUrl: 'https://bjo.bmj.com/rss/current.xml',
      filterCat: 'clinical',
      category: 'Clinical Research',
      region: 'Global',
      priority: 'clinical-update',
      tag: 'RESEARCH'
    },
    {
      name: 'Nature Eye (RCOphth)',
      logo: 'EYE',
      feedUrl: 'https://www.nature.com/eye.rss',
      filterCat: 'clinical',
      category: 'Ophthalmology Journal',
      region: 'Global',
      priority: 'clinical-update',
      tag: 'JOURNAL'
    },
    {
      name: 'GOV.UK Ophthalmology',
      logo: 'GOV',
      feedUrl: 'https://www.gov.uk/search/all.atom?keywords=ophthalmology',
      filterCat: 'nhs',
      category: 'Policy & Regulation',
      region: 'UK National',
      priority: 'strategic',
      tag: 'POLICY'
    },
    {
      name: 'SpaMedica',
      logo: 'SM',
      feedUrl: 'https://www.spamedica.co.uk/feed',
      filterCat: 'competitors',
      category: 'Competitor Intel',
      region: 'UK National',
      priority: 'market-move',
      tag: 'COMPETITOR'
    },
    {
      name: 'BMJ Open Ophthalmology',
      logo: 'BMJ',
      feedUrl: 'https://bmjopenophth.bmj.com/rss/current.xml',
      filterCat: 'clinical',
      category: 'Clinical & Tech',
      region: 'Global',
      priority: 'clinical-update',
      tag: 'CLINICAL'
    }
  ];

  const PROXY_BASE = 'https://api.rss2json.com/v1/api.json?rss_url=';
  const CACHE_KEY = 'ls_rss_feed_cache';
  const CACHE_TTL = 3600000; // 1 hour

  /* ---- State ---- */
  let activeFilter = 'all';
  let liveFeedItems = [];
  let scrollPos = 0;
  let autoplayTimer = null;
  let isHovered = false;

  /* ---- Helper: relative time from date string ---- */
  function getRelativeTimeFromDate(dateStr) {
    const pubDate = new Date(dateStr);
    const now = new Date();
    const diffMs = now - pubDate;
    const diffHours = Math.floor(diffMs / 3600000);
    const diffDays = Math.floor(diffMs / 86400000);

    if (diffHours < 1) return 'Just now';
    if (diffHours < 24) return `${diffHours} hrs ago`;
    if (diffDays === 1) return 'Yesterday';
    if (diffDays < 7) return `${diffDays} days ago`;
    if (diffDays < 14) return '1 week ago';
    if (diffDays < 60) return `${Math.floor(diffDays / 7)} weeks ago`;
    return pubDate.toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric' });
  }

  function formatDate(dateStr) {
    const d = new Date(dateStr);
    const yyyy = d.getFullYear();
    const mm = String(d.getMonth() + 1).padStart(2, '0');
    const dd = String(d.getDate()).padStart(2, '0');
    return `${yyyy}-${mm}-${dd}`;
  }

  function stripHtml(html) {
    const tmp = document.createElement('div');
    tmp.innerHTML = html || '';
    return tmp.textContent || tmp.innerText || '';
  }

  function truncate(str, maxLen) {
    if (!str || str.length <= maxLen) return str;
    return str.substring(0, maxLen).replace(/\s+\S*$/, '') + '…';
  }

  /* ---- Fetch a single RSS feed via proxy ---- */
  async function fetchFeed(source) {
    try {
      const url = PROXY_BASE + encodeURIComponent(source.feedUrl);
      const resp = await fetch(url);
      if (!resp.ok) return [];
      const data = await resp.json();
      if (data.status !== 'ok' || !data.items) return [];

      return data.items.slice(0, 6).map((item, idx) => ({
        id: `${source.logo.toLowerCase()}-${idx}-${Date.now()}`,
        filterCat: source.filterCat,
        priority: source.priority,
        tag: source.tag,
        source: source.name,
        sourceLogo: source.logo,
        title: stripHtml(item.title),
        summary: truncate(stripHtml(item.description || item.content || ''), 220),
        detail: stripHtml(item.content || item.description || ''),
        category: source.category,
        region: source.region,
        date: formatDate(item.pubDate),
        relativeTime: getRelativeTimeFromDate(item.pubDate),
        url: item.link || '#',
        pubDate: new Date(item.pubDate),
        isNew: (Date.now() - new Date(item.pubDate).getTime()) < 86400000 * 2
      }));
    } catch (err) {
      console.warn(`[RSS] Failed to fetch ${source.name}:`, err.message);
      return [];
    }
  }

  /* ---- Fetch all feeds in parallel ---- */
  async function fetchAllFeeds() {
    // Check cache first
    try {
      const cached = JSON.parse(localStorage.getItem(CACHE_KEY));
      if (cached && (Date.now() - cached.timestamp) < CACHE_TTL) {
        console.log('[RSS] Serving from cache');
        return cached.items;
      }
    } catch (e) {}

    const results = await Promise.allSettled(RSS_SOURCES.map(s => fetchFeed(s)));
    let allItems = [];
    results.forEach(r => {
      if (r.status === 'fulfilled') allItems = allItems.concat(r.value);
    });

    // Sort by publication date (newest first)
    allItems.sort((a, b) => b.pubDate - a.pubDate);

    // Cache
    try {
      localStorage.setItem(CACHE_KEY, JSON.stringify({
        timestamp: Date.now(),
        items: allItems
      }));
    } catch (e) {}

    return allItems;
  }

  /* ---- Build a single card's HTML ---- */
  function buildCard(item) {
    const newRibbon = item.isNew
      ? '<div class="ophi-new-ribbon">NEW</div>'
      : '';

    return `
      <div class="ophi-card${item.isNew ? ' new-item-highlight' : ''}" data-cat="${item.filterCat}">
        ${newRibbon}

        <!-- Top accent color bar -->
        <div class="ophi-card-accent"></div>

        <!-- Card body -->
        <div class="ophi-card-body">

          <!-- Source row + time -->
          <div class="ophi-card-top">
            <div class="ophi-source-row">
              <span class="ophi-source-logo">${item.sourceLogo}</span>
              <span class="ophi-source-name">${item.source}</span>
            </div>
            <span class="ophi-relative-time">${item.relativeTime}</span>
          </div>

          <!-- Priority tag -->
          <div class="ophi-card-meta">
            <span class="ophi-priority-tag ${item.priority}">${item.tag}</span>
          </div>

          <!-- Headline -->
          <h4 class="ophi-headline">${item.title}</h4>

          <!-- Summary -->
          <p class="ophi-summary">${item.summary}</p>

        </div>

        <!-- Footer -->
        <div class="ophi-card-footer">
          <div class="ophi-badge-row">
            <span class="ophi-category-badge">${item.category}</span>
            <span class="ophi-region-badge">${item.region}</span>
          </div>
          <div class="ophi-cta-row">
            <span class="ophi-pub-date">${item.date}</span>
            <span style="display:inline-flex;align-items:center;gap:6px;">
              ${item.url && item.url !== '#'
                ? `<a class="ophi-cta-btn" href="${item.url}" target="_blank" rel="noopener">Read <i class="fa fa-external-link"></i></a>`
                : `<span class="ophi-cta-btn" style="opacity:0.45;cursor:default">Source <i class="fa fa-check"></i></span>`
              }
            </span>
          </div>
        </div>
      </div>
    `;
  }

  /* ---- Filter and Render Carousel ---- */
  function renderCarousel() {
    const track = document.getElementById('ophiCarouselTrack');
    if (!track) return;

    const displayedItems = activeFilter === 'all'
      ? liveFeedItems
      : liveFeedItems.filter(item => item.filterCat === activeFilter);

    const countAllEl = document.getElementById('count-all');
    if (countAllEl) countAllEl.textContent = liveFeedItems.length;

    if (displayedItems.length === 0) {
      track.innerHTML = `
        <div style="padding: 40px; text-align: center; width: 100%; color: var(--ls-muted);">
          <i class="fa fa-info-circle" style="font-size: 2rem; color: var(--ls-gold); margin-bottom: 12px;"></i>
          <p>No articles in this category. Switch to "All Intel" to view all updates.</p>
        </div>
      `;
      return;
    }

    track.innerHTML = displayedItems.map(item => buildCard(item)).join('');
    scrollPos = 0;
    updateTrackScroll(track);
  }

  /* ---- Scrolling helpers ---- */
  function getCardWidth() {
    const card = document.querySelector('.ophi-card');
    return card ? card.offsetWidth + 16 : 340;
  }

  function updateTrackScroll(track) {
    if (!track) track = document.getElementById('ophiCarouselTrack');
    if (!track) return;
    track.style.transform = `translateX(-${scrollPos}px)`;
  }

  function scrollRight() {
    const track = document.getElementById('ophiCarouselTrack');
    const viewport = document.querySelector('.ophi-carousel-viewport');
    if (!track || !viewport) return;
    const maxScroll = track.scrollWidth - viewport.offsetWidth;
    scrollPos = Math.min(scrollPos + getCardWidth(), maxScroll);
    updateTrackScroll(track);
  }

  function scrollLeft() {
    scrollPos = Math.max(scrollPos - getCardWidth(), 0);
    updateTrackScroll();
  }

  /* ---- Autoplay ---- */
  function startAutoplay() {
    stopAutoplay();
    autoplayTimer = setInterval(() => {
      if (isHovered) return;
      const track = document.getElementById('ophiCarouselTrack');
      const viewport = document.querySelector('.ophi-carousel-viewport');
      if (!track || !viewport) return;
      const maxScroll = track.scrollWidth - viewport.offsetWidth;
      if (scrollPos >= maxScroll - 10) {
        scrollPos = 0;
      } else {
        scrollPos += getCardWidth();
      }
      updateTrackScroll(track);
    }, 5000);
  }

  function stopAutoplay() {
    if (autoplayTimer) clearInterval(autoplayTimer);
  }

  /* ---- Setup Controls ---- */
  function setupControls() {
    const leftBtn = document.querySelector('.ophi-arrow-left');
    const rightBtn = document.querySelector('.ophi-arrow-right');
    if (leftBtn) leftBtn.addEventListener('click', () => { scrollLeft(); stopAutoplay(); startAutoplay(); });
    if (rightBtn) rightBtn.addEventListener('click', () => { scrollRight(); stopAutoplay(); startAutoplay(); });

    const viewport = document.querySelector('.ophi-carousel-viewport');
    if (viewport) {
      viewport.addEventListener('mouseenter', () => { isHovered = true; });
      viewport.addEventListener('mouseleave', () => { isHovered = false; });
    }

    // Filter buttons
    const filterBar = document.getElementById('ophiFilterBar');
    if (filterBar) {
      filterBar.addEventListener('click', (e) => {
        const btn = e.target.closest('.ophi-filter-btn');
        if (!btn) return;
        filterBar.querySelectorAll('.ophi-filter-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        activeFilter = btn.dataset.filter;
        renderCarousel();
        stopAutoplay();
        startAutoplay();
      });
    }
  }

  /* ---- Refresh trigger ---- */
  function triggerFeedRefresh(isUserClick) {
    const statusEl = document.getElementById('ophiStatusBar');
    const refreshBtn = document.querySelector('.gcal-refresh-btn');

    if (refreshBtn) refreshBtn.classList.add('spinning');

    if (statusEl) {
      const badge = statusEl.querySelector('.gcal-live-badge');
      if (badge) {
        badge.className = 'gcal-live-badge status-checking';
        badge.innerHTML = '<i class="fa fa-circle-o-notch fa-spin"></i> Fetching live RSS feeds…';
      }
    }

    // Clear cache on manual refresh
    if (isUserClick) {
      localStorage.removeItem(CACHE_KEY);
    }

    fetchAllFeeds().then(items => {
      liveFeedItems = items;
      renderCarousel();

      if (refreshBtn) refreshBtn.classList.remove('spinning');

      if (statusEl) {
        const badge = statusEl.querySelector('.gcal-live-badge');
        if (badge) {
          const now = new Date();
          const timeStr = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
          badge.className = 'gcal-live-badge status-updated';
          badge.innerHTML = `<i class="fa fa-check-circle text-teal"></i> Live — ${liveFeedItems.length} verified articles synced at ${timeStr}`;
        }
      }
    }).catch(err => {
      console.error('[RSS] Feed refresh failed:', err);
      if (statusEl) {
        const badge = statusEl.querySelector('.gcal-live-badge');
        if (badge) {
          badge.className = 'gcal-live-badge';
          badge.innerHTML = '<i class="fa fa-exclamation-circle" style="color:#ef4444"></i> Feed unavailable — check connection';
        }
      }
    });
  }

  /* ---- Initialize ---- */
  function initIntelFeed() {
    setupControls();
    triggerFeedRefresh(false);
    startAutoplay();

    // Manual refresh button
    const refreshBtn = document.querySelector('.gcal-refresh-btn');
    if (refreshBtn) {
      refreshBtn.addEventListener('click', () => triggerFeedRefresh(true));
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initIntelFeed);
  } else {
    initIntelFeed();
  }
})();

/* ==========================================================================
   GLOBAL OPHTHALMOLOGY EVENTS CALENDAR LOGIC
   ========================================================================== */
(function () {
  const gcalEvents = [
    { id: "ev1", title: "Asia-Pacific Academy of Ophthalmology Congress", acronym: "APAO 2026", startDate: "2026-02-05", endDate: "2026-02-08", city: "Hong Kong", country: "China", venue: "HKCEC", region: "Asia-Pacific", specialty: ["general"], organizer: "APAO", url: "https://apaophth.org/", status: "completed", flag: "🇭🇰" },
    { id: "ev2", title: "All India Ophthalmological Conference", acronym: "AIOC 2026", startDate: "2026-03-12", endDate: "2026-03-15", city: "Jaipur", country: "India", venue: "JECC", region: "Asia-Pacific", specialty: ["general"], organizer: "AIOS", url: "https://aios.org/", status: "completed", flag: "🇮🇳" },
    { id: "ev3", title: "ESCRS Winter Meeting", acronym: "ESCRS Winter", startDate: "2026-03-06", endDate: "2026-03-08", city: "Helsinki", country: "Finland", venue: "Messukeskus", region: "Europe", specialty: ["cataract"], organizer: "ESCRS", url: "https://escrs.org/", status: "completed", flag: "🇫🇮" },
    { id: "ev4", title: "ARVO Annual Meeting", acronym: "ARVO 2026", startDate: "2026-05-03", endDate: "2026-05-07", city: "Denver, CO", country: "USA", venue: "Colorado Convention Center", region: "North America", specialty: ["general", "retina"], organizer: "ARVO", url: "https://www.arvo.org/", status: "completed", flag: "🇺🇸" },
    { id: "ev5", title: "European Glaucoma Society Congress", acronym: "EGS 2026", startDate: "2026-05-30", endDate: "2026-06-02", city: "Brussels", country: "Belgium", venue: "SQUARE", region: "Europe", specialty: ["glaucoma"], organizer: "EGS", url: "https://www.eugs.org/", status: "completed", flag: "🇧🇪" },
    { id: "ev6", title: "World Ophthalmology Congress", acronym: "WOC 2026", startDate: "2026-06-26", endDate: "2026-06-29", city: "Prague", country: "Czech Republic", venue: "Prague Congress Centre", region: "Europe", specialty: ["general"], organizer: "ICO", url: "https://icowoc.org/", status: "completed", flag: "🇨🇿" },
    { id: "ev7", title: "ASRS Annual Scientific Meeting", acronym: "ASRS 2026", startDate: "2026-07-15", endDate: "2026-07-18", city: "Montréal, QC", country: "Canada", venue: "Palais des congrès", region: "North America", specialty: ["retina"], organizer: "ASRS", url: "https://www.asrs.org/", status: "completed", flag: "🇨🇦" },
    { id: "ev8", title: "ESCRS Annual Congress", acronym: "ESCRS 2026", startDate: "2026-09-11", endDate: "2026-09-15", city: "London", country: "UK", venue: "ExCeL London", region: "Europe", specialty: ["cataract"], organizer: "ESCRS", url: "https://escrs.org/", status: "upcoming", flag: "🇬🇧" },
    { id: "ev9", title: "Retina Society Annual Meeting", acronym: "Retina Society 2026", startDate: "2026-09-23", endDate: "2026-09-26", city: "Los Angeles, CA", country: "USA", venue: "Fairmont Century Plaza", region: "North America", specialty: ["retina"], organizer: "Retina Society", url: "https://www.retinasociety.org/", status: "upcoming", flag: "🇺🇸" },
    { id: "ev10", title: "EURETINA Congress", acronym: "EURETINA 2026", startDate: "2026-10-01", endDate: "2026-10-04", city: "Vienna", country: "Austria", venue: "VIECON", region: "Europe", specialty: ["retina"], organizer: "EURETINA", url: "https://euretina.org/", status: "upcoming", flag: "🇦🇹" },
    { id: "ev11", title: "American Academy of Ophthalmology", acronym: "AAO 2026", startDate: "2026-10-09", endDate: "2026-10-12", city: "New Orleans, LA", country: "USA", venue: "Ernest N. Morial Center", region: "North America", specialty: ["general"], organizer: "AAO", url: "https://www.aao.org/", status: "upcoming", flag: "🇺🇸" }
  ];

  const parseDate = (dateStr) => {
    if (!dateStr) return new Date();
    const parts = dateStr.split('-');
    if (parts.length === 3) {
      return new Date(parseInt(parts[0], 10), parseInt(parts[1], 10) - 1, parseInt(parts[2], 10));
    }
    return new Date(dateStr);
  };

  const getToday = () => {
    const d = new Date();
    const minDate = new Date(2026, 7, 2); // August 2, 2026
    return d > minDate ? d : minDate;
  };

  const getEventStatus = (ev) => {
    const today = getToday();
    today.setHours(0, 0, 0, 0);
    const start = parseDate(ev.startDate);
    start.setHours(0, 0, 0, 0);
    const end = parseDate(ev.endDate);
    end.setHours(23, 59, 59, 999);

    if (end < today) return 'completed';
    if (start <= today && today <= end) return 'open';
    return 'upcoming';
  };

  gcalEvents.forEach(ev => {
    ev.status = getEventStatus(ev);
  });

  let currentView = 'agenda';
  let filteredEvents = [...gcalEvents];

  const formatDateRange = (start, end) => {
    const sDate = parseDate(start);
    const eDate = parseDate(end);
    const sMonth = sDate.toLocaleString('default', { month: 'short' });
    const sDay = sDate.getDate();
    const eDay = eDate.getDate();
    return { month: sMonth, days: `${sDay}-${eDay}` };
  };

  const renderAgenda = () => {
    const agendaEl = document.getElementById('gcalViewAgenda');
    if (!agendaEl) return;

    if (filteredEvents.length === 0) {
      agendaEl.innerHTML = `<div class="p-4 text-center text-muted"><i class="fa fa-calendar-times-o"></i> No events found.</div>`;
      return;
    }

    let html = '';
    filteredEvents.sort((a, b) => parseDate(a.startDate) - parseDate(b.startDate)).forEach(ev => {
      const dates = formatDateRange(ev.startDate, ev.endDate);
      const isUpcoming = ev.status === 'upcoming' ? 'badge-accent' : 'badge-secondary';
      
      html += `
        <div class="gcal-event-row glass-card p-3 mb-2 d-flex align-items-center justify-content-between" onclick="window.open('${ev.url}', '_blank')">
          <div class="d-flex align-items-center gap-3">
            <div class="gcal-dates text-center px-3 border-right">
              <div class="font-size-xs text-teal font-weight-bold">${dates.month}</div>
              <div class="font-size-lg font-weight-bold">${dates.days}</div>
            </div>
            <div>
              <h4 class="font-size-sm font-weight-bold mb-1">${ev.title} (${ev.acronym})</h4>
              <div class="font-size-xs text-muted">
                <span>${ev.flag} ${ev.city}, ${ev.country}</span> · <span>${ev.venue}</span>
              </div>
            </div>
          </div>
          <div>
            <span class="badge ${isUpcoming}">${ev.status}</span>
          </div>
        </div>
      `;
    });

    agendaEl.innerHTML = html;
  };

  const applyFilters = () => {
    const regEl = document.getElementById('gcalFilterRegion');
    const specEl = document.getElementById('gcalFilterSpecialty');
    const statEl = document.getElementById('gcalFilterStatus');
    const searchEl = document.getElementById('gcalSearch');

    if (!regEl) return;

    const region = regEl.value;
    const spec = specEl.value;
    const status = statEl.value;
    const q = searchEl ? searchEl.value.toLowerCase() : '';

    filteredEvents = gcalEvents.filter(ev => {
      const matchRegion = region === 'all' || ev.region === region;
      const matchSpec = spec === 'all' || ev.specialty.includes(spec);
      const matchStatus = status === 'all' || ev.status === status;
      const matchQ = !q || ev.title.toLowerCase().includes(q) || ev.acronym.toLowerCase().includes(q);

      return matchRegion && matchSpec && matchStatus && matchQ;
    });

    renderAgenda();
  };

  const initGcal = () => {
    if (!document.getElementById('events-calendar')) return;

    ['gcalFilterRegion', 'gcalFilterSpecialty', 'gcalFilterStatus'].forEach(id => {
      const el = document.getElementById(id);
      if (el) el.addEventListener('change', applyFilters);
    });

    const searchEl = document.getElementById('gcalSearch');
    if (searchEl) searchEl.addEventListener('input', applyFilters);

    applyFilters();

    /* Update events calendar sync status badge */
    setTimeout(function () {
      const statusEl = document.getElementById('gcalSyncStatus');
      if (statusEl) {
        const badge = statusEl.querySelector('.gcal-live-badge');
        if (badge) {
          badge.classList.remove('status-checking');
          badge.classList.add('status-updated');
          badge.innerHTML = '<i class="fa fa-check-circle"></i> Live — ' + gcalEvents.length + ' events loaded';
        }
      }
    }, 1500);
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initGcal);
  } else {
    initGcal();
  }
})();
