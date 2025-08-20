#!/usr/bin/env python3
import pathlib, re, sys
def main():
    violations=[]
    for p in pathlib.Path('.').rglob('*.html'):
        if '.git/' in str(p) or '.github/' in str(p): continue
        t=p.read_text(encoding='utf-8', errors='ignore')
        m=re.search(r'<pre>(.*?)</pre>', t, re.S|re.I)
        if not m: violations.append(f"{p}: missing <pre> metadata block"); continue
        pre=m.group(1)
        for key in ['Title:','ID:','Status:','Parents:','Tags:']:
            if key not in pre: violations.append(f"{p}: missing '{key}'")
        if 'Version:' not in pre: violations.append(f"{p}: missing 'Version:' on the Status line")
        sm=re.search(r'Status:\s*([A-Z]+)', pre)
        if not sm or sm.group(1) not in {'DRAFT','ACTIVE','FROZEN','ARCHIVED'}:
            violations.append(f"{p}: invalid Status")
    if violations:
        print('Metadata Lint — FAIL'); print('\n'.join('- '+v for v in violations)); sys.exit(1)
    print('Metadata Lint — OK'); sys.exit(0)
if __name__=='__main__': main()
