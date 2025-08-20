#!/usr/bin/env python3
import pathlib, datetime
T='''<!doctype html><html lang="sq"><head><meta charset="utf-8"><title>Retro</title></head>
<body><pre>
Title: Retro
ID: DOC-{DATE}-RETRO | Owner: PROJECT
Status: ACTIVE | Version: v1.0
Parents: ../_index.html ; SSOT: /00_CORE/_MASTER_INDEX.html
Tags: type:record, scope:local
</pre>
<h1>Retro</h1><h3>Çfarë shkoi mirë</h3><ul></ul>
<h3>Çfarë s’shkoi</h3><ul></ul>
<h3>Çfarë ndryshojmë</h3><ul></ul>
<h3>Veprime të matshme</h3><ul></ul></body></html>'''
def main():
    root=pathlib.Path('20_PROJECTS')
    if not root.exists(): print('No 20_PROJECTS/'); return 0
    d=datetime.date.today().strftime('%Y%m%d'); created=0
    for prj in root.iterdir():
        if prj.is_dir() and prj.name.startswith('PRJ-'):
            dest=prj/'4_Learn'/f'Retro_{d}.html'
            if not dest.exists():
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(T.replace('{DATE}', d), encoding='utf-8')
                print('Created', dest); created+=1
    if not created: print('No Retro files created.')
    return 0
if __name__=='__main__': raise SystemExit(main())
