#!/usr/bin/env python3
"""
Script to fix the "Jestem Programista" footer link positioning and visibility issues.
The link is currently overlapped and not properly visible. This script will:
1. Simplify the complex inline CSS
2. Make the link centered and properly visible
3. Maintain the yellow hover effect
4. Apply changes to all HTML files
"""

import re
import os

def fix_footer_link(file_path):
    """Fix the Jestem Programista footer link in a single HTML file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to match the Jestem Programista link with its complex inline styles
        pattern = r'<a\s+href="https://jestemprogramista\.pl"\s+[^>]*>Jestem Programista</a>'
        
        # Find the current link
        match = re.search(pattern, content, re.IGNORECASE | re.DOTALL)
        if match:
            # Create a simplified, centered version of the link
            new_link = '''<a href="https://jestemprogramista.pl" target="_blank" style="display: block; text-align: center; margin: 10px auto; padding: 8px; background-color: rgba(255, 255, 255, 0.1); border-radius: 4px; transition: all 0.3s ease; position: relative; z-index: 10;" onmouseover="this.style.color='#FFD700'; this.style.backgroundColor='rgba(255, 255, 255, 0.2)';" onmouseout="this.style.color='#ffffff'; this.style.backgroundColor='rgba(255, 255, 255, 0.1)';">Jestem Programista</a>'''
            
            # Replace the old link with the new one
            content = content.replace(match.group(0), new_link)
            
            # Write the updated content back to the file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✓ Fixed footer link in {os.path.basename(file_path)}")
            return True
        else:
            print(f"⚠ No Jestem Programista link found in {os.path.basename(file_path)}")
            return False
            
    except Exception as e:
        print(f"✗ Error processing {file_path}: {str(e)}")
        return False

def main():
    """Main function to fix footer links in all HTML files."""
    html_files = [
        'index.html',
        'carta.html', 
        'contacto.html',
        'eventos.html',
        'pedidos.html',
        'cookies-policy.html',
        'sucursales.html'
    ]
    
    print("🔧 Fixing Jestem Programista footer link positioning and visibility...")
    print("=" * 60)
    
    fixed_count = 0
    for html_file in html_files:
        if os.path.exists(html_file):
            if fix_footer_link(html_file):
                fixed_count += 1
        else:
            print(f"⚠ File not found: {html_file}")
    
    print("=" * 60)
    print(f"✅ Fixed footer link in {fixed_count} files")
    print("The Jestem Programista link should now be:")
    print("- Properly centered in the footer")
    print("- Clearly visible (not overlapped)")
    print("- Have a yellow hover effect")
    print("- Have proper spacing and positioning")

if __name__ == "__main__":
    main()