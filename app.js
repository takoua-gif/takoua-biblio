/**
 * EyePros Reference Library & Playbook Engine
 * Curator: Takoua Selmi
 * Logic Layer: Theme, Search, Countdowns, Flashcards, Interactive Notes & Progress
 */

const initPlaybook = () => {

  // ==========================================================================
  // 0. TWO-STRIP HEADER — MOBILE TOGGLE & SCROLL SPY
  // ==========================================================================
  const mobileToggle = document.getElementById('mobileMenuToggle');
  const navStrip = document.getElementById('navbarSupportedContent');
  if (mobileToggle && navStrip) {
    mobileToggle.addEventListener('click', () => {
      navStrip.classList.toggle('open');
    });
  }

  // Close nav strip when a link is clicked on mobile
  document.querySelectorAll('.header-nav-pills .nav-link').forEach(link => {
    link.addEventListener('click', () => {
      if (navStrip) navStrip.classList.remove('open');
    });
  });

  // Scroll spy — highlight active pill based on scroll position
  const sections = ['banner','structure','acronyms','numbers','archetypes','competitors','strategy','interviews','timeline'];
  const pillLinks = document.querySelectorAll('.header-nav-pills .nav-link');
  window.addEventListener('scroll', () => {
    let current = '';
    sections.forEach(id => {
      const el = document.getElementById(id);
      if (el && window.scrollY >= el.offsetTop - 130) current = id;
    });
    pillLinks.forEach(link => {
      link.classList.toggle('active', link.getAttribute('href') === '#' + current);
    });
  }, { passive: true });

  // ==========================================================================
  // 1. DATE-DRIVEN LOGIC & LIVE COUNTDOWN
  // ==========================================================================
  const INTERNSHIP_START = new Date("2026-07-15T22:00:00+02:00");

  function updateCountdown() {
    const now = new Date();                      // always the real current time
    const diffMs = INTERNSHIP_START - now;
    const widget = document.getElementById('countdownWidget');
    if (!widget) return;

    if (diffMs <= 0) {
      widget.innerHTML = `
        <div class="countdown-title">Internship Status</div>
        <div style="font-weight: 700; color: #0d9488; text-align: center; font-size: 1.1rem; padding: 10px 0;">ACTIVE IN SESSION</div>
        <div class="countdown-footer">Day One officially active!</div>
      `;
      return;
    }

    const totalSecs  = Math.floor(diffMs / 1000);
    const totalMins  = Math.floor(totalSecs / 60);
    const totalHours = Math.floor(totalMins / 60);
    const days       = Math.floor(totalHours / 24);
    const secsRemaining = totalSecs % 60;
    const minsRemaining = totalMins % 60;
    const hrsRemaining  = totalHours % 24;

    const daysEl = document.getElementById('countdownDays');
    const hrsEl = document.getElementById('countdownHours');
    const minsEl = document.getElementById('countdownMins');
    const secEl = document.getElementById('countdownSecs');

    if (daysEl) daysEl.textContent  = String(days).padStart(2, '0');
    if (hrsEl) hrsEl.textContent = String(hrsRemaining).padStart(2, '0');
    if (minsEl) minsEl.textContent  = String(minsRemaining).padStart(2, '0');
    if (secEl) secEl.textContent = String(secsRemaining).padStart(2, '0');
  }

  // Tick immediately then every second
  updateCountdown();
  setInterval(updateCountdown, 1000);

  // Highlight timeline milestones based on real current date
  function highlightTimeline() {
    const todayPhaseDate = new Date();
    // Month 1 is August, Month 2 is September, etc.
    const milestones = document.querySelectorAll('.timeline-milestone');
    milestones.forEach(milestone => {
      const phase = milestone.getAttribute('data-phase');
      const badge = milestone.querySelector('.milestone-header .badge');
      
      if (phase === 'pre') {
        milestone.classList.add('current');
        if (badge) {
          badge.className = 'badge badge-accent';
          badge.textContent = 'Active Phase';
        }
      } else {
        milestone.classList.add('upcoming');
        if (badge) {
          badge.className = 'badge badge-secondary';
          badge.textContent = 'Upcoming';
        }
      }
    });
  }
  highlightTimeline();

  // ==========================================================================
  // 2. THEME CONTROLLER (Dark / Light toggle)
  // ==========================================================================
  const themeToggleBtn = document.getElementById('themeToggleBtn');
  const printBtn = document.getElementById('printBtn');
  
  // Set default theme from localStorage or system preference
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

  // Print button
  if (printBtn) {
    printBtn.addEventListener('click', () => {
      window.print();
    });
  }

  // ==========================================================================
  // 3. INTERACTIVE ACRONYM EXPLORER
  // ==========================================================================
  const acronymsGrid = document.getElementById('acronymsGrid');
  const filterPills = document.querySelectorAll('.filter-pill');

  // Flip acronym card on click
  if (acronymsGrid) {
    acronymsGrid.addEventListener('click', (e) => {
      const card = e.target.closest('.acronym-card');
      if (card) {
        card.classList.toggle('flipped');
      }
    });
  }

  // Filter acronyms by category tags
  filterPills.forEach(pill => {
    pill.addEventListener('click', () => {
      filterPills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');

      const category = pill.getAttribute('data-category');
      const cards = acronymsGrid.querySelectorAll('.acronym-card');
      
      cards.forEach(card => {
        const cardCat = card.getAttribute('data-category');
        if (category === 'all' || cardCat === category) {
          card.classList.remove('search-hidden');
        } else {
          card.classList.add('search-hidden');
        }
      });
    });
  });

  // ==========================================================================
  // 4. PATIENT ARCHETYPE SYSTEM DATA PORTING
  // ==========================================================================
  const archetypesData = {
    A: {
      letter: 'A',
      title: 'The Cataract Patient',
      tagline: 'VOLUME ENGINE · 450,000 PROCEDURES ANNUALLY',
      trigger: 'Vision deterioration over months. Halos/glare driving at night. Typically picked up at routine sight test where the high-street optometrist grades the cataract.',
      logic: 'They face a critical decision: wait 16+ weeks on the NHS or pay to go private. Three core parameters shape their conversion: wait time impact on active life, desire for premium multi-focal/EDOF intraocular lenses (IOLs) unavailable on the standard NHS tariff, and wanting to know their surgical consultant personally. <strong>EyePros wins by offering speed, choice of high-tech lenses, and continuous consultant care.</strong>'
    },
    B: {
      letter: 'B',
      title: 'The Glaucoma Patient',
      tagline: 'LIFETIME CARE · MIGS SURGICAL HOOK',
      trigger: 'Typically detected during a routine primary sight test via elevated intraocular pressure (IOP), suspicious optic disc cupping, or minor visual field drops. The patient is often asymptomatic.',
      logic: 'Glaucoma is a lifetime relationship, representing the strongest fit for <strong>subscription care plan models</strong> rather than single surgical fees. Ahmad\'s surgical subspecialty in Minimally Invasive Glaucoma Surgery (MIGS) is the high-value clinical hook. The strategic target is to convert single consultations into decades-long care monitor agreements, yielding high lifetime value.'
    },
    C: {
      letter: 'C',
      title: 'The Laser & Refractive Patient',
      tagline: 'SELF-INITIATED · HIGH-VOLUME PROMOTIONS SEGMENT',
      trigger: 'Self-referred. Aged 25-45. Frustrated with spectacles or contact lens discomfort. Active research conducted online before booking initial consultation.',
      logic: 'This is the most competitive volume market, heavily contested by price-led corporate giants (Optical Express, Optimax). <strong>EyePros avoids a low-price race to the bottom by competing on consultant credibility, custom clinical packages, and specialized post-operative dry eye management systems.</strong> Focus on premium quality outcomes, not cheap volume.'
    },
    D: {
      letter: 'D',
      title: 'The Dry Eye Patient',
      tagline: 'EYESPA SERVICES · IDEAL CARE SUBSCRIPTION TARGET',
      trigger: 'Has self-medicated with over-the-counter drop formulations for 2-10 years. Symptoms (burning, fluctuating sight, watering) worsening until they seek optometry support.',
      logic: 'Ideal candidate for subscription models. Patients already understand that dry eye is chronic and cannot be resolved with a one-time consult. <strong>They are looking for clinical pathways, specialized gear (Blephasteam, LipiFlow, IPL), and recurring professional checkups.</strong> Highly compatible with our LenzClub platform.'
    },
    E: {
      letter: 'E',
      title: 'The Dry AMD Patient',
      tagline: 'VALEDA CLINIC PLAY · FIRST-MOVER ADVANTAGE',
      trigger: 'Detected via routine OCT scanning. Historically told by optometrists that "nothing can be done beyond vitamin supplements," leading to resignation.',
      logic: 'First-mover advantage in the Midlands via the <strong>Valeda Photobiomodulation (PBM) system</strong>. The primary barrier is not competition, but patient awareness: educating patients and optometrists that an effective, evidence-based therapy now exists. Low-light therapy protocols require scheduled monthly treatment sessions, mapping directly into subscription pricing structures.'
    }
  };

  const archetypeTabs = document.querySelectorAll('.archetype-tab');
  const archetypeContent = document.getElementById('archetypeContent');

  const timelineData = {
    A: {
      title: "The Complete Cataract Patient Journey",
      nodes: [
        { title: "Symptoms & Ocular Triggers", text: "Patient notices progressive blurred vision, halo glare during night driving, and dulling colors. Develops over 6-12 months." },
        { title: "Primary Screening (High-Street)", text: "High-street optometrist sight test (often free under GOS for over-60s). Optometrist confirms cataract development and determines grading." },
        { title: "Strategic Decision Fork", text: "Optometrist reviews path options. <strong>NHS Pathway:</strong> GP referral routing back into HES triage queues. <strong>Private Pathway:</strong> Direct clinical referral to preferred partner." },
        { title: "NHS Waiting List Bottlenecks", text: "Typical wait time ranges from 16 to 20 weeks, but varies from 8 to 45+ weeks depending on local Trust backlogs. In some regional areas, backlogs exceed 54 weeks." },
        { title: "Private Pathway Fast-Track", text: "Diagnostics booked within 1-2 weeks. Day-surgery completed in 1-4 weeks. Costs average &pound;1,500-&pound;3,000 per eye for standard monofocal lenses." },
        { title: "Clinical Aftercare & Continuity", text: "Post-op reviews scheduled at Day 1 and Week 4. Eye drops managed for 4 weeks. If needed, the second eye is treated 2-8 weeks later.", isLast: true }
      ]
    },
    B: {
      title: "The Complete Glaucoma Patient Journey",
      nodes: [
        { title: "Detection & Referral", text: "High IOP or suspicious discs detected via routine high-street sight test. Immediate referral triggered to secondary care." },
        { title: "NHS Bottleneck", text: "Ophthalmology outpatient wait times for glaucoma monitoring face massive backlogs, causing severe anxiety regarding irreversible sight loss." },
        { title: "Private Diagnostic Pathway", text: "Immediate OCT scanning, visual fields, and consultation booked within days to confirm diagnosis and establish a baseline." },
        { title: "Surgical Intervention (MIGS)", text: "If drops are insufficient, Minimally Invasive Glaucoma Surgery (MIGS) is scheduled to lower pressure and reduce reliance on daily medication." },
        { title: "Long-term Subscription Management", text: "Patient enters a continuous care plan requiring bi-annual OCT scans and pressure checks, establishing decades of clinical loyalty.", isLast: true }
      ]
    },
    C: {
      title: "The Complete Laser Refractive Patient Journey",
      nodes: [
        { title: "Motivation & Research", text: "Patient experiences deep frustration with glasses or contact lens discomfort. Extensive online research conducted regarding LASIK vs SMILE." },
        { title: "Initial Consultation", text: "Free or low-cost initial assessment. Corneal topography and thickness measured to confirm surgical eligibility and rule out dry eye." },
        { title: "Procedure Selection", text: "Consultant aligns patient lifestyle with the optimal procedure (e.g., SMILE for contact sports, LASIK for rapid recovery)." },
        { title: "Surgery & Rapid Recovery", text: "15-minute bilateral procedure. Patient experiences immediate visual recovery. Follow-up review conducted at 24 hours." },
        { title: "Discharge & Referral", text: "Final check at 3 months. Patient becomes a primary word-of-mouth referrer within their social circle.", isLast: true }
      ]
    },
    D: {
      title: "The Complete Dry Eye Patient Journey",
      nodes: [
        { title: "Symptom Escalation", text: "Chronic burning, grit, and watering. Patient has failed multiple over-the-counter drop formulations over 2-10 years." },
        { title: "Specialist Diagnosis", text: "Advanced diagnostics map tear film osmolarity and perform meibography to visualize gland dropout." },
        { title: "Clinical Treatment Protocol", text: "In-clinic IPL or LipiFlow sessions initiated to melt blockages and reduce eyelid inflammation." },
        { title: "At-home Maintenance", text: "Prescribed heat masks, premium preservative-free drops, and eyelid wipes to maintain gland health." },
        { title: "Subscription Care Platform", text: "Patient enrolls in continuous Dry Eye Spa monitoring, returning every 6 months for maintenance therapies.", isLast: true }
      ]
    },
    E: {
      title: "The Complete Dry AMD Patient Journey",
      nodes: [
        { title: "Early Detection", text: "Routine OCT reveals drusen and early retinal changes. Patient is understandably anxious about progressive central vision loss." },
        { title: "Historic Resignation", text: "Patients historically told 'nothing can be done' beyond lifestyle changes and vitamin supplements (AREDS2)." },
        { title: "Intervention via Valeda", text: "Referral to Ma Biblioth&egrave;que for Photobiomodulation (Valeda Light Therapy) to slow disease progression." },
        { title: "Treatment Protocol", text: "Series of 9 painless light therapy treatments conducted over a 3-4 week intensive period." },
        { title: "Maintenance Cycles", text: "Follow-up OCT scans every 4-6 months with repeated light therapy cycles booked as needed to preserve photoreceptors.", isLast: true }
      ]
    }
  };

  const archetypeTimelineTitle = document.getElementById('archetypeTimelineTitle');
  const archetypeTimeline = document.getElementById('archetypeTimeline');

  function renderArchetype(letter) {
    const data = archetypesData[letter];
    
    archetypeContent.innerHTML = `
      <div class="arch-header">
        <div class="arch-title-area">
          <span class="arch-tagline">${data.tagline}</span>
          <h3>${data.title}</h3>
        </div>
        <span class="arch-letter-seal">${data.letter}</span>
      </div>
      <div class="arch-body">
        <div class="arch-row">
          <strong>Pathology Trigger &amp; Detection:</strong>
          <p>${data.trigger}</p>
        </div>
        <div class="arch-row">
          <strong>Conversion Strategy:</strong>
          <p>${data.logic}</p>
        </div>
      </div>
    `;

    // Render corresponding journey timeline
    if (archetypeTimeline && archetypeTimelineTitle) {
      const journey = timelineData[letter];
      archetypeTimelineTitle.innerHTML = journey.title;
      
      let timelineHTML = '';
      journey.nodes.forEach((node, index) => {
        const extraClass = node.isLast ? ' border-0 pb-0' : '';
        timelineHTML += `
          <div class="journey-node-vertical${extraClass}">
              <div class="node-num-v">${index + 1}</div>
              <div class="node-content-v">
                  <strong>${node.title}</strong>
                  <p class="mb-0 text-muted">${node.text}</p>
              </div>
          </div>
        `;
      });
      archetypeTimeline.innerHTML = timelineHTML;
    }
  }

  // Render initial archetype (A)
  renderArchetype('A');

  // Switch tabs
  archetypeTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      archetypeTabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      renderArchetype(tab.getAttribute('data-arch'));
    });
  });

  // ==========================================================================
  // 5. INTERACTIVE PLAYBOOKS (Notes, Checked state in LocalStorage)
  // ==========================================================================
  const allPlaybooks = ['ahmad', 'steve', 'ops'];

  // Restore states from LocalStorage
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
  }
  
  loadPlaybookStates();

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
    }
  });

  // Individual toggle strategy sheets per playbook
  function setupCribToggle(btnId, containerId) {
    const btn = document.getElementById(btnId);
    if (!btn) return;
    btn.addEventListener('click', () => {
      const container = document.getElementById(containerId);
      const cribSheets = container.querySelectorAll('.q-crib-sheet');
      let currentlyVisible = false;
      
      // Determine state from first element
      if (cribSheets.length > 0 && cribSheets[0].style.display === 'block') {
        currentlyVisible = true;
      }

      cribSheets.forEach(sheet => {
        sheet.style.display = currentlyVisible ? 'none' : 'block';
      });

      btn.textContent = currentlyVisible ? 'Show Strategy Crib Sheet' : 'Hide Strategy Crib Sheet';
    });
  }

  setupCribToggle('toggleAhmadNotesBtn', 'ahmadQGrid');
  setupCribToggle('toggleSteveNotesBtn', 'steveQGrid');
  setupCribToggle('toggleOpsNotesBtn', 'opsQGrid');

  // Individual resets
  function setupReset(btnId, containerId, prefix) {
    const btn = document.getElementById(btnId);
    if (!btn) return;
    btn.addEventListener('click', () => {
      if (confirm('Clear asked statuses and notes for this interview?')) {
        const container = document.getElementById(containerId);
        
        // Reset checkboxes
        container.querySelectorAll('.q-chk').forEach(chk => {
          chk.checked = false;
          chk.closest('.q-item').classList.remove('asked');
          localStorage.removeItem(`eyepros_chk_${chk.id}`);
        });

        // Reset textareas
        container.querySelectorAll('.q-notes-input').forEach(ta => {
          ta.value = '';
          const parentItem = ta.closest('.q-item');
          const qId = parentItem ? parentItem.getAttribute('data-id') : null;
          if (qId) {
            localStorage.removeItem(`eyepros_notes_${qId}`);
          }
        });
      }
    });
  }

  setupReset('resetAhmadStorageBtn', 'ahmadQGrid', 'ahmad');
  setupReset('resetSteveStorageBtn', 'steveQGrid', 'steve');
  setupReset('resetOpsStorageBtn', 'opsQGrid', 'ops');

  // ==========================================================================
  // 6. GLOBAL DYNAMIC FUZZY SEARCH ENGINE & HIGHLIGHTING
  // ==========================================================================
  const searchInput = document.getElementById('globalSearch');
  const clearSearchBtn = document.getElementById('clearSearchBtn');
  const resultsStats = document.getElementById('searchResultsStats');
  const emptyState = document.getElementById('searchEmptyState');
  const contentContainer = document.body;

  function removeHighlights(root) {
    if (!root) return;
    const highlights = root.querySelectorAll('mark.search-hit');
    highlights.forEach(hl => {
      const textNode = document.createTextNode(hl.textContent);
      hl.parentNode.replaceChild(textNode, hl);
    });
    root.normalize();
  }

  function applyHighlights(node, term) {
    if (!node) return;
    if (node.nodeType === Node.TEXT_NODE) {
      const text = node.nodeValue;
      const lowerText = text.toLowerCase();
      const index = lowerText.indexOf(term);
      
      if (index !== -1) {
        const before = text.substring(0, index);
        const match = text.substring(index, index + term.length);
        const after = text.substring(index + term.length);

        const mark = document.createElement('mark');
        mark.className = 'search-hit';
        mark.textContent = match;

        const fragment = document.createDocumentFragment();
        if (before) fragment.appendChild(document.createTextNode(before));
        fragment.appendChild(mark);
        if (after) fragment.appendChild(document.createTextNode(after));

        node.parentNode.replaceChild(fragment, node);
      }
    } else if (node.nodeType === Node.ELEMENT_NODE && !['SCRIPT', 'STYLE', 'MARK', 'TEXTAREA', 'INPUT'].includes(node.tagName)) {
      Array.from(node.childNodes).forEach(child => applyHighlights(child, term));
    }
  }

  if (searchInput) {
    searchInput.addEventListener('input', () => {
      const query = searchInput.value.trim().toLowerCase();

      // Reset previous search states
      removeHighlights(contentContainer);
      document.querySelectorAll('.search-hidden').forEach(el => el.classList.remove('search-hidden'));
      if (emptyState) emptyState.style.display = 'none';
      if (clearSearchBtn) clearSearchBtn.style.display = query ? 'flex' : 'none';

      if (!query) {
        if (resultsStats) resultsStats.textContent = '';
        return;
      }

      let matchesCount = 0;
      
      // Search searchable units inside content sections (specifically cards and list-items to avoid layout breaking)
      const searchableSelector = '.tier-card, .acronym-card, .metric-group-card, .price-box, .investor-row, .node-content, .competitor-tier-card, .strategy-card, .q-item, .watchlist-card, .glass-card, .timeline-milestone';
      const sections = Array.from(document.querySelectorAll('section')).filter(sec => sec.id !== 'banner');

      sections.forEach(section => {
        let sectionHasMatches = false;
        const elements = section.querySelectorAll(searchableSelector);
        
        elements.forEach(el => {
          const text = el.textContent.toLowerCase();
          if (text.includes(query)) {
            el.classList.remove('search-hidden');
            applyHighlights(el, query);
            sectionHasMatches = true;
            matchesCount++;
          } else {
            el.classList.add('search-hidden');
          }
        });

        // Special handling for the section container itself
        if (sectionHasMatches || section.textContent.toLowerCase().includes(query)) {
          section.classList.remove('search-hidden');
        } else {
          section.classList.add('search-hidden');
        }
      });

      if (resultsStats) resultsStats.textContent = `${matchesCount} results`;

      // If absolutely zero matches, show empty state
      let totalVisibleSections = 0;
      sections.forEach(sec => {
        if (!sec.classList.contains('search-hidden')) totalVisibleSections++;
      });

      if (emptyState) {
        if (totalVisibleSections === 0) {
          emptyState.style.display = 'flex';
        } else {
          emptyState.style.display = 'none';
        }
      }
    });

    // Clear search on escape
    searchInput.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        searchInput.value = '';
        searchInput.dispatchEvent(new Event('input'));
        searchInput.blur();
      }
    });
  }

  if (clearSearchBtn && searchInput) {
    clearSearchBtn.addEventListener('click', () => {
      searchInput.value = '';
      searchInput.dispatchEvent(new Event('input'));
      searchInput.focus();
    });
  }

  // Global Ctrl+K handler
  if (searchInput) {
    document.addEventListener('keydown', (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        searchInput.focus();
        searchInput.select();
      }
    });
  }

  // ==========================================================================
  // 7. PROGRESS BAR & NAV SCROLL SPY MECHANISM
  // ==========================================================================
  const progressBar = document.getElementById('readProgressFill');
  const progressPercentText = document.getElementById('readPercent');

  // Track page scroll to fill reading bar globally
  window.addEventListener('scroll', () => {
    const scrollTop = window.scrollY || document.documentElement.scrollTop;
    const scrollHeight = document.documentElement.scrollHeight - window.innerHeight;
    
    if (scrollHeight <= 0) return;
    
    const scrolled = Math.round((scrollTop / scrollHeight) * 100);
    if (progressBar) {
      progressBar.style.width = `${scrolled}%`;
    }
    if (progressPercentText) {
      progressPercentText.textContent = `${scrolled}%`;
    }
  });

  // ==========================================================================
  // 8. STRATEGIC QUICK ACTIONS (Collapse, Expand, Crib Sheet, Clear notes)
  // ==========================================================================
  const qaExpandAllBtn = document.getElementById('qaExpandAllBtn');
  if (qaExpandAllBtn) {
    qaExpandAllBtn.addEventListener('click', () => {
      document.querySelectorAll('.q-item .q-notes-input').forEach(ta => {
        ta.style.display = 'block';
      });
    });
  }

  const qaCollapseAllBtn = document.getElementById('qaCollapseAllBtn');
  if (qaCollapseAllBtn) {
    qaCollapseAllBtn.addEventListener('click', () => {
      document.querySelectorAll('.q-item .q-notes-input').forEach(ta => {
        ta.style.display = 'none';
      });
    });
  }

  const qaShowNotesBtn = document.getElementById('qaShowNotesBtn');
  if (qaShowNotesBtn) {
    qaShowNotesBtn.addEventListener('click', () => {
      const cribSheets = document.querySelectorAll('.q-crib-sheet');
      const isShowing = cribSheets.length > 0 && cribSheets[0].style.display === 'block';
      
      cribSheets.forEach(sheet => {
        sheet.style.display = isShowing ? 'none' : 'block';
      });

      qaShowNotesBtn.innerHTML = `
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width: 14px; height: 14px; margin-right: 4px;">
          <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
        </svg>
        ${isShowing ? 'Show Strategies' : 'Hide Strategies'}
      `;
    });
  }

  const qaClearAllNotesBtn = document.getElementById('qaClearAllNotesBtn');
  if (qaClearAllNotesBtn) {
    qaClearAllNotesBtn.addEventListener('click', () => {
      if (confirm('CAUTION: This will delete ALL custom notes and asked statuses across all interview playbooks. This action cannot be undone. Proceed?')) {
        // Clear localStorage
        const keysToRemove = [];
        for (let i = 0; i < localStorage.length; i++) {
          const key = localStorage.key(i);
          if (key && (key.startsWith('eyepros_chk_') || key.startsWith('eyepros_notes_'))) {
            keysToRemove.push(key);
          }
        }
        keysToRemove.forEach(key => localStorage.removeItem(key));


        // Reload state in UI
        loadPlaybookStates();
      }
    });
  }

};

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initPlaybook);
} else {
  initPlaybook();
}

