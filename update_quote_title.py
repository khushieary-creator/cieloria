import os

with open('cieloria_app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace FROM SHRADDHA, FOR YOU with FOR YOU
js = js.replace('FROM SHRADDHA, FOR YOU', 'FOR YOU')
js = js.replace('<!-- 7. FROM SHRADDHA, FOR YOU Quote -->', '<!-- 7. FOR YOU Quote -->')

with open('cieloria_app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print('Successfully updated section title to "FOR YOU" in cieloria_app.js!')
