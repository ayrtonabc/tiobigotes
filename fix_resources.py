#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import glob

def replace_fuego_yamana_footer(file_path):
    """
    Reemplaza los enlaces de Fuego Yamana en el footer con Jestem Programista
    """
    try:
        # Leer el archivo
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        # Si falla UTF-8, intentar con latin-1
        with open(file_path, 'r', encoding='latin-1') as f:
            content = f.read()
    
    # Patrón para encontrar el enlace completo de Fuego Yamana
    pattern = r'<a href="https://www\.fuegoyamana\.com/" target="_blank"><span class="et_pb_image_wrap "><img loading="lazy" decoding="async" width="298" height="42" src="wp-content/uploads/2021/08/FuegoYamana-1\.svg" alt="Fuego Yamana" title="Fuego Yamana" class="wp-image-163" /></span></a>'
    
    # Nuevo enlace con estilo hover amarillo
    replacement = '''<a href="https://jestemprogramista.pl" target="_blank" style="color: #333; text-decoration: none; font-weight: bold; transition: color 0.3s ease;" onmouseover="this.style.color='#FFD700'" onmouseout="this.style.color='#333'">Jestem Programista</a>'''
    
    # Contar reemplazos
    matches = len(re.findall(pattern, content))
    
    if matches > 0:
        # Realizar el reemplazo
        new_content = re.sub(pattern, replacement, content)
        
        # Escribir el archivo modificado
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✓ {file_path}: {matches} enlace(s) de Fuego Yamana reemplazado(s)")
        return matches
    else:
        print(f"- {file_path}: No se encontraron enlaces de Fuego Yamana")
        return 0

def main_footer():
    """
    Función principal que procesa todos los archivos HTML para reemplazar footer
    """
    html_files = glob.glob("*.html")
    total_replacements = 0
    
    print("Reemplazando enlaces de Fuego Yamana en el footer...")
    print("=" * 50)
    
    for html_file in html_files:
        replacements = replace_fuego_yamana_footer(html_file)
        total_replacements += replacements
    
    print("=" * 50)
    print(f"Total de enlaces reemplazados: {total_replacements}")
    print("¡Proceso completado!")

# Ejecutar la función de reemplazo del footer
main_footer()

def improve_footer_css(file_path):
    """
    Mejora el CSS del enlace Jestem Programista en el footer para mejor visibilidad
    """
    try:
        # Leer el archivo
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        # Si falla UTF-8, intentar con latin-1
        with open(file_path, 'r', encoding='latin-1') as f:
            content = f.read()
    
    # Patrón para encontrar el enlace actual de Jestem Programista
    pattern = r'<a href="https://jestemprogramista\.pl" target="_blank" style="color: #333; text-decoration: none; font-weight: bold; transition: color 0\.3s ease;" onmouseover="this\.style\.color=\'#FFD700\'" onmouseout="this\.style\.color=\'#333\'">Jestem Programista</a>'
    
    # Nuevo enlace con CSS mejorado para mejor visibilidad y posicionamiento
    replacement = '''<a href="https://jestemprogramista.pl" target="_blank" style="display: inline-block; color: #333; text-decoration: none; font-weight: bold; font-size: 14px; padding: 8px 12px; margin: 10px 0; background-color: rgba(255, 255, 255, 0.9); border-radius: 4px; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); transition: all 0.3s ease; z-index: 10; position: relative; border: 1px solid #ddd;" onmouseover="this.style.color='#FFD700'; this.style.backgroundColor='rgba(255, 255, 255, 1)'; this.style.boxShadow='0 4px 8px rgba(0, 0, 0, 0.2)'; this.style.transform='translateY(-1px)';" onmouseout="this.style.color='#333'; this.style.backgroundColor='rgba(255, 255, 255, 0.9)'; this.style.boxShadow='0 2px 4px rgba(0, 0, 0, 0.1)'; this.style.transform='translateY(0)';">Jestem Programista</a>'''
    
    # Contar reemplazos
    matches = len(re.findall(pattern, content))
    
    if matches > 0:
        # Realizar el reemplazo
        new_content = re.sub(pattern, replacement, content)
        
        # Escribir el archivo modificado
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✓ {file_path}: {matches} enlace(s) de Jestem Programista mejorado(s)")
        return matches
    else:
        print(f"- {file_path}: No se encontraron enlaces de Jestem Programista para mejorar")
        return 0