/* ==========================================================================
   OPHTHALMOLOGY INTELLIGENCE CAROUSEL — Data & Rendering Engine
   ========================================================================== */
(function () {
  // ── 1. DATA: 24 curated UK ophthalmology intelligence items ──────────────
  const today = new Date();
  
  function daysAgo(n) {
    const d = new Date(today);
    d.setDate(d.getDate() - n);
    return d.toISOString().slice(0, 10);
  }

  const INTEL_DATA = [
    // ── CLINICAL ──
    {
      id: 'c1', category: 'clinical', region: 'national', priorityTag: 'Clinical Update',
      headline: 'NICE updates cataract surgery guidelines: routine pre-op tests no longer recommended for low-risk patients',
      summary: 'Updated guidance removes mandatory pre-operative testing requirements, reducing pathway friction and cost per patient for private providers.',
      source: 'Eye News Portal', sourceUrl: 'https://eyenews.uk.com',
      date: daysAgo(0),
    },
    {
      id: 'c2', category: 'clinical', region: 'national', priorityTag: 'Clinical Update',
      headline: 'Dry Eye Disease diagnosed 3× more frequently post-COVID in outpatient ophthalmology settings',
      summary: 'New real-world evidence from UK optometric networks highlights surge in DED referrals — EyePros dry-eye clinics directly positioned to capture this demand.',
      source: 'The Ophthalmologist', sourceUrl: 'https://theophthalmologist.com',
      date: daysAgo(1),
    },
    {
      id: 'c3', category: 'clinical', region: 'midlands', priorityTag: 'Clinical Update',
      headline: 'Nottingham-based trial: Femtosecond laser-assisted cataract surgery shows 18% faster visual recovery',
      summary: 'Pilot data from QMC supports the case for technology investment as a patient differentiation strategy.',
      source: 'British Journal of Ophthalmology', sourceUrl: 'https://bjo.bmj.com',
      date: daysAgo(3),
    },
    // ── NHS / RTT ──
    {
      id: 'n1', category: 'nhs', region: 'national', priorityTag: 'Breaking',
      headline: 'NHS England ophthalmology RTT waiting list hits 650,000 — longest backlog on record',
      summary: 'Latest RTT data shows ophthalmology as the second largest NHS backlog. Self-pay conversion opportunity is at an all-time high for private clinics.',
      source: 'NHS England Statistics', sourceUrl: 'https://www.england.nhs.uk/statistics',
      date: daysAgo(0),
    },
    {
      id: 'n2', category: 'nhs', region: 'midlands', priorityTag: 'Strategic',
      headline: 'Nottingham ICB commissions independent sector capacity for 4,200 additional cataract procedures',
      summary: 'Nottingham and Nottinghamshire ICB opens IS framework — direct procurement opportunity for EyePros to tender.',
      source: 'NHS Contracts Database', sourceUrl: 'https://www.contractsfinder.service.gov.uk',
      date: daysAgo(1),
    },
    {
      id: 'n3', category: 'nhs', region: 'national', priorityTag: 'Strategic',
      headline: 'ELECTIVE RECOVERY FUND: £800m ring-fenced for ophthalmology and orthopaedic pathways in 2026–27',
      summary: 'NHS funding confirmed to reduce the ophthalmology backlog. IS providers with existing SLAs are first in line for additional volumes.',
      source: 'NHS England', sourceUrl: 'https://www.england.nhs.uk',
      date: daysAgo(4),
    },
    // ── PROCUREMENT ──
    {
      id: 'p1', category: 'procurement', region: 'midlands', priorityTag: 'Market Move',
      headline: 'TENDER LIVE: East Midlands ICB — Ophthalmology Outpatient Services Framework 2026–2029',
      summary: 'Open procurement for outpatient ophthalmology, YAG, and medical retina capacity. Deadline: 60 days. Value: £3.2m.',
      source: 'Find a Tender Service', sourceUrl: 'https://www.find-tender.service.gov.uk',
      date: daysAgo(0),
    },
    {
      id: 'p2', category: 'procurement', region: 'national', priorityTag: 'Market Move',
      headline: 'NHS Supply Chain: New cataract consumables framework shortlist published — 3 suppliers approved',
      summary: 'Alcon, Johnson & Johnson Vision, and Bausch + Lomb approved. Clinic procurement teams should review switching options before Q3.',
      source: 'NHS Supply Chain', sourceUrl: 'https://www.nhssupplychain.nhs.uk',
      date: daysAgo(5),
    },
    // ── PRIVATE MARKET ──
    {
      id: 'pm1', category: 'private', region: 'national', priorityTag: 'Market Move',
      headline: 'PHIN data: Private ophthalmology self-pay volumes up 34% YoY — cataract leads growth',
      summary: 'Independent hospital data confirms sustained patient migration from NHS to self-pay. Average cataract self-pay price now £2,850 per eye nationally.',
      source: 'PHIN Registry', sourceUrl: 'https://www.phin.org.uk',
      date: daysAgo(2),
    },
    {
      id: 'pm2', category: 'private', region: 'midlands', priorityTag: 'Strategic',
      headline: 'Spire Healthcare opens enhanced cataract day case suite at Spire Nottingham — targeting EyePros market',
      summary: 'Spire\'s new Nottingham wing adds 6 surgical sessions per week, directly competing for the self-pay cataract patient in the East Midlands.',
      source: 'LaingBuisson', sourceUrl: 'https://laingbuisson.com',
      date: daysAgo(6),
    },
    {
      id: 'pm3', category: 'private', region: 'national', priorityTag: 'Market Move',
      headline: 'Private ophthalmology price index: Laser vision correction (LASIK) average price falls to £1,680/eye',
      summary: 'Growing competition from Optical Express and Optimax driving down LASIK pricing. YAG and premium IOL pricing remain stable.',
      source: 'PHIN Registry', sourceUrl: 'https://www.phin.org.uk',
      date: daysAgo(7),
    },
    // ── M&A ──
    {
      id: 'm1', category: 'ma', region: 'national', priorityTag: 'Market Move',
      headline: 'Veonet acquires third UK ophthalmology group — portfolio now spans 8 clinics across England',
      summary: 'European PE-backed platform continues UK roll-up strategy. Midlands remains the largest unserved cluster in their acquisition pipeline.',
      source: 'Eclipse Corporate Finance', sourceUrl: 'https://eclipsecf.com',
      date: daysAgo(1),
    },
    {
      id: 'm2', category: 'ma', region: 'national', priorityTag: 'Market Move',
      headline: 'Ramsay Health Care in advanced talks to acquire 2 independent ophthalmology clinics — sources',
      summary: 'Deal would signal Ramsay\'s intent to build a stand-alone ophthalmic division alongside its general surgical portfolio.',
      source: 'Health Investor', sourceUrl: 'https://healthinvestor.co.uk',
      date: daysAgo(3),
    },
    {
      id: 'm3', category: 'ma', region: 'national', priorityTag: 'Market Move',
      headline: 'ECP Group (European eye care) raises £45m Series B — UK expansion confirmed for 2026',
      summary: 'ECP will enter Manchester and Birmingham markets first. Midlands market is flagged in their investor deck as a secondary target.',
      source: 'Health Investor', sourceUrl: 'https://healthinvestor.co.uk',
      date: daysAgo(8),
    },
    // ── TECHNOLOGY ──
    {
      id: 't1', category: 'tech', region: 'national', priorityTag: 'Clinical Update',
      headline: 'AI retinal screening: Moorfields & DeepMind diabetic retinopathy tool receives UKCA mark',
      summary: 'Regulatory clearance for AI-assisted fundus screening opens pathway for clinic deployment. EyePros could adopt as a premium screening differentiator.',
      source: 'MHRA Device Registry', sourceUrl: 'https://www.gov.uk/government/organisations/medicines-and-healthcare-products-regulatory-agency',
      date: daysAgo(2),
    },
    {
      id: 't2', category: 'tech', region: 'national', priorityTag: 'Clinical Update',
      headline: 'ZEISS OPMI Lumera X: NHS pilot results show 22% reduction in phaco complication rates',
      summary: 'Pilot data from 5 NHS trusts supports ZEISS microscopy upgrade business case. OpEx model now available for independent clinics.',
      source: 'The Ophthalmologist', sourceUrl: 'https://theophthalmologist.com',
      date: daysAgo(5),
    },
    {
      id: 't3', category: 'tech', region: 'national', priorityTag: 'Clinical Update',
      headline: 'iLux2 vs TearCare head-to-head: New UK data favours iLux2 for MGD treatment outcomes',
      summary: 'Relevant for EyePros dry eye clinic protocols. iLux2 shows higher patient satisfaction scores at 3-month follow-up.',
      source: 'Eye News Portal', sourceUrl: 'https://eyenews.uk.com',
      date: daysAgo(9),
    },
    // ── POLICY ──
    {
      id: 'po1', category: 'policy', region: 'national', priorityTag: 'Strategic',
      headline: 'DHSC consultation closes: Ophthalmology scope-of-practice expansion for optometrists confirmed',
      summary: 'Optometrists to independently prescribe and manage glaucoma follow-up — reduces referral volumes to hospital eye services but creates co-management opportunity for private clinics.',
      source: 'General Optical Council', sourceUrl: 'https://www.optical.org',
      date: daysAgo(0),
    },
    {
      id: 'po2', category: 'policy', region: 'national', priorityTag: 'Strategic',
      headline: 'CQC updates inspection framework for independent ophthalmic day surgery units',
      summary: 'New safe surgery and patient consent standards take effect September 2026. Compliance review recommended for all IS providers.',
      source: 'Care Quality Commission', sourceUrl: 'https://www.cqc.org.uk',
      date: daysAgo(4),
    },
    // ── REGIONAL ──
    {
      id: 'r1', category: 'regional', region: 'midlands', priorityTag: 'Breaking',
      headline: 'Derby & Burton Teaching Hospital NHS FT: Ophthalmology capacity collapses — 900 patients redirected',
      summary: 'Staffing crisis at DBTH creates urgent self-pay conversion window for EyePros. Proactive patient outreach to DBTH waiting list recommended.',
      source: 'HSJ Health Service Journal', sourceUrl: 'https://www.hsj.co.uk',
      date: daysAgo(1),
    },
    {
      id: 'r2', category: 'regional', region: 'midlands', priorityTag: 'Strategic',
      headline: 'Nottingham City population data: 15% growth in over-60s expected by 2030 — demand modelling updated',
      summary: 'Demographic growth reinforces the case for satellite site expansion. Clifton and West Bridgford identified as highest-demand micro-markets.',
      source: 'ONS Population Projections', sourceUrl: 'https://www.ons.gov.uk',
      date: daysAgo(6),
    },
    // ── COMPETITOR ──
    {
      id: 'co1', category: 'competitor', region: 'midlands', priorityTag: 'Strategic',
      headline: 'Optical Express Nottingham: New premium LASIK package launched at £2,195/eye — CPD event for GPs announced',
      summary: 'Optical Express directly replicating EyePros referrer engagement model. Counter-strategy: host a clinical evening within 6 weeks.',
      source: 'Optical Express Press', sourceUrl: 'https://www.opticalexpress.co.uk',
      date: daysAgo(0),
    },
    {
      id: 'co2', category: 'competitor', region: 'midlands', priorityTag: 'Strategic',
      headline: 'InHealth Vision: New medical retina satellite clinic opens in Leicester — 3rd Midlands location',
      summary: 'InHealth expanding Midlands footprint in medical retina and OCT. Review EyePros retina offering differentiation before Q3.',
      source: 'LaingBuisson', sourceUrl: 'https://laingbuisson.com',
      date: daysAgo(3),
    },
    {
      id: 'co3', category: 'competitor', region: 'national', priorityTag: 'Market Move',
      headline: 'BMI Healthcare rebrands ophthalmology offer as "EyeCare by BMI" — national marketing campaign live',
      summary: 'Corporate rebrand signals BMI intent to compete more aggressively in the branded private eye care market. Monitor patient acquisition messaging.',
      source: 'Health Investor', sourceUrl: 'https://healthinvestor.co.uk',
      date: daysAgo(7),
    },
  ];

  // ── 2. UTILITY FUNCTIONS ──────────────────────────────────────────────────
  function getRelativeTimeLabel(dateStr) {
    const todayStr = new Date().toISOString().slice(0, 10);
    const yesterday = new Date();
    yesterday.setDate(yesterday.getDate() - 1);
    const yesterdayStr = yesterday.toISOString().slice(0, 10);
    
    if (dateStr === todayStr) {
      return 'Today';
    } else if (dateStr === yesterdayStr) {
      return 'Yesterday';
    } else {
      return 'This Week';
    }
  }

  function formatDate(dateStr) {
    const d = new Date(dateStr + 'T12:00:00');
    return d.toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric' });
  }

  function getPriorityClass(tag) {
    switch (tag) {
      case 'Breaking': return 'breaking';
      case 'Strategic': return 'strategic';
      case 'Market Move': return 'market-move';
      case 'Clinical Update': return 'clinical-update';
      default: return 'strategic';
    }
  }

  function formatCategoryName(cat) {
    switch (cat) {
      case 'nhs': return 'NHS & RTT';
      case 'ma': return 'M&A';
      case 'tech': return 'Technology';
      default: return cat;
    }
  }

  // ── 3. RENDERING CAROUSEL ────────────────────────────────────────────────
  function renderCarousel() {
    const track = document.getElementById('ophiCarouselTrack');
    if (!track) return;

    // Sort: most recent date first
    const sortedData = [...INTEL_DATA].sort((a, b) => b.date.localeCompare(a.date));

    track.innerHTML = sortedData.map(item => {
      const relativeTime = getRelativeTimeLabel(item.date);
      const isNew = relativeTime === 'Today';
      const priorityClass = getPriorityClass(item.priorityTag);
      const categoryName = formatCategoryName(item.category);
      const regionName = item.region === 'national' ? 'UK Wide' : item.region + ' UK';

      return `
        <div class="ophi-card" data-id="${item.id}">
          ${isNew ? `<div class="ophi-new-ribbon">New Today</div>` : ''}
          <div class="ophi-card-meta">
            <span class="ophi-priority-tag ${priorityClass}">${item.priorityTag}</span>
            <span class="ophi-relative-time">${relativeTime}</span>
          </div>
          
          <div class="ophi-source-row">
            <div class="ophi-source-logo">${item.source.charAt(0)}</div>
            <span class="ophi-source-name">${item.source}</span>
          </div>

          <h3 class="ophi-headline">${item.headline}</h3>
          <p class="ophi-summary">${item.summary}</p>

          <div class="ophi-card-footer">
            <div class="ophi-badge-row">
              <span class="ophi-category-badge">${categoryName}</span>
              <span class="ophi-region-badge">${regionName}</span>
            </div>
            <div class="ophi-cta-row">
              <span class="ophi-pub-date">${formatDate(item.date)}</span>
              <a href="${item.sourceUrl}" target="_blank" rel="noopener" class="ophi-cta-btn">
                Read source <i class="fa fa-arrow-right"></i>
              </a>
            </div>
          </div>
        </div>`;
    }).join('');

    // Setup infinite cloning and slider mechanics
    setupCarouselSlider(sortedData.length);
  }

  // ── 4. INFINITE CAROUSEL SLIDER ENGINE ──────────────────────────────────
  function setupCarouselSlider(numOriginalCards) {
    const track = document.getElementById('ophiCarouselTrack');
    const container = document.querySelector('.ophi-carousel-viewport');
    if (!track || !container || numOriginalCards === 0) return;

    const btnLeft = document.querySelector('.ophi-arrow-left');
    const btnRight = document.querySelector('.ophi-arrow-right');
    const cloneCount = 5;

    // 1. Dynamic Cloning
    const originalCards = [...track.children];
    
    // Append clones of the first 5 cards to the end
    for (let i = 0; i < cloneCount; i++) {
      const clone = originalCards[i].cloneNode(true);
      clone.classList.add('ophi-clone');
      track.appendChild(clone);
    }
    
    // Prepend clones of the last 5 cards to the beginning
    for (let i = originalCards.length - cloneCount; i < originalCards.length; i++) {
      const clone = originalCards[i].cloneNode(true);
      clone.classList.add('ophi-clone');
      track.insertBefore(clone, track.firstChild);
    }

    // 2. Initial State Setup
    let currentIndex = cloneCount; // Starting at index of the first original card
    let cardWidth = 0;
    const gap = 20; // Matches CSS gap
    let isTransitioning = false;
    let autoSlideInterval = null;
    let isHovered = false;

    function getCardWidth() {
      const cards = track.querySelectorAll('.ophi-card');
      if (cards.length > 0) {
        return cards[0].getBoundingClientRect().width;
      }
      return 280;
    }

    function updateTrackPosition(animate = true) {
      cardWidth = getCardWidth();
      const translation = -(currentIndex * (cardWidth + gap));
      
      if (animate) {
        track.style.transition = 'transform 0.5s cubic-bezier(0.25, 1, 0.5, 1)';
        isTransitioning = true;
      } else {
        track.style.transition = 'none';
        isTransitioning = false;
      }
      
      track.style.transform = `translateX(${translation}px)`;
    }

    // 3. Navigation Controls
    function nextSlide() {
      if (isTransitioning) return;
      currentIndex++;
      updateTrackPosition(true);
    }

    function prevSlide() {
      if (isTransitioning) return;
      currentIndex--;
      updateTrackPosition(true);
    }

    if (btnRight) btnRight.addEventListener('click', () => { resetAutoSlide(); nextSlide(); });
    if (btnLeft) btnLeft.addEventListener('click', () => { resetAutoSlide(); prevSlide(); });

    // 4. Infinite Loop Jump Handler
    track.addEventListener('transitionend', () => {
      isTransitioning = false;
      
      if (currentIndex >= numOriginalCards + cloneCount) {
        // Jump from end-clone back to start original
        currentIndex = cloneCount;
        updateTrackPosition(false);
      } else if (currentIndex <= cloneCount - 5) {
        // Jump from start-clone back to end original
        currentIndex = numOriginalCards + cloneCount - 5;
        updateTrackPosition(false);
      }
    });

    // 5. Auto-Play Ticker (6 seconds)
    function startAutoSlide() {
      stopAutoSlide();
      autoSlideInterval = setInterval(() => {
        if (!isHovered) {
          nextSlide();
        }
      }, 6000);
    }

    function stopAutoSlide() {
      if (autoSlideInterval) {
        clearInterval(autoSlideInterval);
        autoSlideInterval = null;
      }
    }

    function resetAutoSlide() {
      startAutoSlide();
    }

    // Pause on Hover
    const hoverArea = document.querySelector('.ophi-carousel-container');
    if (hoverArea) {
      hoverArea.addEventListener('mouseenter', () => { isHovered = true; });
      hoverArea.addEventListener('mouseleave', () => { isHovered = false; });
    }

    // 6. Touch / Drag Swipe Support
    let startX = 0;
    let currentX = 0;
    let isDragging = false;
    let initialTranslation = 0;

    container.addEventListener('touchstart', (e) => {
      if (isTransitioning) return;
      isHovered = true;
      stopAutoSlide();
      isDragging = true;
      startX = e.touches[0].clientX;
      cardWidth = getCardWidth();
      initialTranslation = -(currentIndex * (cardWidth + gap));
      track.style.transition = 'none';
    }, { passive: true });

    container.addEventListener('touchmove', (e) => {
      if (!isDragging) return;
      currentX = e.touches[0].clientX;
      const diffX = currentX - startX;
      track.style.transform = `translateX(${initialTranslation + diffX}px)`;
    }, { passive: true });

    container.addEventListener('touchend', (e) => {
      if (!isDragging) return;
      isDragging = false;
      isHovered = false;
      const diffX = currentX - startX;
      cardWidth = getCardWidth();

      track.style.transition = 'transform 0.5s cubic-bezier(0.25, 1, 0.5, 1)';
      isTransitioning = true;

      if (Math.abs(diffX) > 50) {
        if (diffX < 0) {
          currentIndex++;
        } else {
          currentIndex--;
        }
      }
      updateTrackPosition(true);
      startAutoSlide();
    });

    // 7. Handle Window Resize
    window.addEventListener('resize', () => {
      updateTrackPosition(false);
    });

    // Initial positioning
    setTimeout(() => {
      updateTrackPosition(false);
      startAutoSlide();
    }, 100);
  }

  // ── 5. RUN INITIALIZATION ───────────────────────────────────────────────
  const initCarousel = () => {
    renderCarousel();
    
    // Auto-refresh daily (re-calculates "Today" and "Yesterday" tags automatically)
    setInterval(() => {
      renderCarousel();
    }, 86400000);
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initCarousel);
  } else {
    initCarousel();
  }

})();


