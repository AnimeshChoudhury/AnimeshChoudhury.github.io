/**
 * Animesh Choudhury Portfolio — 3D Interactive Effects
 * Features: Three.js particles, GSAP scroll, cursor glow,
 *           reveal animations, counter, tilt, parallax
 */

// ═════════════════════════════════════════════════════
// THREE.JS HERO PARTICLE FIELD
// ═════════════════════════════════════════════════════

const initHeroCanvas = () => {
    const canvas = document.getElementById('hero-canvas');
    if (!canvas || typeof THREE === 'undefined') return;

    const renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: true });
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.setSize(canvas.offsetWidth, canvas.offsetHeight);

    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, canvas.offsetWidth / canvas.offsetHeight, 0.1, 1000);
    camera.position.z = 5;

    // ── Particle geometry ──
    const COUNT = window.innerWidth < 768 ? 900 : 2000;
    const positions = new Float32Array(COUNT * 3);
    const colors    = new Float32Array(COUNT * 3);
    const sizes     = new Float32Array(COUNT);

    const palette = [
        new THREE.Color('#00d9ff'),
        new THREE.Color('#7c3aed'),
        new THREE.Color('#f43f8e'),
        new THREE.Color('#a78bfa'),
    ];

    for (let i = 0; i < COUNT; i++) {
        const i3 = i * 3;
        positions[i3]     = (Math.random() - 0.5) * 18;
        positions[i3 + 1] = (Math.random() - 0.5) * 14;
        positions[i3 + 2] = (Math.random() - 0.5) * 10;

        const col = palette[Math.floor(Math.random() * palette.length)];
        colors[i3]     = col.r;
        colors[i3 + 1] = col.g;
        colors[i3 + 2] = col.b;

        sizes[i] = Math.random() * 2.5 + 0.5;
    }

    const geometry = new THREE.BufferGeometry();
    geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    geometry.setAttribute('color',    new THREE.BufferAttribute(colors, 3));
    geometry.setAttribute('size',     new THREE.BufferAttribute(sizes, 1));

    const material = new THREE.PointsMaterial({
        size:            0.06,
        vertexColors:    true,
        transparent:     true,
        opacity:         0.75,
        sizeAttenuation: true,
        depthWrite:      false,
    });

    const particles = new THREE.Points(geometry, material);
    scene.add(particles);

    // ── Mouse interaction ──
    let mouseX = 0; let mouseY = 0;
    let targetX = 0; let targetY = 0;

    window.addEventListener('mousemove', (e) => {
        mouseX = (e.clientX / window.innerWidth  - 0.5) * 0.8;
        mouseY = (e.clientY / window.innerHeight - 0.5) * 0.5;
    }, { passive: true });

    // ── Resize handler ──
    const onResize = () => {
        const w = canvas.offsetWidth;
        const h = canvas.offsetHeight;
        renderer.setSize(w, h);
        camera.aspect = w / h;
        camera.updateProjectionMatrix();
    };
    window.addEventListener('resize', onResize, { passive: true });

    // ── Animate ──
    let frameId;
    const clockStart = Date.now();

    const animate = () => {
        frameId = requestAnimationFrame(animate);
        const elapsed = (Date.now() - clockStart) * 0.0004;

        targetX += (mouseX - targetX) * 0.05;
        targetY += (mouseY - targetY) * 0.05;

        particles.rotation.y = elapsed * 0.06 + targetX;
        particles.rotation.x = elapsed * 0.03 + targetY;

        renderer.render(scene, camera);
    };
    animate();

    // ── Pause when not visible ──
    const observer = new IntersectionObserver(([entry]) => {
        if (entry.isIntersecting) { animate(); }
        else { cancelAnimationFrame(frameId); }
    });
    observer.observe(canvas);
};

// ═════════════════════════════════════════════════════
// REVEAL ANIMATIONS ON SCROLL
// ═════════════════════════════════════════════════════

const initReveal = () => {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.08,
        rootMargin: '0px 0px -40px 0px',
    });

    document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
};

// ═════════════════════════════════════════════════════
// CUSTOM CURSOR EFFECT
// ═════════════════════════════════════════════════════

const initCursor = () => {
    if (!window.matchMedia('(pointer:fine)').matches) return;

    const glow = document.createElement('div');
    const dot  = document.createElement('div');
    glow.className = 'cursor-glow';
    dot.className  = 'cursor-dot';
    document.body.appendChild(glow);
    document.body.appendChild(dot);

    let gx = 0, gy = 0, dx = 0, dy = 0;

    document.addEventListener('mousemove', (e) => {
        gx = e.clientX; gy = e.clientY;
        glow.classList.add('active');
        dot.classList.add('active');
        glow.style.left = gx + 'px';
        glow.style.top  = gy + 'px';
    }, { passive: true });

    // Dot follows with slight lag
    const tickDot = () => {
        dx += (gx - dx) * 0.18;
        dy += (gy - dy) * 0.18;
        dot.style.left = dx + 'px';
        dot.style.top  = dy + 'px';
        requestAnimationFrame(tickDot);
    };
    tickDot();

    // Scale cursor on interactive elements
    const interactiveSelector = 'a, button, input, textarea, [role="button"], .project-card, .service-card';

    document.querySelectorAll(interactiveSelector).forEach(el => {
        el.addEventListener('mouseenter', () => glow.classList.add('hovering'), { passive: true });
        el.addEventListener('mouseleave', () => glow.classList.remove('hovering'), { passive: true });
    });

    document.addEventListener('mouseleave', () => {
        glow.classList.remove('active', 'hovering');
        dot.classList.remove('active');
    });
};

// ═════════════════════════════════════════════════════
// NAVIGATION — SCROLL SHRINK
// ═════════════════════════════════════════════════════

