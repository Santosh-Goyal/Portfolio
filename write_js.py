#!/usr/bin/env python3
import os

css_content = """/* ===== MODERN PROFESSIONAL PORTFOLIO STYLES ===== */

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

:root {
    --color-bg-primary: #0a192f;
    --color-bg-secondary: #112240;
    --color-bg-tertiary: #1a2f4a;
    --color-text-primary: #ccd6f6;
    --color-text-secondary: #8892b0;
    --color-text-tertiary: #495670;
    --color-accent-primary: #64ffda;
    --color-accent-glow: rgba(100, 255, 218, 0.3);
    --color-gradient-1: #667eea;
    --color-gradient-2: #764ba2;
    --color-gradient-3: #f093fb;
    --font-primary: 'Inter', -apple-system, system-ui, sans-serif;
    --font-mono: 'JetBrains Mono', 'Fira Code', monospace;
    --font-display: 'Space Grotesk', sans-serif;
    --font-size-xs: 0.75rem;
    --font-size-sm: 0.875rem;
    --font-size-base: 1rem;
    --font-size-lg: 1.125rem;
    --font-size-xl: 1.25rem;
    --font-size-2xl: 1.5rem;
    --font-size-3xl: 1.875rem;
    --font-size-4xl: 2.25rem;
    --font-size-5xl: 3rem;
    --spacing-xs: 0.25rem;
    --spacing-sm: 0.5rem;
    --spacing-md: 1rem;
    --spacing-lg: 1.5rem;
    --spacing-xl: 2rem;
    --spacing-2xl: 3rem;
    --spacing-3xl: 4rem;
    --spacing-4xl: 6rem;
    --container-width: 1200px;
    --container-padding: 2rem;
    --section-padding: 8rem 0;
    --radius-sm: 0.25rem;
    --radius-md: 0.5rem;
    --radius-lg: 0.75rem;
    --radius-xl: 1rem;
    --radius-2xl: 1.5rem;
    --radius-full: 9999px;
    --transition-fast: 150ms cubic-bezier(0.4, 0, 0.2, 1);
    --transition-base: 300ms cubic-bezier(0.4, 0, 0.2, 1);
    --transition-slow: 500ms cubic-bezier(0.4, 0, 0.2, 1);
    --z-fixed: 1030;
}

html {
    font-size: 16px;
    scroll-behavior: smooth;
    scroll-padding-top: 80px;
}

body {
    font-family: var(--font-primary);
    font-size: var(--font-size-base);
    line-height: 1.6;
    color: var(--color-text-primary);
    background-color: var(--color-bg-primary);
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    overflow-x: hidden;
}

::selection {
    background-color: var(--color-accent-primary);
    color: var(--color-bg-primary);
}

::-webkit-scrollbar {
    width: 12px;
}

::-webkit-scrollbar-track {
    background: var(--color-bg-primary);
}

::-webkit-scrollbar-thumb {
    background: var(--color-bg-tertiary);
    border-radius: var(--radius-full);
    border: 3px solid var(--color-bg-primary);
}

::-webkit-scrollbar-thumb:hover {
    background: var(--color-accent-primary);
}

.cursor-dot,
.cursor-outline {
    pointer-events: none;
    position: fixed;
    top: 0;
    left: 0;
    transform: translate(-50%, -50%);
    border-radius: 50%;
    z-index: 10000;
}

.cursor-dot {
    width: 8px;
    height: 8px;
    background-color: var(--color-accent-primary);
    box-shadow: 0 0 10px var(--color-accent-primary);
}

.cursor-outline {
    width: 40px;
    height: 40px;
    border: 2px solid var(--color-accent-primary);
    transition: all 0.15s ease-out;
}

@media (max-width: 768px) {
    .cursor-dot,
    .cursor-outline {
        display: none;
    }
}

#loading-screen {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100vh;
    background: var(--color-bg-primary);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    z-index: 10000;
    transition: opacity 0.5s ease, visibility 0.5s ease;
}

#loading-screen.loaded {
    opacity: 0;
    visibility: hidden;
}

.loader-wrapper {
    position: relative;
    width: 150px;
    height: 150px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.loader-ring {
    position: absolute;
    width: 100%;
    height: 100%;
    border: 4px solid transparent;
    border-top-color: var(--color-accent-primary);
    border-radius: 50%;
    animation: spin 1.5s cubic-bezier(0.68, -0.55, 0.265, 1.55) infinite;
}

.loader-ring:nth-child(2) {
    width: 80%;
    height: 80%;
    border-top-color: var(--color-gradient-1);
    animation-duration: 2s;
    animation-direction: reverse;
}

.loader-ring:nth-child(3) {
    width: 60%;
    height: 60%;
    border-top-color: var(--color-gradient-3);
    animation-duration: 1s;
}

.loader-text {
    font-family: var(--font-display);
    font-size: var(--font-size-3xl);
    font-weight: 700;
    color: var(--color-accent-primary);
    text-shadow: 0 0 20px var(--color-accent-glow);
}

.loading-percentage {
    margin-top: var(--spacing-2xl);
    font-family: var(--font-mono);
    font-size: var(--font-size-xl);
    color: var(--color-text-secondary);
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

.navbar {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 80px;
    padding: 0 var(--spacing-2xl);
    background: rgba(10, 25, 47, 0.85);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border-bottom: 1px solid rgba(100, 255, 218, 0.1);
    z-index: var(--z-fixed);
    transition: all var(--transition-base);
}

.navbar.scrolled {
    height: 70px;
    box-shadow: 0 10px 30px -10px rgba(2, 12, 27, 0.7);
}

.nav-container {
    max-width: var(--container-width);
    margin: 0 auto;
    height: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo {
    font-family: var(--font-mono);
    font-size: var(--font-size-lg);
    font-weight: 700;
    color: var(--color-accent-primary);
    text-decoration: none;
    display: flex;
    align-items: center;
    gap: var(--spacing-xs);
    transition: transform var(--transition-base);
}

.logo:hover {
    transform: translateY(-2px);
}

.logo-bracket {
    color: var(--color-accent-primary);
    font-size: var(--font-size-2xl);
}

.logo-text {
    color: var(--color-text-primary);
}

.logo-accent {
    background: linear-gradient(135deg, var(--color-gradient-1), var(--color-gradient-3));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.nav-menu {
    display: flex;
    list-style: none;
    gap: var(--spacing-2xl);
    align-items: center;
}

.nav-link {
    font-family: var(--font-mono);
    font-size: var(--font-size-sm);
    color: var(--color-text-primary);
    text-decoration: none;
    padding: var(--spacing-sm) 0;
    position: relative;
    transition: color var(--transition-base);
    display: flex;
    align-items: center;
    gap: var(--spacing-xs);
}

.nav-number {
    color: var(--color-accent-primary);
    font-size: var(--font-size-xs);
}

.nav-link::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 0;
    height: 2px;
    background: var(--color-accent-primary);
    transition: width var(--transition-base);
}

.nav-link:hover {
    color: var(--color-accent-primary);
}

.nav-link:hover::after {
    width: 100%;
}

.theme-toggle {
    width: 40px;
    height: 40px;
    border: 2px solid var(--color-accent-primary);
    border-radius: var(--radius-md);
    background: transparent;
    color: var(--color-accent-primary);
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
    transition: all var(--transition-base);
    position: relative;
    overflow: hidden;
}

.theme-toggle:hover {
    background: rgba(100, 255, 218, 0.1);
    transform: scale(1.05);
}

.theme-toggle i {
    position: absolute;
    font-size: var(--font-size-lg);
    transition: all var(--transition-base);
}

.theme-toggle .fa-moon {
    opacity: 1;
}

.theme-toggle .fa-sun {
    opacity: 0;
}

body.light-theme .theme-toggle .fa-moon {
    opacity: 0;
}

body.light-theme .theme-toggle .fa-sun {
    opacity: 1;
}

.hamburger {
    display: none;
    flex-direction: column;
    gap: 6px;
    background: transparent;
    border: none;
    cursor: pointer;
    padding: var(--spacing-sm);
}

.hamburger span {
    width: 25px;
    height: 2px;
    background: var(--color-accent-primary);
    transition: all var(--transition-base);
}

.hamburger.active span:nth-child(1) {
    transform: rotate(45deg) translate(8px, 8px);
}

.hamburger.active span:nth-child(2) {
    opacity: 0;
}

.hamburger.active span:nth-child(3) {
    transform: rotate(-45deg) translate(7px, -7px);
}

.container {
    max-width: var(--container-width);
    margin: 0 auto;
    padding: 0 var(--container-padding);
}

.hero {
    min-height: 100vh;
    display: flex;
    align-items: center;
    position: relative;
    overflow: hidden;
    padding: 120px 0 var(--spacing-4xl);
}

.hero-background {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
    overflow: hidden;
}

.grid-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: 
        linear-gradient(rgba(100, 255, 218, 0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(100, 255, 218, 0.03) 1px, transparent 1px);
    background-size: 50px 50px;
    opacity: 0.5;
}

.gradient-orb {
    position: absolute;
    border-radius: 50%;
    filter: blur(80px);
    opacity: 0.15;
    animation: float 20s ease-in-out infinite;
}

.orb-1 {
    width: 500px;
    height: 500px;
    background: linear-gradient(135deg, var(--color-gradient-1), var(--color-gradient-2));
    top: -200px;
    left: -200px;
    animation-delay: 0s;
}

.orb-2 {
    width: 400px;
    height: 400px;
    background: linear-gradient(135deg, var(--color-gradient-2), var(--color-gradient-3));
    bottom: -150px;
    right: -150px;
    animation-delay: -10s;
}

.orb-3 {
    width: 600px;
    height: 600px;
    background: radial-gradient(circle, var(--color-accent-primary), transparent);
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    animation-delay: -5s;
}

@keyframes float {
    0%, 100% {
        transform: translate(0, 0) scale(1);
    }
    33% {
        transform: translate(30px, -30px) scale(1.1);
    }
    66% {
        transform: translate(-20px, 20px) scale(0.9);
    }
}

.hero-content {
    position: relative;
    z-index: 1;
}

.hero-greeting {
    font-family: var(--font-mono);
    font-size: var(--font-size-base);
    color: var(--color-accent-primary);
    margin-bottom: var(--spacing-lg);
}

.hero-title {
    font-family: var(--font-display);
    font-size: clamp(3rem, 8vw, 6rem);
    font-weight: 800;
    line-height: 1.1;
    color: var(--color-text-primary);
    margin-bottom: var(--spacing-md);
}

.text-gradient {
    background: linear-gradient(135deg, var(--color-gradient-1), var(--color-gradient-3));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.hero-subtitle {
    font-family: var(--font-display);
    font-size: clamp(2rem, 5vw, 4rem);
    font-weight: 700;
    line-height: 1.2;
    color: var(--color-text-secondary);
    margin-bottom: var(--spacing-xl);
}

.hero-description {
    max-width: 600px;
    font-size: var(--font-size-lg);
    line-height: 1.8;
    color: var(--color-text-secondary);
    margin-bottom: var(--spacing-2xl);
}

.hero-description strong {
    color: var(--color-text-primary);
    font-weight: 600;
}

.hero-cta {
    display: flex;
    gap: var(--spacing-lg);
    flex-wrap: wrap;
    margin-bottom: var(--spacing-4xl);
}

.btn {
    display: inline-flex;
    align-items: center;
    gap: var(--spacing-sm);
    padding: 1rem 2rem;
    font-family: var(--font-mono);
    font-size: var(--font-size-sm);
    font-weight: 600;
    text-decoration: none;
    border-radius: var(--radius-md);
    transition: all var(--transition-base);
    cursor: pointer;
    border: none;
    position: relative;
    overflow: hidden;
}

.btn::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 0;
    height: 100%;
    background: rgba(255, 255, 255, 0.1);
    transition: width var(--transition-base);
}

.btn:hover::before {
    width: 100%;
}

.btn span,
.btn i {
    position: relative;
    z-index: 1;
}

.btn-primary {
    background: var(--color-accent-primary);
    color: var(--color-bg-primary);
    border: 2px solid var(--color-accent-primary);
}

.btn-primary:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 30px var(--color-accent-glow);
}

.btn-outline {
    background: transparent;
    color: var(--color-accent-primary);
    border: 2px solid var(--color-accent-primary);
}

.btn-outline:hover {
    background: rgba(100, 255, 218, 0.1);
    transform: translateY(-3px);
}

.btn-large {
    padding: 1.25rem 2.5rem;
    font-size: var(--font-size-base);
}

.hero-social,
.hero-email {
    position: fixed;
    bottom: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: var(--spacing-lg);
    z-index: 10;
}

.hero-social {
    left: var(--spacing-2xl);
}

.hero-email {
    right: var(--spacing-2xl);
}

.hero-social a {
    color: var(--color-text-secondary);
    font-size: var(--font-size-xl);
    transition: all var(--transition-base);
}

.hero-social a:hover {
    color: var(--color-accent-primary);
    transform: translateY(-3px);
}

.social-line,
.email-line {
    width: 1px;
    height: 90px;
    background: var(--color-text-tertiary);
}

.hero-email a {
    writing-mode: vertical-rl;
    font-family: var(--font-mono);
    font-size: var(--font-size-sm);
    color: var(--color-text-secondary);
    text-decoration: none;
    transition: all var(--transition-base);
}

.hero-email a:hover {
    color: var(--color-accent-primary);
    transform: translateY(-3px);
}

.scroll-indicator {
    position: absolute;
    bottom: var(--spacing-2xl);
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: var(--spacing-sm);
    font-family: var(--font-mono);
    font-size: var(--font-size-xs);
    color: var(--color-text-secondary);
    animation: bounce 2s infinite;
}

.scroll-line {
    width: 1px;
    height: 40px;
    background: linear-gradient(to bottom, var(--color-accent-primary), transparent);
}

@keyframes bounce {
    0%, 20%, 50%, 80%, 100% {
        transform: translateX(-50%) translateY(0);
    }
    40% {
        transform: translateX(-50%) translateY(-10px);
    }
    60% {
        transform: translateX(-50%) translateY(-5px);
    }
}

.section {
    padding: var(--section-padding);
    position: relative;
}

.section-header {
    margin-bottom: var(--spacing-4xl);
}

.section-title {
    font-family: var(--font-display);
    font-size: clamp(2rem, 5vw, 3rem);
    font-weight: 700;
    color: var(--color-text-primary);
    display: flex;
    align-items: center;
    gap: var(--spacing-md);
    position: relative;
}

.title-number {
    font-family: var(--font-mono);
    font-size: var(--font-size-xl);
    color: var(--color-accent-primary);
}

.title-line {
    flex: 1;
    height: 1px;
    background: var(--color-text-tertiary);
    max-width: 300px;
}

.section-subtitle {
    font-size: var(--font-size-lg);
    color: var(--color-text-secondary);
    margin-top: var(--spacing-md);
}

.about-content {
    display: grid;
    grid-template-columns: 3fr 2fr;
    gap: var(--spacing-4xl);
    align-items: start;
}

.text-content {
    display: flex;
    flex-direction: column;
    gap: var(--spacing-lg);
}

.text-content p {
    font-size: var(--font-size-lg);
    line-height: 1.8;
    color: var(--color-text-secondary);
}

.highlight {
    color: var(--color-accent-primary);
    font-weight: 600;
}

.tech-intro {
    margin-top: var(--spacing-md);
    margin-bottom: var(--spacing-sm);
}

.tech-stack {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: var(--spacing-sm);
    list-style: none;
    font-family: var(--font-mono);
    font-size: var(--font-size-sm);
}

.tech-stack li {
    color: var(--color-text-secondary);
}

.tech-stack li span {
    color: var(--color-accent-primary);
    margin-right: var(--spacing-sm);
}

.about-stats {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: var(--spacing-lg);
    margin-top: var(--spacing-2xl);
}

.stat-item {
    text-align: center;
    padding: var(--spacing-lg);
    background: rgba(100, 255, 218, 0.05);
    border: 1px solid rgba(100, 255, 218, 0.1);
    border-radius: var(--radius-lg);
    transition: all var(--transition-base);
}

.stat-item:hover {
    transform: translateY(-5px);
    border-color: var(--color-accent-primary);
    box-shadow: 0 10px 30px var(--color-accent-glow);
}

.stat-number {
    font-size: var(--font-size-4xl);
    font-weight: 700;
    color: var(--color-accent-primary);
    font-family: var(--font-display);
}

.stat-label {
    font-size: var(--font-size-sm);
    color: var(--color-text-secondary);
    margin-top: var(--spacing-xs);
}

.about-image {
    position: relative;
}

.image-wrapper {
    position: relative;
    width: 100%;
    max-width: 350px;
    aspect-ratio: 1;
    margin: 0 auto;
}

.image-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, rgba(100, 255, 218, 0.3), rgba(102, 126, 234, 0.3));
    border-radius: var(--radius-xl);
    z-index: 2;
    transition: all var(--transition-base);
    mix-blend-mode: multiply;
}

.image-wrapper:hover .image-overlay {
    opacity: 0;
}

.profile-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: var(--radius-xl);
    filter: grayscale(100%);
    transition: all var(--transition-base);
    position: relative;
    z-index: 1;
}

.image-wrapper:hover .profile-img {
    filter: grayscale(0%);
}

.image-border {
    position: absolute;
    top: 20px;
    left: 20px;
    width: 100%;
    height: 100%;
    border: 2px solid var(--color-accent-primary);
    border-radius: var(--radius-xl);
    z-index: 0;
    transition: all var(--transition-base);
}

.image-wrapper:hover .image-border {
    top: 15px;
    left: 15px;
}

.experience-section {
    background: var(--color-bg-secondary);
}

.experience-container {
    display: grid;
    grid-template-columns: 250px 1fr;
    gap: var(--spacing-3xl);
    min-height: 500px;
}

.experience-tabs {
    display: flex;
    flex-direction: column;
    gap: var(--spacing-xs);
    position: relative;
}

.tab-button {
    font-family: var(--font-mono);
    font-size: var(--font-size-sm);
    color: var(--color-text-secondary);
    background: transparent;
    border: none;
    border-left: 2px solid var(--color-text-tertiary);
    padding: var(--spacing-md) var(--spacing-lg);
    text-align: left;
    cursor: pointer;
    transition: all var(--transition-base);
}

.tab-button:hover,
.tab-button.active {
    color: var(--color-accent-primary);
    background: rgba(100, 255, 218, 0.05);
    border-left-color: var(--color-accent-primary);
}

.tab-indicator {
    position: absolute;
    left: 0;
    width: 2px;
    height: 42px;
    background: var(--color-accent-primary);
    transition: transform var(--transition-base);
    z-index: 1;
}

.experience-content {
    position: relative;
}

.tab-panel {
    display: none;
    animation: fadeIn 0.5s ease;
}

.tab-panel.active {
    display: block;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.timeline {
    display: flex;
    flex-direction: column;
    gap: var(--spacing-3xl);
    position: relative;
}

.timeline::before {
    content: '';
    position: absolute;
    left: 15px;
    top: 0;
    bottom: 0;
    width: 2px;
    background: var(--color-text-tertiary);
}

.timeline-item {
    position: relative;
    padding-left: var(--spacing-3xl);
}

.timeline-marker {
    position: absolute;
    left: 0;
    top: 0;
    width: 32px;
    height: 32px;
    border-radius: 50%;
    background: var(--color-bg-secondary);
    border: 2px solid var(--color-accent-primary);
    z-index: 1;
}

.timeline-marker::after {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background: var(--color-accent-primary);
}

.timeline-content h3 {
    font-size: var(--font-size-xl);
    color: var(--color-text-primary);
    margin-bottom: var(--spacing-sm);
}

.company {
    color: var(--color-accent-primary);
}

.timeline-date {
    font-family: var(--font-mono);
    font-size: var(--font-size-sm);
    color: var(--color-text-secondary);
    margin-bottom: var(--spacing-lg);
}

.timeline-list {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: var(--spacing-sm);
    margin-bottom: var(--spacing-lg);
}

.timeline-list li {
    padding-left: var(--spacing-lg);
    position: relative;
    color: var(--color-text-secondary);
    line-height: 1.6;
}

.timeline-list li::before {
    content: '?';
    position: absolute;
    left: 0;
    color: var(--color-accent-primary);
}

.tech-tags {
    display: flex;
    flex-wrap: wrap;
    gap: var(--spacing-sm);
}

.tech-tags span {
    padding: var(--spacing-xs) var(--spacing-md);
    font-family: var(--font-mono);
    font-size: var(--font-size-xs);
    color: var(--color-accent-primary);
    background: rgba(100, 255, 218, 0.1);
    border: 1px solid var(--color-accent-primary);
    border-radius: var(--radius-full);
}

.education-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: var(--spacing-xl);
}

.education-card {
    padding: var(--spacing-xl);
    background: rgba(100, 255, 218, 0.05);
    border: 1px solid rgba(100, 255, 218, 0.1);
    border-radius: var(--radius-xl);
    transition: all var(--transition-base);
}

.education-card:hover {
    transform: translateY(-5px);
    border-color: var(--color-accent-primary);
    box-shadow: 0 10px 30px var(--color-accent-glow);
}

.edu-icon {
    font-size: var(--font-size-4xl);
    color: var(--color-accent-primary);
    margin-bottom: var(--spacing-lg);
}

.education-card h3 {
    font-size: var(--font-size-xl);
    color: var(--color-text-primary);
    margin-bottom: var(--spacing-sm);
}

.edu-institution {
    font-size: var(--font-size-base);
    color: var(--color-text-secondary);
    margin-bottom: var(--spacing-xs);
}

.edu-location {
    font-size: var(--font-size-sm);
    color: var(--color-text-tertiary);
    margin-bottom: var(--spacing-sm);
}

.edu-location i {
    margin-right: var(--spacing-xs);
}

.edu-date {
    font-family: var(--font-mono);
    font-size: var(--font-size-sm);
    color: var(--color-text-secondary);
    margin-bottom: var(--spacing-md);
}

.edu-grade {
    display: inline-block;
    padding: var(--spacing-sm) var(--spacing-md);
    background: linear-gradient(135deg, var(--color-gradient-1), var(--color-gradient-3));
    color: white;
    font-weight: 600;
    border-radius: var(--radius-md);
    font-size: var(--font-size-sm);
}

.edu-details {
    margin-top: var(--spacing-md);
    padding-top: var(--spacing-md);
    border-top: 1px solid rgba(100, 255, 218, 0.1);
}

.edu-details p {
    font-size: var(--font-size-sm);
    color: var(--color-text-tertiary);
}

.cert-list {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: var(--spacing-md);
}

.cert-list li {
    padding: var(--spacing-md);
    background: rgba(100, 255, 218, 0.05);
    border-left: 3px solid var(--color-accent-primary);
    border-radius: var(--radius-sm);
}

.cert-list strong {
    display: block;
    color: var(--color-text-primary);
    margin-bottom: var(--spacing-xs);
}

.cert-list span {
    font-size: var(--font-size-sm);
    color: var(--color-text-tertiary);
}

.research-item {
    display: flex;
    flex-direction: column;
    gap: var(--spacing-sm);
}

.research-item strong {
    color: var(--color-text-primary);
    font-size: var(--font-size-base);
}

.research-item p {
    color: var(--color-text-secondary);
    font-size: var(--font-size-sm);
    line-height: 1.6;
}

.research-date {
    display: inline-block;
    padding: var(--spacing-xs) var(--spacing-md);
    background: rgba(100, 255, 218, 0.1);
    border: 1px solid var(--color-accent-primary);
    border-radius: var(--radius-full);
    font-family: var(--font-mono);
    font-size: var(--font-size-xs);
    color: var(--color-accent-primary);
}

.skills-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: var(--spacing-2xl);
}

.skill-category h3 {
    font-size: var(--font-size-xl);
    color: var(--color-text-primary);
    margin-bottom: var(--spacing-lg);
    padding-bottom: var(--spacing-sm);
    border-bottom: 2px solid rgba(100, 255, 218, 0.2);
}

.skill-list {
    display: flex;
    flex-direction: column;
    gap: var(--spacing-lg);
}

.skill-item {
    display: flex;
    flex-direction: column;
    gap: var(--spacing-sm);
}

.skill-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: var(--font-size-sm);
}

.skill-header span:first-child {
    color: var(--color-text-primary);
    display: flex;
    align-items: center;
    gap: var(--spacing-sm);
}

.skill-header i {
    color: var(--color-accent-primary);
}

.skill-header span:last-child {
    color: var(--color-accent-primary);
    font-family: var(--font-mono);
}

.skill-bar {
    height: 8px;
    background: rgba(100, 255, 218, 0.1);
    border-radius: var(--radius-full);
    overflow: hidden;
}

.skill-fill {
    height: 100%;
    width: 0%;
    background: linear-gradient(90deg, var(--color-accent-primary), var(--color-gradient-1));
    border-radius: var(--radius-full);
    transition: width 1s ease-out;
    position: relative;
}

.skill-fill::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
    transform: translateX(-100%);
    animation: shimmer 2s infinite;
}

@keyframes shimmer {
    100% {
        transform: translateX(100%);
    }
}

.projects-grid {
    display: flex;
    flex-direction: column;
    gap: var(--spacing-4xl);
    margin-bottom: var(--spacing-4xl);
}

.project-card {
    display: grid;
    grid-template-columns: repeat(12, 1fr);
    gap: var(--spacing-lg);
    align-items: center;
    position: relative;
}

.project-card.reverse {
    direction: rtl;
}

.project-card.reverse > * {
    direction: ltr;
}

.project-image {
    grid-column: 1 / 8;
    position: relative;
    border-radius: var(--radius-lg);
    overflow: hidden;
    height: 400px;
}

.project-card.reverse .project-image {
    grid-column: 6 / -1;
}

.project-placeholder {
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, var(--color-bg-tertiary), var(--color-bg-secondary));
    display: flex;
    justify-content: center;
    align-items: center;
}

.project-placeholder i {
    font-size: 5rem;
    color: var(--color-accent-primary);
    opacity: 0.3;
}

.project-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, rgba(100, 255, 218, 0.3), rgba(102, 126, 234, 0.3));
    mix-blend-mode: multiply;
    transition: all var(--transition-base);
}

.project-card:hover .project-overlay {
    opacity: 0;
}

.project-content {
    grid-column: 7 / -1;
    display: flex;
    flex-direction: column;
    gap: var(--spacing-md);
    align-items: flex-end;
    text-align: right;
}

.project-card.reverse .project-content {
    grid-column: 1 / 7;
    align-items: flex-start;
    text-align: left;
}

.project-overline {
    font-family: var(--font-mono);
    font-size: var(--font-size-sm);
    color: var(--color-accent-primary);
}

.project-title a {
    font-size: var(--font-size-2xl);
    font-weight: 700;
    color: var(--color-text-primary);
    text-decoration: none;
    transition: color var(--transition-base);
}

.project-title a:hover {
    color: var(--color-accent-primary);
}

.project-description {
    padding: var(--spacing-xl);
    background: var(--color-bg-tertiary);
    border-radius: var(--radius-lg);
    box-shadow: 0 10px 30px -10px rgba(2, 12, 27, 0.7);
    z-index: 2;
}

.project-description p {
    color: var(--color-text-secondary);
    line-height: 1.6;
}

.project-tech-list {
    display: flex;
    gap: var(--spacing-lg);
    list-style: none;
    flex-wrap: wrap;
}

.project-tech-list li {
    font-family: var(--font-mono);
    font-size: var(--font-size-sm);
    color: var(--color-text-secondary);
}

.project-links {
    display: flex;
    gap: var(--spacing-lg);
}

.project-links a {
    color: var(--color-text-primary);
    font-size: var(--font-size-xl);
    transition: all var(--transition-base);
}

.project-links a:hover {
    color: var(--color-accent-primary);
    transform: translateY(-3px);
}

.more-projects {
    margin-top: var(--spacing-4xl);
}

.more-projects-title {
    text-align: center;
    font-size: var(--font-size-2xl);
    color: var(--color-text-primary);
    margin-bottom: var(--spacing-2xl);
}

.small-projects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: var(--spacing-xl);
}

.small-project-card {
    padding: var(--spacing-xl);
    background: var(--color-bg-secondary);
    border: 1px solid rgba(100, 255, 218, 0.1);
    border-radius: var(--radius-lg);
    display: flex;
    flex-direction: column;
    gap: var(--spacing-md);
    transition: all var(--transition-base);
    height: 100%;
}

.small-project-card:hover {
    transform: translateY(-10px);
    border-color: var(--color-accent-primary);
    box-shadow: 0 10px 30px var(--color-accent-glow);
}

.small-project-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.small-project-header i:first-child {
    font-size: var(--font-size-3xl);
    color: var(--color-accent-primary);
}

.small-project-links {
    display: flex;
    gap: var(--spacing-md);
}

.small-project-links a {
    color: var(--color-text-secondary);
    font-size: var(--font-size-lg);
    transition: all var(--transition-base);
}

.small-project-links a:hover {
    color: var(--color-accent-primary);
}

.small-project-title {
    font-size: var(--font-size-lg);
    color: var(--color-text-primary);
    margin-bottom: var(--spacing-sm);
}

.small-project-description {
    color: var(--color-text-secondary);
    line-height: 1.6;
    flex: 1;
}

.small-project-tech {
    display: flex;
    flex-wrap: wrap;
    gap: var(--spacing-md);
    list-style: none;
    font-family: var(--font-mono);
    font-size: var(--font-size-xs);
    color: var(--color-text-tertiary);
}

.contact-section {
    padding: var(--spacing-4xl) 0;
}

.contact-content {
    max-width: 800px;
    margin: 0 auto;
    text-align: center;
}

.contact-overline {
    font-family: var(--font-mono);
    font-size: var(--font-size-base);
    color: var(--color-accent-primary);
    display: block;
    margin-bottom: var(--spacing-md);
}

.contact-title {
    font-family: var(--font-display);
    font-size: clamp(2.5rem, 5vw, 4rem);
    font-weight: 700;
    color: var(--color-text-primary);
    margin-bottom: var(--spacing-lg);
}

.contact-description {
    font-size: var(--font-size-lg);
    color: var(--color-text-secondary);
    line-height: 1.8;
    margin-bottom: var(--spacing-3xl);
}

.contact-methods {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: var(--spacing-xl);
    margin-bottom: var(--spacing-3xl);
}

.contact-card {
    padding: var(--spacing-xl);
    background: rgba(100, 255, 218, 0.05);
    border: 1px solid rgba(100, 255, 218, 0.1);
    border-radius: var(--radius-xl);
    text-decoration: none;
    transition: all var(--transition-base);
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: var(--spacing-md);
}

.contact-card:hover {
    transform: translateY(-10px);
    border-color: var(--color-accent-primary);
    box-shadow: 0 10px 30px var(--color-accent-glow);
}

.contact-icon {
    width: 60px;
    height: 60px;
    display: flex;
    justify-content: center;
    align-items: center;
    background: linear-gradient(135deg, var(--color-gradient-1), var(--color-gradient-3));
    border-radius: var(--radius-lg);
    font-size: var(--font-size-2xl);
    color: white;
}

.contact-card h3 {
    font-size: var(--font-size-lg);
    color: var(--color-text-primary);
}

.contact-card p {
    font-size: var(--font-size-sm);
    color: var(--color-text-secondary);
}

.footer {
    padding: var(--spacing-2xl) 0;
    background: var(--color-bg-secondary);
    border-top: 1px solid rgba(100, 255, 218, 0.1);
}

.footer-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: var(--spacing-lg);
}

.footer-content p {
    font-family: var(--font-mono);
    font-size: var(--font-size-sm);
    color: var(--color-text-secondary);
}

.footer-links {
    display: flex;
    gap: var(--spacing-xl);
}

.footer-links a {
    color: var(--color-text-secondary);
    font-size: var(--font-size-xl);
    transition: all var(--transition-base);
}

.footer-links a:hover {
    color: var(--color-accent-primary);
    transform: translateY(-3px);
}

[data-aos] {
    opacity: 0;
    transition: opacity 0.8s ease, transform 0.8s ease;
}

[data-aos].aos-animate {
    opacity: 1;
}

[data-aos="fade-up"].aos-animate {
    animation: fadeInUp 0.8s ease forwards;
}

[data-aos="fade-left"].aos-animate {
    animation: fadeInLeft 0.8s ease forwards;
}

[data-aos="fade-right"].aos-animate {
    animation: fadeInRight 0.8s ease forwards;
}

[data-aos="zoom-in"].aos-animate {
    animation: zoomIn 0.8s ease forwards;
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes fadeInLeft {
    from {
        opacity: 0;
        transform: translateX(-30px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

@keyframes fadeInRight {
    from {
        opacity: 0;
        transform: translateX(30px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

@keyframes zoomIn {
    from {
        opacity: 0;
        transform: scale(0.9);
    }
    to {
        opacity: 1;
        transform: scale(1);
    }
}

@media (max-width: 1024px) {
    :root {
        --container-padding: 1.5rem;
        --section-padding: 6rem 0;
    }

    .hero-social,
    .hero-email {
        display: none;
    }

    .about-content {
        grid-template-columns: 1fr;
        gap: var(--spacing-2xl);
    }

    .about-image {
        order: -1;
    }

    .experience-container {
        grid-template-columns: 1fr;
    }

    .experience-tabs {
        flex-direction: row;
        overflow-x: auto;
        gap: var(--spacing-md);
    }

    .tab-button {
        border-left: none;
        border-bottom: 2px solid var(--color-text-tertiary);
        padding: var(--spacing-md);
        white-space: nowrap;
    }

    .tab-button:hover,
    .tab-button.active {
        border-left: none;
        border-bottom-color: var(--color-accent-primary);
    }

    .tab-indicator {
        top: auto;
        bottom: 0;
        left: 0;
        width: 100px;
        height: 2px;
    }

    .project-card,
    .project-card.reverse {
        grid-template-columns: 1fr;
        direction: ltr;
    }

    .project-image,
    .project-card.reverse .project-image {
        grid-column: 1 / -1;
        height: 300px;
    }

    .project-content,
    .project-card.reverse .project-content {
        grid-column: 1 / -1;
        align-items: flex-start;
        text-align: left;
    }

    .project-description {
        background: transparent;
        padding: 0;
    }
}

@media (max-width: 768px) {
    :root {
        --container-padding: 1rem;
        --section-padding: 4rem 0;
    }

    .nav-menu {
        position: fixed;
        top: 80px;
        left: -100%;
        width: 100%;
        height: calc(100vh - 80px);
        background: rgba(10, 25, 47, 0.98);
        backdrop-filter: blur(10px);
        flex-direction: column;
        justify-content: center;
        padding: var(--spacing-2xl);
        transition: left var(--transition-base);
    }

    .nav-menu.active {
        left: 0;
    }

    .nav-link {
        font-size: var(--font-size-xl);
    }

    .hamburger {
        display: flex;
    }

    .hero {
        padding: 100px 0 var(--spacing-2xl);
    }

    .hero-title {
        font-size: clamp(2.5rem, 10vw, 4rem);
    }

    .hero-subtitle {
        font-size: clamp(1.5rem, 7vw, 2.5rem);
    }

    .hero-cta {
        flex-direction: column;
    }

    .btn {
        width: 100%;
        justify-content: center;
    }

    .about-stats {
        grid-template-columns: 1fr;
    }

    .skills-grid {
        grid-template-columns: 1fr;
    }

    .small-projects-grid {
        grid-template-columns: 1fr;
    }

    .contact-methods {
        grid-template-columns: 1fr;
    }
}

@media (max-width: 480px) {
    .section-title {
        font-size: var(--font-size-2xl);
    }

    .title-line {
        display: none;
    }

    .timeline::before {
        left: 8px;
    }

    .timeline-item {
        padding-left: var(--spacing-2xl);
    }

    .timeline-marker {
        width: 20px;
        height: 20px;
    }

    .timeline-marker::after {
        width: 8px;
        height: 8px;
    }
}
"""

# Write to file
with open('C:/Users/Bhuvan/Desktop/Portfolio/styles.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("? CSS file created successfully!")
print(f"File size: {len(css_content)} characters")
