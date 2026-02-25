// ===== CONFIGURATION =====
const CONFIG = {
    animationDelay: 100,
    scrollThreshold: 100,
    counterSpeed: 2000,
    loadingDuration: 2000
};

// ===== LOADING SCREEN =====
class LoadingScreen {
    constructor() {
        this.loadingScreen = document.getElementById('loading-screen');
        this.percentage = document.querySelector('.loading-percentage');
        this.progress = 0;
    }

    init() {
        if (!this.loadingScreen) return;
        this.simulateLoading();
    }

    simulateLoading() {
        const interval = setInterval(() => {
            this.progress += Math.random() * 15 + 5;
            
            if (this.progress >= 100) {
                this.progress = 100;
                clearInterval(interval);
                setTimeout(() => this.hide(), 300);
            }
            
            if (this.percentage) {
                this.percentage.textContent = `${Math.floor(this.progress)}%`;
            }
        }, 150);
    }

    hide() {
        this.loadingScreen.classList.add('loaded');
        document.body.style.overflow = 'visible';
    }
}

// ===== CUSTOM CURSOR =====
class CustomCursor {
    constructor() {
        this.cursorDot = document.querySelector('[data-cursor-dot]');
        this.cursorOutline = document.querySelector('[data-cursor-outline]');
        this.mouseX = 0;
        this.mouseY = 0;
        this.outlineX = 0;
        this.outlineY = 0;
    }

    init() {
        if (!this.cursorDot || !this.cursorOutline) return;
        if (window.innerWidth <= 768) return;

        document.addEventListener('mousemove', (e) => {
            this.mouseX = e.clientX;
            this.mouseY = e.clientY;
            
            this.cursorDot.style.left = `${e.clientX}px`;
            this.cursorDot.style.top = `${e.clientY}px`;
        });

        this.animate();
        this.addInteractiveEffects();
    }

    animate() {
        this.outlineX += (this.mouseX - this.outlineX) * 0.2;
        this.outlineY += (this.mouseY - this.outlineY) * 0.2;
        
        this.cursorOutline.style.left = `${this.outlineX}px`;
        this.cursorOutline.style.top = `${this.outlineY}px`;
        
        requestAnimationFrame(() => this.animate());
    }

    addInteractiveEffects() {
        const interactiveElements = document.querySelectorAll('a, button, .project-card, .contact-card');
        
        interactiveElements.forEach(el => {
            el.addEventListener('mouseenter', () => {
                this.cursorDot.style.transform = 'translate(-50%, -50%) scale(2)';
                this.cursorOutline.style.transform = 'translate(-50%, -50%) scale(1.5)';
            });
            
            el.addEventListener('mouseleave', () => {
                this.cursorDot.style.transform = 'translate(-50%, -50%) scale(1)';
                this.cursorOutline.style.transform = 'translate(-50%, -50%) scale(1)';
            });
        });
    }
}

// ===== NAVIGATION =====
class Navigation {
    constructor() {
        this.navbar = document.querySelector('[data-navbar]');
        this.hamburger = document.querySelector('[data-hamburger]');
        this.navMenu = document.querySelector('[data-nav-menu]');
        this.navLinks = document.querySelectorAll('.nav-link');
        this.themeToggle = document.querySelector('.theme-toggle');
    }

    init() {
        this.handleScroll();
        this.handleMobileMenu();
        this.handleSmoothScroll();
        this.handleThemeToggle();
        
        window.addEventListener('scroll', () => this.handleScroll());
    }

    handleScroll() {
        if (window.scrollY > CONFIG.scrollThreshold) {
            this.navbar?.classList.add('scrolled');
        } else {
            this.navbar?.classList.remove('scrolled');
        }
    }

    handleMobileMenu() {
        this.hamburger?.addEventListener('click', () => {
            this.hamburger.classList.toggle('active');
            this.navMenu?.classList.toggle('active');
            document.body.style.overflow = this.navMenu?.classList.contains('active') ? 'hidden' : '';
        });

        this.navLinks.forEach(link => {
            link.addEventListener('click', () => {
                this.hamburger?.classList.remove('active');
                this.navMenu?.classList.remove('active');
                document.body.style.overflow = '';
            });
        });
    }

