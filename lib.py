"""Общая дизайн-система и каркас страниц для всех сайтов CakesCats."""
import html as _html

ESC = _html.escape

# ---------------------------------------------------------------- сайты
SITES = {
    'home':  {'domain': 'cakescats.com',       'name': 'Cakes Cats',     'sub': {'en': 'Consulting', 'ru': 'Консалтинг'}},
    'main':  {'domain': 'main.cakescats.com',  'name': 'CakesCats',      'sub': {'en': 'Products', 'ru': 'Продукты'}},
    'os':    {'domain': 'os.cakescats.com',    'name': 'VirtualCatsOS',  'sub': {'en': 'for Mac', 'ru': 'для Mac'}},
    'phone': {'domain': 'phone.cakescats.com', 'name': 'CakesCats Phone','sub': {'en': 'GrapheneOS', 'ru': 'GrapheneOS'}},
    'vpn':   {'domain': 'vpn.cakescats.com',   'name': 'VPN Router',     'sub': {'en': 'by CakesCats', 'ru': 'от CakesCats'}},
    'llm':   {'domain': 'llm.cakescats.com',   'name': 'LLM EdgeBox',    'sub': {'en': 'Private AI', 'ru': 'Приватный ИИ'}},
}
ORDER = ['home', 'main', 'os', 'phone', 'vpn', 'llm']

ECO = {
    'home':  ({'en': 'Consulting', 'ru': 'Консалтинг'},
              {'en': 'Crisis communications, PR and AI adoption for technology companies.',
               'ru': 'Антикризисные коммуникации, PR и внедрение ИИ для технологических компаний.'}),
    'main':  ({'en': 'CakesCats', 'ru': 'CakesCats'},
              {'en': 'The product family for privacy and local AI, plus security insights.',
               'ru': 'Линейка продуктов для приватности и локального ИИ, материалы о безопасности.'}),
    'os':    ({'en': 'VirtualCatsOS', 'ru': 'VirtualCatsOS'},
              {'en': 'A private, isolated workspace for Macs with Apple silicon.',
               'ru': 'Приватная изолированная рабочая среда для Mac на Apple silicon.'}),
    'phone': ({'en': 'CakesCats Phone', 'ru': 'CakesCats Phone'},
              {'en': 'Google Pixel with GrapheneOS, set up and ready to use.',
               'ru': 'Google Pixel с GrapheneOS — настроен и готов к работе.'}),
    'vpn':   ({'en': 'VPN Router', 'ru': 'VPN-роутер'},
              {'en': 'A private Wi-Fi network with a dedicated server, out of the box.',
               'ru': 'Приватная Wi-Fi-сеть с выделенным сервером — из коробки.'}),
    'llm':   ({'en': 'LLM EdgeBox', 'ru': 'LLM EdgeBox'},
              {'en': 'Private AI that runs on your premises, with no cloud.',
               'ru': 'Приватный ИИ, который работает у вас, без облака.'}),
}

TG = 'https://t.me/cakescats'
MAIL = 'mail@cakescats.com'
GITHUB = 'https://github.com/cakescats'
LEGAL = 'FUNDACJA ROZWOJU PRZEDSIĘBIORCZOŚCI „TWÓJ STARTUP” · ul. Żurawia 6/12 lok. 766, 00-503 Warszawa · KRS 0000442857 · NIP 5213641211'


def url(key):
    return 'https://' + SITES[key]['domain'] + '/'


