import os

with open('cieloria_app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Extract lines 24 to 88 (0-indexed: lines 23 to 88)
mangalsutra_lines = lines[23:88]
rest_lines = lines[:23] + lines[88:]

# Find where PRODUCTS array ends (before const CUSTOMER_REVIEWS)
for idx, line in enumerate(rest_lines):
    if 'const CUSTOMER_REVIEWS =' in line:
        break

# Insert mangalsutra_lines right before const CUSTOMER_REVIEWS (and fix comma)
# Remove closing bracket of previous item if needed
rest_lines[idx - 2] = rest_lines[idx - 2].rstrip() + ',\n'
final_lines = rest_lines[:idx - 1] + mangalsutra_lines + rest_lines[idx - 1:]

with open('cieloria_app.js', 'w', encoding='utf-8') as f:
    f.writelines(final_lines)

print('Successfully moved Mangalsutra products to end of PRODUCTS array!')
