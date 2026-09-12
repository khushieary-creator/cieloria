import os, shutil

# Paths to uploaded images
img1_src = '/Users/khushi/.gemini/antigravity/brain/6eec9aed-fb87-45bd-a237-54b066bc82a1/.user_uploaded/media_1789238113223.jpg'
img2_src = '/Users/khushi/.gemini/antigravity/brain/6eec9aed-fb87-45bd-a237-54b066bc82a1/.user_uploaded/media_1789238113332.png'
img3_src = '/Users/khushi/.gemini/antigravity/brain/6eec9aed-fb87-45bd-a237-54b066bc82a1/.user_uploaded/media_1789238113368.jpg'

dirs_to_copy = ['.', 'public', 'dist']

for d in dirs_to_copy:
    os.makedirs(d, exist_ok=True)
    shutil.copy(img1_src, os.path.join(d, 'blog_1.jpg'))
    shutil.copy(img2_src, os.path.join(d, 'blog_2.jpg'))
    shutil.copy(img3_src, os.path.join(d, 'blog_3.jpg'))

print('Successfully copied all 3 blog images to root, public, and dist!')

# Now update BLOG_POSTS in cieloria_app.js to use /blog_1.jpg, /blog_2.jpg, /blog_3.jpg
with open('cieloria_app.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace('image: "/cieloria_hero_rings.jpg"', 'image: "/blog_1.jpg"')
js = js.replace('image: "/cieloria_hero_necklaces.jpg"', 'image: "/blog_2.jpg"')
js = js.replace('image: "/cieloria_hero_bracelets.jpg"', 'image: "/blog_3.jpg"')

with open('cieloria_app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print('Successfully updated cieloria_app.js to use new model images for all 3 blog posts!')
