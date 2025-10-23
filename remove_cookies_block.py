import re
import os
from pathlib import Path

ROOT = Path(r"c:\Users\Ayrton\Desktop\tiobigotes.pl")

# Regex que elimina desde el banner hasta el último overlay del modal
PATTERN = re.compile(r"<!--googleoff: all-->.*?<div class=\"cli-modal-backdrop cli-fade cli-popupbar-overlay\"></div>", re.S)

# Solo procesar archivos HTML en el directorio raíz (páginas del sitio)
# Evita tocar plugin assets y contenido dentro de wp-content y otras carpetas
EXCLUDE_DIRS = {"wp-content", "wp-admin", "wp-includes", "wp-json", "fonts", "tiobigotes-react"}

changed = []
skipped = []

for entry in ROOT.iterdir():
    if entry.is_dir():
        if entry.name in EXCLUDE_DIRS:
            continue
        # También mirar HTML directos en subcarpetas de primer nivel útiles (si existen)
        for html in entry.glob("*.html"):
            try:
                text = html.read_text(encoding="utf-8")
            except Exception:
                skipped.append(str(html))
                continue
            new_text, n = PATTERN.subn("", text)
            if n > 0:
                html.write_text(new_text, encoding="utf-8")
                changed.append(str(html))
            else:
                skipped.append(str(html))
        continue
    # Archivos sueltos en raíz
    if entry.suffix.lower() == ".html":
        try:
            text = entry.read_text(encoding="utf-8")
        except Exception:
            skipped.append(str(entry))
            continue
        new_text, n = PATTERN.subn("", text)
        if n > 0:
            entry.write_text(new_text, encoding="utf-8")
            changed.append(str(entry))
        else:
            skipped.append(str(entry))

print("Changed:")
for c in changed:
    print(" -", c)
print("\nChecked (no match or unreadable):")
for s in skipped:
    print(" -", s)