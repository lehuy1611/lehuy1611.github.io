# Publication Images

## Standard Format

All publication images are standardized to:

- **Size:** 800 x 450 px (16:9)
- **Format:** PNG with transparent background (RGBA)
- **Layout:** Original image scaled to fit with 20px padding, centered on the canvas

## Adding a New Image

1. Place the original image in this folder as a `.png` file
2. Name it `<short_name>_<year>.png` (e.g., `bima_2024.png`)
3. Run the standardization script:

```bash
source Code/env/mila/bin/activate
python3 scripts/standardize_pub_images.py
```

The script will process **all** `.png` files in this folder, resizing and centering them onto an 800x450 transparent canvas.

## Rules

- Always run the script after adding or replacing an image
- Use `.png` format only (the script converts to RGBA for transparency)
- Do not manually resize images to 800x450 -- let the script handle it to ensure consistent padding and centering
- Avoid images with baked-in white backgrounds when possible; transparent or clean backgrounds work best in both light and dark mode