# ---------------------------------------------------------------- иконки
_IC = {
    'shield': '<path d="M12 3l7 3v6c0 4.5-3 7.6-7 9-4-1.4-7-4.5-7-9V6l7-3z"/>',
    'lock': '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
    'cpu': '<rect x="7" y="7" width="10" height="10" rx="1"/><path d="M9 2v3M15 2v3M9 19v3M15 19v3M2 9h3M2 15h3M19 9h3M19 15h3"/>',
    'wifi': '<path d="M2 9a15 15 0 0 1 20 0M5 12.5a10 10 0 0 1 14 0M8.5 16a5 5 0 0 1 7 0"/><path d="M12 19.5h.01"/>',
    'eyeoff': '<path d="M3 3l18 18"/><path d="M10.6 6.1A10 10 0 0 1 12 6c5 0 9 4 10 6-.5 1-1.6 2.6-3.2 3.9M6.6 6.6C4.4 8 2.8 10.2 2 12c1 2 5 6 10 6 1.7 0 3.2-.4 4.6-1.1"/><path d="M9.9 9.9a3 3 0 0 0 4.2 4.2"/>',
    'zap': '<path d="M13 2L4 14h7l-1 8 9-12h-7l1-8z"/>',
    'users': '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M21.5 20a6.5 6.5 0 0 0-4-6"/>',
    'globe': '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
    'check': '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
    'layers': '<path d="M12 3l9 5-9 5-9-5 9-5z"/><path d="M3 13l9 5 9-5"/>',
    'server': '<rect x="3" y="4" width="18" height="7" rx="1.5"/><rect x="3" y="13" width="18" height="7" rx="1.5"/><path d="M7 7.5h.01M7 16.5h.01"/>',
    'phone': '<rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 18h2"/>',
    'laptop': '<rect x="4" y="5" width="16" height="11" rx="1.5"/><path d="M2 19h20"/>',
    'chat': '<path d="M4 5h16v11H9l-5 4V5z"/>',
    'doc': '<path d="M6 2h8l4 4v16H6z"/><path d="M14 2v4h4M9 12h6M9 16h6"/>',
    'sliders': '<path d="M4 6h10M18 6h2M4 12h4M12 12h8M4 18h12"/><circle cx="16" cy="6" r="2"/><circle cx="10" cy="12" r="2"/><circle cx="18" cy="18" r="2"/>',
    'wipe': '<path d="M4 7h16M9 7V4h6v3M6 7l1 13h10l1-13"/>',
    'key': '<circle cx="8" cy="15" r="4"/><path d="M11 12l9-9M17 6l3 3"/>',
    'briefcase': '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5h6v2M3 13h18"/>',
    'megaphone': '<path d="M3 10v4h4l8 5V5L7 10H3z"/><path d="M18 9a4 4 0 0 1 0 6"/>',
    'compass': '<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5l-2 5-5 2 2-5 5-2z"/>',
    'search': '<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/>',
    'book': '<path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2z"/><path d="M4 19V5"/>',
    'arrow': '<path d="M5 12h14M13 6l6 6-6 6"/>',
    'send': '<path d="M21 4L3 11l6 2 2 6 3-4 5 4 2-15z"/>',
    'mail': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
    'code': '<path d="M8 7l-5 5 5 5M16 7l5 5-5 5M14 4l-4 16"/>',
    'heart': '<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/>',
    'route': '<circle cx="6" cy="18" r="2"/><circle cx="18" cy="6" r="2"/><path d="M8 18h6a4 4 0 0 0 0-8h-4a4 4 0 0 1 0-8h6"/>',
    'box': '<path d="M3 7l9-4 9 4v10l-9 4-9-4z"/><path d="M3 7l9 4 9-4M12 11v10"/>',
    'tool': '<path d="M14.5 6.5a4 4 0 0 0 5 5L12 19l-3 1 1-3 7.5-7.5"/><path d="M14.5 6.5L17 4l3 3-2.5 2.5"/>',
    'menu': '<path d="M4 7h16M4 12h16M4 17h16"/>',
}


def icon(name, size=24):
    return (f'<svg class="i" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{_IC[name]}</svg>')