const initNav = () => {
    const nav = document.getElementById('mainNav');
    if (!nav) return;

    window.addEventListener('scroll', () => {
        nav.classList.toggle('scrolled', window.scrollY > 50);
    }, { passive: true });
};

// ═════════════════════════════════════════════════════
// 3D TILT EFFECT
// ═════════════════════════════════════════════════════

const initTilt = () => {
    if (window.innerWidth < 768) return; // Skip on mobile

    const cards = document.querySelectorAll('.project-card, .service-card, .impact-item');

    cards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const r = card.getBoundingClientRect();
            const x = e.clientX - r.left;
            const y = e.clientY - r.top;
            const rx = ((y - r.height / 2) / r.height) * 10;
            const ry = ((r.width  / 2 - x) / r.width)  * 10;
            card.style.transform = `perspective(1000px) rotateX(${rx}deg) rotateY(${ry}deg) scale(1.02)`;
        }, { passive: true });

        card.addEventListener('mouseleave', () => {
            card.style.transform = '';
            card.style.transition = 'transform 0.5s cubic-bezier(0.34,1.56,0.64,1)';
        }, { passive: true });

        card.addEventListener('mouseenter', () => {
            card.style.transition = 'transform 0.15s ease';
        }, { passive: true });
    });
};

// ═════════════════════════════════════════════════════
// PARALLAX SCROLLING
// ═════════════════════════════════════════════════════

const initParallax = () => {
    const els = document.querySelectorAll('[data-parallax]');
    if (els.length === 0) return;

    const tick = () => {
        const scrollY = window.scrollY;
        els.forEach(el => {
            const speed = parseFloat(el.dataset.parallax) || 0.4;
            el.style.transform = `translateY(${scrollY * speed}px)`;
        });
    };

    window.addEventListener('scroll', tick, { passive: true });
    tick();
};

// ═════════════════════════════════════════════════════
// COUNTER ANIMATION — targets .impact-number[data-target]
// ═════════════════════════════════════════════════════

const animateCounter = (el, target, duration = 1600) => {
    const start = performance.now();
    const ease  = t => 1 - Math.pow(1 - t, 3);

    const tick = (ts) => {
        const p = Math.min((ts - start) / duration, 1);
        el.textContent = Math.round(target * ease(p));
        if (p < 1) requestAnimationFrame(tick);
    };

    requestAnimationFrame(tick);
};

const initCounters = () => {
    // Targets both .impact-number and .stat-number for safety
    const counters = document.querySelectorAll('.impact-number[data-target], .stat-number[data-target]');
    if (counters.length === 0) return;

    let started = false;
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !started) {
                started = true;
                counters.forEach(c => animateCounter(c, parseInt(c.dataset.target, 10)));
                observer.disconnect();
            }
        });
    }, { threshold: 0.4 });

    observer.observe(counters[0]);
};

// ═════════════════════════════════════════════════════
// SMOOTH SCROLL FOR ANCHOR LINKS
// ═════════════════════════════════════════════════════

const initSmoothScroll = () => {
    document.querySelectorAll('a[href^="#"]').forEach(link => {
        link.addEventListener('click', e => {
            const href = link.getAttribute('href');
            if (href === '#') return;
            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });
};

// ═════════════════════════════════════════════════════
// MOBILE MENU TOGGLE (backup — base.html also handles it)
// ═════════════════════════════════════════════════════

const initMobileMenu = () => {
    const btn   = document.getElementById('menuToggleBtn');
    const links = document.getElementById('navLinks');
    if (!btn || !links) return;

    btn.addEventListener('click', () => {
        const isOpen = links.classList.toggle('active');
        btn.classList.toggle('open', isOpen);
        btn.setAttribute('aria-expanded', isOpen);
    });

    // Close when a link is clicked
    links.querySelectorAll('a').forEach(a => {
        a.addEventListener('click', () => {
            links.classList.remove('active');
            btn.classList.remove('open');
            btn.setAttribute('aria-expanded', 'false');
        });
    });
};

// ═════════════════════════════════════════════════════
// LAZY LOAD IMAGES
// ═════════════════════════════════════════════════════

const initLazyImages = () => {
    if (!('IntersectionObserver' in window)) return;

    const obs = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                if (img.dataset.src) { img.src = img.dataset.src; }
                img.classList.add('loaded');
                obs.unobserve(img);
            }
        });
    });

    document.querySelectorAll('img[data-src]').forEach(img => obs.observe(img));
};

// ═════════════════════════════════════════════════════
// GSAP SCROLL ANIMATIONS (if GSAP is loaded)
// ═════════════════════════════════════════════════════

const initGSAP = () => {
    if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') return;

    gsap.registerPlugin(ScrollTrigger);

    // Hero text stagger
    gsap.from('.hero-text > *', {
        y: 40,
        opacity: 0,
        duration: 0.9,
        stagger: 0.15,
        ease: 'back.out(1.4)',
        delay: 0.2,
    });

    // Section headers
    gsap.utils.toArray('.section-header').forEach(header => {
        gsap.from(header, {
            scrollTrigger: { trigger: header, start: 'top 85%', toggleActions: 'play none none none' },
            y: 35,
            opacity: 0,
            duration: 0.8,
            ease: 'power3.out',
        });
    });
};

// ═════════════════════════════════════════════════════
// BOOT
// ═════════════════════════════════════════════════════

const boot = () => {
    initReveal();
    initNav();
    initCursor();
    initTilt();
    initParallax();
    initCounters();
    initSmoothScroll();
    initMobileMenu();
    initLazyImages();
    initGSAP();

    // Three.js canvas (only runs if canvas + THREE exist)
    if (typeof THREE !== 'undefined') {
        initHeroCanvas();
    }
};

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
} else {
    boot();
}
