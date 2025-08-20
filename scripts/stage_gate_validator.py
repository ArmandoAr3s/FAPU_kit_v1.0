#!/usr/bin/env python3
import pathlib, re, sys
def status(p): 
    if not p.exists(): return None
    m=re.search(r'Status:\s*([A-Z]+)', p.read_text(encoding='utf-8', errors='ignore'))
    return m.group(1) if m else None
def has_files(d): return d.exists() and any(d.iterdir())
def has_retro(d): 
    return d.exists() and any(x.is_file() and x.name.lower().startswith('retro') for x in d.iterdir())
def validate(prj):
    errs=[]
    for sub in ['0_Intake','1_Plan','2_Build','3_Deliverables','4_Learn']:
        if not (prj/sub).exists(): errs.append(f"{prj}: missing folder {sub}")
    idx=prj/'_index.html'
    if not idx.exists(): errs.append(f"{prj}: missing _index.html"); return errs
    st=status(idx)
    if not st: errs.append(f"{prj}: cannot detect Status in _index.html"); return errs
    if st=='ACTIVE' and not has_files(prj/'1_Plan'): errs.append(f"{prj}: ACTIVE requires files in 1_Plan")
    if st in {'FROZEN','ARCHIVED'} and not has_files(prj/'3_Deliverables'): errs.append(f"{prj}: {st} requires files in 3_Deliverables")
    if st=='ARCHIVED' and not has_retro(prj/'4_Learn'): errs.append(f"{prj}: ARCHIVED requires Retro* in 4_Learn")
    return errs
def main():
    root=pathlib.Path('20_PROJECTS'); 
    if not root.exists(): print('No 20_PROJECTS/ folder.'); return 0
    errs=[]
    for p in root.iterdir():
        if p.is_dir() and p.name.startswith('PRJ-'): errs+=validate(p)
    if errs: print('Stage Gate Validator — FAIL'); print('\n'.join('- '+e for e in errs)); sys.exit(1)
    print('Stage Gate Validator — OK'); sys.exit(0)
if __name__=='__main__': main()