# ---------------------------------------------------------------- CSS
CSS = r"""
:root{
  --bg:#070c2b;--bg-2:#0a1035;--card:#10173f;--card-2:#161e4d;--navy-3:#050920;
  --ink:#f3f4fb;--ink-2:#d6d9ee;--muted:#a3a9cf;--line:#1f2758;--line-2:#2d3568;
  --brand:#8f6bff;--brand-2:#7a55f5;--pink:#cd89e8;--violet:#aa81ff;--cyan:#57f3fe;
  --brand-soft:rgba(170,129,255,.14);--ok:#57f3fe;
  --r:12px;--shadow:0 10px 30px rgba(0,0,0,.35);
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{font-family:Inter,system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;color:var(--ink);background:var(--bg);line-height:1.6;font-size:16px;overflow-x:hidden}
a{color:inherit;text-decoration:none}
img{max-width:100%;display:block}
.wrap{max-width:1240px;margin:0 auto;padding:0 24px}
.i{flex:none}
.grad{background:linear-gradient(90deg,var(--pink),var(--violet) 50%,var(--cyan));-webkit-background-clip:text;background-clip:text;color:transparent}

/* шапка */
.hdr{position:sticky;top:0;z-index:50;background:rgba(7,12,43,.82);backdrop-filter:saturate(160%) blur(14px);border-bottom:1px solid var(--line)}
.hdr .wrap{display:flex;align-items:center;height:72px;gap:24px}
.logo{display:flex;align-items:center;gap:10px;font-weight:700;font-size:18px;letter-spacing:-.01em;white-space:nowrap}
.logo img{width:36px;height:36px;border-radius:50%}
.logo small{font-weight:500;color:var(--muted);font-size:14px;padding-left:10px;border-left:1px solid var(--line-2)}
.mainnav{display:flex;align-items:center;gap:2px;margin-left:8px}
.mainnav>a,.dd-b{white-space:nowrap;padding:8px 11px;border-radius:8px;font-weight:500;font-size:15px;color:var(--ink-2);background:none;border:0;font-family:inherit;cursor:pointer;display:inline-flex;align-items:center;gap:6px}
.mainnav>a:hover,.dd-b:hover,.dd.open .dd-b{background:rgba(255,255,255,.06);color:#fff}
.dd{position:relative}
.dd-b svg{transition:transform .2s}
.dd.open .dd-b svg{transform:rotate(180deg)}
.dd-m{display:none;position:absolute;top:calc(100% + 12px);right:-120px;width:620px;background:var(--card);border:1px solid var(--line-2);border-radius:14px;box-shadow:var(--shadow);padding:12px;grid-template-columns:1fr 1fr;gap:4px}
.dd.open .dd-m{display:grid}
.dd-m a{display:flex;gap:12px;padding:12px;border-radius:10px;transition:background .15s}
.dd-m a:hover{background:rgba(255,255,255,.05)}
.dd-m img{width:44px;height:44px;border-radius:10px;object-fit:cover;flex:none;border:1px solid var(--line-2)}
.dd-m b{display:block;font-size:15px;color:#fff}
.dd-m span{display:block;font-size:13px;color:var(--muted);line-height:1.4}
.dd-m em{font-style:normal;font-size:11px;font-weight:600;color:var(--cyan);margin-left:6px}
.hdr .cta{margin-left:auto;display:flex;gap:14px;align-items:center}
.lang{display:inline-flex;border:1px solid var(--line-2);border-radius:999px;overflow:hidden;font-size:12.5px;font-weight:600}
.lang a{padding:5px 11px;color:var(--muted)}
.lang a.on{background:var(--brand-soft);color:#fff}
.burger{display:none;background:none;border:1px solid var(--line-2);border-radius:8px;padding:7px;color:var(--ink);cursor:pointer}

/* кнопки */
.btn{display:inline-flex;align-items:center;gap:8px;padding:12px 22px;border-radius:8px;font-weight:600;font-size:15px;line-height:1.2;border:1px solid transparent;cursor:pointer;transition:background .15s,border-color .15s,color .15s,box-shadow .15s}
.btn-p{background:linear-gradient(90deg,var(--pink),var(--violet));color:var(--bg)}
.btn-p:hover{box-shadow:0 8px 24px rgba(170,129,255,.35)}
.btn-s,.btn-l{background:transparent;color:var(--ink);border-color:var(--line-2)}
.btn-s:hover,.btn-l:hover{border-color:var(--pink);color:#fff}
.btn-sm{padding:9px 16px;font-size:14px}
.link{color:var(--cyan);font-weight:600;display:inline-flex;align-items:center;gap:6px}
.link:hover{text-decoration:underline}

/* hero */
.hero{position:relative;border-bottom:1px solid var(--line);overflow:hidden}
.hero::before{content:"";position:absolute;inset:0;pointer-events:none;background:radial-gradient(640px 420px at 85% 0,rgba(170,129,255,.22),transparent 70%),radial-gradient(520px 380px at 0 60%,rgba(87,243,254,.08),transparent 70%)}
.hero .wrap{position:relative;display:grid;grid-template-columns:1.05fr .95fr;gap:56px;align-items:center;padding-top:76px;padding-bottom:76px}
.eyebrow{display:inline-block;font-size:13px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--cyan);margin-bottom:16px}
h1{font-size:clamp(34px,4.6vw,54px);line-height:1.08;letter-spacing:-.025em;font-weight:700;margin-bottom:20px;color:#fff}
.lead{font-size:19px;color:var(--muted);max-width:620px;margin-bottom:30px}
.btns{display:flex;flex-wrap:wrap;gap:12px}
.trust{display:flex;flex-wrap:wrap;gap:22px;margin-top:34px;color:var(--ink-2);font-size:14px;font-weight:500}
.trust span{display:inline-flex;align-items:center;gap:8px}
.trust .i{color:var(--pink)}
.media{background:var(--card);border:1px solid var(--line);border-radius:16px;overflow:hidden;box-shadow:var(--shadow);display:flex;align-items:center;justify-content:center;min-height:320px}
.media img{width:100%;height:100%;object-fit:cover}
.portrait{position:relative;width:min(380px,100%);aspect-ratio:1;justify-self:center}
.portrait::before{content:"";position:absolute;inset:-16px;border-radius:24px;background:conic-gradient(from 90deg,var(--pink),var(--violet),var(--cyan),var(--pink));filter:blur(30px);opacity:.4}
.portrait img{position:relative;width:100%;height:100%;object-fit:cover;object-position:center top;border-radius:16px;border:1px solid var(--line-2)}

/* секции */
section{padding:84px 0}
section.alt{background:var(--bg-2);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.sh{max-width:760px;margin-bottom:44px}
.sh.c{margin-left:auto;margin-right:auto;text-align:center}
h2{font-size:clamp(28px,3.2vw,38px);line-height:1.15;letter-spacing:-.02em;font-weight:700;margin-bottom:12px;color:#fff}
.sh p{color:var(--muted);font-size:17px}
h3{font-size:19px;line-height:1.3;font-weight:600;letter-spacing:-.01em;margin-bottom:8px;color:#fff}

.g2{display:grid;grid-template-columns:repeat(2,1fr);gap:24px}
.g3{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
.g4{display:grid;grid-template-columns:repeat(4,1fr);gap:24px}
.feat .ic{width:46px;height:46px;border-radius:12px;background:var(--brand-soft);color:var(--pink);display:grid;place-items:center;margin-bottom:16px}
.feat p{color:var(--muted);font-size:15px}
.card{background:var(--card);border:1px solid var(--line);border-radius:var(--r);padding:28px;transition:box-shadow .2s,border-color .2s,transform .2s}
a.card:hover{border-color:var(--pink);box-shadow:var(--shadow);transform:translateY(-3px)}
.card p{color:var(--muted);font-size:15px}
.card ul{list-style:none;margin-top:14px;display:grid;gap:8px}
.card li{display:flex;gap:10px;font-size:15px;color:var(--ink-2)}
.card li .i{color:var(--cyan);margin-top:3px}
.card .tag{display:inline-block;font-size:12px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--cyan);margin-bottom:10px}
.card .link{margin-top:16px}

.prod{display:flex;flex-direction:column;padding:0;overflow:hidden}
.prod .pi{background:var(--card-2);aspect-ratio:16/10;overflow:hidden}
.prod .pi img{width:100%;height:100%;object-fit:cover}
.prod .pb{padding:24px;display:flex;flex-direction:column;flex:1}
.prod .pb p{flex:1}
.from{margin-top:16px;font-size:14px;color:var(--muted)}
.from b{font-size:22px;color:#fff;font-weight:700;letter-spacing:-.01em}

/* конфигурации */
.cfg{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;align-items:stretch}
.tier{position:relative;display:flex;flex-direction:column;background:var(--card);border:1px solid var(--line);border-radius:var(--r);padding:30px}
.cfg.n4{grid-template-columns:repeat(4,1fr);gap:20px}
.cfg.n4 .tier{padding:26px}
.tier.free-t{border-style:dashed;border-color:rgba(87,243,254,.4)}
.tier.pop{border-color:var(--violet);box-shadow:0 0 0 1px var(--violet),var(--shadow)}
.badge{position:absolute;top:-12px;left:30px;background:linear-gradient(90deg,var(--pink),var(--violet));color:var(--bg);font-size:12px;font-weight:700;padding:4px 12px;border-radius:999px}
.tier .ti{background:var(--card-2);border-radius:8px;aspect-ratio:16/9;margin-bottom:20px;overflow:hidden}
.tier .ti img{width:100%;height:100%;object-fit:cover}
.tier h3{font-size:21px}
.tier .d{color:var(--muted);font-size:15px;min-height:48px}
.price{margin:18px 0 4px;font-size:34px;font-weight:700;letter-spacing:-.02em;line-height:1.1;color:#fff}
.price small{font-size:15px;font-weight:500;color:var(--muted);letter-spacing:0}
.pnote{font-size:13px;color:var(--muted);min-height:20px}
.tier ul{list-style:none;margin:18px 0 24px;display:grid;gap:9px;flex:1}
.tier li{display:flex;gap:10px;font-size:15px;color:var(--ink-2)}
.tier li .i{color:var(--cyan);margin-top:3px}
.tier .btns{flex-direction:column}
.tier .btn{justify-content:center}
.np{display:flex;align-items:center;gap:16px;max-width:980px;margin:0 auto 36px;padding:18px 22px;border:1px solid rgba(87,243,254,.28);background:rgba(87,243,254,.06);border-radius:12px}
.np>.i{color:var(--cyan)}
.np p{flex:1;color:var(--ink-2);font-size:15px}
.np b{color:#fff}
.np .btn{flex:none}
.free{display:flex;align-items:center;gap:7px;margin-top:8px;font-size:13px;font-weight:500;color:var(--cyan)}
@media (max-width:720px){.np{flex-direction:column;align-items:flex-start}}
.alert-pill{display:inline-flex;align-items:center;gap:8px;margin-bottom:22px;padding:7px 14px;border-radius:999px;font-size:14px;font-weight:600;color:var(--cyan);background:rgba(87,243,254,.08);border:1px solid rgba(87,243,254,.35);transition:background .15s}
.alert-pill:hover{background:rgba(87,243,254,.16)}
.mainnav>a[href="#urgent"]{color:var(--cyan)}
.urgent{border:1px solid rgba(87,243,254,.3);border-radius:16px;padding:40px;background:radial-gradient(700px 260px at 0 0,rgba(87,243,254,.08),transparent 70%),var(--card)}
.urgent-h{max-width:760px}
.urgent-h p{color:var(--muted);font-size:17px;margin-bottom:24px}
.todo{margin:14px 0 0;padding-left:24px;list-style:decimal outside;display:grid;gap:10px;color:var(--ink-2);font-size:15px}
.todo li{display:list-item;padding-left:4px}
.todo li::marker{color:var(--cyan);font-weight:700}
@media (max-width:720px){.urgent{padding:24px}}
.fine{margin-top:22px;font-size:13px;color:var(--muted);text-align:center}

.spec{width:100%;border-collapse:collapse;background:var(--card);border:1px solid var(--line);border-radius:var(--r);overflow:hidden;font-size:15px}
.spec th,.spec td{text-align:left;padding:14px 18px;border-bottom:1px solid var(--line);vertical-align:top}
.spec th{width:32%;font-weight:600;color:#fff;background:var(--card-2)}
.spec td{color:var(--ink-2)}
.spec tr:last-child th,.spec tr:last-child td{border-bottom:0}
.spec-wrap{overflow-x:auto}

.split{display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:center}
.split .media{min-height:360px}
.steps{display:grid;gap:18px;margin-top:8px}
.step{display:flex;gap:16px}
.step b{flex:none;width:32px;height:32px;border-radius:50%;background:linear-gradient(135deg,var(--pink),var(--violet));color:var(--bg);display:grid;place-items:center;font-size:14px}
.step p{color:var(--muted);font-size:15px}

.stats{display:grid;grid-template-columns:repeat(3,1fr);border:1px solid var(--line);border-radius:var(--r);background:var(--card)}
.stat{padding:26px 28px;border-right:1px solid var(--line)}
.stat:last-child{border-right:0}
.stat b{display:block;font-size:34px;font-weight:700;letter-spacing:-.02em;background:linear-gradient(90deg,var(--pink),var(--violet));-webkit-background-clip:text;background-clip:text;color:transparent}
.stat span{color:var(--muted);font-size:15px}

.faq{max-width:860px;margin:0 auto;border-top:1px solid var(--line)}
.faq details{border-bottom:1px solid var(--line)}
.faq summary{list-style:none;cursor:pointer;padding:20px 40px 20px 0;font-weight:600;font-size:17px;position:relative;color:#fff}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"";position:absolute;right:6px;top:50%;width:11px;height:11px;border-right:2px solid var(--pink);border-bottom:2px solid var(--pink);transform:translateY(-70%) rotate(45deg);transition:transform .2s}
.faq details[open] summary::after{transform:translateY(-30%) rotate(-135deg)}
.faq .a{padding:0 0 22px;color:var(--muted);font-size:16px;max-width:760px}

.chips{display:flex;flex-wrap:wrap;gap:10px}
.chips span,.chips a{padding:7px 14px;border:1px solid var(--line-2);border-radius:999px;font-size:14px;font-weight:500;color:var(--pink);background:var(--brand-soft)}
.chips a:hover{border-color:var(--pink);color:#fff}
.tl{display:grid;gap:16px}
.tl .card{display:grid;grid-template-columns:180px 1fr;gap:24px}
.tl .when{font-weight:600;color:var(--cyan);font-size:14px}
.sub{font-size:18px;font-weight:600;margin:40px 0 14px;color:#fff}

.book{display:flex;gap:20px}
.cover{flex:none;width:86px;height:120px;border-radius:4px 8px 8px 4px;padding:10px;display:flex;align-items:flex-end;font-size:11px;font-weight:700;line-height:1.2;color:var(--bg);background:linear-gradient(160deg,var(--cyan),var(--violet) 60%,var(--pink));box-shadow:5px 5px 0 rgba(170,129,255,.2)}
.cover.b{background:linear-gradient(160deg,var(--violet),var(--cyan))}
.cover.c{background:linear-gradient(160deg,var(--pink),var(--violet))}
.cover.d{background:linear-gradient(160deg,var(--card-2),#3a4380);color:var(--ink)}

.eco{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.eco a{display:flex;gap:16px;align-items:flex-start;background:var(--card);border:1px solid var(--line);border-radius:var(--r);padding:20px 22px;transition:border-color .15s,transform .15s}
.eco a:hover{border-color:var(--pink);transform:translateY(-2px)}
.eco img{width:56px;height:56px;border-radius:12px;object-fit:cover;flex:none;border:1px solid var(--line-2)}
.eco b{display:block;font-size:16px;color:#fff}
.eco span{display:block;color:var(--muted);font-size:14px;line-height:1.45;margin-top:2px}
.eco em{display:inline-block;font-style:normal;font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:.05em;color:var(--cyan);background:rgba(87,243,254,.1);padding:2px 8px;border-radius:999px;margin-left:8px;vertical-align:2px}
.eco .d{font-size:13px;color:var(--violet);margin-top:6px}

.band{background:radial-gradient(800px 300px at 50% 0,rgba(205,137,232,.18),transparent 70%),var(--card);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.band .wrap{display:flex;align-items:center;justify-content:space-between;gap:32px;padding-top:56px;padding-bottom:56px;flex-wrap:wrap}
.band h2{margin-bottom:6px}
.band p{color:var(--muted);font-size:17px}

footer{background:var(--navy-3);color:var(--muted);font-size:14px}
footer .top{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:40px;padding-top:56px;padding-bottom:40px}
footer h4{color:#fff;font-size:14px;font-weight:600;margin-bottom:14px}
footer ul{list-style:none;display:grid;gap:9px}
footer a:hover{color:#fff}
footer .about p{margin-top:12px;max-width:340px;line-height:1.55}
footer .bot{border-top:1px solid var(--line);padding-top:22px;padding-bottom:28px;display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap;font-size:12.5px;color:#7d84ad}

.prose{max-width:860px}
.prose p{margin-bottom:14px;color:var(--ink-2);font-size:15px}
.prose h3{margin-top:26px}

@media (max-width:1360px){.logo small{display:none}}
@media (max-width:1180px){
  .mainnav{display:none}
  .burger{display:inline-flex}
  .hdr .cta .btn{display:none}
  .hdr.open .mainnav{display:flex;position:absolute;top:72px;left:0;right:0;flex-direction:column;align-items:stretch;background:var(--bg);border-bottom:1px solid var(--line);padding:10px 16px 18px;max-height:calc(100vh - 72px);overflow-y:auto}
  .hdr.open .mainnav>a,.hdr.open .dd-b{padding:12px;width:100%;justify-content:space-between}
  .dd-m{position:static;width:auto;box-shadow:none;grid-template-columns:1fr;margin-top:4px}
  .hero .wrap,.split{grid-template-columns:1fr;gap:40px}
  .g4{grid-template-columns:repeat(2,1fr)}
  .g3,.cfg,.cfg.n4,.eco{grid-template-columns:1fr 1fr}
  footer .top{grid-template-columns:1fr 1fr}
}
@media (max-width:720px){
  .wrap{padding:0 16px}
  .hdr .wrap{gap:12px}
  .logo small{display:none}
  section{padding:56px 0}
  .hero .wrap{padding-top:44px;padding-bottom:44px}
  .g2,.g3,.g4,.cfg,.cfg.n4,.eco{grid-template-columns:1fr}
  .stats{grid-template-columns:1fr}
  .stat{border-right:0;border-bottom:1px solid var(--line)}
  .stat:last-child{border-bottom:0}
  .tl .card{grid-template-columns:1fr;gap:6px}
  .spec th{width:42%}
  .band .wrap{flex-direction:column;align-items:flex-start}
  footer .top{grid-template-columns:1fr}
}
"""

