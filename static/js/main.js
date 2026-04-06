/**
 * main.js — Portfolio by Animesh Choudhury
 * Handles: scroll-reveal animations, nav scroll-shrink,
 *          image lazy-fade, mobile menu close on link click.
 */

/* ══ Scroll-Reveal via IntersectionObserver ══════════ */
(function initReveal() {
    const revealEls = document.querySelectorAll('.reveal');
    if (!revealEls.length) return;

    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                }
            });
        },
        { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
    );

    revealEls.forEach(el => observer.observe(el));
})();


/* ══ Navbar scroll-shrink (reinforced in JS) ════════ */
(function initNavScroll() {
    const nav = document.getElementById('mainNav');
    if (!nav) return;

    let ticking = false;
    window.addEventListener('scroll', () => {
        if (!ticking) {
            window.requestAnimationFrame(() => {
                nav.classList.toggle('scrolled', window.scrollY > 40);
                ticking = false;
            });
            ticking = true;
        }
    }, { passive: true });
})();


/* ══ Mobile nav: close on link click ═══════════════ */
(function initMobileNavClose() {
    const links     = document.querySelectorAll('.nav-links a');
    const navLinks  = document.getElementById('navLinks');
    const menuBtn   = document.getElementById('menuToggleBtn');

    links.forEach(link => {
        link.addEventListener('click', () => {
            if (navLinks) navLinks.classList.remove('active');
            if (menuBtn)  menuBtn.setAttribute('aria-expanded', 'false');
        });
    });
})();


/* ══ Image lazy-fade ════════════════════════════════ */
(function initImageFade() {
    const images = document.querySelectorAll('img');
    images.forEach(img => {
        if (img.complete) {
            img.style.opacity = '1';
            return;
        }
        img.style.opacity = '0';
        img.style.transition = 'opacity 0.5s ease';
        img.addEventListener('load', () => {
            img.style.opacity = '1';
        });
        img.addEventListener('error', () => {
            img.style.opacity = '0.4';
        });
    });
})();


/* ══ Smooth scroll for anchor links ═════════════════ */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            e.preventDefault();
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });
});