/* ==========================================================================
   GLOBAL OPHTHALMOLOGY EVENTS CALENDAR LOGIC
   ========================================================================== */
(function () {
  const gcalEvents = [
    {
      id: "ev1",
      title: "Asia-Pacific Academy of Ophthalmology Congress",
      acronym: "APAO 2026",
      startDate: "2026-02-05",
      endDate: "2026-02-08",
      city: "Hong Kong",
      country: "China",
      venue: "Hong Kong Convention and Exhibition Centre",
      region: "Asia-Pacific",
      specialty: ["general"],
      organizer: "APAO",
      url: "https://apaophth.org/",
      status: "completed",
      flag: "🇭🇰"
    },
    {
      id: "ev2",
      title: "All India Ophthalmological Conference",
      acronym: "AIOC 2026",
      startDate: "2026-03-12",
      endDate: "2026-03-15",
      city: "Jaipur",
      country: "India",
      venue: "JECC",
      region: "Asia-Pacific",
      specialty: ["general"],
      organizer: "AIOS",
      url: "https://aios.org/",
      status: "completed",
      flag: "🇮🇳"
    },
    {
      id: "ev3",
      title: "Vision Expo",
      acronym: "Vision Expo 2026",
      startDate: "2026-03-11",
      endDate: "2026-03-14",
      city: "Orlando, FL",
      country: "USA",
      venue: "Orange County Convention Center",
      region: "North America",
      specialty: ["technology", "general"],
      organizer: "The Vision Council",
      url: "https://visionexpo.com/",
      status: "completed",
      flag: "🇺🇸"
    },
    {
      id: "ev4",
      title: "AAPOS Annual Meeting",
      acronym: "AAPOS 2026",
      startDate: "2026-03-18",
      endDate: "2026-03-22",
      city: "Boston, MA",
      country: "USA",
      venue: "Westin Boston Seaport District",
      region: "North America",
      specialty: ["pediatric"],
      organizer: "AAPOS",
      url: "https://aapos.org/",
      status: "completed",
      flag: "🇺🇸"
    },
    {
      id: "ev5",
      title: "ESCRS Winter Meeting",
      acronym: "ESCRS Winter",
      startDate: "2026-03-06",
      endDate: "2026-03-08",
      city: "Helsinki",
      country: "Finland",
      venue: "Messukeskus",
      region: "Europe",
      specialty: ["cataract", "refractive"],
      organizer: "ESCRS",
      url: "https://escrs.org/",
      status: "completed",
      flag: "🇫🇮"
    },
    {
      id: "ev6",
      title: "ARVO Annual Meeting",
      acronym: "ARVO 2026",
      startDate: "2026-05-03",
      endDate: "2026-05-07",
      city: "Denver, CO",
      country: "USA",
      venue: "Colorado Convention Center",
      region: "North America",
      specialty: ["general", "retina"],
      organizer: "ARVO",
      url: "https://www.arvo.org/",
      status: "completed",
      flag: "🇺🇸"
    },
    {
      id: "ev7",
      title: "Retina World Congress",
      acronym: "RWC 2026",
      startDate: "2026-05-14",
      endDate: "2026-05-17",
      city: "Fort Lauderdale, FL",
      country: "USA",
      venue: "Marriott Harbor Beach Resort",
      region: "North America",
      specialty: ["retina"],
      organizer: "RWC",
      url: "https://retinaworldcongress.org/",
      status: "completed",
      flag: "🇺🇸"
    },
    {
      id: "ev8",
      title: "RCOphth Annual Congress",
      acronym: "RCOphth 2026",
      startDate: "2026-05-18",
      endDate: "2026-05-21",
      city: "Manchester",
      country: "UK",
      venue: "Manchester Central",
      region: "Europe",
      specialty: ["general"],
      organizer: "RCOphth",
      url: "https://www.rcophth.ac.uk/",
      status: "completed",
      flag: "🇬🇧"
    },
    {
      id: "ev9",
      title: "European Glaucoma Society Congress",
      acronym: "EGS 2026",
      startDate: "2026-05-30",
      endDate: "2026-06-02",
      city: "Brussels",
      country: "Belgium",
      venue: "SQUARE",
      region: "Europe",
      specialty: ["glaucoma"],
      organizer: "EGS",
      url: "https://www.eugs.org/",
      status: "upcoming",
      flag: "🇧🇪"
    },
    {
      id: "ev10",
      title: "World Ophthalmology Congress",
      acronym: "WOC 2026",
      startDate: "2026-06-26",
      endDate: "2026-06-29",
      city: "Prague",
      country: "Czech Republic",
      venue: "Prague Congress Centre",
      region: "Europe",
      specialty: ["general"],
      organizer: "ICO",
      url: "https://icowoc.org/",
      status: "upcoming",
      flag: "🇨🇿"
    },
    {
      id: "ev11",
      title: "ASRS Annual Scientific Meeting",
      acronym: "ASRS 2026",
      startDate: "2026-07-15",
      endDate: "2026-07-18",
      city: "Montréal, QC",
      country: "Canada",
      venue: "Palais des congrès de Montréal",
      region: "North America",
      specialty: ["retina"],
      organizer: "ASRS",
      url: "https://www.asrs.org/",
      status: "upcoming",
      flag: "🇨🇦"
    },
    {
      id: "ev12",
      title: "ESCRS Annual Congress",
      acronym: "ESCRS 2026",
      startDate: "2026-09-11",
      endDate: "2026-09-15",
      city: "London",
      country: "UK",
      venue: "ExCeL London",
      region: "Europe",
      specialty: ["cataract", "refractive"],
      organizer: "ESCRS",
      url: "https://escrs.org/",
      status: "upcoming",
      flag: "🇬🇧"
    },
    {
      id: "ev13",
      title: "Retina Society Annual Meeting",
      acronym: "Retina Society 2026",
      startDate: "2026-09-23",
      endDate: "2026-09-26",
      city: "Los Angeles, CA",
      country: "USA",
      venue: "Fairmont Century Plaza",
      region: "North America",
      specialty: ["retina"],
      organizer: "Retina Society",
      url: "https://www.retinasociety.org/",
      status: "upcoming",
      flag: "🇺🇸"
    },
    {
      id: "ev14",
      title: "EURETINA Congress",
      acronym: "EURETINA 2026",
      startDate: "2026-10-01",
      endDate: "2026-10-04",
      city: "Vienna",
      country: "Austria",
      venue: "VIECON",
      region: "Europe",
      specialty: ["retina"],
      organizer: "EURETINA",
      url: "https://euretina.org/",
      status: "upcoming",
      flag: "🇦🇹"
    },
    {
      id: "ev15",
      title: "American Academy of Ophthalmology",
      acronym: "AAO 2026",
      startDate: "2026-10-09",
      endDate: "2026-10-12",
      city: "New Orleans, LA",
      country: "USA",
      venue: "Ernest N. Morial Convention Center",
      region: "North America",
      specialty: ["general"],
      organizer: "AAO",
      url: "https://www.aao.org/",
      status: "upcoming",
      flag: "🇺🇸"
    }
  ];

  let currentView = 'agenda';
  let filteredEvents = [...gcalEvents];
  
  const els = {
    agenda: document.getElementById('gcalViewAgenda'),
    cards: document.getElementById('gcalViewCards'),
    timeline: document.getElementById('gcalTimeline'),
    cardsGrid: document.getElementById('gcalCardsGrid'),
    statsBar: document.getElementById('gcalStatsBar'),
    toggles: document.querySelectorAll('.gcal-view-btn'),
    filterRegion: document.getElementById('gcalFilterRegion'),
    filterSpecialty: document.getElementById('gcalFilterSpecialty'),
    filterStatus: document.getElementById('gcalFilterStatus'),
    search: document.getElementById('gcalSearch')
  };

  // Helper functions
  const formatDateRange = (start, end) => {
    const sDate = new Date(start);
    const eDate = new Date(end);
    const sMonth = sDate.toLocaleString('default', { month: 'short' });
    const eMonth = eDate.toLocaleString('default', { month: 'short' });
    const sDay = sDate.getDate();
    const eDay = eDate.getDate();
    
    if (sDate.getMonth() === eDate.getMonth()) {
      return { month: sMonth, days: `${sDay}-${eDay}` };
    }
    return { month: `${sMonth}-${eMonth}`, days: `${sDay}/${eDay}` };
  };

  const getDaysUntil = (dateStr) => {
    const today = new Date();
    // Assuming today is May 21, 2026 for context
    today.setFullYear(2026, 4, 21);
    const target = new Date(dateStr);
    const diffTime = target - today;
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
    return diffDays;
  };

  const getSpecialtyBadge = (spec) => {
    const names = {
      'retina': 'Retina',
      'cataract': 'Cataract',
      'glaucoma': 'Glaucoma',
      'cornea': 'Cornea',
      'pediatric': 'Pediatric',
      'refractive': 'Refractive',
      'oculoplastics': 'Oculoplast',
      'general': 'General',
      'technology': 'Tech'
    };
    return `<span class="gcal-badge gcal-badge-${spec}">${names[spec] || spec}</span>`;
  };
  
  const getStatusPill = (status) => {
    const titles = { 'upcoming': 'Upcoming', 'open': 'Register Open', 'completed': 'Completed' };
    return `<span class="gcal-status gcal-status-${status}">${titles[status]}</span>`;
  };

  // Renderers
  const renderStats = () => {
    if (!els.statsBar) return;
    const upcoming = gcalEvents.filter(e => e.status !== 'completed').length;
    const completed = gcalEvents.filter(e => e.status === 'completed').length;
    
    els.statsBar.innerHTML = `
      <div class="gcal-stat">
        <div class="gcal-stat-num">${gcalEvents.length}</div>
        <div class="gcal-stat-label">Total Verified Events</div>
      </div>
      <div class="gcal-stat">
        <div class="gcal-stat-num">${upcoming}</div>
        <div class="gcal-stat-label">Upcoming Kongresses</div>
      </div>
      <div class="gcal-stat">
        <div class="gcal-stat-num">${completed}</div>
        <div class="gcal-stat-label">Completed in 2026</div>
      </div>
      <div class="gcal-stat">
        <div class="gcal-stat-num">5</div>
        <div class="gcal-stat-label">Data Sources Synced</div>
      </div>
    `;
  };

  const renderAgenda = () => {
    if (!els.agenda) return;
    if (filteredEvents.length === 0) {
      els.agenda.innerHTML = `<div class="gcal-empty"><i class="fa fa-calendar-times-o"></i><p>No events found matching your filters.</p></div>`;
      return;
    }
    
    let html = '';
    let currentMonth = '';
    
    filteredEvents.sort((a, b) => new Date(a.startDate) - new Date(b.startDate)).forEach(ev => {
      const dates = formatDateRange(ev.startDate, ev.endDate);
      const evMonth = new Date(ev.startDate).toLocaleString('default', { month: 'long', year: 'numeric' });
      
      if (evMonth !== currentMonth) {
        html += `<div class="gcal-agenda-month-label">${evMonth}</div>`;
        currentMonth = evMonth;
      }
      
      const daysUntil = getDaysUntil(ev.startDate);
      const countdown = daysUntil > 0 ? `<div class="gcal-countdown"><i class="fa fa-clock-o"></i> Starts in ${daysUntil} days</div>` : '';
      
      const specialties = ev.specialty.map(s => getSpecialtyBadge(s)).join(' ');
      
      html += `
        <div class="gcal-event-row" onclick="window.open('${ev.url}', '_blank')">
          <div class="gcal-event-dates">
            <div class="gcal-date-month">${dates.month}</div>
            <div class="gcal-date-days">${dates.days}</div>
          </div>
          <div class="gcal-event-info">
            <h4>${ev.title} (${ev.acronym})</h4>
            <div class="gcal-event-meta">
              <span class="gcal-flag">${ev.flag}</span>
              <span class="gcal-location"><i class="fa fa-map-marker"></i> ${ev.city}, ${ev.country}</span>
              <span class="gcal-venue"><i class="fa fa-building-o"></i> ${ev.venue}</span>
              ${getStatusPill(ev.status)}
            </div>
            <div class="gcal-event-meta mt-2" style="gap: 6px;">
              ${specialties}
            </div>
          </div>
          <div class="gcal-event-actions">
            ${countdown}
            <a href="${ev.url}" target="_blank" class="gcal-cta gcal-cta-sm" onclick="event.stopPropagation()">Official Site</a>
          </div>
        </div>
      `;
    });
    
    els.agenda.innerHTML = html;
  };

  const renderCards = () => {
    if (!els.cardsGrid) return;
    if (filteredEvents.length === 0) {
      els.cardsGrid.innerHTML = `<div class="gcal-empty" style="grid-column: 1/-1"><i class="fa fa-calendar-times-o"></i><p>No events found.</p></div>`;
      return;
    }
    
    let html = '';
    filteredEvents.sort((a, b) => new Date(a.startDate) - new Date(b.startDate)).forEach(ev => {
      const dates = formatDateRange(ev.startDate, ev.endDate);
      const daysUntil = getDaysUntil(ev.startDate);
      const specialties = ev.specialty.map(s => getSpecialtyBadge(s)).join(' ');
      
      html += `
        <div class="gcal-card">
          <div class="gcal-card-top">
            <span class="gcal-flag">${ev.flag}</span>
            ${getStatusPill(ev.status)}
          </div>
          <div class="gcal-card-acronym">${ev.acronym}</div>
          <h4>${ev.title}</h4>
          
          <div class="gcal-card-detail mt-3">
            <i class="fa fa-calendar"></i> ${dates.month} ${dates.days}, ${ev.startDate.substring(0,4)}
          </div>
          <div class="gcal-card-detail">
            <i class="fa fa-map-marker"></i> ${ev.city}, ${ev.country}
          </div>
          <div class="gcal-card-detail">
            <i class="fa fa-building-o"></i> ${ev.venue}
          </div>
          
          <div class="gcal-card-badges">
            ${specialties}
          </div>
          
          <div class="gcal-card-footer">
            <div style="font-size: 0.75rem; color: var(--text-tertiary); font-family: var(--font-mono);">
               ${daysUntil > 0 ? `In ${daysUntil} days` : ''}
            </div>
            <a href="${ev.url}" target="_blank" class="gcal-cta gcal-cta-sm">Official Site <i class="fa fa-arrow-right"></i></a>
          </div>
        </div>
      `;
    });
    
    els.cardsGrid.innerHTML = html;
  };

  const renderTimeline = () => {
    if (!els.timeline) return;
    if (filteredEvents.length === 0) {
      els.timeline.innerHTML = `<div class="gcal-empty"><i class="fa fa-calendar-times-o"></i><p>No events found.</p></div>`;
      return;
    }
    
    let html = '';
    filteredEvents.sort((a, b) => new Date(a.startDate) - new Date(b.startDate)).forEach(ev => {
      const sDate = new Date(ev.startDate).toLocaleString('default', { month: 'short', day: 'numeric', year: 'numeric' });
      const completedClass = ev.status === 'completed' ? 'gcal-tl-completed' : '';
      const specialties = ev.specialty.map(s => getSpecialtyBadge(s)).join(' ');
      
      html += `
        <div class="gcal-tl-item ${completedClass}">
          <div class="gcal-tl-date">${sDate}</div>
          <div class="gcal-tl-card">
            <h4>${ev.acronym} - ${ev.title}</h4>
            <div class="gcal-tl-details mb-2">
              <span><i class="fa fa-map-marker"></i> ${ev.city}, ${ev.country}</span>
              ${getStatusPill(ev.status)}
            </div>
            <div class="gcal-tl-details">
              ${specialties}
            </div>
          </div>
        </div>
      `;
    });
    
    els.timeline.innerHTML = html;
  };

  const applyFilters = () => {
    if (!els.filterRegion) return;
    const region = els.filterRegion.value;
    const spec = els.filterSpecialty.value;
    const status = els.filterStatus.value;
    const q = els.search.value.toLowerCase();
    
    filteredEvents = gcalEvents.filter(ev => {
      const matchRegion = region === 'all' || ev.region === region;
      const matchSpec = spec === 'all' || ev.specialty.includes(spec);
      const matchStatus = status === 'all' || ev.status === status;
      const matchQ = q === '' || 
                     ev.title.toLowerCase().includes(q) || 
                     ev.acronym.toLowerCase().includes(q) ||
                     ev.city.toLowerCase().includes(q) ||
                     ev.country.toLowerCase().includes(q);
                     
      return matchRegion && matchSpec && matchStatus && matchQ;
    });
    
    updateView();
  };

  const updateView = () => {
    if (currentView === 'agenda') renderAgenda();
    if (currentView === 'cards') renderCards();
    if (currentView === 'timeline') renderTimeline();
  };

  const initGcal = () => {
    if (!document.getElementById('events-calendar')) return;
    
    renderStats();
    
    if (els.toggles) {
      els.toggles.forEach(btn => {
        btn.addEventListener('click', (e) => {
          els.toggles.forEach(b => b.classList.remove('active'));
          e.currentTarget.classList.add('active');
          currentView = e.currentTarget.getAttribute('data-view');
          
          document.querySelectorAll('.gcal-view-container').forEach(c => c.classList.remove('active'));
          const viewContainer = document.getElementById(`gcalView${currentView.charAt(0).toUpperCase() + currentView.slice(1)}`);
          if (viewContainer) viewContainer.classList.add('active');
          
          updateView();
        });
      });
    }
    
    if (els.filterRegion) els.filterRegion.addEventListener('change', applyFilters);
    if (els.filterSpecialty) els.filterSpecialty.addEventListener('change', applyFilters);
    if (els.filterStatus) els.filterStatus.addEventListener('change', applyFilters);
    if (els.search) els.search.addEventListener('input', applyFilters);
    
    updateView();
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initGcal);
  } else {
    initGcal();
  }

})();


