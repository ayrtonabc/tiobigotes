#!/usr/bin/env python3
"""
Script to clean up sucursales.html by removing HTTrack comments and broken external CSS links
"""

import re
import os

def clean_sucursales_html():
    """Clean up sucursales.html file"""
    file_path = 'sucursales.html'
    
    if not os.path.exists(file_path):
        print(f"File {file_path} not found!")
        return
    
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Remove HTTrack comments
    print("Removing HTTrack comments...")
    content = re.sub(r'<!-- Mirrored from [^>]* -->', '', content)
    content = re.sub(r'<!-- Added by HTTrack -->', '', content)
    content = re.sub(r'<!-- /Added by HTTrack -->', '', content)
    
    # Remove broken external CSS links that point to ../wp-content/plugins/
    print("Removing broken external CSS links...")
    
    # List of CSS IDs to remove
    css_ids_to_remove = [
        'wpml-blocks-css',
        'contact-form-7-css',
        'cookie-law-info-css',
        'cookie-law-info-gdpr-css',
        'dipi-popup-maker-popup-effect-css',
        'dipi_font-css',
        'dipi_general-css',
        'maps-extended-css-css',
        'uaf_client_css-css',
        'wpcf7-redirect-script-frontend-css',
        'wpml-menu-item-0-css'
    ]
    
    removed_links = 0
    for css_id in css_ids_to_remove:
        # Pattern to match the entire link tag with this ID
        pattern = rf"<link[^>]*id='{css_id}'[^>]*/?>"
        matches = re.findall(pattern, content)
        if matches:
            content = re.sub(pattern, '', content)
            removed_links += len(matches)
            print(f"  Removed {len(matches)} link(s) with ID '{css_id}'")
    
    # Clean up any extra whitespace or empty lines left behind
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
    
    # Write the cleaned content back to the file
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"\nSuccessfully cleaned {file_path}:")
        print(f"  - Removed HTTrack comments")
        print(f"  - Removed {removed_links} broken CSS links")
    else:
        print(f"No changes needed in {file_path}")

if __name__ == "__main__":
    clean_sucursales_html()