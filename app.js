/**
 * EyePros Command Hub Engine
 * Unified JavaScript Engine
 */

const initApp = () => {

  // ==========================================================================
  // 1. ZONE ROUTER
  // ==========================================================================
  const validZones = ['dashboard', 'playbook', 'studio', 'workbench', 'calendar'];

  function getZoneForElement(el) {
    const panel = el.closest('.zone-panel');
    if (panel && panel.id) {
      // Return the zone name without 'zone-' if it has it, otherwise just the id
      return panel.id.replace(/^zone-/, '');
    }
    return null;
  }

  function navigateToZone(zoneName) {
    if (!validZones.includes(zoneName)) zoneName = 'dashboard';
    
    // Hide all, show matching
    document.querySelectorAll('.zone-panel').forEach(panel => {
      if (panel.id === zoneName || panel.id === `zone-${zoneName}`) {
        panel.style.display = 'block';
        panel.classList.add('active');
      } else {
        panel.style.display = 'none';
        panel.classList.remove('active');
      }
    });

    // Update sidebar active state
    document.querySelectorAll('.app-sidebar .nav-item, .app-sidebar .sidebar-nav-link').forEach(nav => {
      nav.classList.remove('active');
      if (nav.getAttribute('href') === `#${zoneName}`) {
        nav.classList.add('active');
      }
    });

    // Update bottom-tab-bar active state
    document.querySelectorAll('.bottom-tab-bar .tab-item').forEach(tab => {
      tab.classList.remove('active');
      if (tab.getAttribute('href') === `#${zoneName}`) {
        tab.classList.add('active');
      }
    });

    // Update header breadcrumb
    const breadcrumb = document.getElementById('headerBreadcrumb');
    if (breadcrumb) {
      breadcrumb.textContent = zoneName.charAt(0).toUpperCase() + zoneName.slice(1);
    }

    // Scroll zone content to top
    const appContent = document.querySelector('.app-content');
    if (appContent) {
      appContent.scrollTop = 0;
    } else {
      window.scrollTo(0, 0);
    }
  }

  window.addEventListener('hashchange', () => {
    const hash = window.location.hash.replace('#', '') || 'dashboard';
    navigateToZone(hash);
  });

  // Initial load
  const initialHash = window.location.hash.replace('#', '') || 'dashboard';
  navigateToZone(initialHash);

  // Set hash on click
  document.querySelectorAll('.app-sidebar .nav-item, .app-sidebar .sidebar-nav-link, .bottom-tab-bar .tab-item').forEach(el => {
    el.addEventListener('click', (e) => {
      const href = el.getAttribute('href');
      if (href && href.startsWith('#')) {
        window.location.hash = href;
      }
    });
  });

  // ==========================================================================
  // 2. SIDEBAR TOGGLE
  // ==========================================================================
  const sidebar = document.querySelector('.app-sidebar');
  const sidebarToggleBtn = document.getElementById('sidebarToggleBtn');
  const appShell = document.querySelector('.app-shell');
  
  // Restore state
  const isCollapsed = localStorage.getItem('eyepros-sidebar-collapsed') === 'true';
  if (isCollapsed && sidebar) {
    sidebar.classList.add('collapsed');
  }

  if (sidebarToggleBtn) {
    sidebarToggleBtn.addEventListener('click', () => {
      if (window.innerWidth <= 768) {
        if (appShell) appShell.classList.toggle('sidebar-open');
      } else {
        if (sidebar) {
          sidebar.classList.toggle('collapsed');
          localStorage.setItem('eyepros-sidebar-collapsed', sidebar.classList.contains('collapsed'));
        }
      }
    });
  }

  // Close sidebar on mobile when a nav item is clicked
  document.querySelectorAll('.app-sidebar .nav-item, .app-sidebar .sidebar-nav-link').forEach(link => {
    link.addEventListener('click', () => {
      if (window.innerWidth <= 768 && appShell) {
        appShell.classList.remove('sidebar-open');
      }
    });
  });

  // ==========================================================================
  // 3. INTERNSHIP DAY COUNTER
  // ==========================================================================
  function updateDayCounter() {
    const widget = document.getElementById('countdownWidget');
    if (!widget) return;
    
    const start = new Date('2026-08-01T00:00:00');
    const end = new Date('2026-12-18T23:59:59');
    const today = new Date();
    
    const totalDiff = end - start;
    const currentDiff = today - start;
    
    const totalDays = Math.ceil(totalDiff / (1000 * 60 * 60 * 24));
    let currentDay = Math.floor(currentDiff / (1000 * 60 * 60 * 24)) + 1;
    
    if (currentDay > totalDays) currentDay = totalDays;
    if (currentDay < 1) currentDay = 1;
    
    const percent = Math.min(100, Math.max(0, (currentDay / totalDays) * 100));
    
    widget.innerHTML = `
      <div class="day-counter text-center" style="padding: 10px 0;">
        <div style="font-weight: 700; color: var(--color-primary, #0d9488); font-size: 1.1rem; margin-bottom: 8px;">
          Day ${currentDay} of ${totalDays}
        </div>
        <div class="progress-bar-wrap" style="width: 100%; background: var(--bg-secondary, #eee); height: 8px; border-radius: 4px; overflow: hidden;">
          <div style="width: ${percent}%; background: var(--color-primary, #0d9488); height: 100%; transition: width 0.3s ease;"></div>
        </div>
      </div>
    `;
  }
  updateDayCounter();

  // ==========================================================================
  // 4. THEME CONTROLLER
  // ==========================================================================
  const themeToggleBtn = document.getElementById('themeToggleBtn');
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

  // ==========================================================================
  // 5. COMMAND PALETTE (ENHANCED)
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
      { selector: '.gcal-event-row', cat: 'Events', getTitle: el => el.querySelector('h4')?.textContent || '', getDesc: el => el.querySelector('.gcal-location')?.textContent || '' },
      { selector: '.film-script-item, .studio-item', cat: 'Studio', getTitle: el => el.querySelector('h3, h4')?.textContent || '', getDesc: el => el.querySelector('p')?.textContent || '' }
    ];

    searchableItems.forEach(item => {
      if (activeCategory !== 'all' && activeCategory !== item.cat) return;

      document.querySelectorAll(item.selector).forEach((el, index) => {
        const title = item.getTitle(el).trim();
        const desc = item.getDesc(el).trim();
        const fullText = (title + ' ' + desc).toLowerCase();

        if (!q || fullText.includes(q)) {
          // Assign unique target ID if missing
          if (!el.id) el.id = `cmd_target_${item.cat.replace(/\s+/g, '')}_${index}`;
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

    // Detect zone and navigate
    const zoneName = getZoneForElement(targetEl);
    if (zoneName) {
      window.location.hash = zoneName;
    }

    // Open parent accordion panel or tab if in Workbench
    const parentPanel = targetEl.closest('.workbench-persona-panel');
    if (parentPanel) {
      const persona = parentPanel.id.replace('panel', '').toLowerCase();
      switchPersonaTab(persona);
    }

    // Smooth scroll with delay for zone render
    setTimeout(() => {
      const appContent = document.querySelector('.app-content');
      if (appContent) {
        // Find relative offset
        const topPos = targetEl.offsetTop - 20; 
        appContent.scrollTo({ top: topPos, behavior: 'smooth' });
      } else {
        const targetTop = targetEl.getBoundingClientRect().top + window.scrollY - 95;
        window.scrollTo({ top: targetTop, behavior: 'smooth' });
      }

      // Flash Teal Highlight
      targetEl.classList.remove('search-highlight-flash');
      void targetEl.offsetWidth; // Trigger reflow
      targetEl.classList.add('search-highlight-flash');
    }, 50);
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
  // 8. UNIFIED INTERVIEW WORKBENCH
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
  const appContent = document.querySelector('.app-content');
  if (appContent) {
    appContent.addEventListener('scroll', () => {
      const scrollTop = appContent.scrollTop;
      const scrollHeight = appContent.scrollHeight - appContent.clientHeight;
      if (scrollHeight <= 0) return;
      
      const scrolled = Math.round((scrollTop / scrollHeight) * 100);
      if (progressBar) progressBar.style.width = `${scrolled}%`;
    }, { passive: true });
  } else {
    window.addEventListener('scroll', () => {
      const scrollTop = window.scrollY || document.documentElement.scrollTop;
      const scrollHeight = document.documentElement.scrollHeight - window.innerHeight;
      if (scrollHeight <= 0) return;
      
      const scrolled = Math.round((scrollTop / scrollHeight) * 100);
      if (progressBar) progressBar.style.width = `${scrolled}%`;
    }, { passive: true });
  }

  // ==========================================================================
  // 12. PRINT HANDLER
  // ==========================================================================
  const printBtn = document.getElementById('printBtn');
  if (printBtn) {
    printBtn.addEventListener('click', () => {
      window.print();
    });
  }

  // ==========================================================================
  // 13. HERO COLLAPSIBLE
  // ==========================================================================
  const toggleAboutBtn = document.getElementById('toggleAboutPlaybookBtn');
  const aboutContent = document.getElementById('aboutPlaybookContent');

  if (toggleAboutBtn && aboutContent) {
    toggleAboutBtn.addEventListener('click', () => {
      aboutContent.classList.toggle('open');
      const isExpanded = aboutContent.classList.contains('open');
      const chevron = toggleAboutBtn.querySelector('.chevron-icon');
      if (chevron) {
        chevron.style.transform = isExpanded ? 'rotate(180deg)' : 'rotate(0deg)';
      }
    });
  }

};

// Initialize App
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initApp);
} else {
  initApp();
}

/* ==========================================================================
   10. CAROUSEL ENGINE (SWR Feed Engine)
   ========================================================================== */
(function () {
  const newsItems = [
    { tag: 'NHS POLICY', title: 'NHS Outpatient Backlogs Driver for Self-Pay Ophthalmology', summary: 'Outpatient backlog tracking shows continuous demand for independent sector cataract procedures in the Midlands.', date: 'Just Now', source: 'Health Policy Journal' },
    { tag: 'COMMISSIONING', title: 'Nottinghamshire ICB Reviews Community Eyecare Pathways', summary: 'Commissioning framework highlights collaborative opportunities for Tier 2 independent surgical providers.', date: 'Today', source: 'NHS Commissioning' },
    { tag: 'TECHNOLOGY', title: 'Photobiomodulation Valeda System Clinical Results', summary: 'Multi-center clinical trials validate light therapy for slowing progression in Dry AMD patients.', date: 'Yesterday', source: 'Ophthalmology Times' },
    { tag: 'SURGICAL', title: 'MIGS Micro-Stent Adoption Accelerates in UK', summary: 'Minimally Invasive Glaucoma Surgery expands across private clinics as patients seek drop-free pressure management.', date: '2 days ago', source: 'Eye News UK' }
  ];

  function renderCarousel() {
    const track = document.getElementById('ophiCarouselTrack');
    if (!track) return;

    let html = '';
    newsItems.forEach(item => {
      html += `
        <div class="ophi-card glass-card p-4 mr-3" style="flex: 0 0 300px;">
          <span class="badge badge-accent mb-2">${item.tag}</span>
          <h4 class="font-size-sm font-weight-bold mb-2">${item.title}</h4>
          <p class="font-size-xs text-secondary mb-3">${item.summary}</p>
          <div class="d-flex justify-content-between font-size-xs text-muted">
            <span><i class="fa fa-clock-o"></i> ${item.date}</span>
            <span><i class="fa fa-rss"></i> ${item.source}</span>
          </div>
        </div>
      `;
    });
    track.innerHTML = html;

    const prevBtn = document.getElementById('ophiPrevBtn');
    const nextBtn = document.getElementById('ophiNextBtn');

    if (prevBtn) {
      prevBtn.addEventListener('click', () => {
        track.scrollBy({ left: -320, behavior: 'smooth' });
      });
    }
    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        track.scrollBy({ left: 320, behavior: 'smooth' });
      });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', renderCarousel);
  } else {
    renderCarousel();
  }
})();

/* ==========================================================================
   11. EVENTS CALENDAR LOGIC
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
    // Only init if filter elements exist
    const regEl = document.getElementById('gcalFilterRegion');
    if (!regEl) return;

    ['gcalFilterRegion', 'gcalFilterSpecialty', 'gcalFilterStatus'].forEach(id => {
      const el = document.getElementById(id);
      if (el) el.addEventListener('change', applyFilters);
    });

    const searchEl = document.getElementById('gcalSearch');
    if (searchEl) searchEl.addEventListener('input', applyFilters);

    applyFilters();
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initGcal);
  } else {
    initGcal();
  }
})();