JS = r"""
(function(){
  var h=document.querySelector('.hdr'),b=document.querySelector('.burger');
  if(b)b.addEventListener('click',function(){h.classList.toggle('open');b.setAttribute('aria-expanded',h.classList.contains('open'))});
  document.querySelectorAll('.mainnav>a').forEach(function(a){a.addEventListener('click',function(){h.classList.remove('open')})});
  var dd=document.querySelector('.dd'),db=document.querySelector('.dd-b');
  if(dd&&db){
    db.addEventListener('click',function(e){e.stopPropagation();dd.classList.toggle('open');db.setAttribute('aria-expanded',dd.classList.contains('open'))});
    document.addEventListener('click',function(e){if(!dd.contains(e.target))dd.classList.remove('open')});
    document.addEventListener('keydown',function(e){if(e.key==='Escape')dd.classList.remove('open')});
  }
  document.querySelectorAll('[data-setlang]').forEach(function(a){a.addEventListener('click',function(){try{localStorage.setItem('cc-lang',a.getAttribute('data-setlang'))}catch(e){}})});
  try{
    var saved=localStorage.getItem('cc-lang'),lang=document.documentElement.lang;
    if(!saved&&lang==='en'&&/^(ru|uk|be|kk)/i.test(navigator.language||'')){
      var alt=document.querySelector('link[rel=alternate][hreflang=ru]');
      if(alt){localStorage.setItem('cc-lang','ru');location.replace(alt.href);}
    }
  }catch(e){}
  var y=document.getElementById('yr'); if(y)y.textContent=new Date().getFullYear();
})();
"""


