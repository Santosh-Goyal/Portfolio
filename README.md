# ?? Shinobi Developer Portfolio

A stunning 3D portfolio website with a **Naruto anime** and **gaming theme**, featuring interactive animations, particle effects, and modern web technologies.

## ? Features

### ?? Gaming & Anime Aesthetics
- **Naruto-inspired color scheme** (Orange, Fire Red, Chakra Blue)
- **Sharingan loading animation** with spinning tomoe
- **Ninja-themed sections** (Jutsu Collection, Shinobi Skills)
- **Gaming glitch effects** and neon accents

### ?? 3D Interactive Elements
- **Three.js 3D background** with particle system
- **Mouse parallax effects** for immersive experience
- **Rotating geometric shapes** (stars, kunai, particles)
- **3D card tilt effect** on About section

### ? Animations & Effects
- **Typing animation** with multiple rotating phrases
- **Fire particle effects** on buttons
- **Cursor trail particles** following mouse movement
- **Smooth scroll animations** with Intersection Observer
- **Skill bar animations** with shimmer effects
- **Counter animations** for statistics

### ?? Responsive Design
- **Mobile-friendly** hamburger navigation
- **Adaptive layouts** for all screen sizes
- **Optimized performance** with lazy loading

### ?? Easter Eggs
- **Konami Code** (????????BA) triggers secret jutsu animation
- **Console messages** with fun developer notes

## ?? Getting Started

### Prerequisites
- A modern web browser (Chrome, Firefox, Safari, Edge)
- No build tools required - pure HTML, CSS, and JavaScript

### Installation

1. **Download the files** to your Portfolio folder:
   - `index.html`
   - `styles.css`
   - `script.js`

2. **Open `index.html`** in your web browser

That's it! No dependencies to install.

## ?? Customization Guide

### 1. Personal Information

**Update in `index.html`:**

```html
<!-- Line 51: Change your name -->
<h1 class="glitch" data-text="YOUR NAME">YOUR NAME</h1>

<!-- Lines 371-385: Update contact methods -->
<a href="mailto:your.email@example.com">your.email@example.com</a>
<a href="https://linkedin.com/in/yourprofile">linkedin.com/in/yourprofile</a>
<a href="https://github.com/yourusername">github.com/yourusername</a>
```

### 2. Profile Picture

Replace the placeholder avatar:
```html
<!-- Line 125: Add your profile image -->
<div class="profile-placeholder">
    <img src="your-photo.jpg" alt="Profile" style="width:100%; border-radius:50%;">
</div>
```

### 3. Skills Section

**Modify skill levels** (Lines 144-225 in `index.html`):
```html
<div class="skill-item" data-skill="95">
    <span class="skill-name">?? Your Skill</span>
    <span class="skill-level">95%</span>
</div>
```

### 4. Projects

**Add your projects** (Lines 232-365 in `index.html`):
```html
<div class="project-card">
    <div class="project-title">Your Project Name</div>
    <p class="project-description">Project description...</p>
    <div class="project-tech">
        <span class="tech-tag">React</span>
        <span class="tech-tag">Node.js</span>
    </div>
</div>
```

### 5. Colors

**Change theme colors** in `styles.css` (Lines 9-30):
```css
:root {
    --primary-orange: #ff6b1a;    /* Main theme color */
    --fire-red: #ff3d00;          /* Accent color */
    --chakra-blue: #00d4ff;       /* Secondary accent */
    --neon-cyan: #00fff9;         /* Gaming accent */
}
```

### 6. Typing Animation

**Update typing phrases** in `script.js` (Lines 21-26):
```javascript
const typingTexts = [
    "Your custom phrase 1",
    "Your custom phrase 2",
    "Your custom phrase 3"
];
```

### 7. Statistics

**Update counter numbers** (Lines 110-130 in `index.html`):
```html
<div class="stat-number" data-target="50">0</div>
```

## ?? Project Structure

```
Portfolio/
??? index.html          # Main HTML structure
??? styles.css          # All styling and animations
??? script.js           # JavaScript functionality
??? README.md          # This file
```

## ?? Sections Overview

1. **Hero Section** - Dynamic introduction with glitch effects
2. **About Section** - Personal info with 3D card and statistics
3. **Skills Section** - Animated skill bars in three categories
4. **Projects Section** - Portfolio showcase with hover effects
5. **Contact Section** - Form and contact methods
6. **Footer** - Social links and ninja quote

## ?? Technologies Used

- **HTML5** - Semantic structure
- **CSS3** - Advanced animations and effects
- **JavaScript (ES6)** - Interactive functionality
- **Three.js** - 3D graphics and particle systems
- **Intersection Observer API** - Scroll animations
- **CSS Grid & Flexbox** - Responsive layouts

## ? Performance Tips

1. **Optimize images**: Compress images before adding them
2. **Lazy loading**: Images load only when visible
3. **Throttled scroll events**: Prevents performance issues
4. **Hardware acceleration**: Uses CSS transforms for smooth animations

## ?? Color Palette

| Color | Hex Code | Usage |
|-------|----------|-------|
| Primary Orange | `#ff6b1a` | Main theme, buttons, highlights |
| Fire Red | `#ff3d00` | Accents, gradients |
| Chakra Blue | `#00d4ff` | Secondary accents |
| Neon Cyan | `#00fff9` | Gaming elements |
| Neon Pink | `#ff00ff` | Special effects |
| Dark Navy | `#0a1628` | Background |

## ?? Browser Compatibility

- ? Chrome 90+
- ? Firefox 88+
- ? Safari 14+
- ? Edge 90+

## ?? To-Do List (Future Enhancements)

- [ ] Add project images/screenshots
- [ ] Implement backend for contact form
- [ ] Add blog section
- [ ] Create project detail pages
- [ ] Add theme switcher (light/dark mode)
- [ ] Integrate with GitHub API for live repo stats
- [ ] Add more anime-themed animations

## ?? Learning Resources

This portfolio uses modern web technologies. Learn more:
- [Three.js Documentation](https://threejs.org/docs/)
- [CSS Animations](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Animations)
- [Intersection Observer API](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API)

## ?? License

Free to use for personal and commercial projects. Attribution appreciated but not required.

## ?? Credits

- **Design & Development**: Bhuvan
- **Inspiration**: Naruto anime series, gaming aesthetics
- **3D Graphics**: Three.js library

## ?? Support

Found a bug or have a suggestion? Feel free to reach out!

---

**"I never go back on my word, that's my ninja way!"** - Naruto Uzumaki ??

Built with ??, ?, and lots of chakra!
