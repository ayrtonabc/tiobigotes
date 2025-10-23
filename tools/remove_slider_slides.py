import io, os, re

# Files to process: Polish, Spanish, and English index pages
paths = [
    r"c:\\Users\\Ayrton\\Desktop\\tiobigotes.pl\\index.html",
    r"c:\\Users\\Ayrton\\Desktop\\tiobigotes.pl\\index-es.html",
    r"c:\\Users\\Ayrton\\Desktop\\tiobigotes.pl\\index-en.html",
]

# Patterns to remove child_3 and child_4 blocks from the hero slider
pat3 = re.compile(r'(<div class="et_pb_module dipi_carousel_child dipi_carousel_child_3 et_clickable">[\s\S]*?<\/div>\s*<\/div>\s*<\/div>)', re.DOTALL)
pat4 = re.compile(r'(<div class="et_pb_module dipi_carousel_child dipi_carousel_child_4 et_clickable">[\s\S]*?<\/div>\s*<\/div>\s*<\/div>)', re.DOTALL)

for p in paths:
    if not os.path.exists(p):
        print(f"Skip: {p} not found")
        continue
    with io.open(p, 'r', encoding='utf-8') as f:
        html = f.read()
    new_html = pat3.sub('', html)
    new_html2 = pat4.sub('', new_html)
    if new_html2 != html:
        with io.open(p, 'w', encoding='utf-8', newline='') as f:
            f.write(new_html2)
        print(f"Updated: Removed slides 3 and 4 in {os.path.basename(p)}")
    else:
        print(f"No changes: Patterns did not match in {os.path.basename(p)}")