# ---------------------------------------------------------------- строительные блоки
def T(lang, en, ru):
    return ru if lang == 'ru' else en


def btn(href, text, kind='p', ic=None, ext=False, sm=False):
    attrs = ' target="_blank" rel="noopener"' if ext else ''
    i = icon(ic, 18) if ic else ''
    return f'<a class="btn btn-{kind}{" btn-sm" if sm else ""}" href="{href}"{attrs}>{i}{text}</a>'


def tg_btn(lang, kind='p', text=None, sm=False):
    return btn(TG, text or T(lang, 'Message us on Telegram', 'Написать в Telegram'), kind, 'send', ext=True, sm=sm)


def mail_btn(lang, subject='', kind='s', text=None, sm=False):
    from urllib.parse import quote
    href = f'mailto:{MAIL}' + (f'?subject={quote(subject)}' if subject else '')
    return btn(href, text or MAIL, kind, 'mail', sm=sm)


def section(inner, sid='', alt=False, head=None, center=False):
    h = ''
    if head:
        title, sub = head
        h = f'<div class="sh{" c" if center else ""}"><h2>{title}</h2>' + (f'<p>{sub}</p>' if sub else '') + '</div>'
    return f'<section{f" id={sid!r}" if sid else ""}{" class=alt" if alt else ""}><div class="wrap">{h}{inner}</div></section>'