    handleSmoothScroll() {
        this.navLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const targetId = link.getAttribute('href');
                const targetSection = document.querySelector(targetId);
                
                if (targetSection) {
                    const offsetTop = targetSection.offsetTop - 80;
                    window.scrollTo({
                        top: offsetTop,
                        behavior: 'smooth'
                    });
                }
            });
        });
    }

    handleThemeToggle() {
        this.themeToggle?.addEventListener('click', () => {
            document.body.classList.toggle('light-theme');
            localStorage.setItem('theme', document.body.classList.contains('light-theme') ? 'light' : 'dark');
        });

        const savedTheme = localStorage.getItem('theme');
        if (savedTheme === 'light') {
            document.body.classList.add('light-theme');
        }
    }
}

// ===== ANIMATED COUNTERS =====
class AnimatedCounters {
    constructor() {
        this.counters = document.querySelectorAll('.stat-number');
        this.observed = new Set();
    }

    init() {
        if (this.counters.length === 0) return;

        const observer = new IntersectionObserver(
            (entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting && !this.observed.has(entry.target)) {
                        this.animateCounter(entry.target);
                        this.observed.add(entry.target);
                    }
                });
            },
            { threshold: 0.5 }
        );

        this.counters.forEach(counter => observer.observe(counter));
    }

    animateCounter(element) {
        const target = parseInt(element.getAttribute('data-target'));
        const duration = CONFIG.counterSpeed;
        const increment = target / (duration / 16);
        let current = 0;

        const updateCounter = () => {
            current += increment;
            if (current < target) {
                element.textContent = Math.ceil(current);
                requestAnimationFrame(updateCounter);
            } else {
                element.textContent = target + '+';
            }
        };

        updateCounter();
    }
}

// ===== EXPERIENCE TABS =====
class ExperienceTabs {
    constructor() {
        this.tabButtons = document.querySelectorAll('.tab-button');
        this.tabPanels = document.querySelectorAll('.tab-panel');
        this.indicator = document.querySelector('.tab-indicator');
    }

    init() {
        if (this.tabButtons.length === 0) return;

        this.tabButtons.forEach((button, index) => {
            button.addEventListener('click', () => this.switchTab(index));
        });

        this.updateIndicator(0);
    }

    switchTab(index) {
        this.tabButtons.forEach(btn => btn.classList.remove('active'));
        this.tabPanels.forEach(panel => panel.classList.remove('active'));

        this.tabButtons[index].classList.add('active');
        this.tabPanels[index].classList.add('active');

        this.updateIndicator(index);
    }

    updateIndicator(index) {
        const button = this.tabButtons[index];
        if (!button || !this.indicator) return;

        if (window.innerWidth > 1024) {
            this.indicator.style.transform = `translateY(${button.offsetTop}px)`;
        } else {
            this.indicator.style.transform = `translateX(${button.offsetLeft}px)`;
        }
    }
}

// ===== SKILL BARS ANIMATION =====
class SkillBars {
    constructor() {
        this.skillItems = document.querySelectorAll('.skill-item');
        this.observed = new Set();
    }

    init() {
        if (this.skillItems.length === 0) return;

        const observer = new IntersectionObserver(
            (entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting && !this.observed.has(entry.target)) {
                        this.animateSkill(entry.target);
                        this.observed.add(entry.target);
                    }
                });
            },
            { threshold: 0.3 }
        );

        this.skillItems.forEach(item => observer.observe(item));
    }

    animateSkill(element) {
        const progressBar = element.querySelector('.skill-progress');
        const fillBar = element.querySelector('.skill-fill');
        
        if (progressBar) {
            const progress = progressBar.getAttribute('data-progress');
            setTimeout(() => {
                progressBar.style.width = progress + '%';
            }, 100);
        }
        
        if (fillBar) {
            const width = fillBar.style.getPropertyValue('--skill-width');
            setTimeout(() => {
                fillBar.style.width = width;
            }, 100);
        }
    }
}

// ===== SCROLL ANIMATIONS (AOS) =====
class ScrollAnimations {
    constructor() {
        this.elements = document.querySelectorAll('[data-aos]');
        this.observed = new Set();
    }

