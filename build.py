"""Сборка статических сайтов CakesCats в out/<домен>/."""
import os, shutil, sys
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
import sites

OUT = os.path.join(os.path.dirname(__file__), 'out')
IMG = os.path.join(os.path.dirname(__file__), 'img')

# какие страницы есть у каждого сайта: (путь EN, путь RU, функция)
PAGES = {
    'home':  [('', 'ru/', sites.home)],
    'main':  [('', 'ru/', sites.main), ('insights/', 'ru/insights/', sites.insights)],
    'os':    [('', 'ru/', sites.os_)],
    'phone': [('', 'ru/', sites.phone)],
    'vpn':   [('', 'ru/', sites.vpn)],
    'llm':   [('', 'ru/', sites.llm)],
}

# редиректы со старых адресов WordPress
REDIRECTS = {
    'main': [('^prods/?$', '/#products'), ('^about/?$', '/#about'), ('^knowledge-base/?$', '/insights/'), ('^article[0-9]+/?$', '/insights/'),
             ('^ru/prods-ru/?$', '/ru/#products'), ('^ru/about-ru/?$', '/ru/#about'), ('^ru/knowledge-base-ru/?$', '/ru/insights/'),
             ('^ru/article.*-ru(-[0-9]+)?/?$', '/ru/insights/'), ('^ru/article.*-en(-[0-9]+)?/?$', '/insights/'), ('^en/?$', '/')],
    'os': [('^operating-system/?$', '/')],
    'phone': [('^en/?$', '/')], 'vpn': [('^en/?$', '/')], 'llm': [('^en/?$', '/')],
}

HTACCESS = """# CakesCats — статический сайт
Options -Indexes
DirectoryIndex index.html
ErrorDocument 404 /index.html

RewriteEngine On
RewriteCond %{{HTTPS}} !=on
RewriteCond %{{REQUEST_URI}} !^/\\.well-known/acme-challenge/
RewriteRule ^ https://%{{HTTP_HOST}}%{{REQUEST_URI}} [L,R=301]
RewriteCond %{{HTTP_HOST}} ^www\\.(.+)$ [NC]
RewriteRule ^ https://%1%{{REQUEST_URI}} [L,R=301]

# остатки WordPress
RewriteRule ^(wp-admin|wp-content|wp-includes|wp-json)(/.*)?$ / [L,R=301]
RewriteRule ^(wp-login|xmlrpc|wp-cron)\\.php$ - [F,L]
RewriteRule ^feed/?$ / [L,R=301]
{redirects}
<IfModule mod_headers.c>
  Header always set X-Content-Type-Options "nosniff"
  Header always set Referrer-Policy "strict-origin-when-cross-origin"
  Header always set X-Frame-Options "SAMEORIGIN"
  Header always set Permissions-Policy "camera=(), microphone=(), geolocation=()"
  Header always set Strict-Transport-Security "max-age=31536000"
  <FilesMatch "\\.(css|js|webp|png|jpg|svg|woff2)$">
    Header set Cache-Control "public, max-age=2592000"
  </FilesMatch>
  <FilesMatch "\\.html$">
    Header set Cache-Control "no-cache"
  </FilesMatch>
</IfModule>
"""


def depth_root(path):
    return '../' * path.count('/')


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)


def main():
    shutil.rmtree(OUT, ignore_errors=True)
    for key, pages in PAGES.items():
        dom = SITES[key]['domain']
        d = os.path.join(OUT, dom)
        urls = []
        for en_path, ru_path, fn in pages:
            for lang, path in (('en', en_path), ('ru', ru_path)):
                root = depth_root(path)
                title, desc, nav, body = fn(lang, root)
                write(os.path.join(d, path, 'index.html'), page(key, lang, (en_path, ru_path), title, desc, nav, body, root))
                urls.append(url(key) + path)
        # политика конфиденциальности (одна, на польском)
        title, desc, nav, body = sites.privacy('en', '../', key)
        write(os.path.join(d, 'privacy', 'index.html'), page(key, 'en', ('privacy/', 'privacy/'), title, desc, nav, body, '../', noindex=True))
        # ассеты
        write(os.path.join(d, 'assets', 'site.css'), CSS.strip() + '\n')
        write(os.path.join(d, 'assets', 'site.js'), JS.strip() + '\n')
        shutil.copytree(IMG, os.path.join(d, 'assets', 'img'))
        # служебные файлы
        rd = '\n'.join(f'RewriteRule {a} {b} [L,R=301]' for a, b in REDIRECTS.get(key, []))
        write(os.path.join(d, '.htaccess'), HTACCESS.format(redirects=rd))
        write(os.path.join(d, 'robots.txt'), f'User-agent: *\nAllow: /\nDisallow: /privacy/\nSitemap: {url(key)}sitemap.xml\n')
        sm = ''.join(f'<url><loc>{u}</loc></url>' for u in urls)
        write(os.path.join(d, 'sitemap.xml'), f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sm}</urlset>\n')
        print(f'{dom:22s} {len(urls)} pages')


if __name__ == '__main__':
    main()
