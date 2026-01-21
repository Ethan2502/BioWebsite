from PIL import Image
import sys

try:
    img_path = sys.argv[1]
    img = Image.open(img_path)
    img = img.convert('RGB')
    width, height = img.size
    
    # The image appears to be vertical stripes of color.
    # We'll sample horizontally across the middle.
    y = height // 2
    colors = []
    
    # Scan across the width to find distinct colors
    # We'll just take a sample every 50 pixels or so, depending on width
    step = max(1, width // 20)
    for x in range(0, width, step):
        r, g, b = img.getpixel((x, y))
        hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        colors.append(hex_color)
    
    # Simple deduplication (consecutive) to find the main blocks
    unique_colors = []
    if colors:
        unique_colors.append(colors[0])
        for c in colors[1:]:
            if c != unique_colors[-1]:
                unique_colors.append(c)
    
    # Filter out very similar colors (optional, but good for noise) - ignoring for now as palette images are usually clean
    
    print("EXTRACTED_COLORS:", unique_colors)

except Exception as e:
    print(f"Error: {e}")
