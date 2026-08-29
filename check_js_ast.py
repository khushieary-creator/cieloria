import re
import sys

with open("app.js") as f:
    code = f.read()

backtick_positions = [m.start() for m in re.finditer(r'`', code)]
print(f"Total backticks in app.js: {len(backtick_positions)}")

if len(backtick_positions) % 2 != 0:
    print("CRITICAL SYNTAX ERROR: Odd number of backticks in app.js! This causes Unterminated Template Literal error!")
else:
    print("Backticks count is even.")
