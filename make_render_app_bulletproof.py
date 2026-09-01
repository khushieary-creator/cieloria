import os, re

with open('cieloria_app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Update renderHomepageView parameter safety
old_hp = 'function renderHomepageView(currentHero) {'
new_hp = """function renderHomepageView(heroParam) {
  const currentHero = heroParam || (HERO_SLIDES && HERO_SLIDES[0]) || {
    image: "/hero_banner.jpg",
    tag: "FESTIVE SALE ✦ FLAT 50% OFF",
    title: "EVERYDAY LUXURY DEMIFINE® JEWELRY",
    subtitle: "100% Anti-Tarnish & Waterproof 18K Gold Plated Collection"
  };"""

js = js.replace(old_hp, new_hp)

# 2. Update renderApp safety guards
old_ra = 'function renderApp() {\n  if (typeof document === \'undefined\') return;\n  const appContainer = document.getElementById(\'app\');\n  if (!appContainer) return;'
new_ra = """function renderApp() {
  if (typeof document === 'undefined') return;
  const appContainer = document.getElementById('app');
  if (!appContainer) return;

  if (!state || typeof state !== 'object') state = {};
  if (typeof state.heroSlideIndex !== 'number' || isNaN(state.heroSlideIndex) || state.heroSlideIndex < 0 || state.heroSlideIndex >= HERO_SLIDES.length) state.heroSlideIndex = 0;
  if (typeof state.tickerIndex !== 'number' || isNaN(state.tickerIndex) || state.tickerIndex < 0 || state.tickerIndex >= ANNOUNCEMENTS.length) state.tickerIndex = 0;
  if (typeof state.searchPlaceholderIndex !== 'number' || isNaN(state.searchPlaceholderIndex) || state.searchPlaceholderIndex < 0 || state.searchPlaceholderIndex >= SEARCH_PLACEHOLDERS.length) state.searchPlaceholderIndex = 0;
  if (typeof state.searchQuery !== 'string') state.searchQuery = '';
  if (!Array.isArray(state.wishlist)) state.wishlist = [];
  if (!Array.isArray(state.cart)) state.cart = [];"""

js = js.replace(old_ra, new_ra)

with open('cieloria_app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print('Successfully added bulletproof safety guards to cieloria_app.js!')
