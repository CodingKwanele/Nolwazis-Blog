// Nolwazi Blog - Enhanced Interactive JS

// ── Theme ────────────────────────────────────────────────────
const html = document.documentElement;

function applyTheme(theme) {
  html.className = theme === 'dark' ? 'dark-theme' : 'light-theme';
  const icon = document.querySelector('#theme-toggle i');
  if (icon) {
    icon.className = theme === 'dark' ? 'bi bi-sun-fill' : 'bi bi-moon-stars-fill';
  }
  // Persist glassmorphism
  document.documentElement.style.setProperty('--glass-bg', theme === 'dark' ? 'rgba(26, 26, 26, 0.7)' : 'rgba(255, 255, 255, 0.25)');
}

function initTheme() {
  const saved = localStorage.getItem('theme');
  const preferred = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  applyTheme(saved || preferred);
}

function toggleTheme() {
  const isDark = html.classList.contains('dark-theme');
  const next = isDark ? 'light' : 'dark';
  localStorage.setItem('theme', next);
  applyTheme(next);
}

// ── HTMX Enhancements ───────────────────────────────────────
document.addEventListener('DOMContentLoaded', function () {
  // Theme toggle
  const themeToggle = document.getElementById('theme-toggle');
  if (themeToggle) themeToggle.addEventListener('click', toggleTheme);

  // Form enhancements
  document.querySelectorAll('input[type=text], input[type=password], input[type=search]').forEach(el => {
    if (!el.classList.contains('form-control')) el.classList.add('form-control');
  });

  // Smooth scrolling
  document.querySelectorAll('a[href^=\"#\"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  // Ingredient checkboxes
  document.querySelectorAll('.form-check-input').forEach(cb => {
    cb.addEventListener('change', function () {
      const label = this.nextElementSibling;
      if (label) label.style.textDecoration = this.checked ? 'line-through' : 'none';
    });
  });

  // Search debounce
  const searchInput = document.querySelector('.search-form input[type=\"search\"]');
  if (searchInput) {
    let debounceTimer;
    searchInput.addEventListener('input', function() {
      clearTimeout(debounceTimer);
      debounceTimer = setTimeout(() => {
        if (this.form) this.form.requestSubmit();
      }, 300);
    });
  }
});

// HTMX Events - Eye-Catching Loaders & Animations
document.body.addEventListener('htmx:beforeRequest', function(evt) {
  const target = document.querySelector(evt.target.getAttribute('hx-target') || evt.target);
  if (target) {
    target.classList.add('htmx-request');
    showSkeleton(target);
  }
});

document.body.addEventListener('htmx:afterRequest', function(evt) {
  const target = document.querySelector(evt.target.getAttribute('hx-target') || evt.target);
  if (target) {
    target.classList.remove('htmx-request');
    hideSkeleton(target);
    staggerAnimateCards(target);
  }
});

function showSkeleton(container) {
  if (container.querySelector('.skeleton')) return;
  container.innerHTML = Array(8).fill().map(() => `
    <div class="col-xl-3 col-lg-4 col-md-6 mb-4">
      <div class="skeleton skeleton-card glass"></div>
    </div>
  `).join('');
}

function hideSkeleton(container) {
  container.querySelectorAll('.skeleton').forEach(s => s.remove());
}

function staggerAnimateCards(container) {
  const cards = container.querySelectorAll('.recipe-card');
  cards.forEach((card, index) => {
    card.style.animationDelay = `${index * 0.1}s`;
    card.style.opacity = '0';
    card.style.animation = 'none';
    card.offsetHeight; // Trigger reflow
    card.style.animation = 'fadeInUpStagger .6s cubic-bezier(0.4, 0, 0.2, 1) forwards';
  });
}

// IntersectionObserver for scroll-triggered animations
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.style.opacity = '1';
      entry.target.style.transform = 'translateY(0)';
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('.fade-in-up, .recipe-card').forEach(el => observer.observe(el));

// Re-apply theme & observers after swaps
document.body.addEventListener('htmx:afterSwap', function() {
  initTheme();
  document.querySelectorAll('.fade-in-up, .recipe-card').forEach(el => observer.observe(el));
});

// Print recipe handler
document.addEventListener('click', function(e) {
  if (e.target.closest('[onclick=\"window.print()\"]')) {
    setTimeout(() => {
      window.print();
    }, 100);
  }
});

