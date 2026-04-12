"""
Standardize publication images to a uniform 640x320 transparent canvas
with 16px rounded corners baked in.

Usage:
    source Code/env/mila/bin/activate
    python3 scripts/standardize_pub_images.py
"""

from PIL import Image, ImageDraw
import os

CANVAS_W, CANVAS_H = 640, 320
RADIUS = 16

IMG_DIR = os.path.join(os.path.dirname(__file__), '..', 'images', 'publications')
IMG_DIR = os.path.abspath(IMG_DIR)


def make_rounded_mask(w, h, radius):
    mask = Image.new('L', (w, h), 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([0, 0, w, h], radius=radius, fill=255)
    return mask


def standardize(path):
    img = Image.open(path).convert('RGBA')

    # Skip if already the correct size
    if img.size == (CANVAS_W, CANVAS_H):
        return None

    original_size = img.size

    scale = min(CANVAS_W / img.width, CANVAS_H / img.height)
    new_w = int(img.width * scale)
    new_h = int(img.height * scale)
    img_resized = img.resize((new_w, new_h), Image.LANCZOS)

    # Apply rounded corners
    mask = make_rounded_mask(new_w, new_h, RADIUS)
    r, g, b, a = img_resized.split()
    a = Image.composite(a, Image.new('L', (new_w, new_h), 0), mask)
    img_rounded = Image.merge('RGBA', (r, g, b, a))

    canvas = Image.new('RGBA', (CANVAS_W, CANVAS_H), (0, 0, 0, 0))
    x = (CANVAS_W - new_w) // 2
    y = (CANVAS_H - new_h) // 2
    canvas.paste(img_rounded, (x, y), img_rounded)
    canvas.save(path)

    return original_size


def main():
    files = sorted(f for f in os.listdir(IMG_DIR) if f.endswith('.png'))
    if not files:
        print('No .png files found.')
        return

    processed = 0
    for fname in files:
        path = os.path.join(IMG_DIR, fname)
        result = standardize(path)
        if result:
            print(f'  {fname}: {result[0]}x{result[1]} -> {CANVAS_W}x{CANVAS_H}')
            processed += 1
        else:
            print(f'  {fname}: already {CANVAS_W}x{CANVAS_H}, skipped')

    print(f'\nDone. {processed}/{len(files)} images processed.')


if __name__ == '__main__':
    main()