    init() {
        if (this.elements.length === 0) return;

        const observer = new IntersectionObserver(
            (entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting && !this.observed.has(entry.target)) {
                        const delay = entry.target.getAttribute('data-aos-delay') || 0;
                        setTimeout(() => {
                            entry.target.classList.add('aos-animate');
                        }, delay);
                        this.observed.add(entry.target);
                    }
                });
            },
            {
                threshold: 0.1,
                rootMargin: '0px 0px -50px 0px'
            }
        );

        this.elements.forEach(el => observer.observe(el));
    }
}

// ===== INITIALIZE ALL =====
class App {
    constructor() {
        this.loadingScreen = new LoadingScreen();
        this.customCursor = new CustomCursor();
        this.navigation = new Navigation();
        this.counters = new AnimatedCounters();
        this.experienceTabs = new ExperienceTabs();
        this.skillBars = new SkillBars();
        this.scrollAnimations = new ScrollAnimations();
    }

    init() {
        this.loadingScreen.init();

        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => this.initAll());
        } else {
            this.initAll();
        }
    }

    initAll() {
        this.customCursor.init();
        this.navigation.init();
        this.counters.init();
        this.experienceTabs.init();
        this.skillBars.init();
        this.scrollAnimations.init();

        this.addConsoleMessage();
    }

    addConsoleMessage() {
        const styles = [
            'color: #64ffda',
            'font-size: 20px',
            'font-weight: bold',
            'text-shadow: 2px 2px 4px rgba(100, 255, 218, 0.3)'
        ].join(';');

        console.log('%c👋 Hello, Developer!', styles);
        console.log('%cThanks for checking out my portfolio!', 'color: #8892b0; font-size: 14px;');
        console.log('%cBuilt with ❤️ using vanilla JavaScript and modern CSS', 'color: #8892b0; font-size: 12px;');
    }
}

// ===== VIDEO HOVER HANDLER =====
class VideoHoverHandler {
    constructor() {
        this.videoContainers = document.querySelectorAll('.project-video-container');
    }

    init() {
        this.videoContainers.forEach(container => {
            const video = container.querySelector('.project-video');
            if (!video) return;

            container.addEventListener('mouseenter', () => {
                video.play().catch(err => console.log('Video play failed:', err));
            });

            container.addEventListener('mouseleave', () => {
                video.pause();
                video.currentTime = 0;
            });
        });
    }
}

// ===== CONTACT FORM HANDLER =====
class ContactForm {
    constructor() {
        this.form = document.getElementById('contact-form');
        this.status = document.getElementById('form-status');
    }

    init() {
        if (!this.form) return;
        this.form.addEventListener('submit', (e) => this.handleSubmit(e));
    }

    async handleSubmit(e) {
        e.preventDefault();
        
        const formData = {
            name: document.getElementById('name').value,
            email: document.getElementById('email').value,
            subject: document.getElementById('subject').value,
            message: document.getElementById('message').value
        };

        try {
            this.showStatus('Sending message...', 'loading');
            
            // Using EmailJS - Replace with your EmailJS credentials
            // For now, simulating form submission
            await emailjs.send('service_tdim05b', 'template_u49eci5', formData);
            
            this.showStatus('Message sent successfully! I\'ll get back to you soon.', 'success');
            this.form.reset();
            
            setTimeout(() => {
                this.hideStatus();
            }, 5000);
            
        } catch (error) {
            this.showStatus('Failed to send message. Please try emailing directly.', 'error');
            console.error('Form submission error:', error);
        }
    }

    simulateFormSubmission(data) {
        return new Promise((resolve) => {
            // Simulate API call
            setTimeout(() => {
                console.log('Form submitted:', data);
                // In production, replace this with actual EmailJS or backend API call:
                // emailjs.send('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', data, 'YOUR_PUBLIC_KEY')
                resolve();
            }, 1500);
        });
    }

    showStatus(message, type) {
        this.status.textContent = message;
        this.status.className = `form-status form-status-${type}`;
        this.status.style.display = 'block';
    }

    hideStatus() {
        this.status.style.display = 'none';
    }
}

// ===== START APPLICATION =====
const app = new App();
app.init();

// Initialize video hover handler
const videoHandler = new VideoHoverHandler();
videoHandler.init();

// Initialize contact form
const contactForm = new ContactForm();
contactForm.init();
