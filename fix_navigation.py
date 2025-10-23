#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para corregir enlaces de navegación del sitio Tío Bigotes
Convierte enlaces de carpetas a archivos HTML directos
"""

import os
import re
import glob

def fix_navigation_links(file_path):
    """Corrige los enlaces de navegación en un archivo HTML"""
    try:
        print(f"Procesando navegación en: {file_path}")
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes_made = 0
        
        # Mapeo específico de enlaces según el archivo
        if file_path == 'index.html':
            # Para index.html, los enlaces son relativos sin ../
            replacements = [
                (r'href="carta/index\.html"', 'href="carta.html"'),
                (r'href="contacto/index\.html"', 'href="contacto.html"'),
                (r'href="eventos/index\.html"', 'href="eventos.html"'),
                (r'href="haz-tu-pedido/index\.html"', 'href="pedidos.html"'),
                (r'href="sucursales/index\.html"', 'href="#sucursales"'),
                (r'href="franquicias/index\.html"', 'href="#franquicias"'),
                (r'href="tio-bigotes/index\.html"', 'href="#nosotros"'),
                (r'href="hisotria/index\.html"', 'href="#historia"'),
                (r'href="productos/[^"]*\.html"', 'href="#productos"'),
                (r'href="aviso-legal/index\.html"', 'href="#aviso-legal"'),
                (r'href="politica-de-privacidad/index\.html"', 'href="#politica-privacidad"'),
                (r'href="politica-de-cookies/index\.html"', 'href="cookies-policy.html"'),
                (r'href="blog/index\.html"', 'href="#blog"')
            ]
        else:
            # Para otros archivos, los enlaces tienen ../
            replacements = [
                (r'href="\.\./carta/index\.html"', 'href="carta.html"'),
                (r'href="\.\./contacto/index\.html"', 'href="contacto.html"'),
                (r'href="\.\./eventos/index\.html"', 'href="eventos.html"'),
                (r'href="\.\./haz-tu-pedido/index\.html"', 'href="pedidos.html"'),
                (r'href="\.\./sucursales/index\.html"', 'href="#sucursales"'),
                (r'href="\.\./franquicias/index\.html"', 'href="#franquicias"'),
                (r'href="\.\./tio-bigotes/index\.html"', 'href="#nosotros"'),
                (r'href="\.\./hisotria/index\.html"', 'href="#historia"'),
                (r'href="\.\./index\.html"', 'href="index.html"'),
                (r'href="\.\./aviso-legal/index\.html"', 'href="#aviso-legal"'),
                (r'href="\.\./politica-de-privacidad/index\.html"', 'href="#politica-privacidad"'),
                (r'href="\.\./politica-de-cookies/index\.html"', 'href="cookies-policy.html"'),
                (r'href="\.\./blog/index\.html"', 'href="#blog"'),
                # Enlaces canónicos y de la misma página
                (r'href="index\.html"', f'href="{os.path.basename(file_path)}"')
            ]
        
        # Aplicar todas las correcciones
        for pattern, replacement in replacements:
            new_content = re.sub(pattern, replacement, content)
            if new_content != content:
                changes_made += 1
                content = new_content
        
        # Escribir el archivo corregido
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Corregido: {os.path.basename(file_path)} - {changes_made} tipos de enlaces actualizados")
        else:
            print(f"Sin cambios: {os.path.basename(file_path)}")
        
        return True
        
    except Exception as e:
        print(f"Error corrigiendo {file_path}: {e}")
        return False

def main():
    """Función principal"""
    print("Iniciando corrección de enlaces de navegación...")
    
    # Buscar todos los archivos HTML
    html_files = glob.glob("*.html")
    
    if not html_files:
        print("No se encontraron archivos HTML")
        return
    
    print(f"Encontrados {len(html_files)} archivos HTML")
    
    # Corregir enlaces en cada archivo
    for html_file in html_files:
        fix_navigation_links(html_file)
    
    print("Corrección de navegación completada")

if __name__ == "__main__":
    main()