def improve_footer_css_enhanced(file_path):
    """Enhanced function to improve CSS for Jestem Programista link with better visibility"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Pattern to find the current Jestem Programista link
        pattern = r'<a href="https://jestemprogramista\.pl"[^>]*>Jestem Programista</a>'
        
        # New enhanced link with better CSS for visibility
        new_link = '''<a href="https://jestemprogramista.pl" target="_blank" style="display: inline-block !important; color: #2c3e50 !important; text-decoration: none !important; font-weight: bold !important; font-size: 16px !important; padding: 12px 20px !important; margin: 15px 5px !important; background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%) !important; border-radius: 8px !important; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15) !important; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important; z-index: 1000 !important; position: relative !important; border: 2px solid #e9ecef !important; font-family: 'Arial', sans-serif !important; letter-spacing: 0.5px !important; text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1) !important; min-width: 160px !important; text-align: center !important; cursor: pointer !important;" onmouseover="this.style.color='#FFD700'; this.style.background='linear-gradient(135deg, #ffffff 0%, #fffbf0 100%)'; this.style.boxShadow='0 6px 20px rgba(255, 215, 0, 0.3)'; this.style.transform='translateY(-2px) scale(1.02)'; this.style.borderColor='#FFD700';" onmouseout="this.style.color='#2c3e50'; this.style.background='linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%)'; this.style.boxShadow='0 4px 12px rgba(0, 0, 0, 0.15)'; this.style.transform='translateY(0) scale(1)'; this.style.borderColor='#e9ecef';">Jestem Programista</a>'''
        
        # Replace the link
        new_content = re.sub(pattern, new_link, content)
        
        # Write the updated content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        
        return True
    except Exception as e:
        print(f"Error improving CSS in {file_path}: {e}")
        return False

def main_improve_css():
    """
    Función principal que mejora el CSS en todos los archivos HTML
    """
    html_files = glob.glob("*.html")
    total_improvements = 0
    
    print("\nMejorando CSS del enlace Jestem Programista en el footer...")
    print("=" * 60)
    
    for html_file in html_files:
        improvements = improve_footer_css(html_file)
        total_improvements += improvements
    
    print("=" * 60)
    print(f"Total de enlaces mejorados: {total_improvements}")
    print("¡Mejoras de CSS completadas!")

def remove_navbar_items(file_path):
    """Remove Franquicias and Blog from navbar"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Pattern to remove Franquicias menu items
        franquicias_patterns = [
            r'<li[^>]*class="[^"]*menu-item[^"]*menu-item-28[^"]*"[^>]*><a href="[^"]*franquicias[^"]*"[^>]*>Franquicias</a></li>',
            r'<li[^>]*><a href="[^"]*franquicias[^"]*"[^>]*title="Franquicias"[^>]*>Franquicias</a></li>',
            r'<li><a href="#franquicias"[^>]*>Franquicias</a></li>'
        ]
        
        # Pattern to remove Blog menu items
        blog_patterns = [
            r'<li[^>]*class="[^"]*menu-item[^"]*menu-item-4395[^"]*"[^>]*><a href="[^"]*blog[^"]*"[^>]*>Blog</a></li>',
            r'<li[^>]*><a href="[^"]*blog[^"]*"[^>]*title="Blog"[^>]*>Blog</a></li>',
            r'<li><a href="#blog"[^>]*>Blog</a></li>'
        ]
        
        # Remove Franquicias items
        for pattern in franquicias_patterns:
            content = re.sub(pattern, '', content, flags=re.IGNORECASE)
        
        # Remove Blog items
        for pattern in blog_patterns:
            content = re.sub(pattern, '', content, flags=re.IGNORECASE)
        
        # Write the updated content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        
        return True
    except Exception as e:
        print(f"Error removing navbar items in {file_path}: {e}")
        return False

