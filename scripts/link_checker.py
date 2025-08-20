#!/usr/bin/env python3
import pathlib, re, sys
SCHEMES=('http:','https:','mailto:','tel:','data:')
def main():
    broken=[]
    for f in pathlib.Path('.').rglob('*.html'):
        if '.git/' in str(f) or '.github/' in str(f): continue
        txt=f.read_text(encoding='utf-8', errors='ignore')
        for href in re.findall(r'href\s*=\s*"(.*?)"', txt, re.I):
            if not href or href.startswith('#') or href.startswith(SCHEMES): continue
            target=(f.parent / href).resolve()
            target=pathlib.Path(str(target).split('#')[0].split('?')[0])
            if not target.exists(): broken.append(f"{f}: broken link -> {href}")
    if broken:
        print('Link Checker — FAIL'); print('\n'.join('- '+b for b in broken)); sys.exit(1)
    print('Link Checker — OK'); sys.exit(0)
if __name__=='__main__': main()
