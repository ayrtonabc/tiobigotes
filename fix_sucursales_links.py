#!/usr/bin/env python3
"""
Script para arreglar los enlaces de navegación a sucursales.html
Cambia href="#sucursales" por href="sucursales.html" en todos los archivos HTML
"""

import os
import re

def fix_sucursales_links():
    """Arregla los enlaces de sucursales en todos los archivos HTML"""
    
    # Lista de archivos HTML a procesar
    html_files = [
        'index.html',
        'carta.html', 
        'contacto.html',
        'eventos.html',
        'pedidos.html',
        'cookies-policy.html',
        'sucursales.html'
    ]
    
    # Patrones a reemplazar
    patterns = [
        # Enlaces principales de navegación
        (r'href="#sucursales"', 'href="sucursales.html"'),
        # Enlaces en el footer
        (r'<a href="#sucursales"', '<a href="sucursales.html"'),
    ]
    
    total_replacements = 0
    
    for filename in html_files:
        if not os.path.exists(filename):
            print(f"Archivo no encontrado: {filename}")
            continue
            
        print(f"Procesando {filename}...")
        
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
            
            original_content = content
            file_replacements = 0
            
            # Aplicar todos los patrones
            for pattern, replacement in patterns:
                matches = re.findall(pattern, content)
                if matches:
                    content = re.sub(pattern, replacement, content)
                    file_replacements += len(matches)
                    print(f"  - Reemplazados {len(matches)} enlaces con patrón: {pattern}")
            
            # Guardar solo si hubo cambios
            if content != original_content:
                with open(filename, 'w', encoding='utf-8') as file:
                    file.write(content)
                print(f"  ✓ {file_replacements} enlaces actualizados en {filename}")
                total_replacements += file_replacements
            else:
                print(f"  - No se encontraron enlaces para actualizar en {filename}")
                
        except Exception as e:
            print(f"Error procesando {filename}: {e}")
    
    print(f"\n✓ Total de enlaces actualizados: {total_replacements}")
    return total_replacements

def fix_ver_sucursales_button():
    """Arregla específicamente el botón 'Ver sucursales' en pedidos.html"""
    
    filename = 'pedidos.html'
    if not os.path.exists(filename):
        print(f"Archivo no encontrado: {filename}")
        return 0
        
    print(f"Arreglando botón 'Ver sucursales' en {filename}...")
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        original_content = content
        
        # Patrón específico para el botón "Ver sucursales"
        pattern = r'(<a class="et_pb_button[^"]*"[^>]*href=")#sucursales(">[^<]*Ver sucursales[^<]*</a>)'
        replacement = r'\1sucursales.html\2'
        
        matches = re.findall(pattern, content)
        if matches:
            content = re.sub(pattern, replacement, content)
            print(f"  - Encontrado y arreglado botón 'Ver sucursales'")
        
        # Patrón alternativo más simple
        if content == original_content:
            pattern2 = r'href="#sucursales">Ver sucursales'
            replacement2 = r'href="sucursales.html">Ver sucursales'
            if re.search(pattern2, content):
                content = re.sub(pattern2, replacement2, content)
                print(f"  - Arreglado enlace 'Ver sucursales' con patrón alternativo")
        
        # Guardar si hubo cambios
        if content != original_content:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"  ✓ Botón 'Ver sucursales' actualizado en {filename}")
            return 1
        else:
            print(f"  - No se encontró el botón 'Ver sucursales' para actualizar")
            return 0
            
    except Exception as e:
        print(f"Error procesando {filename}: {e}")
        return 0

if __name__ == "__main__":
    print("=== Arreglando enlaces de navegación a sucursales.html ===\n")
    
    # Arreglar enlaces generales
    general_fixes = fix_sucursales_links()
    
    print("\n" + "="*50)
    
    # Arreglar botón específico
    button_fixes = fix_ver_sucursales_button()
    
    print("\n" + "="*50)
    print(f"RESUMEN:")
    print(f"- Enlaces generales actualizados: {general_fixes}")
    print(f"- Botones específicos actualizados: {button_fixes}")
    print(f"- Total de correcciones: {general_fixes + button_fixes}")
    print("\n✓ Proceso completado. Todos los enlaces ahora apuntan a sucursales.html")