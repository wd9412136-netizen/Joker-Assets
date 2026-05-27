#!/usr/bin/env python3
"""
Script to generate PNG icons from SVG
Requirements: pip install cairosvg pillow
"""

import os
from pathlib import Path
try:
    import cairosvg
except ImportError:
    print("❌ Please install cairosvg: pip install cairosvg")
    exit(1)

try:
    from PIL import Image
except ImportError:
    print("❌ Please install Pillow: pip install pillow")
    exit(1)

# Icon sizes to generate
ICON_SIZES = {
    'joker-icon-16': 16,
    'joker-icon-32': 32,
    'joker-icon-96': 96,
    'joker-icon-192': 192,
    'joker-icon-512': 512,
    'apple-touch-icon': 180,
}

MASKABLE_SIZES = {
    'joker-icon-192-maskable': 192,
    'joker-icon-512-maskable': 512,
}

def create_icons():
    """Generate all icon sizes from SVG"""
    
    svg_file = 'joker-icon.svg'
    
    if not os.path.exists(svg_file):
        print(f"❌ SVG file not found: {svg_file}")
        return False
    
    print("🎨 Starting icon generation...\n")
    
    # Create basic icons
    for name, size in ICON_SIZES.items():
        output_file = f"{name}.png"
        try:
            cairosvg.svg2png(
                url=svg_file,
                write_to=output_file,
                output_width=size,
                output_height=size
            )
            print(f"✅ Created {output_file} ({size}x{size})")
        except Exception as e:
            print(f"❌ Error creating {output_file}: {e}")
            return False
    
    # Create maskable icons (with padding)
    padding_ratio = 0.1  # 10% padding
    
    for name, size in MASKABLE_SIZES.items():
        temp_file = f"{name}_temp.png"
        output_file = f"{name}.png"
        
        try:
            # Create SVG with padding
            with open(svg_file, 'r', encoding='utf-8') as f:
                svg_content = f.read()
            
            # Scale down to 80% and center
            padded_svg = svg_content.replace(
                'viewBox="0 0 200 200"',
                'viewBox="0 0 250 250"'
            )
            
            padded_svg_file = f"{name}_padded.svg"
            with open(padded_svg_file, 'w', encoding='utf-8') as f:
                f.write(f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 250 250">
  <rect width="250" height="250" fill="none"/>
  <g transform="translate(25, 25) scale(0.8)">
    {svg_content.split('<svg')[1].split('>')[1].split('</svg>')[0]}
  </g>
</svg>
''')
            
            cairosvg.svg2png(
                url=padded_svg_file,
                write_to=output_file,
                output_width=size,
                output_height=size
            )
            print(f"✅ Created {output_file} ({size}x{size}) - Maskable")
            
            # Clean up temp file
            os.remove(padded_svg_file)
            
        except Exception as e:
            print(f"❌ Error creating {output_file}: {e}")
            return False
    
    # Create favicon.ico
    try:
        img = Image.open('joker-icon-32.png')
        img.save('favicon.ico')
        print(f"✅ Created favicon.ico")
    except Exception as e:
        print(f"❌ Error creating favicon.ico: {e}")
    
    print("\n🎉 All icons generated successfully!")
    print("\n📋 Next steps:")
    print("1. Move all PNG files to your project root")
    print("2. Update index.html with the icon references")
    print("3. Test the app on your device")
    
    return True

if __name__ == '__main__':
    create_icons()