def features(items, cols=3):
    out = ''.join(f'<div class="feat"><div class="ic">{icon(i)}</div><h3>{t}</h3><p>{d}</p></div>' for i, t, d in items)
    return f'<div class="g{cols}">{out}</div>'


def tiers(lang, items, subject, guide=TG):
    out = []
    for it in items:
        lis = ''.join(f'<li>{icon("check", 18)}<span>{x}</span></li>' for x in it['list'])
        img = f'<div class="ti"><img src="{it["img"]}" alt="" loading="lazy"></div>' if it.get('img') else ''
        badge = f'<span class="badge">{it["badge"]}</span>' if it.get('badge') else ''
        if it.get('free'):
            b = btn(guide, T(lang, 'Open the guide', 'Открыть инструкцию'), 's', 'book', ext=True)
        else:
            b = btn(it.get('href', TG), it.get('cta') or T(lang, 'Order in Telegram', 'Заказать в Telegram'), 'p' if it.get('badge') else 's', 'send', ext=True)
        out.append(
            f'<div class="tier{" pop" if it.get("badge") else ""}{" free-t" if it.get("free") else ""}">{badge}{img}<h3>{it["name"]}</h3>'
            f'<p class="d">{it["desc"]}</p><div class="price">{it["price"]}</div><div class="pnote">{it.get("note", "")}</div>'
            f'<ul>{lis}</ul><div class="btns">{b}</div></div>')
    from urllib.parse import quote
    subject = quote(subject)
    fine = T(lang, f'Prices in USD. Shipping and taxes are calculated individually. Questions: <a class="link" href="mailto:{MAIL}?subject={subject}">{MAIL}</a>',
             f'Цены в долларах США. Доставка и налоги считаются отдельно. Вопросы: <a class="link" href="mailto:{MAIL}?subject={subject}">{MAIL}</a>')
    note = T(lang, '<b>The guide is free.</b> CakesCats is a non-profit project. Everything we sell can be built yourself with our open guide on GitHub. '
                   'Buying a ready-made device or individual support helps the project keep going.',
             '<b>Инструкция бесплатна.</b> CakesCats — некоммерческий проект. Всё, что мы продаём, можно собрать самому по открытой инструкции на GitHub. '
             'Покупая готовое устройство или индивидуальную поддержку, вы помогаете проекту работать дальше.')
    gbtn = btn(guide, T(lang, 'Guide on GitHub', 'Инструкция на GitHub'), 's', 'book', ext=True, sm=True)
    return (f'<div class="np">{icon("heart")}<p>{note}</p>{gbtn}</div>'
            f'<div class="cfg n{len(items)}">{"".join(out)}</div><p class="fine">{fine}</p>')


