# -*- coding: utf-8 -*-
# شغّل:  python build.py   (يحتاج data.py بجانبه)
# عدّل الأربعة التالية فقط:
APP   = "Hey Hello World!"
MAIL  = "hey.hello.world.2027@gmail.com"
DATE  = "2026-11-01"
ORDER = ['ar','en','ru','ur','es','de','fr','tr','zh','hi']

from data import L
RTL = {'ar','ur'}

def blk(text, mail, plink):
    text = text.replace('{mail}', f'<a href="mailto:{mail}">{mail}</a>').replace('{plink}', plink)
    out, ul = [], []
    for ln in text.split('\n'):
        if ln.startswith('- '): ul.append(f'<li>{ln[2:]}</li>')
        else:
            if ul: out.append('<ul>'+''.join(ul)+'</ul>'); ul=[]
            out.append(f'<p>{ln}</p>')
    if ul: out.append('<ul>'+''.join(ul)+'</ul>')
    return ''.join(out)

def spans(key):  # نص قصير بكل اللغات
    return ''.join(f'<span data-l="{c}">{L[c][key].replace("&","&amp;") if key=="terms" else L[c][key]}</span>' for c in ORDER)

def page(fname, title, content):
    nav = ''.join(f'<a href="{f}" class="{"on" if f==fname else ""}">{spans(k)}</a>'
                  for f,k in [("index.html","home"),("privacy.html","privacy"),("terms.html","terms")])
    opts = ''.join(f'<option value="{c}">{L[c]["name"]}</option>' for c in ORDER)
    foot = ''.join(f'<span data-l="{c}">© {APP} — {L[c]["rights"]}</span>' for c in ORDER)
    return f'''<!DOCTYPE html>
<html lang="ar" dir="rtl" data-lang="ar">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | {APP}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
<script src="lang.js"></script>
</head>
<body><div class="wrap">
<header class="top">
<nav>{nav}</nav>
<div class="lang"><select id="langSel" aria-label="Language">{opts}</select></div>
</header>
{content}
<footer>{foot}</footer>
</div></body></html>'''

def doc(kind):
    parts=[]
    for c in ORDER:
        d=L[c]
        plink=f'<a href="privacy.html">{d["privacy"]}</a>'
        head = d['privacy'] if kind=='ps' else d['terms']
        intro = d['pi'] if kind=='ps' else d['ti']
        body = ''.join(f'<h2>{i}. {t}</h2>{blk(b,MAIL,plink)}' for i,(t,b) in enumerate(d[kind],1))
        parts.append(f'<section data-l="{c}"><h1>{head}</h1><p class="date">{d["upd"]}: {DATE}</p><div class="box">{intro.format(app=APP)}</div>{body}</section>')
    return ''.join(parts)

cards=''.join(f'''<section data-l="{c}"><h1>{APP}</h1><p class="date">{L[c]["docs"]}</p><div class="cards">
<a href="privacy.html"><b>{L[c]["privacy"]}</b>{L[c]["cp"]}</a>
<a href="terms.html"><b>{L[c]["terms"]}</b>{L[c]["ct"]}</a></div></section>''' for c in ORDER)

open('index.html','w',encoding='utf-8').write(page('index.html','Home',cards))
open('privacy.html','w',encoding='utf-8').write(page('privacy.html','Privacy Policy',doc('ps')))
open('terms.html','w',encoding='utf-8').write(page('terms.html','Terms & Conditions',doc('ts')))
print('done')
