#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para descargar fuentes de Google Fonts y localizarlas
"""

import os
import re
import requests
import glob
from urllib.parse import urlparse

def download_font(url, filename):
    """Descarga una fuente desde una URL"""
    try:
        print(f"Descargando: {filename}")
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        with open(f"fonts/{filename}", 'wb') as f:
            f.write(response.content)
        
        print(f"Descargado: {filename}")
        return True
    except Exception as e:
        print(f"Error descargando {filename}: {e}")
        return False

def extract_font_urls(html_content):
    """Extrae URLs de fuentes de Google Fonts del contenido HTML"""
    font_urls = set()
    
    # Buscar URLs de fuentes en @font-face
    font_face_pattern = r'url\((https://fonts\.gstatic\.com/[^)]+)\)'
    matches = re.findall(font_face_pattern, html_content)
    
    for match in matches:
        font_urls.add(match)
    
    return font_urls

def replace_font_urls_in_file(file_path, url_mapping):
    """Reemplaza URLs de fuentes remotas con rutas locales"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        for remote_url, local_path in url_mapping.items():
            content = content.replace(remote_url, local_path)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Actualizadas URLs de fuentes en: {os.path.basename(file_path)}")
        
        return True
    except Exception as e:
        print(f"Error actualizando {file_path}: {e}")
        return False

def main():
    """Función principal"""
    print("Iniciando descarga y localización de fuentes...")
    
    # Crear directorio de fuentes si no existe
    os.makedirs("fonts", exist_ok=True)
    
    # Buscar todos los archivos HTML
    html_files = glob.glob("*.html")
    
    if not html_files:
        print("No se encontraron archivos HTML")
        return
    
    all_font_urls = set()
    
    # Extraer URLs de fuentes de todos los archivos HTML
    for html_file in html_files:
        print(f"Analizando fuentes en: {html_file}")
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            # Intentar con latin-1 si utf-8 falla
            with open(html_file, 'r', encoding='latin-1') as f:
                content = f.read()
        
        font_urls = extract_font_urls(content)
        all_font_urls.update(font_urls)
        print(f"Encontradas {len(font_urls)} fuentes en {html_file}")
    
    print(f"Total de fuentes únicas encontradas: {len(all_font_urls)}")
    
    if not all_font_urls:
        print("No se encontraron fuentes para descargar")
        return
    
    # Descargar fuentes y crear mapeo
    url_mapping = {}
    
    for i, url in enumerate(all_font_urls, 1):
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        
        print(f"Procesando fuente {i}/{len(all_font_urls)}: {filename}")
        
        if download_font(url, filename):
            local_path = f"fonts/{filename}"
            url_mapping[url] = local_path
    
    print(f"Descargadas {len(url_mapping)} fuentes exitosamente")
    
    # Actualizar URLs en archivos HTML
    for html_file in html_files:
        replace_font_urls_in_file(html_file, url_mapping)
    
    print("Localización de fuentes completada")

if __name__ == "__main__":
    main()