def spec(rows):
    r = ''.join(f'<tr><th>{k}</th><td>{v}</td></tr>' for k, v in rows)
    return f'<div class="spec-wrap"><table class="spec">{r}</table></div>'


def faq(items):
    return '<div class="faq">' + ''.join(f'<details><summary>{q}</summary><div class="a">{a}</div></details>' for q, a in items) + '</div>'


def eco(lang, cur, root):
    cards = []
    for k in ORDER:
        name, desc = ECO[k]
        here = f'<em>{T(lang, "You are here", "Вы здесь")}</em>' if k == cur else ''
        href = url(k) + ('ru/' if lang == 'ru' else '')
        cards.append(f'<a href="{href}"><img src="{root}assets/img/th-{k}.webp" alt="" width="56" height="56" loading="lazy"><div><b>{name[lang]}{here}</b>'
                     f'<span>{desc[lang]}</span><span class="d">{SITES[k]["domain"]}</span></div></a>')
    return section(f'<div class="eco">{"".join(cards)}</div>', 'ecosystem', alt=True,
                   head=(T(lang, 'The CakesCats family', 'Экосистема CakesCats'),
                         T(lang, "All our sites and products.", "Все наши сайты и продукты.")))


def band(lang, title, sub, subject=''):
    from urllib.parse import quote
    subject = quote(subject)
    return (f'<div class="band" id="contact"><div class="wrap"><div><h2>{title}</h2><p>{sub}</p></div>'
            f'<div class="btns">{tg_btn(lang)}{btn("mailto:" + MAIL + ("?subject=" + subject if subject else ""), MAIL, "l", "mail")}</div></div></div>')


