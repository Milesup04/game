#!/usr/bin/env python3
"""Build ValegendsGame.html — a fully self-contained single file.

Reads valegends.html, base64-embeds every image the game uses (scenes,
sprites, npcs, enemies, hero portraits) into the window.ASSETS map, and
writes ValegendsGame.html.  The result runs from a double-click anywhere:
no assets folder, no server, no internet needed.
"""
import base64, glob, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC  = os.path.join(ROOT, 'valegends.html')
OUT  = os.path.join(ROOT, 'ValegendsGame.html')

FOLDERS = ['assets/scenes', 'assets/sprites', 'assets/npcs',
           'assets/enemies', 'assets/heroes']
MIME = {'.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.png': 'image/png'}

def main():
    assets = {}
    for folder in FOLDERS:
        for f in sorted(glob.glob(os.path.join(ROOT, folder, '*.*'))):
            ext = os.path.splitext(f)[1].lower()
            if ext not in MIME:
                continue
            rel = os.path.relpath(f, ROOT).replace('\\', '/')
            with open(f, 'rb') as fh:
                assets[rel] = f'data:{MIME[ext]};base64,' + \
                    base64.b64encode(fh.read()).decode()
    html = open(SRC, encoding='utf-8').read()
    marker = 'window.ASSETS=null;//__ASSETS__'
    if marker not in html:
        sys.exit('marker not found in valegends.html')
    html = html.replace(marker,
        'window.ASSETS=' + json.dumps(assets) + ';//__ASSETS__')
    open(OUT, 'w', encoding='utf-8').write(html)
    print(f'embedded {len(assets)} assets -> {OUT} '
          f'({os.path.getsize(OUT)/1e6:.1f} MB)')

if __name__ == '__main__':
    main()
