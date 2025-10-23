#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para limpiar archivos HTML del sitio Tío Bigotes
Elimina comentarios de HTTrack y enlaces hreflang
"""

import os
import re
import glob

def clean_html_file(file_path):
    """Limpia un archivo HTML eliminando comentarios de HTTrack y enlaces hreflang"""
    try:
        print(f"Procesando: {file_path}")
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_length = len(content)
        
        # Eliminar comentarios de HTTrack
        content = re.sub(r'<!-- Mirrored from [^>]* -->', '', content)
        content = re.sub(r'<!-- Added by HTTrack -->', '', content)
        
        # Eliminar enlaces hreflang
        content = re.sub(r'<link rel="alternate" hreflang="[^"]*" href="[^"]*" />', '', content)
        
        new_length = len(content)
        
        # Escribir el archivo limpio
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Limpiado: {os.path.basename(file_path)} - Reducido {original_length - new_length} caracteres")
        return True
        
    except Exception as e:
        print(f"Error limpiando {file_path}: {e}")
        return False

def main():
    """Función principal"""
    print("Iniciando limpieza de archivos HTML...")
    
    # Buscar todos los archivos HTML
    html_files = glob.glob("*.html")
    
    if not html_files:
        print("No se encontraron archivos HTML")
        return
    
    print(f"Encontrados {len(html_files)} archivos HTML: {html_files}")
    
    # Limpiar cada archivo
    for html_file in html_files:
        clean_html_file(html_file)
    
    print("Limpieza completada")

if __name__ == "__main__":
    main()