# ---------------------------------------------------------------- страница
def page(key, lang, paths, title, desc, nav, body, root, noindex=False):
    """paths = (путь EN-версии, путь RU-версии) относительно корня сайта."""
    s = SITES[key]
    base = url(key)
    en_url, ru_url = base + paths[0], base + paths[1]
    canonical = ru_url if lang == 'ru' else en_url
    dd_links = ''.join(
        f'<a href="{url(k)}{"ru/" if lang == "ru" else ""}"><img src="{root}assets/img/th-{k}.webp" alt="" width="44" height="44"><div><b>{ECO[k][0][lang]}'
        f'{"<em>" + T(lang, "here", "вы здесь") + "</em>" if k == key else ""}</b><span>{ECO[k][1][lang]}</span></div></a>' for k in ORDER)
    chev = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>'
    dd = (f'<div class="dd"><button class="dd-b" type="button" aria-expanded="false">{T(lang, "CakesCats sites", "Сайты CakesCats")}{chev}</button>'
          f'<div class="dd-m">{dd_links}</div></div>')
    navh = ''.join(f'<a href="{h}">{t}</a>' for t, h in nav)
    lang_sw = (f'<span class="lang"><a href="{en_url}" data-setlang="en"{" class=on" if lang == "en" else ""}>EN</a>'
               f'<a href="{ru_url}" data-setlang="ru"{" class=on" if lang == "ru" else ""}>RU</a></span>')
    prod_links = ''.join(f'<li><a href="{url(k)}{"ru/" if lang == "ru" else ""}">{ECO[k][0][lang]}</a></li>' for k in ['os', 'phone', 'vpn', 'llm'])
    co_links = ''.join(f'<li><a href="{url(k)}{"ru/" if lang == "ru" else ""}">{ECO[k][0][lang]}</a></li>' for k in ['home', 'main'])
    co_links += f'<li><a href="{url("main")}{"ru/" if lang == "ru" else ""}insights/">{T(lang, "Security insights", "Материалы о безопасности")}</a></li>'
    co_links += f'<li><a href="{GITHUB}/guides" target="_blank" rel="noopener">{T(lang, "Free setup guides", "Бесплатные инструкции")}</a></li>'
    co_links += f'<li><a href="{GITHUB}" target="_blank" rel="noopener">GitHub</a></li>'
    privacy = f'{root}privacy/'
    robots = '<meta name="robots" content="noindex">' if noindex else ''
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{ESC(title)}</title>
<meta name="description" content="{ESC(desc)}">
{robots}<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="alternate" hreflang="ru" href="{ru_url}">
<meta property="og:title" content="{ESC(title)}">
<meta property="og:description" content="{ESC(desc)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<link rel="icon" href="{root}assets/img/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/site.css?v=9">
</head>
<body>
<header class="hdr"><div class="wrap">
<a class="logo" href="{root}{"ru/" if lang == "ru" else ""}"><img src="{root}assets/img/logo.png" alt="">{s["name"]}<small>{s["sub"][lang]}</small></a>
<nav class="mainnav" aria-label="{T(lang, "Main", "Основное")}">{navh}{dd}</nav>
<div class="cta">{lang_sw}{btn(TG, T(lang, "Contact us", "Связаться"), "p", None, ext=True, sm=True)}</div>
<button class="burger" aria-label="{T(lang, "Menu", "Меню")}" aria-expanded="false">{icon("menu")}</button>
</div></header>
<main>
{body}
</main>
<footer><div class="wrap top">
<div class="about"><a class="logo" href="{url("main")}"><img src="{root}assets/img/logo.png" alt="">CakesCats</a>
<p>{T(lang, "Privacy products, local AI and consulting. Open source at heart: everything we build can be assembled yourself for free.", "Продукты для приватности, локальный ИИ и консалтинг. В основе — открытый код: всё, что мы делаем, можно собрать самому бесплатно.")}</p></div>
<div><h4>{T(lang, "Products", "Продукты")}</h4><ul>{prod_links}</ul></div>
<div><h4>{T(lang, "Company", "Компания")}</h4><ul>{co_links}</ul></div>
<div><h4>{T(lang, "Contact", "Контакты")}</h4><ul><li><a href="{TG}" target="_blank" rel="noopener">Telegram @cakescats</a></li><li><a href="mailto:{MAIL}">{MAIL}</a></li><li><a href="{privacy}">{T(lang, "Privacy &amp; cookie policy", "Политика конфиденциальности")}</a></li></ul></div>
</div>
<div class="wrap bot"><span>© <span id="yr">2026</span> CakesCats · {LEGAL}</span><span>{T(lang, "This site does not use tracking cookies.", "Этот сайт не использует отслеживающие cookie.")}</span></div>
</footer>
<script src="{root}assets/site.js?v=3" defer></script>
</body>
</html>
'''
