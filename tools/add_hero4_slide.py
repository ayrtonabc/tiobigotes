import io, os, re

paths = [
    (r"c:\\Users\\Ayrton\\Desktop\\tiobigotes.pl\\index.html", "pl", "menu.html"),
    (r"c:\\Users\\Ayrton\\Desktop\\tiobigotes.pl\\index-es.html", "es", "carta-es.html"),
    (r"c:\\Users\\Ayrton\\Desktop\\tiobigotes.pl\\index-en.html", "en", "carta-en.html"),
]

DIV_OPEN = re.compile(r"<div\b", re.IGNORECASE)
DIV_CLOSE = re.compile(r"</div>", re.IGNORECASE)

for p, lang, link in paths:
    if not os.path.exists(p):
        print(f"Skip: {p} not found")
        continue

    with io.open(p, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the FIRST hero carousel wrapper
    wrapper_pos = html.find('<div class="dipi-carousel-wrapper">')
    if wrapper_pos == -1:
        print(f"Wrapper not found in {os.path.basename(p)}")
        continue

    # Find closing position of that wrapper by counting divs from wrapper_pos
    depth = 0
    i = wrapper_pos
    end_pos = None
    # From wrapper start, set depth to 1 after encountering the first <div
    # and then iterate through subsequent tags to find matching closing
    while i < len(html):
        m_open = DIV_OPEN.search(html, i)
        m_close = DIV_CLOSE.search(html, i)
        if not m_open and not m_close:
            break
        # Determine which comes next
        if m_close and (not m_open or m_close.start() < m_open.start()):
            # closing div
            if depth == 0:
                # This close matches the wrapper itself
                end_pos = m_close.start()
                break
            else:
                depth -= 1
            i = m_close.end()
        else:
            # opening div
            depth += 1
            i = m_open.end()

    if end_pos is None:
        print(f"Failed to compute wrapper end in {os.path.basename(p)}")
        continue

    hero_src = f"hero/hero4-{lang}.webp"

    # Construct new slide block (child_3) similar to existing slides
    new_block = (
        "\n\t\t\t<div class=\"et_pb_module dipi_carousel_child dipi_carousel_child_3 et_clickable\">\n"
        "\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n"
        "\t\t\t\t\t\t\t<div class=\"et_pb_module_inner\">\n\t\t\t\t\t\t\t\t\n"
        "            <div class=\"dipi-carousel-child-wrapper\">\n"
        f"                <a href=\"{link}\" >\n"
        "                <div class=\"dipi-image-wrap\"><span class=\"dipi-carousel-image  \"   >\n"
        f"                        <img loading=\"lazy\" decoding=\"async\" width=\"1920\" height=\"800\" src=\"{hero_src}\" alt=\"\" class=\"dipi-c-img\" />\n"
        "                        \n"
        "                    </span></div>\n"
        "                </a>\n\t\t\t\t\t\t\t\n"
        f"                <a href=\"{link}\" >\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\n"
        "            </div>\n"
        "\t\t\t\t\t\t\t</div>\n"
        "\t\t\t</div>\n"
    )

    # Insert new slide block just before the wrapper close
    new_html = html[:end_pos] + new_block + html[end_pos:]
    if new_html != html:
        with io.open(p, 'w', encoding='utf-8', newline='') as f:
            f.write(new_html)
        print(f"Inserted hero4 slide in {os.path.basename(p)}")
    else:
        print(f"No insertion performed in {os.path.basename(p)}")