def main_improve_css_enhanced():
    """Main function to apply enhanced CSS improvements for Jestem Programista link"""
    html_files = ['index.html', 'carta.html', 'contacto.html', 'eventos.html', 'pedidos.html', 'cookies-policy.html', 'sucursales.html']
    
    improved_count = 0
    for file_name in html_files:
        if os.path.exists(file_name):
            if improve_footer_css_enhanced(file_name):
                improved_count += 1
                print(f"Enhanced CSS improved in {file_name}")
            else:
                print(f"Failed to improve CSS in {file_name}")
        else:
            print(f"File {file_name} not found")
    
    print(f"Enhanced CSS improvements applied to {improved_count} files")

def main_remove_navbar_items():
    """Main function to remove Franquicias and Blog from navbar in all HTML files"""
    html_files = ['index.html', 'carta.html', 'contacto.html', 'eventos.html', 'pedidos.html', 'cookies-policy.html', 'sucursales.html']
    
    removed_count = 0
    for file_name in html_files:
        if os.path.exists(file_name):
            if remove_navbar_items(file_name):
                removed_count += 1
                print(f"Navbar items removed from {file_name}")
            else:
                print(f"Failed to remove navbar items from {file_name}")
        else:
            print(f"File {file_name} not found")
    
    print(f"Navbar items removed from {removed_count} files")

# Ejecutar la función de mejora de CSS
main_improve_css()
main_improve_css_enhanced()
main_remove_navbar_items()
# -*- coding: utf-8 -*-
"""
Script para corregir rutas de recursos locales (imágenes, CSS, JS)
"""

import os
import re
import glob

def fix_resource_paths(file_path):
    """Corrige las rutas de recursos en un archivo HTML"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='latin-1') as f:
            content = f.read()
    
    original_content = content
    changes_made = 0
    
    # Corregir rutas que empiezan con "../wp-content" a "wp-content"
    pattern1 = r'(src|href)="\.\./(wp-content/[^"]*)"'
    matches1 = re.findall(pattern1, content)
    content = re.sub(pattern1, r'\1="\2"', content)
    changes_made += len(matches1)
    
    # Corregir rutas que empiezan con "../awards.infcdn.net" (recursos externos)
    pattern2 = r'href="\.\./(awards\.infcdn\.net/[^"]*)"'
    matches2 = re.findall(pattern2, content)
    content = re.sub(pattern2, r'href="https://\1"', content)
    changes_made += len(matches2)
    
    # Corregir rutas de imágenes que apuntan a tiobigotes.com
    pattern3 = r'(src|srcset)="https://tiobigotes\.com/(wp-content/[^"]*)"'
    matches3 = re.findall(pattern3, content)
    content = re.sub(pattern3, r'\1="\2"', content)
    changes_made += len(matches3)
    
    # Corregir data-lazyload que apunta a tiobigotes.com
    pattern4 = r'data-lazyload="//tiobigotes\.com/(wp-content/[^"]*)"'
    matches4 = re.findall(pattern4, content)
    content = re.sub(pattern4, r'data-lazyload="\1"', content)
    changes_made += len(matches4)
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Corregidas {changes_made} rutas de recursos en: {os.path.basename(file_path)}")
        return True
    else:
        print(f"No se encontraron rutas para corregir en: {os.path.basename(file_path)}")
        return False

def main():
    """Función principal"""
    print("Iniciando corrección de rutas de recursos...")
    
    # Buscar todos los archivos HTML
    html_files = glob.glob("*.html")
    
    if not html_files:
        print("No se encontraron archivos HTML")
        return
    
    total_files_fixed = 0
    
    for html_file in html_files:
        print(f"Procesando: {html_file}")
        if fix_resource_paths(html_file):
            total_files_fixed += 1
    
    print(f"\nCorrección completada. {total_files_fixed} archivos modificados.")

if __name__ == "__main__":
    main()