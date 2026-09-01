import os, re

with open('cieloria_app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Update PLP_CATEGORY_DATA for Earrings
old_earrings_data = r'Earrings: \{\s*title: "Earrings",\s*heading: "All Earrings",\s*tagline: "Statement for every occasion",\s*bannerImage: ".*?",'

new_earrings_data = """Earrings: {
    title: "Earrings",
    heading: "All Earrings",
    tagline: "Elegantly styled on her ear • 100% Anti-Tarnish & Hypoallergenic",
    bannerImage: "/hero_earrings.jpg","""

js = re.sub(old_earrings_data, new_earrings_data, js, flags=re.DOTALL)

with open('cieloria_app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print('Successfully updated Earrings category PLP hero banner image to /hero_earrings.jpg!')
