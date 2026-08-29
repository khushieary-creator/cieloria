import re

with open("app.js") as f:
    code = f.read()

print("File length:", len(code))

# Check template string variable references
matches = re.findall(r'\${([^}]+)}', code)
print(f"Found {len(matches)} interpolation placeholders")

# Check for undefined variables in app.js
vars_in_code = set(re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', code))
print("Sample identifier check complete.")
