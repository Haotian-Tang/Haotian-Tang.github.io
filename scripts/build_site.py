#!/usr/bin/env python3
"""Build the static site from HTML-only R Markdown sources, using Python 3."""
from html import escape
from pathlib import Path
from urllib.parse import urljoin
import json
import re

ROOT = Path(__file__).resolve().parents[1]
PAGES = ('index', 'research', 'publications', 'experience', 'education', 'teaching')
BASE_URL = 'https://haotian-tang.github.io/'

def build():
    template = (ROOT / '_templates/page.html').read_text()
    urls = []
    for name in PAGES:
        source = (ROOT / f'{name}.Rmd').read_text()
        match = re.fullmatch(r'---\n(.*?)\n---\n\s*```\{=html\}\n(.*?)\n```\s*', source, re.S)
        if not match:
            raise ValueError(f'{name}.Rmd must contain metadata and one raw HTML block')
        metadata = dict(line.split(': ', 1) for line in match[1].splitlines())
        values = {key: escape(json.loads(value), quote=True) for key, value in metadata.items()}
        values['body'] = match[2]
        output = re.sub(r'\$([a-z-]+)\$', lambda m: values[m[1]], template)
        (ROOT / f'{name}.html').write_text(output)
        urls.append(urljoin(BASE_URL, '' if name == 'index' else f'{name}.html'))

    (ROOT / 'publication.html').write_text('''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Publications | Haotian Tang</title><meta http-equiv="refresh" content="0; url=publications.html">
<link rel="canonical" href="https://haotian-tang.github.io/publications.html"><link rel="stylesheet" href="styles.css"></head>
<body><main class="container page-heading"><h1>Publications</h1><p><a href="publications.html">Continue to publications →</a></p></main></body></html>
''')
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sitemap += ''.join(f'  <url><loc>{escape(url)}</loc></url>\n' for url in urls)
    (ROOT / 'sitemap.xml').write_text(sitemap + '</urlset>\n')
    print(f'Built {len(PAGES)} pages, the legacy redirect, and sitemap.xml.')

if __name__ == '__main__':
    build()
