"""
Standardize publication images to a uniform 800x450 transparent canvas.

Usage:
    source Code/env/mila/bin/activate
    python3 scripts/standardize_pub_images.py
"""

from PIL import Image
import os

CANVAS_W, CANVAS_H = 800, 450
PADDING = 20

IMG_DIR = os.path.join(os.path.dirname(__file__), '..', 'images', 'publications')
IMG_DIR = os.path.abspath(IMG_DIR)


def standardize(path):
    img = Image.open(path).convert('RGBA')

    # Skip if already the correct size
    if img.size == (CANVAS_W, CANVAS_H):
        return None

    original_size = img.size

    avail_w = CANVAS_W - 2 * PADDING
    avail_h = CANVAS_H - 2 * PADDING

    scale = min(avail_w / img.width, avail_h / img.height)
    new_w = int(img.width * scale)
    new_h = int(img.height * scale)
    img_resized = img.resize((new_w, new_h), Image.LANCZOS)

    canvas = Image.new('RGBA', (CANVAS_W, CANVAS_H), (0, 0, 0, 0))
    x = (CANVAS_W - new_w) // 2
    y = (CANVAS_H - new_h) // 2
    canvas.paste(img_resized, (x, y), img_resized)
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
