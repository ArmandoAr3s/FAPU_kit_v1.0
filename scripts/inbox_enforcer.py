#!/usr/bin/env python3
import argparse, pathlib, time, sys
from datetime import datetime
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--hours', type=int, default=24); ap.add_argument('--create-report', action='store_true')
    a=ap.parse_args()
    inbox=pathlib.Path('80_INBOX'); 
    if not inbox.exists(): print('No 80_INBOX/ folder.'); return 0
    th=time.time()-a.hours*3600; offenders=[]
    for p in inbox.rglob('*'):
        if p.is_file() and p.name!='.gitkeep' and p.stat().st_mtime<th: offenders.append(p)
    if a.create_report:
        with open('inbox_report.md','w',encoding='utf-8') as f:
            if offenders:
                f.write('# INBOX Enforcer Report\n\n')
                for p in offenders:
                    age=int((time.time()-p.stat().st_mtime)/3600)
                    f.write(f'- `{p}` — ~{age}h old\n')
            else: f.write('# INBOX Enforcer Report\n\nNo stale items.\n')
    if offenders: print(f'INBOX Enforcer — {len(offenders)} stale items'); return 1
    print('INBOX Enforcer — OK'); return 0
if __name__=='__main__': sys.exit(main())
