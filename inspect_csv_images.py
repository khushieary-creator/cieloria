import csv

with open("parse_full_csv.py") as f:
    text = f.read()

start_idx = text.find("csv_raw = \"\"\"") + len("csv_raw = \"\"\"")
end_idx = text.rfind("\"\"\"")
csv_data = text[start_idx:end_idx]

lines = csv_data.splitlines()
reader = csv.reader(lines)
header = next(reader)

product_images_map = {}

for row in reader:
    if not row or len(row) < 33: continue
    handle = row[0].strip()
    title = row[1].strip()
    
    if not handle or not title or "http" in handle or "<p" in handle or "<ul" in handle:
        continue
    if not handle[0].isalnum():
        continue
        
    imgs = [cell.strip() for cell in row if "https://cdn.shopify.com" in cell]
    if handle not in product_images_map:
        product_images_map[handle] = {
            "title": title,
            "images": []
        }
    for img in imgs:
        if img not in product_images_map[handle]["images"]:
            product_images_map[handle]["images"].append(img)

print(f"Total unique product handles found: {len(product_images_map)}")
multi_img_count = sum(1 for h, p in product_images_map.items() if len(p["images"]) > 1)
print(f"Products with multiple images in CSV: {multi_img_count}")

# Print first 5 products and their exact images
for h, p in list(product_images_map.items())[:5]:
    print(f"\nProduct: {p['title']}")
    print(f"Images count: {len(p['images'])}")
    for img in p['images']:
        print(" -", img)
