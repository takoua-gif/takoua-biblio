/* ==========================================================================
   EYEPROS SOLO FILMS WORKSPACE BEHAVIOR
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
    // DOM Elements
    const themeToggleBtn = document.getElementById('themeToggleBtn');
    const printBtn = document.getElementById('printBtn');
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const sidebarOverlay = document.getElementById('sidebarOverlay');
    const navItems = document.querySelectorAll('.nav-item');
    const filmSections = document.querySelectorAll('.film-section');
    const filterPills = document.querySelectorAll('.filter-pill');
    const copyBtns = document.querySelectorAll('.copy-btn');

    // Active subtitle player state
    let playerInterval = null;
    let currentPlayerId = null;
    let currentCaptionIndex = 0;

    // Transcripts database for Talking Head (Style B) interactive player
    const transcripts = {
        2: [
            { text: "There is a moment in your forties", highlight: [] },
            { text: "when the menu suddenly feels too close to read.", highlight: [] },
            { text: "You are not imagining it,", highlight: [] },
            { text: "and you are certainly not the only one.", highlight: [] },
            { text: "It is not your ARMS getting shorter,", highlight: ["arms"] },
            { text: "it is PRESBYOPIA,", highlight: ["presbyopia"] },
            { text: "and it happens to every single one of us in time.", highlight: [] },
            { text: "The lens inside your eye gradually loses the flexibility", highlight: [] },
            { text: "to focus up close, usually from your MID FORTIES.", highlight: ["mid", "forties"] },
            { text: "Distance vision often stays fine.", highlight: [] },
            { text: "It is the NEAR work that suffers,", highlight: ["near"] },
            { text: "reading, your phone, threading a needle.", highlight: [] },
            { text: "Reading glasses are the usual answer,", highlight: [] },
            { text: "but they are NO LONGER THE ONLY ONE.", highlight: ["no", "longer", "the", "only", "one"] }
        ],
        4: [
            { text: "Most people do not realise you can have", highlight: [] },
            { text: "two different eye conditions at the same time", highlight: [] },
            { text: "and feel completely fine.", highlight: [] },
            { text: "Cataract clouds the lens at the FRONT of the eye.", highlight: ["front"] },
            { text: "Glaucoma damages the optic nerve at the BACK.", highlight: ["back"] },
            { text: "Two separate things.", highlight: [] },
            { text: "They tend to appear in the same age group,", highlight: [] },
            { text: "so it is common to be developing BOTH TOGETHER.", highlight: ["both", "together"] },
            { text: "They hide in different ways.", highlight: [] },
            { text: "The cataract slowly blurs your vision,", highlight: [] },
            { text: "while the glaucoma stays completely SILENT.", highlight: ["silent"] },
            { text: "So you cannot rely on how your eyes feel", highlight: [] },
            { text: "to tell you whether either one is there.", highlight: [] },
            { text: "One appointment catches both.", highlight: [] }
        ],
        6: [
            { text: "If you love someone with diabetes,", highlight: [] },
            { text: "this is worth two minutes of your time,", highlight: [] },
            { text: "and possibly their sight.", highlight: [] },
            { text: "Diabetes can quietly damage the tiny blood vessels", highlight: [] },
            { text: "at the back of the eye.", highlight: [] },
            { text: "That is DIABETIC RETINOPATHY.", highlight: ["diabetic", "retinopathy"] },
            { text: "Early on there are usually NO SYMPTOMS AT ALL.", highlight: ["no", "symptoms", "at", "all"] },
            { text: "Vision can feel completely normal while the damage builds.", highlight: [] },
            { text: "This is exactly why the NHS sends that YEARLY LETTER.", highlight: ["yearly", "letter"] },
            { text: "It exists to catch this EARLY.", highlight: ["early"] },
            { text: "Do not ignore it.", highlight: [] }
        ],
        8: [
            { text: "If one eye has gone red and achy,", highlight: [] },
            { text: "and suddenly you cannot stand bright light,", highlight: [] },
            { text: "please do not just wait for it to pass.", highlight: [] },
            { text: "That combination is not always the minor thing it looks like.", highlight: [] },
            { text: "Uveitis is INFLAMMATION INSIDE THE EYE itself,", highlight: ["inflammation", "inside", "the", "eye"] },
            { text: "in the middle layer we call the uvea.", highlight: [] },
            { text: "The tell tale signs are a red eye that genuinely aches,", highlight: [] },
            { text: "real SENSITIVITY TO LIGHT,", highlight: ["sensitivity", "to", "light"] },
            { text: "blurred vision, and sometimes floaters.", highlight: [] },
            { text: "It behaves differently. It does NOT SETTLE ON ITS OWN.", highlight: ["not", "settle", "on", "its", "own"] },
            { text: "Do not wait.", highlight: [] }
        ],
        9: [
            { text: "If your eyes water so much", highlight: [] },
            { text: "that people keep asking if you have been crying,", highlight: [] },
            { text: "here is the twist.", highlight: [] },
            { text: "That watering is very often a sign your eyes are TOO DRY.", highlight: ["too", "dry"] },
            { text: "WATERY EYES are one of the most common signs of dry eye.", highlight: ["watery", "eyes"] },
            { text: "When the surface dries out, the eye panics", highlight: [] },
            { text: "and floods itself with REFLEX TEARS,", highlight: ["reflex", "tears"] },
            { text: "which spill over instead of coating the eye.", highlight: [] },
            { text: "Drops that only add water often do NOT FIX IT.", highlight: ["not", "fix", "it"] },
            { text: "It is about fixing the TEAR FILM.", highlight: ["tear", "film"] },
            { text: "And there are proper ways to do that.", highlight: [] }
        ]
    };

    /* ==========================================================================
       SAFE STORAGE & UTILITIES FOR FILE:// COMPATIBILITY
       ========================================================================== */
    const safeStorage = {
        getItem: (key) => {
            try {
                return localStorage.getItem(key);
            } catch (e) {
                console.warn('localStorage is blocked on local file protocol: ', e);
                return null;
            }
        },
        setItem: (key, value) => {
            try {
                localStorage.setItem(key, value);
            } catch (e) {
                console.warn('localStorage is blocked on local file protocol: ', e);
            }
        }
    };

    const safeUpdateHash = (hash) => {
        try {
            history.pushState(null, null, hash);
        } catch (e) {
            console.warn('history.pushState blocked (expected on local file://): ', e);
            window.location.hash = hash;
        }
    };

    /* ==========================================================================
       THEME CONTROLLER
       ========================================================================== */
    const initTheme = () => {
        const savedTheme = safeStorage.getItem('eyepros-theme');
        
        if (savedTheme === 'dark') {
            document.documentElement.setAttribute('data-theme', 'dark');
        } else {
            // Default to Light Mode on first load, even if the OS prefers dark
            document.documentElement.setAttribute('data-theme', 'light');
        }
    };

    themeToggleBtn.addEventListener('click', () => {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        
        document.documentElement.setAttribute('data-theme', newTheme);
        safeStorage.setItem('eyepros-theme', newTheme);
    });

    initTheme();

    /* ==========================================================================
       ROUTING & NAVIGATION SWITCHER
       ========================================================================== */

    const navigateTo = (targetId) => {
        console.log('navigateTo triggered for targetId:', targetId);
        const targetSection = document.getElementById(targetId);
        if (!targetSection) {
            console.error('navigateTo error: Element with ID not found in DOM:', targetId);
            return;
        }

        // Early exit if already navigated to avoid redundant work/animations
        if (targetSection.classList.contains('active-section')) {
            console.log('Already on section, returning early:', targetId);
            return;
        }

        // Stop any running subtitle animations (inline safe-stop — avoids hoisting issue)
        if (playerInterval) { clearInterval(playerInterval); playerInterval = null; }
        if (currentPlayerId) {
            const prevSection = document.getElementById(`film-${currentPlayerId}`);
            if (prevSection) {
                const pb = prevSection.querySelector('.play-btn');
                const pauseB = prevSection.querySelector('.pause-btn');
                if (pb) { pb.disabled = false; pb.innerHTML = '<i class="fa fa-play"></i> Play'; }
                if (pauseB) pauseB.disabled = true;
            }
            currentPlayerId = null;
            currentCaptionIndex = 0;
        }

        // Remove active class from all sections
        filmSections.forEach(sec => sec.classList.remove('active-section'));

        // Add active class to target section
        targetSection.classList.add('active-section');
        console.log('Active-section class added to element:', targetId);

        // Update active class in sidebar items
        navItems.forEach(item => {
            if (item.getAttribute('href') === `#${targetId}`) {
                item.classList.add('active');
            } else {
                item.classList.remove('active');
            }
        });

        // Close mobile menu drawer if open
        document.body.classList.remove('sidebar-open');

        // Scroll the viewport of content pane back to top
        const contentPane = document.getElementById('contentPane');
        if (contentPane) {
            contentPane.scrollTop = 0;
        }
    };

    // Route matching from hash changes
    const handleRoute = () => {
        const hash = window.location.hash.substring(1);
        console.log('handleRoute triggered with hash:', hash);
        if (hash) {
            const targetSection = document.getElementById(hash);
            if (targetSection) {
                navigateTo(hash);
                return;
            } else {
                console.warn('handleRoute warn: Hash points to missing element:', hash);
            }
        }
        // Fallback: Default to film-1
        console.log('No hash or target found, falling back to film-1');
        navigateTo('film-1');
    };

    window.addEventListener('hashchange', () => {
        console.log('hashchange event fired! New hash:', window.location.hash);
        handleRoute();
    });

    // Direct click listeners for bulletproof navigation triggers
    navItems.forEach(item => {
        item.addEventListener('click', (e) => {
            const href = item.getAttribute('href');
            console.log('navItem click detected for href:', href);
            if (href && href.startsWith('#')) {
                e.preventDefault();
                const targetId = href.substring(1);
                
                // Navigate immediately
                navigateTo(targetId);
                
                // Safe history state update
                safeUpdateHash(href);
            }
        });
    });
    
    // Initial check on load
    console.log('Initializing scriptbook navigation routing...');
    handleRoute();

    /* ==========================================================================
       MOBILE DRAWER NAVIGATION
       ========================================================================== */
    const toggleSidebar = () => {
        document.body.classList.toggle('sidebar-open');
    };

    mobileMenuBtn.addEventListener('click', toggleSidebar);
    sidebarOverlay.addEventListener('click', toggleSidebar);

    /* ==========================================================================
       EPISODES STYLE FILTERING
       ========================================================================== */
    filterPills.forEach(pill => {
        pill.addEventListener('click', () => {
            // Remove active style from pills
            filterPills.forEach(p => p.classList.remove('active'));
            pill.classList.add('active');

            const filterValue = pill.getAttribute('data-filter');
            const episodeLinks = document.querySelectorAll('#episodesLinks .nav-item');

            episodeLinks.forEach(link => {
                const styleType = link.getAttribute('data-style');
                if (filterValue === 'all' || styleType === filterValue) {
                    link.style.display = 'flex';
                } else {
                    link.style.display = 'none';
                }
            });

            // If the active episode became hidden, redirect to the first visible one
            const currentActiveItem = document.querySelector(`.nav-item.active`);
            
            if (currentActiveItem && currentActiveItem.style.display === 'none') {
                const firstVisible = Array.from(episodeLinks).find(item => item.style.display !== 'none');
                if (firstVisible) {
                    const href = firstVisible.getAttribute('href');
                    navigateTo(href.substring(1));
                    safeUpdateHash(href);
                }
            }
        });
    });

    /* ==========================================================================
       PRODUCTION TAB CONTROL LOGIC
       ========================================================================== */
    document.querySelectorAll('.tabbed-card').forEach(card => {
        const tabBtns = card.querySelectorAll('.tab-btn');
        const tabContents = card.querySelectorAll('.tab-content');

        tabBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                const targetTab = btn.getAttribute('data-tab');

                // Toggle Active Tab Button
                tabBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');

                // Toggle Active Content Pane
                tabContents.forEach(content => {
                    if (content.getAttribute('data-tab-content') === targetTab) {
                        content.classList.add('active-tab');
                    } else {
                        content.classList.remove('active-tab');
                    }
                });
            });
        });
    });

    /* ==========================================================================
       PRINT ACTIONS
       ========================================================================== */
    printBtn.addEventListener('click', () => {
        window.print();
    });

    /* ==========================================================================
       CLIPBOARD UTILITIES
       ========================================================================== */
    const showCopyFeedback = (btn) => {
        const originalHTML = btn.innerHTML;
        btn.innerHTML = '<i class="fa fa-check"></i> Copied!';
        btn.classList.add('copied');
        
        setTimeout(() => {
            btn.innerHTML = originalHTML;
            btn.classList.remove('copied');
        }, 2000);
    };

    copyBtns.forEach(btn => {
        btn.addEventListener('click', async () => {
            const targetSelector = btn.getAttribute('data-clipboard-target');
            const targetElement = document.querySelector(targetSelector);
            
            if (targetElement) {
                // Fallback for non-secure contexts (such as file:// protocol)
                if (!navigator.clipboard) {
                    try {
                        targetElement.select();
                        document.execCommand('copy');
                        showCopyFeedback(btn);
                    } catch (err) {
                        console.error('Fallback copy failed: ', err);
                    }
                    return;
                }

                try {
                    await navigator.clipboard.writeText(targetElement.value);
                    showCopyFeedback(btn);
                } catch (err) {
                    console.error('Failed to copy text: ', err);
                }
            }
        });
    });

    /* ==========================================================================
       INTERACTIVE SUBTITLE / CAPTION PLAYER
       ========================================================================== */
    const highlightWords = (text, highlightList) => {
        if (!highlightList || highlightList.length === 0) return text;
        
        let words = text.split(' ');
        words = words.map(word => {
            const cleanWord = word.toLowerCase().replace(/[.,\/#!$%\^&\*;:{}=\-_`~()?"']/g, "");
            const isMatch = highlightList.some(hl => cleanWord === hl.toLowerCase());
            
            if (isMatch) {
                return `<span class="hl">${word}</span>`;
            }
            return word;
        });
        
        return words.join(' ');
    };

    const updateCaptionDisplay = (scriptId, textNodeHTML) => {
        const display = document.getElementById(`caption-display-${scriptId}`);
        if (display) {
            display.innerHTML = `<span class="animated-caption">${textNodeHTML}</span>`;
        }
    };

    const playCaptionPlayer = (scriptId) => {
        const scriptCaptions = transcripts[scriptId];
        if (!scriptCaptions) return;

        stopCaptionPlayer();

        currentPlayerId = scriptId;
        currentCaptionIndex = 0;
        
        setPlayerButtonStates(scriptId, { playing: true });
        renderNextCaption(scriptId);

        playerInterval = setInterval(() => {
            renderNextCaption(scriptId);
        }, 1900);
    };

    const renderNextCaption = (scriptId) => {
        const scriptCaptions = transcripts[scriptId];
        
        if (currentCaptionIndex >= scriptCaptions.length) {
            stopCaptionPlayer();
            updateCaptionDisplay(scriptId, "Preview completed. Click Play to watch again.");
            return;
        }

        const captionData = scriptCaptions[currentCaptionIndex];
        const formattedHTML = highlightWords(captionData.text, captionData.highlight);
        
        updateCaptionDisplay(scriptId, formattedHTML);
        currentCaptionIndex++;
    };

    const pauseCaptionPlayer = (scriptId) => {
        if (playerInterval) {
            clearInterval(playerInterval);
            playerInterval = null;
            setPlayerButtonStates(scriptId, { playing: false, paused: true });
        }
    };

    const stopCaptionPlayer = () => {
        if (playerInterval) {
            clearInterval(playerInterval);
            playerInterval = null;
        }
        if (currentPlayerId) {
            setPlayerButtonStates(currentPlayerId, { playing: false });
            updateCaptionDisplay(currentPlayerId, "Click Play to preview caption highlights...");
            currentPlayerId = null;
            currentCaptionIndex = 0;
        }
    };

    const resetCaptionPlayer = (scriptId) => {
        stopCaptionPlayer();
        playCaptionPlayer(scriptId);
    };

    const setPlayerButtonStates = (scriptId, state) => {
        const section = document.getElementById(`film-${scriptId}`);
        if (!section) return;

        const playBtn = section.querySelector('.play-btn');
        const pauseBtn = section.querySelector('.pause-btn');
        const resetBtn = section.querySelector('.reset-btn');

        if (state.playing) {
            playBtn.disabled = true;
            pauseBtn.disabled = false;
            resetBtn.disabled = false;
        } else if (state.paused) {
            playBtn.disabled = false;
            pauseBtn.disabled = true;
            resetBtn.disabled = false;
        } else {
            playBtn.disabled = false;
            pauseBtn.disabled = true;
            resetBtn.disabled = true;
        }
    };

    document.querySelectorAll('.play-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const scriptId = btn.getAttribute('data-script-id');
            playCaptionPlayer(scriptId);
        });
    });

    document.querySelectorAll('.pause-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            if (currentPlayerId) {
                pauseCaptionPlayer(currentPlayerId);
            }
        });
    });

    document.querySelectorAll('.reset-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const scriptId = btn.getAttribute('data-script-id');
            resetCaptionPlayer(scriptId);
        });
    });

    /* ==========================================================================
       TELEPROMPTER IMPLEMENTATION LOGIC
       ========================================================================== */
    const teleprompterOverlay = document.getElementById('teleprompterOverlay');
    const tpTitle = document.getElementById('tpTitle');
    const tpContent = document.getElementById('tpContent');
    const tpScrollContainer = document.getElementById('tpScrollContainer');
    const tpPlayBtn = document.getElementById('tpPlayBtn');
    const tpSpeedSlider = document.getElementById('tpSpeedSlider');
    const tpFontInc = document.getElementById('tpFontInc');
    const tpFontDec = document.getElementById('tpFontDec');
    const tpExitBtn = document.getElementById('tpExitBtn');

    let tpScrollInterval = null;
    let isTpScrolling = false;
    let tpScrollSpeed = 3; // range 1-10
    let tpFontSizeMultiplier = 1.0;
    const tpFontSizeBase = 2.2; // base rem

    // Auto-scroll loop
    const startTpScroll = () => {
        if (tpScrollInterval) clearInterval(tpScrollInterval);
        
        isTpScrolling = true;
        tpPlayBtn.innerHTML = '<i class="fa fa-pause"></i> Pause';
        
        // Speed delay calculations (higher speed = lower delay)
        const delay = Math.max(12, 140 - (tpScrollSpeed * 12));
        
        tpScrollInterval = setInterval(() => {
            tpScrollContainer.scrollBy(0, 1);
        }, delay);
    };

    const stopTpScroll = () => {
        isTpScrolling = false;
        tpPlayBtn.innerHTML = '<i class="fa fa-play"></i> Scroll';
        if (tpScrollInterval) {
            clearInterval(tpScrollInterval);
            tpScrollInterval = null;
        }
    };

    const toggleTpScroll = () => {
        if (isTpScrolling) {
            stopTpScroll();
        } else {
            startTpScroll();
        }
    };

    let wakeLock = null;
    const requestWakeLock = async () => {
        try {
            if ('wakeLock' in navigator) {
                wakeLock = await navigator.wakeLock.request('screen');
            }
        } catch (err) {
            console.warn('Screen Wake Lock blocked: ', err);
        }
    };

    const releaseWakeLock = () => {
        if (wakeLock) {
            try {
                wakeLock.release();
            } catch (err) {
                console.error('Error releasing wake lock: ', err);
            }
            wakeLock = null;
        }
    };

    // Open Teleprompter View
    const openTeleprompter = (scriptId) => {
        const section = document.getElementById(`film-${scriptId}`);
        if (!section) return;

        // Stop standard subtitle players if running
        stopCaptionPlayer();

        // Retrieve script items
        const titleText = section.querySelector('.film-title').innerText;
        const hookHTML = section.querySelector('[data-tp-hook]').innerHTML;
        const pointsHTML = section.querySelector('[data-tp-points]').innerHTML;
        const reassureHTML = section.querySelector('[data-tp-reassure]').innerHTML;
        const ctaHTML = section.querySelector('[data-tp-cta]').innerHTML;

        // Build clean reader structure
        let contentHTML = `
            <h1>${titleText}</h1>
            <div class="tp-hook-block">${hookHTML}</div>
            <div class="tp-points-block">${pointsHTML}</div>
            <div class="tp-reassure-block">${reassureHTML}</div>
            <div class="tp-cta-block">${ctaHTML}</div>
        `;

        // Load teleprompter DOM
        tpTitle.innerText = titleText;
        tpContent.innerHTML = contentHTML;
        
        // Reset scroll position and formatting
        tpScrollContainer.scrollTop = 0;
        tpFontSizeMultiplier = 1.0;
        tpContent.style.fontSize = `${tpFontSizeBase}rem`;
        
        // Show Overlay
        document.body.classList.add('tp-active');
        
        // Request wake lock to keep screen active
        requestWakeLock();
        
        // Set speed value
        tpScrollSpeed = parseInt(tpSpeedSlider.value);
        stopTpScroll();
    };

    const closeTeleprompter = () => {
        stopTpScroll();
        releaseWakeLock();
        document.body.classList.remove('tp-active');
    };

    // Font controllers
    tpFontInc.addEventListener('click', () => {
        if (tpFontSizeMultiplier < 2.0) {
            tpFontSizeMultiplier += 0.1;
            tpContent.style.fontSize = `${tpFontSizeMultiplier * tpFontSizeBase}rem`;
        }
    });

    tpFontDec.addEventListener('click', () => {
        if (tpFontSizeMultiplier > 0.6) {
            tpFontSizeMultiplier -= 0.1;
            tpContent.style.fontSize = `${tpFontSizeMultiplier * tpFontSizeBase}rem`;
        }
    });

    // Speed slider listener
    tpSpeedSlider.addEventListener('input', () => {
        tpScrollSpeed = parseInt(tpSpeedSlider.value);
        if (isTpScrolling) {
            startTpScroll(); // Restart with new tick speed
        }
    });

    // Control buttons listeners
    tpPlayBtn.addEventListener('click', toggleTpScroll);
    tpExitBtn.addEventListener('click', closeTeleprompter);
    
    // Bind click to all teleprompter buttons
    document.querySelectorAll('.teleprompter-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const scriptId = btn.getAttribute('data-script-id');
            openTeleprompter(scriptId);
        });
    });

    // Keyboard Shortcuts for Teleprompter
    window.addEventListener('keydown', (e) => {
        if (document.body.classList.contains('tp-active')) {
            if (e.code === 'Space') {
                e.preventDefault();
                toggleTpScroll();
            } else if (e.code === 'Escape') {
                e.preventDefault();
                closeTeleprompter();
            } else if (e.code === 'ArrowUp') {
                e.preventDefault();
                tpScrollContainer.scrollBy(0, -40);
            } else if (e.code === 'ArrowDown') {
                e.preventDefault();
                tpScrollContainer.scrollBy(0, 40);
            }
        }
    });

    /* ==========================================================================
       INTERACTIVE SETUP FLOORPLAN CONTROLLER
       ========================================================================== */
    const fpElements = document.querySelectorAll('.fp-element');
    const detailCards = document.querySelectorAll('.setup-detail-card');

    // Hover floorplan element -> highlight matching card
    fpElements.forEach(el => {
        const itemKey = el.getAttribute('data-item');
        if (!itemKey) return;

        el.addEventListener('mouseenter', () => {
            el.classList.add('highlighted');
            
            const matchingCard = Array.from(detailCards).find(card => card.getAttribute('data-detail') === itemKey);
            if (matchingCard) {
                matchingCard.classList.add('highlighted');
                matchingCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
            }
        });

        el.addEventListener('mouseleave', () => {
            el.classList.remove('highlighted');
            
            const matchingCard = Array.from(detailCards).find(card => card.getAttribute('data-detail') === itemKey);
            if (matchingCard) {
                matchingCard.classList.remove('highlighted');
            }
        });
    });

    // Hover card -> highlight matching floorplan element
    detailCards.forEach(card => {
        const detailKey = card.getAttribute('data-detail');
        if (!detailKey) return;

        card.addEventListener('mouseenter', () => {
            card.classList.add('highlighted');
            
            const matchingEl = Array.from(fpElements).find(el => el.getAttribute('data-item') === detailKey);
            if (matchingEl) {
                matchingEl.classList.add('highlighted');
            }
        });

        card.addEventListener('mouseleave', () => {
            card.classList.remove('highlighted');
            
            const matchingEl = Array.from(fpElements).find(el => el.getAttribute('data-item') === detailKey);
            if (matchingEl) {
                matchingEl.classList.remove('highlighted');
            }
        });
    });

    // Dynamic Prev/Next Episode Pager Injection for Mobile
    const injectPagers = () => {
        const sections = Array.from(filmSections);
        
        // Filter sections into groups
        const soloSections = sections.filter(sec => sec.id.startsWith('film-'));
        const podcastSections = sections.filter(sec => sec.id.startsWith('podcast-'));
        
        // Helper to setup pager for a list
        const setupListPager = (list, labelPrefix) => {
            const total = list.length;
            list.forEach((sec, index) => {
                const pager = document.createElement('div');
                pager.className = 'episode-pager';
                
                const prevIndex = index - 1;
                const nextIndex = index + 1;
                
                const prevDisabled = prevIndex < 0 ? 'disabled' : '';
                const nextDisabled = nextIndex >= total ? 'disabled' : '';
                
                const currentNum = index + 1;
                
                pager.innerHTML = `
                    <button class="pager-btn prev-btn" ${prevDisabled} title="Previous Episode">
                        <i class="fa fa-chevron-left"></i> Prev
                    </button>
                    <span class="pager-info">${labelPrefix} ${currentNum} / ${total}</span>
                    <button class="pager-btn next-btn" ${nextDisabled} title="Next Episode">
                        Next <i class="fa fa-chevron-right"></i>
                    </button>
                `;
                
                const scriptCard = sec.querySelector('.script-card');
                if (scriptCard) {
                    scriptCard.appendChild(pager);
                }
                
                pager.querySelector('.prev-btn').addEventListener('click', () => {
                    if (prevIndex >= 0) {
                        const prevSectionId = list[prevIndex].id;
                        navigateTo(prevSectionId);
                        safeUpdateHash(`#${prevSectionId}`);
                    }
                });
                
                pager.querySelector('.next-btn').addEventListener('click', () => {
                    if (nextIndex < total) {
                        const nextSectionId = list[nextIndex].id;
                        navigateTo(nextSectionId);
                        safeUpdateHash(`#${nextSectionId}`);
                    }
                });
            });
        };
        
        setupListPager(soloSections, 'Solo Film');
        setupListPager(podcastSections, 'Podcast');
    };

    injectPagers();

});
