#!/usr/bin/env python3
"""
Script para corregir enlaces rotos en el sitio web de Tío Bigotes
Convierte enlaces de carpetas/index.html a archivos .html directos
"""

import os
import re
import glob

def fix_links_in_file(file_path):
    """Corrige los enlaces en un archivo HTML específico"""
    print(f"Procesando: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Mapeo de enlaces a corregir
    link_mappings = {
        # Enlaces principales del menú
        'carta/index.html': 'carta.html',
        'contacto/index.html': 'contacto.html', 
        'eventos/index.html': 'eventos.html',
        'pedidos/index.html': 'pedidos.html',
        'haz-tu-pedido/index.html': 'pedidos.html',
        
        # Enlaces con rutas relativas (para páginas en subdirectorios)
        '../carta/index.html': 'carta.html',
        '../contacto/index.html': 'contacto.html',
        '../eventos/index.html': 'eventos.html', 
        '../haz-tu-pedido/index.html': 'pedidos.html',
        '../index.html': 'index.html',
        
        # Enlaces que no tienen páginas correspondientes - convertir a anclas
        'sucursales/index.html': '#sucursales',
        'franquicias/index.html': '#franquicias', 
        'tio-bigotes/index.html': '#tio-bigotes',
        'hisotria/index.html': '#historia',  # Nota: hay un typo en el original
        'blog/index.html': '#blog',
        'aviso-legal/index.html': '#aviso-legal',
        'politica-de-privacidad/index.html': '#politica-privacidad',
        'politica-de-cookies/index.html': 'cookies-policy.html',
        
        # Enlaces con rutas relativas
        '../sucursales/index.html': '#sucursales',
        '../franquicias/index.html': '#franquicias',
        '../tio-bigotes/index.html': '#tio-bigotes', 
        '../hisotria/index.html': '#historia',
        '../blog/index.html': '#blog',
        '../aviso-legal/index.html': '#aviso-legal',
        '../politica-de-privacidad/index.html': '#politica-privacidad',
        '../politica-de-cookies/index.html': 'cookies-policy.html',
    }
    
    # Aplicar las correcciones
    for old_link, new_link in link_mappings.items():
        # Buscar y reemplazar enlaces en href
        pattern = f'href="{re.escape(old_link)}"'
        replacement = f'href="{new_link}"'
        content = re.sub(pattern, replacement, content)
        
        # También buscar sin comillas (por si acaso)
        pattern = f'href={re.escape(old_link)}'
        replacement = f'href={new_link}'
        content = re.sub(pattern, replacement, content)
    
    # Corregir enlaces de productos (que no existen, convertir a anclas)
    content = re.sub(r'href="productos/[^"]*"', 'href="#productos"', content)
    
    # Si hubo cambios, guardar el archivo
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Corregido: {file_path}")
        return True
    else:
        print(f"- Sin cambios: {file_path}")
        return False

def main():
    """Función principal"""
    print("Iniciando corrección de enlaces...")
    
    # Buscar todos los archivos HTML en el directorio actual
    html_files = glob.glob("*.html")
    
    if not html_files:
        print("No se encontraron archivos HTML")
        return
    
    corrected_files = 0
    
    for html_file in html_files:
        if fix_links_in_file(html_file):
            corrected_files += 1
    
    print(f"\n✓ Proceso completado!")
    print(f"Archivos procesados: {len(html_files)}")
    print(f"Archivos corregidos: {corrected_files}")

if __name__ == "__main__":
    main()