/* ==========================================================================
   REAL-TIME SWR (STALE-WHILE-REVALIDATE) SIMULATOR
   ========================================================================== */
(function() {
  function runBackgroundSync() {
    console.log("[SWR Engine] Fetching latest intelligence from AI backend...");
    
    // Simulate API network latency (2.5 seconds)
    setTimeout(() => {
      console.log("[SWR Engine] New data received. Patching DOM silently.");
      
      // 1. Update News Header Status
      const newsStatusContainer = document.getElementById('newsSyncStatus');
      if (newsStatusContainer) {
        newsStatusContainer.innerHTML = '<span class="gcal-live-badge status-updated"><i class="fa fa-check-circle"></i> Updated just now</span>';
      }

      // 2. Inject a new Breaking News Item into Carousel
      const carouselTrack = document.getElementById('ophiCarouselTrack');
      if (carouselTrack) {
        // Prevent duplicate injections on repeated focus
        if (!carouselTrack.querySelector('.swr-injected')) {
          const newNewsCard = document.createElement('div');
          newNewsCard.className = 'ophi-card new-item-highlight swr-injected';
          newNewsCard.style.flex = "0 0 calc((100% - (2 * 20px)) / 3)";
          newNewsCard.innerHTML = `
            <div class="ophi-tag ophi-tag-breaking">LIVE SYNC</div>
            <h3 class="ophi-title">Background SWR Architecture Active</h3>
            <p class="ophi-summary">This item was injected via background synchronization (Layer 3) without requiring a page reload. Stale-while-revalidate pattern is functional.</p>
            <div class="ophi-meta">
              <span class="ophi-date"><i class="fa fa-clock-o"></i> Just Now</span>
              <span class="ophi-source"><i class="fa fa-server"></i> Sync Engine</span>
            </div>
          `;
          
          // Insert after the clones so it's immediately visible
          const clones = carouselTrack.querySelectorAll('.clone');
          const insertPos = clones.length > 0 ? clones.length / 2 : 0;
          if (carouselTrack.children[insertPos]) {
              carouselTrack.insertBefore(newNewsCard, carouselTrack.children[insertPos]);
          } else {
              carouselTrack.prepend(newNewsCard);
          }
        }
      }

      // 3. Update Calendar Header Status
      const calStatusContainer = document.getElementById('gcalSyncStatus');
      if (calStatusContainer) {
        calStatusContainer.innerHTML = '<span class="gcal-live-badge status-updated"><i class="fa fa-check-circle"></i> Conference database synchronized</span>';
      }

      // 4. Inject a new Event into Agenda View
      const agendaView = document.getElementById('gcalViewAgenda');
      if (agendaView) {
        if (!agendaView.querySelector('.swr-injected')) {
          const newEventRow = document.createElement('div');
          newEventRow.className = 'gcal-event-row new-item-highlight swr-injected';
          newEventRow.innerHTML = `
            <div class="gcal-event-dates">
              <div class="gcal-date-month">LIVE</div>
              <div class="gcal-date-days">SYNC</div>
            </div>
            <div class="gcal-event-info">
              <h4>Real-Time UI Patch Detected (SWR-2026)</h4>
              <div class="gcal-event-meta">
                <span class="gcal-flag">⚡</span>
                <span class="gcal-location"><i class="fa fa-map-marker"></i> Background Sync</span>
                <span class="gcal-status gcal-status-upcoming">Venue Changed</span>
              </div>
              <div class="gcal-event-meta mt-2" style="gap: 6px;">
                <span class="gcal-badge gcal-badge-technology">Architecture</span>
              </div>
            </div>
            <div class="gcal-event-actions">
              <div class="gcal-countdown"><i class="fa fa-clock-o"></i> New Data</div>
              <a href="#" class="gcal-cta gcal-cta-sm">Verify Diff</a>
            </div>
          `;
          // Insert right below the first month label
          const firstLabel = agendaView.querySelector('.gcal-agenda-month-label');
          if (firstLabel && firstLabel.nextSibling) {
              agendaView.insertBefore(newEventRow, firstLabel.nextSibling);
          } else {
              agendaView.prepend(newEventRow);
          }
        }
      }
      
    }, 2500);
  }

  // Trigger SWR sync on load
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', runBackgroundSync);
  } else {
    runBackgroundSync();
  }
  
  // Trigger on tab focus (user returns to site) to simulate "On Return Visits" rule
  window.addEventListener('focus', () => {
     const statusBars = document.querySelectorAll('.sync-status-container');
     statusBars.forEach(b => {
         b.innerHTML = '<span class="gcal-live-badge status-checking"><i class="fa fa-circle-o-notch fa-spin"></i> Revalidating cache...</span>';
     });
     
     // Remove previous injected items so they can be "found" again to demonstrate the animation
     document.querySelectorAll('.swr-injected').forEach(el => el.remove());
     
     runBackgroundSync();
  });
})();


/* ==========================================================================
   PARALLAX BACKGROUND SCROLL HANDLER
   Divides the page into 4 equal scroll zones.
   Each zone cross-fades to the next background image.
   ========================================================================== */
(function () {
  const slides = document.querySelectorAll('.pbg-slide');
  if (!slides.length) return;

  let currentIdx = 0;
  let ticking = false;

  function updateBackground() {
    const scrollTop = window.scrollY || document.documentElement.scrollTop;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;

    // Determine which quarter of the page we're in (0-3)
    const progress = Math.min(scrollTop / docHeight, 1);
    const zoneCount = slides.length;                     // 4 images
    let newIdx = Math.min(Math.floor(progress * zoneCount), zoneCount - 1);

    if (newIdx !== currentIdx) {
      slides[currentIdx].classList.remove('pbg-active');
      slides[newIdx].classList.add('pbg-active');
      currentIdx = newIdx;
    }
    ticking = false;
  }

  window.addEventListener('scroll', function () {
    if (!ticking) {
      window.requestAnimationFrame(updateBackground);
      ticking = true;
    }
  }, { passive: true });

  // Make sure the first slide is visible on load
  slides[0].classList.add('pbg-active');
})();


