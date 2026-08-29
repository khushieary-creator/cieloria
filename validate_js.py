import re

with open("app.js") as f:
    code = f.read()

# Check for unescaped template backticks or dollar signs inside template literals
lines = code.splitlines()

errors = []
for i, line in enumerate(lines, 1):
    # Check if there are raw backticks inside template literal lines that are not escaped
    if "${" in line:
        # verify template interpolation syntax
        count_open = line.count("${")
        count_close = line.count("}")
        if count_open > count_close:
            errors.append((i, line))

print("Total lines:", len(lines))
print("Potentially unmatched template interpolations:", len(errors))
for err in errors[:10]:
    print(f"Line {err[0]}: {err[1]}")
