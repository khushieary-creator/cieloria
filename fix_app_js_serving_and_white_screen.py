import os, shutil

# 1. Read full JS from cieloria_app.js and clean_app.py output
with open('app.js', 'r', encoding='utf-8') as f:
    js_code = f.read()

# Make sure app.js exists in root, public/, and dist/
with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js_code)

os.makedirs('public', exist_ok=True)
with open('public/app.js', 'w', encoding='utf-8') as f:
    f.write(js_code)

os.makedirs('dist', exist_ok=True)
with open('dist/app.js', 'w', encoding='utf-8') as f:
    f.write(js_code)

print('Successfully ensured app.js exists in root, public/, and dist/!')
