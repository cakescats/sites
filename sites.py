"""Содержимое всех сайтов CakesCats (EN/RU)."""
import os
from lib import *


def L(lang):
    return lambda en, ru: T(lang, en, ru)


def ru(lang):
    return 'ru/' if lang == 'ru' else ''


# =====================================================================================
# cakescats.com — консалтинг
# =====================================================================================
def home(lang, root):
    t = L(lang)
    hero = f'''<div class="hero"><div class="wrap">
<div><span class="eyebrow">{t("Crisis · PR · Technology", "Антикризис · PR · Технологии")}</span>
<h1>{t("Crisis communications and reputation for technology companies", "Антикризисные коммуникации и репутация для технологических компаний")}</h1>
<p class="lead">{t("When something goes wrong — an incident, an outage or a wave of bad press — I cover both sides: the technical investigation and how people talk about it. In calmer times I get companies into top-tier media and bring in AI where it makes money.",
"Когда что-то идёт не так — инцидент, сбой или волна негатива, — я закрываю обе стороны: техническое расследование и то, как об этом говорят. В спокойное время вывожу компании в ведущие СМИ и внедряю ИИ там, где он приносит деньги.")}</p>
<div class="btns">{tg_btn(lang, text=t("Discuss your task", "Обсудить задачу"))}{btn("#cases", t("See cases", "Смотреть кейсы"), "s")}</div>
<div class="trust"><span>{icon("briefcase", 18)}MBA</span><span>{icon("book", 18)}{t("Author of 3 books", "Автор 3 книг")}</span><span>{icon("megaphone", 18)}{t("KP expert", "Эксперт КП")} · Forbes · {t("Xakep", "«Хакер»")}</span></div></div>
<div class="portrait"><img src="{root}assets/img/photo.jpg" alt="Cakes Cats" width="320" height="320"></div>
</div></div>'''

    stats = f'''<section style="padding:40px 0 0"><div class="wrap"><div class="stats">
<div class="stat"><b>15+</b><span>{t("years in management: from IT specialist to C-level", "лет в управлении: от IT-специалиста до C-level")}</span></div>
<div class="stat"><b>5</b><span>{t("years of commercial AI projects", "лет коммерческих проектов с ИИ")}</span></div>
<div class="stat"><b>3</b><span>{t("books on AI agents, digital safety and communications", "книги об ИИ-агентах, цифровой безопасности и коммуникациях")}</span></div>
</div></div></section>'''

    services = section(features([
        ('shield', t("Crisis communications", "Антикризисные коммуникации"),
         t("Get through a crisis without reputational damage: situation assessment, your position, communication with clients, partners and the press, handling negative coverage.",
           "Пройти кризис без потерь для репутации: оценка ситуации, позиция компании, общение с клиентами, партнёрами и прессой, работа с негативным фоном.")),
        ('megaphone', t("PR & media support", "PR и медиасопровождение"),
         t("Placement in Tier 1 media for companies and their leaders, turnkey personal support — clients don't spend their own time on it.",
           "Публикации в СМИ первого эшелона для компаний и их руководителей, персональное сопровождение под ключ — без затрат времени клиента.")),
        ('cpu', t("AI agents & GenAI", "ИИ-агенты и GenAI"),
         t("Designing and deploying AI agents, local LLMs and generative AI in your processes — with the costs under control.",
           "Проектирование и внедрение ИИ-агентов, локальных LLM и генеративного ИИ в процессы компании — с контролем расходов.")),
        ('compass', t("Strategy & technology consulting", "Стратегия и технологический консалтинг"),
         t("Fractional C-level and strategic advice: 0-to-1 launches, unit economics, IT processes, incident analysis, digital hygiene for teams.",
           "Fractional C-level и стратегический совет: запуск с нуля, юнит-экономика, IT-процессы, разбор инцидентов, цифровая гигиена для команды.")),
    ], cols=4), 'services', head=(t("Services", "Услуги"), t("Communications, business and technology for companies whose reputation is at stake.", "Коммуникации, бизнес и технологии для компаний, у которых на кону репутация.")))

    def case(tag, title, text, items=None, link=None):
        ul = '<ul>' + ''.join(f'<li>{icon("check", 18)}<span>{x}</span></li>' for x in items) + '</ul>' if items else ''
        lk = f'<a class="link" href="{link[0]}" target="_blank" rel="noopener">{link[1]} {icon("arrow", 16)}</a>' if link else ''
        return f'<div class="card"><span class="tag">{tag}</span><h3>{title}</h3><p>{text}</p>{ul}{lk}</div>'

    cases = section('<div class="g3">' + ''.join([
        case(t("Crisis PR", "Антикризисный PR"), t("Turning bad press into new clients", "Из негатива — в новых клиентов"),
             t("Helping companies weather a wave of negative coverage and turn it to their advantage: growing trust and inbound leads instead of churn.",
               "Помогаю компаниям пережить волну негативных публикаций и обратить её себе на пользу: рост доверия и входящие заявки вместо оттока клиентов."),
             [t("Media landscape analysis and response strategy", "Анализ информационного фона и стратегия ответа"),
              t("Reframing the negative agenda", "Переработка негативной повестки в позитивную"),
              t("Placement in Tier 1 media", "Вывод компании в СМИ первого эшелона")]),
        case(t("Media & marketing", "Медиа и маркетинг"), t("Turnkey personal support", "Персональное сопровождение под ключ"),
             t("Personal support in marketing and public relations. My clients' companies have been featured in Forbes without any effort on their part.",
               "Индивидуальное ведение в маркетинге и публичном поле. Компании моих клиентов получали упоминания в Forbes без их собственного участия.")),
        case(t("Jan — Jun 2026", "Январь — июнь 2026"), t("Fractional C-level at an AI startup", "Fractional C-level в ИИ-стартапе"),
             t("Guided a fast-growing generative AI and infrastructure startup through its 0-to-1 launch.",
               "Вёл быстрорастущий стартап в генеративном ИИ и инфраструктуре через запуск с нуля."),
             [t("Financial discipline in AI spending", "Финансовая дисциплина в расходах на ИИ"),
              t("Product architecture aligned with unit economics (CAC/LTV)", "Архитектура продукта связана с юнит-экономикой (CAC/LTV)"),
              t("The right moment to go to market", "Правильный момент выхода на рынок")]),
        case(t("Incident analysis", "Разбор инцидентов"), t("Calmly finding out what happened", "Спокойно разобраться, что произошло"),
             t("From the first call to closure: reconstructing events, preserving data for follow-up, coordinating the team and everyone involved.",
               "От первого звонка до закрытия: восстановление картины событий, сохранение данных для разбирательства, координация команды и всех участников."),
             [t("Log analysis and event timeline", "Анализ журналов и хронология событий"),
              t("Digital evidence collection (DFIR)", "Сбор цифровых данных (DFIR)"),
              t("Client communications all the way", "Коммуникации с клиентом на всём пути")]),
        case(t("AI · 2026", "ИИ · 2026"), t("A 125B-parameter model on a laptop", "Модель на 125 млрд параметров на ноутбуке"),
             t("An inference-engine fork with fixes, speed-ups, Russian UI and authentication. A modern large model runs locally — company data stays in the company.",
               "Форк движка инференса: исправления, ускорение, русский интерфейс и авторизация. Большая современная модель работает локально — данные остаются в компании."),
             link=(GITHUB + '/QwFNfer-Secure-Multilang', t("Code on GitHub", "Код на GitHub"))),
        case(t("AI agents", "ИИ-агенты"), t("An AI agent in Telegram", "ИИ-агент в Telegram"),
             t("A Telegram interface for an AI agent on a local model: live progress and confirmation before important actions.",
               "Telegram-интерфейс для ИИ-агента на локальной модели: ход работы в реальном времени и подтверждение важных действий."),
             link=(GITHUB + '/opencode-telegram-slow-llm', t("Code on GitHub", "Код на GitHub"))),
    ]) + '</div>', 'cases', alt=True, head=(t("Selected cases", "Избранные кейсы"), None))

    def book(cls, cover, when, title, text, link=None):
        lk = f'<a class="link" href="{link}" target="_blank" rel="noopener" style="margin-top:10px">{t("About the book", "О книге")} {icon("arrow", 16)}</a>' if link else ''
        return f'<div class="card book"><div class="cover {cls}">{cover}</div><div><span class="tag">{when}</span><h3>{title}</h3><p>{text}</p>{lk}</div></div>'

    books = section('<div class="g2">' + ''.join([
        book('', t("AI Agent Development", "Разработка ИИ-агентов"), t("New book", "Новая книга"), t("“AI Agent Development”", "«Разработка ИИ-агентов»"),
             t("How to design, launch and control AI agents — and understand what your agent is really doing.", "Как проектировать, запускать и контролировать ИИ-агентов — и понимать, что на самом деле делает ваш агент.")),
        book('b', t("Communications in a New Era", "Коммуникации в новом времени"), t("Co-author · 2024", "Соавтор · 2024"), t("“Communications in a New Era”", "«Коммуникации в новом времени»"),
             t("Advice from leading PR specialists on digital communications, media and social networks. Features my case.", "Советы ведущих PR-специалистов о цифровых коммуникациях, СМИ и соцсетях. В книге представлен мой кейс."),
             'https://www.litres.ru/book/adel-zamalutdniov/kommunikacii-v-novom-vremeni-71340895/'),
        book('c', t("Digital Immunity", "Цифровой иммунитет"), t("Bombora · 2025", "Бомбора · 2025"), t("“Digital Immunity”", "«Цифровой иммунитет»"),
             t("A practical guide to digital hygiene: using technology calmly and confidently.", "Практическое руководство по цифровой гигиене: как спокойно и уверенно пользоваться технологиями."),
             'https://eksmo.ru/book/kiberbezopasnost-i-informatsionnaya-gigiena-ITD1392994/'),
        book('d', t("Publishing Python Packages", "Публикация пакетов Python"), t("Bombora · 2024", "Бомбора · 2024"), t("Dane Hillard, “Publishing Python Packages”", "Дейн Хиллард, «Публикация пакетов Python»"),
             t("Cover review for the Russian edition.", "Рецензия на обложке русского издания.")),
    ]) + '</div>', 'books', head=(t("Books", "Книги"), None))

    tl = [
        (t("Jan — Jun 2026", "Янв — июн 2026"), "AI &amp; Ecosystem Fractional C-Level &amp; Strategic Advisor",
         t("AI startup (GenAI and infrastructure): strategy, AI cost discipline, unit economics, fundraising.", "ИИ-стартап (GenAI и инфраструктура): стратегия, дисциплина расходов на ИИ, юнит-экономика, инвестиции.")),
        (t("2023 — present", "2023 — сейчас"), t("Founder, CakesCats", "Основатель, CakesCats"),
         t("Crisis communications and support for executives and companies; products for privacy and local AI.", "Антикризисные коммуникации и поддержка руководителей и компаний; продукты для приватности и локального ИИ.")),
        (t("15+ years", "15+ лет"), t("Fintech: from IT specialist to C-level", "Финтех: от IT-специалиста до C-level"),
         t("Managing business, teams and IT projects for banks, telecom operators and large companies.", "Управление бизнесом, командами и IT-проектами для банков, телеком-операторов и крупных компаний.")),
    ]
    tlh = '<div class="tl">' + ''.join(f'<div class="card"><span class="when">{w}</span><div><h3>{h}</h3><p>{p}</p></div></div>' for w, h, p in tl) + '</div>'
    media = [(t("KP expert", "Эксперт КП"), 'https://www.kp.ru/edu/spetsialisty/anton-shustikov/'), ('Forbes', None), (t("Xakep", "«Хакер»"), None),
             (t("Izvestia", "Известия"), 'https://iz.ru/1633388/alena-svetunkova/vyiti-na-sled-kak-poznakomit-rebenka-s-osnovami-tcifrovoi-gramotnosti'),
             (t("Sistemny Administrator", "«Системный администратор»"), 'https://samag.ru/archive/article/4839'),
             ('SecurityMedia', 'https://securitymedia.org/info/nevidimaya-svyaz-kak-proiskhodit-vzlom-wi-fi-i-kak-ot-nego-zashchititsya.html'),
             ('CoinsPaid Media', 'https://coinspaidmedia.com/forecasts/top-2024-trends-web3/'),
             ('crypto.ru', 'https://crypto.ru/eksklyuziv-kriptomoshenniki-ai/'),
             ('block-chain24', 'https://www.block-chain24.com/articles/dipfeyki-palka-o-dvuh-koncah-tehnologiy')]
    mh = '<div class="chips">' + ''.join(f'<a href="{u}" target="_blank" rel="noopener">{n}</a>' if u else f'<span>{n}</span>' for n, u in media) + '</div>'
    skills = '<div class="chips">' + ''.join(f'<span>{x}</span>' for x in ["Crisis Communications", "PR", "Media Relations", "ORM", "Marketing", "AI Agents", "GenAI / LLM", "Fractional C-level", "IT Strategy", "Unit Economics", "FinTech", "DFIR", "MBA"]) + '</div>'
    exp = section(tlh + f'<div class="sub">{t("Publications &amp; media", "Публикации и СМИ")}</div>{mh}<div class="sub">{t("Skills", "Компетенции")}</div>{skills}',
                  'experience', alt=True, head=(t("Experience", "Опыт"), None))

    oss = section('<div class="g4">' + ''.join(
        f'<a class="card" href="{GITHUB}/{repo}" target="_blank" rel="noopener"><span class="tag">{tag}</span><h3>{name}</h3><p>{d}</p><span class="link">GitHub {icon("arrow", 16)}</span></a>'
        for repo, tag, name, d in [
            ('QwFNfer-Secure-Multilang', 'C++ · LLM', 'QwFNfer Secure Multilang', t("Runs a 125B-parameter model on a single 16 GB GPU: measured fixes, sign-in, API key, EN/RU UI.", "Модель на 125 млрд параметров на одной видеокарте 16 ГБ: исправления с замерами, вход, API-ключ, интерфейс EN/RU.")),
            ('opencode-telegram-slow-llm', 'TypeScript · AI agents', 'opencode-telegram-slow-llm', t("A Telegram bridge for the opencode agent, built for unhurried local models.", "Telegram-мост для агента opencode, рассчитанный на неторопливые локальные модели.")),
            ('airborn-IOS-CVE-2025-24252', 'DFIR · iOS', 'Airborne Log Extractor', t("Checks an iPhone's system logs (LogArchive) for signs of a known AirPlay issue, CVE-2025-24252.", "Проверяет системные журналы iPhone (LogArchive) на признаки известной проблемы AirPlay, CVE-2025-24252.")),
            ('qwen3.8-125b-q4-expert-repacker', 'C++ · LLM', 'Qwen 125B Expert Repacker', t("Repacks a large MoE model so each part is read from disk in one request: +10% read speed.", "Перепаковывает большую MoE-модель для чтения с диска одним запросом: +10% к скорости чтения.")),
        ]) + '</div>', 'opensource', head=(t("Open source", "Open source"), t("Tools I build for my own work and share with everyone.", "Инструменты, которые я делаю для своей работы и выкладываю для всех.")))

    vol = section('<div class="g4">' + ''.join(f'<div class="card"><span class="tag">{w}</span><h3>{h}</h3><p>{p}</p>{x}</div>' for w, h, p, x in [
        (t("Since 2023", "С 2023 года"), t("CakesCats non-profit", "Некоммерческий проект CakesCats"),
         t("Bridging the digital divide: free materials and simple digital-hygiene tools for people in difficult situations.", "Сокращаю цифровой разрыв: бесплатные материалы и простые инструменты цифровой гигиены для людей в сложных ситуациях."), ''),
        (t("Since 2024", "С 2024 года"), t("Journal reviewer", "Рецензент журнала"),
         t("Journal Cybernetics and Physics (CAP): reviewing manuscripts, methodology and data.", "Journal Cybernetics and Physics (CAP): рецензирую рукописи, методологию и данные."),
         '<div class="chips" style="margin-top:14px"><a href="http://cap.physcon.ru/" target="_blank" rel="noopener">cap.physcon.ru</a></div>'),
        (t("Helping companies", "Помощь компаниям"), t("Acknowledged by", "Благодарности"),
         t("Reporting issues in products to their makers so they can fix them.", "Сообщаю компаниям о найденных ошибках в продуктах, чтобы они могли их исправить."),
         '<div class="chips" style="margin-top:14px"><a href="https://accenture.responsibledisclosure.com/hc/en-us/articles/360040573233/" target="_blank" rel="noopener">Accenture · 2025</a><span>Telegram · 2024</span><span>Volla · 2022</span></div>'),
        (t("Education", "Просвещение"), t("Digital literacy for everyone", "Цифровая грамотность для всех"),
         t("Plain-language advice: home Wi-Fi, digital literacy for children, spotting deepfakes.", "Простым языком: домашний Wi-Fi, цифровая грамотность для детей, как распознать дипфейк."), ''),
    ]) + '</div>', 'volunteering', head=(t("Volunteering &amp; community", "Волонтёрство и сообщество"), t("What I do pro bono.", "Что я делаю безвозмездно.")))

    prods = section(product_cards(lang, root), 'products', alt=False,
                    head=(t("CakesCats products", "Продукты CakesCats"), NONPROFIT[lang]))
    body = hero + stats + services + cases + prods + oss + books + exp + vol + eco(lang, 'home', root) + band(
        lang, t("Let's talk", "Давайте поговорим"), t("A crisis, PR, AI adoption or strategy. I reply personally.", "Кризис, PR, внедрение ИИ или стратегия. Отвечаю лично."))
    nav = [(t("Services", "Услуги"), '#services'), (t("Cases", "Кейсы"), '#cases'),
           (t("Products", "Продукты"), '#products'), (t("Books", "Книги"), '#books'), (t("Experience", "Опыт"), '#experience')]
    return (t("Cakes Cats — crisis communications, PR and AI consulting", "Cakes Cats — антикризисные коммуникации, PR и ИИ"),
            t("Crisis communications and reputation for technology companies, PR and media support, AI agents and strategy. Author of books on AI agents and digital safety.",
              "Антикризисные коммуникации и репутация для технологических компаний, PR и медиасопровождение, ИИ-агенты и стратегия. Автор книг об ИИ-агентах и цифровой безопасности."),
            nav, body)


# =====================================================================================
# main.cakescats.com — продуктовая линейка
# =====================================================================================
PRICES = {
    'os': '$990', 'phone': '$1,490', 'vpn': '$990', 'llm': '$9,900',
}


NONPROFIT = {
    'en': "CakesCats is a non-profit project: every product is open source and can be downloaded for free or built yourself from our step-by-step guide. You pay only for hardware, setup and support — and that funds the project.",
    'ru': "CakesCats — некоммерческий проект: каждый продукт открыт, его можно бесплатно скачать или собрать самому по нашей инструкции. Платите вы только за оборудование, настройку и поддержку — это и поддерживает проект.",
}

PRODUCTS = [
    ('phone', 'phone-fold', ("Google Pixel with GrapheneOS, private apps and isolated profiles — configured and ready.", "Google Pixel с GrapheneOS, приватными приложениями и изолированными профилями — настроен и готов.")),
    ('vpn', 'router', ("A plug-and-play router with a dedicated V2Ray server and a separate private Wi-Fi network.", "Роутер «включил и работает» с выделенным сервером V2Ray и отдельной приватной Wi-Fi-сетью.")),
    ('os', 'mac-hero', ("An isolated virtual workspace for Macs with Apple silicon, with encrypted storage and Tor routing.", "Изолированная виртуальная среда для Mac на Apple silicon с шифрованным хранилищем и маршрутизацией через Tor.")),
    ('llm', 'llm-card', ("A private AI appliance: chat, documents and automation on your premises, with no cloud.", "Приватный ИИ-сервер: чат, документы и автоматизация у вас, без облака.")),
]


def product_cards(lang, root, exclude=None):
    t = L(lang)
    cards = []
    for k, img, (den, dru) in PRODUCTS:
        if k == exclude:
            continue
        cards.append(f'<a class="card prod" href="{url(k)}{ru(lang)}"><div class="pi"><img src="{root}assets/img/{img}.webp" alt="" loading="lazy"></div>'
                     f'<div class="pb"><h3>{ECO[k][0][lang]}</h3><p>{t(den, dru)}</p><div class="from">{t("Ready-made from", "Готовое решение от")} <b>{PRICES[k]}</b></div>'
                     f'<div class="free">{icon("heart", 16)}{t("Free to download or build from the guide", "Бесплатно: скачать или собрать по инструкции")}</div>'
                     f'<span class="link" style="margin-top:12px">{t("Learn more", "Подробнее")} {icon("arrow", 16)}</span></div></a>')
    return f'<div class="g{len(cards)}">{"".join(cards)}</div>'


def other_products(lang, root, key):
    t = L(lang)
    return section(product_cards(lang, root, exclude=key), 'products',
                   head=(t("Other CakesCats products", "Другие продукты CakesCats"), NONPROFIT[lang]))


def main(lang, root):
    t = L(lang)
    hero = f'''<div class="hero"><div class="wrap">
<div><span class="eyebrow">{t("Privacy · Local AI · Open source", "Приватность · Локальный ИИ · Open source")}</span>
<h1>{t("Privacy devices and private AI", "Устройства для приватности и локальный ИИ")}</h1>
<p class="lead">{t("CakesCats builds ready-to-use devices for private work: a protected phone, a private network, an isolated workspace for Mac and AI that runs on your premises. Everything is built on open source — you can assemble it yourself for free, or get it set up and supported by us.",
"CakesCats делает готовые устройства для приватной работы: защищённый телефон, приватную сеть, изолированную среду для Mac и ИИ, который работает у вас. Всё построено на открытом коде — можно собрать самому бесплатно или получить готовое решение с настройкой и поддержкой.")}</p>
<div class="btns">{btn("#products", t("Explore products", "Смотреть продукты"))}{tg_btn(lang, "s", t("Talk to us", "Связаться"))}</div>
<div class="trust"><span>{icon("code", 18)}{t("Open source", "Открытый код")}</span><span>{icon("tool", 18)}{t("Set up for you", "Настройка за вас")}</span><span>{icon("users", 18)}{t("Personal support", "Личная поддержка")}</span></div></div>
<div class="media"><img src="{root}assets/img/brand-banner.webp" alt="" width="1375" height="681"></div>
</div></div>'''

    products = section(product_cards(lang, root), 'products', head=(t("Products", "Продукты"), NONPROFIT[lang]))

    why = section(features([
        ('code', t("Open by design", "Открыто по умолчанию"), t("We use only open-source components trusted by experts. Every build is documented, so you can check it — or assemble it yourself.", "Мы используем только открытые компоненты, которым доверяют эксперты. Каждая сборка задокументирована — её можно проверить или собрать самому.")),
        ('tool', t("Ready to use", "Готово к работе"), t("No configuration on your side: we set everything up, test it and hand it over working.", "Никакой настройки с вашей стороны: мы всё настраиваем, проверяем и передаём работающим.")),
        ('users', t("Direct support", "Прямая поддержка"), t("You talk to the people who built your device — in Telegram or by e-mail.", "Вы общаетесь с теми, кто собирал ваше устройство, — в Telegram или по почте.")),
        ('heart', t("Non-profit roots", "Некоммерческие корни"), t("CakesCats started as an educational project. Buying a device funds open, independent digital-safety tools.", "CakesCats начинался как образовательный проект. Покупка устройства поддерживает открытые и независимые инструменты цифровой безопасности.")),
    ], cols=4), 'why', alt=True, head=(t("Why CakesCats", "Почему CakesCats"), None))

    how = section(f'''<div class="split"><div class="media"><img src="{root}assets/img/mac-desk.webp" alt="" loading="lazy"></div><div>
<h2>{t("Three ways to get started", "Три способа начать")}</h2>
<div class="steps">
<div class="step"><b>1</b><div><h3>{t("Build it yourself — free", "Собрать самому — бесплатно")}</h3><p>{t("Every product has an open step-by-step guide.", "У каждого продукта есть открытая пошаговая инструкция.")} <a class="link" href="{GITHUB}/guides" target="_blank" rel="noopener">{t("Guides on GitHub", "Инструкции на GitHub")}</a></p></div></div>
<div class="step"><b>2</b><div><h3>{t("We set it up on your hardware", "Настроим на вашем оборудовании")}</h3><p>{t("A specialist configures your device remotely and checks everything works.", "Специалист настроит ваше устройство удалённо и проверит, что всё работает.")}</p></div></div>
<div class="step"><b>3</b><div><h3>{t("Turnkey device", "Готовое устройство")}</h3><p>{t("Get a fully configured device with support — switch it on and use it.", "Получите полностью настроенное устройство с поддержкой — включите и пользуйтесь.")}</p></div></div>
</div></div></div>''', 'how')

    ins = section('<div class="g3">' + ''.join(
        f'<a class="card" href="{root}{ru(lang)}insights/#{a}"><span class="tag">{tag}</span><h3>{h}</h3><p>{p}</p><span class="link">{t("Read", "Читать")} {icon("arrow", 16)}</span></a>'
        for a, tag, h, p in [
            ('triangulation', 'iOS · 2023', t("Operation Triangulation", "Операция «Триангуляция»"), t("How a zero-click iMessage chain was used to spy on iPhones — and what it teaches about updates.", "Как цепочка атак через iMessage без участия пользователя использовалась для слежки за iPhone — и чему это учит.")),
            ('notpetya', 'Windows · 2017', 'NotPetya', t("How one malicious update paralysed hundreds of companies in a day.", "Как одно вредоносное обновление за день парализовало сотни компаний.")),
            ('solarwinds', 'Supply chain · 2020', 'SolarWinds', t("When a signed software update becomes the way in — supply-chain risks explained.", "Когда подписанное обновление становится входной дверью — о рисках цепочки поставок.")),
        ]) + '</div>', 'insights', alt=True,
        head=(t("Security insights", "Материалы о безопасности"), t("Real incidents explained in plain language.", "Разборы реальных инцидентов простым языком.")))

    about = section(f'''<div class="split"><div>
<h2>{t("About CakesCats", "О CakesCats")}</h2>
<p class="lead" style="margin-bottom:18px">{t("CakesCats is a team of enthusiasts who believe everyone has the right to privacy and safe access to the internet.", "CakesCats — команда энтузиастов, которые верят, что у каждого есть право на приватность и безопасный доступ в интернет.")}</p>
<p style="color:var(--muted)">{t("Our mission is to make digital safety accessible and understandable. We build ready-to-use solutions that need no technical knowledge, yet provide a high level of protection — and we explain how they work, without fear and without dark patterns.",
"Наша миссия — сделать цифровую безопасность доступной и понятной. Мы делаем готовые решения, которые не требуют технических знаний и при этом дают высокий уровень защиты, — и объясняем, как они работают, без запугивания и скрытых механизмов.")}</p>
</div><div class="g2">
{"".join(f'<div class="card"><h3>{h}</h3><p>{p}</p></div>' for h, p in [
    (t("Freedom first", "Свобода прежде всего"), t("Users should own their data, devices and digital lives.", "Пользователь должен владеть своими данными, устройствами и цифровой жизнью.")),
    (t("Transparency", "Прозрачность"), t("Open technologies, no hidden mechanisms.", "Открытые технологии, никаких скрытых механизмов.")),
    (t("Simplicity", "Простота"), t("Security shouldn't be a luxury for the tech-savvy.", "Безопасность не должна быть роскошью для технарей.")),
    (t("Education over fear", "Знания вместо страха"), t("We explain and teach so you can decide with confidence.", "Мы объясняем и учим, чтобы вы принимали решения уверенно.")),
])}</div></div>''', 'about')

    body = hero + products + why + how + ins + about + eco(lang, 'main', root) + band(
        lang, t("Not sure which product fits?", "Не знаете, что выбрать?"), t("Tell us what you need and we'll suggest a setup and a price.", "Расскажите о задаче, и мы предложим решение и цену."))
    nav = [(t("Products", "Продукты"), '#products'), (t("Why us", "Почему мы"), '#why'), (t("Insights", "Материалы"), '#insights'),
           (t("About", "О нас"), '#about')]
    return (t("CakesCats — privacy devices and private AI", "CakesCats — устройства для приватности и приватный ИИ"),
            t("Ready-to-use privacy devices built on open source: CakesCats Phone, VPN Router, VirtualCatsOS for Mac and LLM EdgeBox private AI.",
              "Готовые устройства для приватности на открытом коде: CakesCats Phone, VPN-роутер, VirtualCatsOS для Mac и приватный ИИ LLM EdgeBox."),
            nav, body)


def insights(lang, root):
    t = L(lang)
    arts = [
        ('triangulation', 'iOS · 2023', t("Operation Triangulation: how iPhones were spied on", "Операция «Триангуляция»: как следили за iPhone"),
         [t("Researchers at Kaspersky uncovered one of the most sophisticated espionage campaigns of recent years. The spyware implant, TriangleDB, was built specifically for iOS.",
            "Исследователи «Лаборатории Касперского» обнаружили одну из самых сложных шпионских кампаний последних лет. Шпионский имплант TriangleDB был создан специально для iOS."),
          t("The victim received an invisible iMessage; a chain of vulnerabilities gave the attackers full control, and the implant lived only in memory — a reboot erased it, so the attackers had to re-infect the device. It could collect files, read the keychain, track location and manage processes, and deleted itself after 30 days.",
            "Жертва получала невидимое сообщение iMessage; цепочка уязвимостей давала атакующим полный контроль, а имплант жил только в памяти — перезагрузка стирала его, и устройство приходилось заражать заново. Он мог собирать файлы, читать связку ключей, отслеживать геолокацию и управлять процессами, а через 30 дней удалял себя."),
          t("<b>Takeaway:</b> install updates promptly, restart your phone regularly and keep sensitive work on hardened devices.",
            "<b>Вывод:</b> своевременно ставьте обновления, регулярно перезагружайте телефон и держите важную работу на защищённых устройствах.")]),
        ('notpetya', 'Windows · 2017', t("NotPetya: one update, hundreds of companies down", "NotPetya: одно обновление — сотни остановленных компаний"),
         [t("On 27 June 2017 a destructive attack spread from a compromised accounting-software update in Ukraine and within hours hit banks, logistics, energy and global brands.",
            "27 июня 2017 года разрушительная атака распространилась через заражённое обновление бухгалтерской программы в Украине и за несколько часов задела банки, логистику, энергетику и мировые бренды."),
          t("It spread on its own using the EternalBlue vulnerability and stolen administrator passwords, encrypted the disk's boot record and showed a ransom note — but the keys were destroyed, so data could not be recovered.",
            "Она распространялась сама, используя уязвимость EternalBlue и украденные пароли администраторов, шифровала загрузочную запись диска и показывала требование выкупа — но ключи уничтожались, и данные восстановить было невозможно."),
          t("<b>Takeaway:</b> patch quickly, separate networks, limit administrator rights and keep offline backups.",
            "<b>Вывод:</b> быстро ставьте исправления, разделяйте сети, ограничивайте права администраторов и храните офлайн-копии данных.")]),
        ('solarwinds', 'Supply chain · 2020', t("SolarWinds: when a trusted update is the way in", "SolarWinds: когда доверенное обновление становится входом"),
         [t("In December 2020 it became known that malicious code had been inserted into official, digitally signed updates of the SolarWinds Orion monitoring platform.",
            "В декабре 2020 года стало известно, что вредоносный код был встроен в официальные подписанные обновления платформы мониторинга SolarWinds Orion."),
          t("The update reached more than 18,000 organisations, including government agencies and major technology companies, and went unnoticed for over nine months.",
            "Обновление получили более 18 000 организаций, включая государственные ведомства и крупные технологические компании, и атака оставалась незамеченной больше девяти месяцев."),
          t("<b>Takeaway:</b> check what your vendors ship, monitor unusual activity after updates, and share information about incidents.",
            "<b>Вывод:</b> проверяйте, что поставляют вендоры, следите за необычной активностью после обновлений и делитесь информацией об инцидентах.")]),
    ]
    topics = [t("Cybersecurity basics", "Основы кибербезопасности"), t("Cyber hygiene &amp; psychology", "Кибергигиена и психология"), t("Digital footprint", "Цифровой след"),
              t("OSINT &amp; data leaks", "OSINT и утечки данных"), t("Social engineering", "Социальная инженерия"), t("How antivirus works", "Как работает антивирус"),
              t("Phishing &amp; scams", "Фишинг и мошенничество"), t("Fakes &amp; info attacks", "Фейки и информационные атаки"), t("Digital anonymity", "Цифровая анонимность"),
              t("Online payment safety", "Безопасность онлайн-платежей"), t("Signs of surveillance", "Признаки слежки"), t("Digital identity", "Цифровая личность")]
    hero = f'''<div class="hero"><div class="wrap" style="grid-template-columns:1fr">
<div><span class="eyebrow">{t("Insights", "Материалы")}</span><h1>{t("Security insights", "Материалы о безопасности")}</h1>
<p class="lead">{t("Real incidents explained in plain language, with practical takeaways.", "Реальные инциденты простым языком — с практическими выводами.")}</p></div></div></div>'''
    arts_h = ''.join(f'<article class="card prose" id="{a}" style="margin-bottom:24px;max-width:none"><span class="tag">{tag}</span><h2 style="font-size:28px">{h}</h2>'
                     + ''.join(f'<p>{p}</p>' for p in ps) + '</article>' for a, tag, h, ps in arts)
    body = (hero + section(arts_h, 'cases')
            + section('<div class="chips">' + ''.join(f'<span>{x}</span>' for x in topics) + '</div>', 'topics', alt=True,
                      head=(t("Knowledge topics", "Темы базы знаний"), t("Want a talk or training on one of these topics for your team? Get in touch.", "Нужна лекция или тренинг по одной из тем для вашей команды? Напишите нам.")))
            + eco(lang, 'main', root) + band(lang, t("Questions about your security?", "Вопросы о вашей безопасности?"), t("We answer personally.", "Ответим лично.")))
    nav = [(t("Products", "Продукты"), f'{root}{ru(lang)}#products'), (t("Insights", "Материалы"), '#cases'), (t("About", "О нас"), f'{root}{ru(lang)}#about')]
    return (t("Security insights — CakesCats", "Материалы о безопасности — CakesCats"),
            t("Operation Triangulation, NotPetya and SolarWinds explained in plain language, with practical takeaways.",
              "Операция «Триангуляция», NotPetya и SolarWinds простым языком — с практическими выводами."),
            nav, body)


# =====================================================================================
# Продуктовые сайты
# =====================================================================================
GUIDE_DIRS = {'os': 'virtualcatsos', 'phone': 'phone', 'vpn': 'vpn-router', 'llm': 'llm-edgebox'}


def guide_url(lang, key):
    return f'{GITHUB}/guides/blob/main/{GUIDE_DIRS[key]}/README{".ru" if lang == "ru" else ""}.md'


def product_page(lang, root, key, *, eyebrow, h1, lead, hero_img, hero_contain, trust, overview, feats, how, tiers_items, spec_rows, faqs, subject, cta_title, cta_sub, nav_extra=()):
    t = L(lang)
    hero = f'''<div class="hero"><div class="wrap">
<div><span class="eyebrow">{eyebrow}</span><h1>{h1}</h1><p class="lead">{lead}</p>
<div class="btns">{btn("#pricing", t("See configurations &amp; prices", "Конфигурации и цены"))}{tg_btn(lang, "s", t("Ask a question", "Задать вопрос"))}</div>
<div class="trust">{"".join(f"<span>{icon(i, 18)}{x}</span>" for i, x in trust)}</div></div>
<div class="media{" contain" if hero_contain else ""}"><img src="{root}assets/img/{hero_img}.webp" alt=""></div>
</div></div>'''
    ov = section(features(overview, cols=3), 'overview', head=(t("Overview", "Обзор"), None))
    ft = section(features(feats, cols=3), 'features', alt=True, head=(t("Features", "Возможности"), None))
    hw = section(how, 'how') if how else ''
    pr = section(tiers(lang, tiers_items, subject, guide_url(lang, key)), 'pricing', alt=True,
                 head=(t("Free, or ready-made", "Бесплатно или готовым решением"), t("Build it yourself from the guide, or support the project with a ready-made device or individual support.", "Соберите сами по инструкции или поддержите проект: купите готовое устройство или индивидуальную поддержку.")), center=True)
    sp = section(spec(spec_rows), 'specs', head=(t("Technical specifications", "Технические характеристики"), None))
    fq = section(faq(faqs), 'faq', alt=True, head=(t("Frequently asked questions", "Частые вопросы"), None), center=True)
    body = hero + ov + ft + hw + pr + sp + fq + other_products(lang, root, key) + eco(lang, key, root) + band(lang, cta_title, cta_sub, subject)
    nav = [(t("Overview", "Обзор"), '#overview'), (t("Features", "Возможности"), '#features')] + list(nav_extra) + [
        (t("Pricing", "Цены"), '#pricing'), (t("Specs", "Характеристики"), '#specs'), (t("FAQ", "Вопросы"), '#faq')]
    return body, nav


def phone(lang, root):
    t = L(lang)
    body, nav = product_page(
        lang, root, 'phone',
        eyebrow=t("CakesCats Phone", "CakesCats Phone"),
        h1=t("A smartphone you can trust", "Смартфон, которому можно доверять"),
        lead=t("Google Pixel with GrapheneOS and a curated set of open-source apps. No Google services, no tracking — configured, tested and ready from the first switch-on.",
               "Google Pixel с GrapheneOS и проверенным набором открытых приложений. Без сервисов Google и слежки — настроен, проверен и готов с первого включения."),
        hero_img='phone-hero', hero_contain=False,
        trust=[('shield', 'GrapheneOS'), ('tool', t("Set up for you", "Настроен за вас")), ('users', t("Personal support", "Личная поддержка"))],
        overview=[
            ('phone', t("Ready to use", "Готов к работе"), t("Configured and tested before it reaches you.", "Настроен и проверен до того, как попадёт к вам.")),
            ('eyeoff', t("No Google services", "Без сервисов Google"), t("GrapheneOS removes tracking and data collection by third-party services.", "GrapheneOS исключает отслеживание и сбор данных сторонними сервисами.")),
            ('key', t("Your digital safe", "Ваш цифровой сейф"), t("A separate space for crypto wallets, messengers and sensitive documents.", "Отдельное пространство для криптокошельков, мессенджеров и важных документов.")),
        ],
        feats=[
            ('code', t("Open technologies", "Открытые технологии"), t("Only open-source software trusted by security experts worldwide.", "Только открытое ПО, которому доверяют эксперты по безопасности по всему миру.")),
            ('layers', t("Isolated profiles", "Изолированные профили"), t("Separate profiles for work, personal life and crypto — data never mixes.", "Отдельные профили для работы, личного и криптовалют — данные не пересекаются.")),
            ('wipe', t("Emergency wipe", "Экстренная очистка"), t("A special duress PIN erases the device in seconds if you ever need it.", "Специальный PIN-код при необходимости стирает данные за секунды.")),
            ('lock', t("Hardware-backed security", "Аппаратная защита"), t("Pixel's Titan M2 chip and verified boot, strengthened by GrapheneOS.", "Чип Titan M2 и проверенная загрузка Pixel, усиленные GrapheneOS.")),
            ('chat', t("Private communication", "Приватное общение"), t("Pre-installed apps for encrypted calls, messaging and browsing.", "Предустановленные приложения для зашифрованных звонков, переписки и браузинга.")),
            ('sliders', t("Network control", "Контроль сети"), t("Per-app network permissions and optional traffic protection.", "Сетевые разрешения для каждого приложения и защита трафика по желанию.")),
        ],
        how=None,
        tiers_items=[
            {'name': t("Do it yourself", "Своими руками"), 'free': True,
             'desc': t("Install GrapheneOS on your own Pixel with our step-by-step guide.", "Установите GrapheneOS на свой Pixel по нашей пошаговой инструкции."),
             'price': '$0', 'note': t("Open guide on GitHub", "Открытая инструкция на GitHub"),
             'list': [t("Official GrapheneOS web installer", "Официальный веб-установщик GrapheneOS"), t("Profiles, duress PIN, network permission", "Профили, Duress PIN, разрешение «Сеть»"), t("Recommended apps", "Рекомендуемые приложения")]},
            {'name': t("Essential", "Essential"), 'img': f'{root}assets/img/phone-back.webp',
             'desc': t("Pixel with GrapheneOS and apps for private calls, messaging and browsing.", "Pixel с GrapheneOS и приложениями для приватных звонков, переписки и браузинга."),
             'price': '$1,490', 'note': t("Google Pixel 10", "Google Pixel 10"),
             'list': [t("GrapheneOS installed and hardened", "GrapheneOS установлена и усилена"), t("Curated open-source apps", "Проверенные открытые приложения"), t("Duress PIN emergency wipe", "Экстренная очистка по PIN"), t("12 months of support", "12 месяцев поддержки")]},
            {'name': t("Privacy Pro", "Privacy Pro"), 'img': f'{root}assets/img/phone-pair.webp', 'badge': t("Most popular", "Популярный выбор"),
             'desc': t("Isolated profiles, crypto tools and traffic protection.", "Изолированные профили, криптоинструменты и защита трафика."),
             'price': '$2,490', 'note': t("Google Pixel 10 Pro XL", "Google Pixel 10 Pro XL"),
             'list': [t("Everything in Essential", "Всё из Essential"), t("Isolated profiles: work, personal, crypto", "Профили: работа, личное, криптовалюты"), t("Crypto wallet setup", "Настройка криптокошельков"), t("12 months of private VPN", "12 месяцев приватного VPN"), t("Personal onboarding session", "Персональное занятие по работе с телефоном")]},
            {'name': t("Fold Ultimate", "Fold Ultimate"), 'img': f'{root}assets/img/phone-fold2.webp',
             'desc': t("Pixel Fold with every protection feature and a separate crypto profile.", "Pixel Fold со всеми функциями защиты и отдельным профилем для криптовалют."),
             'price': '$4,490', 'note': t("Google Pixel 10 Pro Fold, 512 GB", "Google Pixel 10 Pro Fold, 512 ГБ"),
             'list': [t("Everything in Privacy Pro", "Всё из Privacy Pro"), t("512 GB storage", "512 ГБ памяти"), t("Priority support for 24 months", "Приоритетная поддержка 24 месяца"), t("Device health check every 6 months", "Проверка устройства каждые 6 месяцев")]},
        ],
        spec_rows=[
            (t("Operating system", "Операционная система"), t("GrapheneOS (latest stable), no Google services", "GrapheneOS (последняя стабильная версия), без сервисов Google")),
            (t("Devices", "Устройства"), "Google Pixel 10 · Pixel 10 Pro XL · Pixel 10 Pro Fold"),
            (t("Security hardware", "Аппаратная защита"), t("Titan M2 security chip, verified boot", "Чип безопасности Titan M2, проверенная загрузка")),
            (t("Profiles", "Профили"), t("Up to 32 isolated user profiles", "До 32 изолированных профилей пользователей")),
            (t("Emergency features", "Экстренные функции"), t("Duress PIN wipe, auto-reboot, USB-C port control", "Очистка по PIN под давлением, автоперезагрузка, контроль порта USB-C")),
            (t("Updates", "Обновления"), t("Official GrapheneOS over-the-air updates", "Официальные обновления GrapheneOS по воздуху")),
            (t("Delivery", "Поставка"), t("Configured, tested and sealed; shipping worldwide on request", "Настроен, проверен и опломбирован; доставка по миру по запросу")),
        ],
        faqs=[
            (t("Is it safe?", "Это безопасно?"), t("GrapheneOS is recognised by security experts as one of the most secure mobile operating systems. It builds on Pixel's hardware security (Titan M2, verified boot) and adds its own protections; apps and data are isolated and network access can be controlled per app.",
                                                   "GrapheneOS признана экспертами одной из самых защищённых мобильных ОС. Она опирается на аппаратную защиту Pixel (Titan M2, проверенная загрузка) и добавляет собственные механизмы; приложения и данные изолированы, сетевой доступ настраивается для каждого приложения.")),
            (t("Why Pixel and GrapheneOS?", "Почему Pixel и GrapheneOS?"), t("Pixel is the widely available phone line that lets you install another operating system while keeping the full hardware chain of trust. GrapheneOS is developed with a strong focus on privacy and has no proprietary Google services.",
                                                                           "Pixel — доступная линейка смартфонов, на которую можно установить другую ОС, сохранив аппаратную цепочку доверия. GrapheneOS разрабатывается с упором на приватность и не содержит проприетарных сервисов Google.")),
            (t("Can I use my usual apps?", "Можно пользоваться привычными приложениями?"), t("Yes. Most apps work; if you need Google services for a specific app, GrapheneOS can run them sandboxed in a separate profile.",
                                                                                             "Да. Большинство приложений работают; если какому-то приложению нужны сервисы Google, GrapheneOS может запустить их в песочнице в отдельном профиле.")),
            (t("Why open source?", "Почему открытый код?"), t("Open code can be reviewed by independent auditors, so issues are found and fixed faster than in closed software.",
                                                              "Открытый код могут проверить независимые аудиторы, поэтому проблемы находят и исправляют быстрее, чем в закрытом ПО.")),
        ],
        subject='CakesCats Phone',
        cta_title=t("Ready for a phone you can trust?", "Готовы к телефону, которому можно доверять?"),
        cta_sub=t("Tell us how you use your phone — we'll suggest the right configuration.", "Расскажите, как вы пользуетесь телефоном, — подберём конфигурацию."))
    return (t("CakesCats Phone — Google Pixel with GrapheneOS, ready to use", "CakesCats Phone — Google Pixel с GrapheneOS, готовый к работе"),
            t("A Google Pixel with GrapheneOS, isolated profiles and private apps — configured, tested and supported. From $1,490.",
              "Google Pixel с GrapheneOS, изолированными профилями и приватными приложениями — настроен, проверен и на поддержке. От $1,490."),
            nav, body)


def vpn(lang, root):
    t = L(lang)
    body, nav = product_page(
        lang, root, 'vpn',
        eyebrow=t("VPN Router", "VPN-роутер"),
        h1=t("Private internet, out of the box", "Приватный интернет из коробки"),
        lead=t("A plug-and-play router with V2Ray and a dedicated server. It creates a separate private Wi-Fi network for all your devices — no apps and no setup.",
               "Роутер «включил и работает» с V2Ray и выделенным сервером. Создаёт отдельную приватную Wi-Fi-сеть для всех ваших устройств — без приложений и настройки."),
        hero_img='router-hero', hero_contain=False,
        trust=[('wifi', t("Private Wi-Fi", "Приватный Wi-Fi")), ('server', t("Dedicated server", "Выделенный сервер")), ('code', 'OpenWrt')],
        overview=[
            ('zap', t("Ready to go", "Готов к работе"), t("Plug in power and internet, and the private Wi-Fi network is up in a couple of minutes.", "Подключите питание и интернет, и через пару минут приватная Wi-Fi-сеть готова.")),
            ('eyeoff', t("Looks like regular traffic", "Выглядит как обычный трафик"), t("V2Ray makes the connection look like ordinary HTTPS.", "V2Ray делает соединение похожим на обычный HTTPS.")),
            ('globe', t("Stable access", "Стабильный доступ"), t("The services you need stay reachable when you travel.", "Нужные сервисы доступны и в поездках.")),
        ],
        feats=[
            ('wifi', t("Separate Wi-Fi network", "Отдельная Wi-Fi-сеть"), t("An isolated network for your devices that doesn't touch your main infrastructure.", "Изолированная сеть для ваших устройств, не затрагивающая основную инфраструктуру.")),
            ('server', t("Dedicated server", "Выделенный сервер"), t("Your own server with no “noisy neighbours” and no logs.", "Собственный сервер без «шумных соседей» и без журналов.")),
            ('shield', t("Kill switch", "Kill switch"), t("On request: internet is cut if the protected connection drops, so nothing leaks.", "По запросу: интернет отключается при обрыве защищённого соединения, чтобы ничего не утекло.")),
            ('sliders', t("Traffic control", "Контроль трафика"), t("Limit excessive traffic such as device telemetry.", "Ограничение лишнего трафика, например телеметрии устройств.")),
            ('code', t("Open-source core", "Открытая основа"), t("Runs on OpenWrt, a time-tested system with a strong community.", "Работает на OpenWrt — проверенной временем системе с сильным сообществом.")),
            ('users', t("Unlimited devices", "Без ограничения устройств"), t("Phones, laptops, tablets and TVs at the same time.", "Телефоны, ноутбуки, планшеты и телевизоры одновременно.")),
        ],
        how=None,
        tiers_items=[
            {'name': t("Build it yourself", "Собрать самому"), 'free': True,
             'desc': t("Set up your own server and router with our step-by-step guide.", "Настройте свой сервер и роутер по нашей пошаговой инструкции."),
             'price': '$0', 'note': t("Open source", "Открытый код"),
             'list': [t("Xray server with VLESS + REALITY", "Сервер Xray с VLESS + REALITY"), t("OpenWrt router with sing-box", "Роутер OpenWrt с sing-box"), t("Optional separate private Wi-Fi", "Отдельная приватная Wi-Fi-сеть по желанию")]},
            {'name': t("Router + 12 months", "Роутер + 12 месяцев"), 'img': f'{root}assets/img/router2.webp', 'badge': t("Most popular", "Популярный выбор"),
             'desc': t("A configured router with a year of access to your own dedicated server.", "Настроенный роутер и год доступа к собственному выделенному серверу."),
             'price': '$990', 'note': t("then $290/year", "далее $290 в год"),
             'list': [t("Pre-configured Wi-Fi 6 router", "Настроенный роутер Wi-Fi 6"), t("12 months of dedicated V2Ray server", "12 месяцев выделенного сервера V2Ray"), t("Kill switch on request", "Kill switch по запросу"), t("12 months of support", "12 месяцев поддержки")]},
            {'name': t("Personal server", "Персональный сервер"),
             'desc': t("A dedicated V2Ray server for your own router — used by you and only you.", "Выделенный сервер V2Ray для вашего роутера — только для вас."),
             'price': f'$29<small>/{t("month", "мес")}</small>', 'note': t("or $290/year", "или $290 в год"),
             'list': [t("Unlimited devices", "Без ограничения устройств"), t("No logs", "Без журналов"), t("Choice of server location", "Выбор расположения сервера"), t("Setup help", "Помощь с подключением")]},
        ],
        spec_rows=[
            (t("Firmware", "Прошивка"), t("OpenWrt with V2Ray (VLESS/VMess over TLS)", "OpenWrt с V2Ray (VLESS/VMess поверх TLS)")),
            (t("Wireless", "Беспроводная сеть"), t("Wi-Fi 6, dual band; separate private network", "Wi-Fi 6, два диапазона; отдельная приватная сеть")),
            (t("Server", "Сервер"), t("Dedicated, single-tenant, no logs; location on request", "Выделенный, только для вас, без журналов; расположение по запросу")),
            (t("Protection", "Защита"), t("Kill switch (on request), DNS through the tunnel, telemetry limits", "Kill switch (по запросу), DNS через туннель, ограничение телеметрии")),
            (t("Devices", "Устройства"), t("Unlimited", "Без ограничений")),
            (t("Setup", "Настройка"), t("None — plug in power and internet", "Не нужна — подключите питание и интернет")),
        ],
        faqs=[
            (t("Is this a VPN?", "Это VPN?"), t("It's a router with V2Ray pre-installed — a technology that makes your protected connection look like ordinary web traffic, so it works reliably even where regular VPNs struggle.",
                                                "Это роутер с предустановленным V2Ray — технологией, которая делает защищённое соединение похожим на обычный веб-трафик, поэтому оно надёжно работает даже там, где обычные VPN не справляются.")),
            (t("Do I need to configure anything?", "Нужно что-то настраивать?"), t("No. Connect power and internet — we've already set everything up.", "Нет. Подключите питание и интернет — мы уже всё настроили.")),
            (t("Can I connect several devices?", "Можно подключить несколько устройств?"), t("Yes, the router creates a separate Wi-Fi network for any number of devices.", "Да, роутер создаёт отдельную Wi-Fi-сеть для любого количества устройств.")),
            (t("What happens if the connection drops?", "Что будет, если соединение оборвётся?"), t("With kill switch enabled, all traffic stops until the protected connection is restored.", "При включённом kill switch весь трафик останавливается, пока защищённое соединение не восстановится.")),
        ],
        subject='VPN Router',
        cta_title=t("Want private Wi-Fi at home or in the office?", "Нужен приватный Wi-Fi дома или в офисе?"),
        cta_sub=t("We'll pick the router and server location for you.", "Подберём роутер и расположение сервера."))
    return (t("VPN Router by CakesCats — private Wi-Fi with a dedicated server", "VPN-роутер CakesCats — приватный Wi-Fi с выделенным сервером"),
            t("A plug-and-play router with V2Ray and a dedicated no-log server: a private Wi-Fi network for all your devices. From $990.",
              "Роутер с V2Ray и выделенным сервером без журналов: приватная Wi-Fi-сеть для всех ваших устройств. От $990."),
            nav, body)


def os_(lang, root):
    t = L(lang)
    how = f'''<div class="split"><div class="media"><img src="{root}assets/img/mac.webp" alt="" loading="lazy"></div><div>
<h2>{t("How it works", "Как это работает")}</h2><div class="steps">
<div class="step"><b>1</b><div><h3>{t("An isolated virtual machine", "Изолированная виртуальная машина")}</h3><p>{t("A pre-configured Linux workspace runs in UTM on your Mac — macOS doesn't see what happens inside.", "Настроенная рабочая среда Linux работает в UTM на вашем Mac — macOS не видит, что происходит внутри.")}</p></div></div>
<div class="step"><b>2</b><div><h3>{t("Encrypted storage", "Шифрованное хранилище")}</h3><p>{t("The workspace lives in an encrypted VeraCrypt container with a private hidden layer for the most sensitive data.", "Среда хранится в зашифрованном контейнере VeraCrypt со скрытым слоем для самых важных данных.")}</p></div></div>
<div class="step"><b>3</b><div><h3>{t("Private network", "Приватная сеть")}</h3><p>{t("All traffic goes through Tor; the turnkey kit adds a protected router.", "Весь трафик идёт через Tor; в готовом комплекте добавляется защищённый роутер.")}</p></div></div>
</div></div></div>'''
    body, nav = product_page(
        lang, root, 'os',
        eyebrow="VirtualCatsOS",
        h1=t("Your Mac stays outside. What matters lives inside.", "Ваш Mac остаётся снаружи. Важное — внутри."),
        lead=t("An isolated, encrypted workspace for Macs with Apple silicon: a pre-configured virtual machine with Tor routing and a curated set of privacy tools — working right out of the box.",
               "Изолированная зашифрованная рабочая среда для Mac на Apple silicon: настроенная виртуальная машина с маршрутизацией через Tor и набором инструментов приватности — работает сразу."),
        hero_img='mac-hero', hero_contain=False,
        trust=[('laptop', 'Apple silicon'), ('lock', t("Encrypted", "Шифрование")), ('code', t("Open source", "Открытый код"))],
        overview=[
            ('layers', t("Work and personal, separated", "Работа и личное — раздельно"), t("Keep them apart on one Mac, without a second device.", "Разделите их на одном Mac, без второго устройства.")),
            ('key', t("Control over your information", "Контроль над информацией"), t("A private hidden layer accessible only to you for your most sensitive data.", "Скрытый слой, доступный только вам, — для самых важных данных.")),
            ('tool', t("No technical background needed", "Технические знания не нужны"), t("Pre-configured, tested and built on community-verified open source.", "Настроено, проверено и построено на открытом ПО, проверенном сообществом.")),
        ],
        feats=[
            ('eyeoff', t("Isolation from telemetry", "Изоляция от телеметрии"), t("macOS doesn't see what you do inside the workspace.", "macOS не видит, что вы делаете внутри среды.")),
            ('lock', t("Encrypted container", "Зашифрованный контейнер"), t("The system runs from a VeraCrypt container with an optional hidden layer.", "Система работает из контейнера VeraCrypt с дополнительным скрытым слоем.")),
            ('route', t("Tor routing", "Маршрутизация через Tor"), t("Network traffic from the workspace is routed through Tor by default.", "Сетевой трафик среды по умолчанию идёт через Tor.")),
            ('wifi', t("Protected network", "Защищённая сеть"), t("The turnkey kit adds an OpenWrt router with VPN and ad blocking.", "Готовый комплект дополняется роутером OpenWrt с VPN и блокировкой рекламы.")),
            ('search', t("Safe file testing", "Безопасная проверка файлов"), t("Open suspicious files in an isolated environment, away from your main system.", "Открывайте сомнительные файлы в изолированной среде, отдельно от основной системы.")),
            ('code', t("Free and open", "Бесплатно и открыто"), t("All instructions are public — build the same solution yourself at no cost.", "Все инструкции открыты — такое же решение можно собрать самому бесплатно.")),
        ],
        how=how,
        tiers_items=[
            {'name': t("Build it yourself", "Собрать самому"), 'free': True,
             'desc': t("Set up the workspace on your Mac with our step-by-step guide.", "Настройте среду на своём Mac по нашей пошаговой инструкции."),
             'price': '$0', 'note': t("Open source", "Открытый код"),
             'list': [t("UTM and Ubuntu ARM64", "UTM и Ubuntu ARM64"), t("All traffic through Tor", "Весь трафик через Tor"), t("VeraCrypt container with a hidden volume", "Контейнер VeraCrypt со скрытым томом")]},
            {'name': t("Setup on your Mac", "Настройка на вашем Mac"), 'badge': t("Most popular", "Популярный выбор"),
             'desc': t("We set up the workspace on your Mac remotely and walk you through it.", "Настроим среду на вашем Mac удалённо и покажем, как ею пользоваться."),
             'price': '$990', 'note': t("Remote, about 2 hours", "Удалённо, около 2 часов"),
             'list': [t("Full installation and hardening", "Полная установка и усиление защиты"), t("Encrypted container with hidden layer", "Шифрованный контейнер со скрытым слоем"), t("Personal walkthrough", "Персональное обучение"), t("3 months of support", "3 месяца поддержки")]},
            {'name': t("Turnkey MacBook", "Готовый MacBook"), 'img': f'{root}assets/img/mac-hero.webp',
             'desc': t("A new MacBook with VirtualCatsOS, protected router and all tools installed.", "Новый MacBook с VirtualCatsOS, защищённым роутером и всеми инструментами."),
             'price': '$4,490', 'note': t("MacBook Air M5, 16 GB / 512 GB", "MacBook Air M5, 16 ГБ / 512 ГБ"),
             'list': [t("MacBook Air M5 included", "MacBook Air M5 в комплекте"), t("VirtualCatsOS, Tor, VeraCrypt installed", "Установлены VirtualCatsOS, Tor, VeraCrypt"), t("Protected OpenWrt router", "Защищённый роутер OpenWrt"), t("12 months of support", "12 месяцев поддержки")]},
        ],
        spec_rows=[
            (t("Compatible Macs", "Совместимые Mac"), t("Apple silicon (M1 and newer), 16 GB RAM recommended", "Apple silicon (M1 и новее), рекомендуется 16 ГБ ОЗУ")),
            (t("Virtualisation", "Виртуализация"), "UTM"),
            (t("Guest system", "Гостевая система"), t("Ubuntu Linux, hardened, with privacy tools", "Ubuntu Linux с усиленной защитой и инструментами приватности")),
            (t("Encryption", "Шифрование"), t("VeraCrypt container with optional hidden volume", "Контейнер VeraCrypt с дополнительным скрытым томом")),
            (t("Network", "Сеть"), t("Enforced Tor routing; OpenWrt router with VPN in the turnkey kit", "Принудительная маршрутизация через Tor; роутер OpenWrt с VPN в готовом комплекте")),
            (t("iPhone / iPad", "iPhone / iPad"), t("Limited support", "Ограниченная поддержка")),
        ],
        faqs=[
            (t("Is it safe?", "Это безопасно?"), t("The whole system runs from an encrypted VeraCrypt container, isolated inside a virtual machine, with enforced Tor routing — your data is protected both at rest and in transit.",
                                                   "Вся система работает из зашифрованного контейнера VeraCrypt, изолирована в виртуальной машине и использует принудительную маршрутизацию через Tor — данные защищены и при хранении, и при передаче.")),
            (t("What is the hidden layer?", "Что такое скрытый слой?"), t("An encrypted hidden section inside the container, accessible only to you and invisible during normal use. It's meant for your most sensitive information.",
                                                                          "Зашифрованный скрытый раздел внутри контейнера, доступный только вам и невидимый при обычной работе. Он предназначен для самой важной информации.")),
            (t("Is it software or a device?", "Это программа или устройство?"), t("Both. You can build it yourself for free, have us set it up on your Mac, or buy a turnkey MacBook.",
                                                                                  "И то и другое. Можно собрать бесплатно самому, доверить настройку на вашем Mac нам или купить готовый MacBook.")),
            (t("Why Tor?", "Зачем Tor?"), t("Tor is one of the most reliable and widely studied tools for private browsing. It's not a magic bullet, but an important part of a thought-through privacy setup.",
                                             "Tor — один из самых надёжных и изученных инструментов приватного доступа в интернет. Это не волшебная таблетка, но важная часть продуманной защиты.")),
        ],
        subject='VirtualCatsOS',
        cta_title=t("A private workspace on your Mac", "Приватная рабочая среда на вашем Mac"),
        cta_sub=t("Tell us your Mac model — we'll suggest the best option.", "Напишите модель вашего Mac — подскажем лучший вариант."),
        nav_extra=[(t("How it works", "Как работает"), '#how')])
    return (t("VirtualCatsOS — a private, isolated workspace for Mac", "VirtualCatsOS — приватная изолированная среда для Mac"),
            t("An encrypted, isolated virtual workspace for Macs with Apple silicon, with Tor routing. Free to build yourself, setup from $990, turnkey MacBook $4,490.",
              "Зашифрованная изолированная рабочая среда для Mac на Apple silicon с маршрутизацией через Tor. Самостоятельно — бесплатно, настройка от $990, готовый MacBook — $4,490."),
            nav, body)


def llm(lang, root):
    t = L(lang)
    how = section('<div class="g3">' + ''.join(f'<div class="card"><div class="feat"><div class="ic">{icon(i)}</div></div><h3>{h}</h3><p>{p}</p></div>' for i, h, p in [
        ('briefcase', t("Confidential industries", "Конфиденциальные отрасли"), t("Banks, legal teams, pharma and the public sector — anyone who can't send data to public AI services.", "Банки, юристы, фарма и госсектор — все, кто не может отправлять данные в публичные ИИ-сервисы.")),
        ('users', t("Teams without AI engineers", "Команды без ИИ-инженеров"), t("No DevOps or ML team needed — everything is ready to use.", "Не нужны DevOps и ML-команда — всё готово к работе.")),
        ('doc', t("Analysts and content teams", "Аналитики и контент-команды"), t("Faster drafts, summaries and rewrites, with data staying in-house.", "Черновики, резюме и правки быстрее, а данные остаются внутри.")),
        ('shield', t("Security and IT leaders", "Руководители ИБ и IT"), t("You know where every request goes.", "Вы знаете, куда уходит каждый запрос.")),
        ('heart', t("Privacy-minded professionals", "Те, кто ценит приватность"), t("A personal AI at home or at work that sends nothing to the cloud.", "Личный ИИ дома или на работе, который ничего не отправляет в облако.")),
        ('cpu', t("Teams building AI agents", "Команды, создающие ИИ-агентов"), t("A local, private backend for agents and automation with an OpenAI-compatible API.", "Локальная приватная основа для агентов и автоматизации с API, совместимым с OpenAI.")),
    ]) + '</div>', 'who', head=(t("Who it's for", "Для кого"), None))
    body, nav = product_page(
        lang, root, 'llm',
        eyebrow="LLM EdgeBox",
        h1=t("Private AI in your office", "Приватный ИИ в вашем офисе"),
        lead=t("A ready-to-use AI appliance for your office: chat assistant, document work and automation — fully offline. Plug it into your network and your team gets a private AI within minutes.",
               "Готовый ИИ-сервер для вашего офиса: чат-ассистент, работа с документами и автоматизация — полностью офлайн. Подключите к сети, и через несколько минут у команды будет приватный ИИ."),
        hero_img='llm-hero', hero_contain=False,
        trust=[('lock', t("Fully offline", "Полностью офлайн")), ('server', t("On your premises", "У вас в офисе")), ('tool', t("Set up for you", "Настройка за вас"))],
        overview=[
            ('zap', t("Ready to go", "Готов к работе"), t("Models and interface are pre-installed and start automatically.", "Модели и интерфейс предустановлены и запускаются автоматически.")),
            ('lock', t("Data stays with you", "Данные остаются у вас"), t("Prompts and answers stay inside your network.", "Запросы и ответы остаются внутри вашей сети.")),
            ('chat', t("Familiar interface", "Привычный интерфейс"), t("A browser-based chat your team already knows how to use.", "Чат в браузере, которым команда уже умеет пользоваться.")),
        ],
        feats=[
            ('doc', t("Work with internal documents", "Работа с внутренними документами"), t("Ask questions about your own files and knowledge base (RAG) — without uploading them anywhere.", "Задавайте вопросы по своим файлам и базе знаний (RAG) — ничего никуда не загружая.")),
            ('megaphone', t("Your tone of voice", "Ваш стиль"), t("The assistant uses your terminology and style; the interface can carry your brand.", "Ассистент использует вашу терминологию и стиль; интерфейс — в вашем фирменном оформлении.")),
            ('code', t("OpenAI-compatible API", "API, совместимый с OpenAI"), t("Connect existing tools, agents and scripts to a local endpoint.", "Подключите существующие инструменты, агентов и скрипты к локальному серверу.")),
            ('users', t("Team access", "Доступ для команды"), t("Accounts and access control for your whole team.", "Учётные записи и разграничение доступа для всей команды.")),
            ('cpu', t("Modern open models", "Современные открытые модели"), t("Current open-weight models, from fast assistants to large reasoning models.", "Актуальные открытые модели — от быстрых ассистентов до больших рассуждающих моделей.")),
            ('tool', t("Updates and support", "Обновления и поддержка"), t("We keep models and software up to date and help your team get the most out of it.", "Мы обновляем модели и ПО и помогаем команде использовать сервер по максимуму.")),
        ],
        how=None,
        tiers_items=[
            {'name': t("Do it yourself", "Своими руками"), 'free': True,
             'desc': t("Run a local AI on your own computer: Ollama and Open WebUI.", "Запустите локальный ИИ на своём компьютере: Ollama и Open WebUI."),
             'price': '$0', 'note': t("Open guide on GitHub", "Открытая инструкция на GitHub"),
             'list': [t("Chat in the browser", "Чат в браузере"), t("Search over your documents and API", "Поиск по документам и API"), t("Fully offline mode", "Полностью офлайн")]},
            {'name': 'EdgeBox Basic', 'img': f'{root}assets/img/llm-basic.webp',
             'desc': t("A compact appliance for a team of up to 20 people.", "Компактный сервер для команды до 20 человек."),
             'price': '$9,900', 'note': t("128 GB unified memory class", "Класс 128 ГБ общей памяти"),
             'list': [t("Models up to ~120B parameters (MoE)", "Модели до ~120 млрд параметров (MoE)"), t("Chat interface and API", "Чат-интерфейс и API"), t("Installation and onboarding", "Установка и обучение"), t("12 months of support", "12 месяцев поддержки")]},
            {'name': 'EdgeBox Pro', 'img': f'{root}assets/img/llm-pro.webp', 'badge': t("Most popular", "Популярный выбор"),
             'desc': t("A workstation for demanding teams, tuned to your documents and tasks.", "Рабочая станция для требовательных команд, настроенная под ваши документы и задачи."),
             'price': f'{t("From", "От")} $24,900', 'note': t("Professional GPU, 96 GB", "Профессиональная видеокарта, 96 ГБ"),
             'list': [t("Large models up to ~235B (MoE)", "Большие модели до ~235 млрд (MoE)"), t("Search over your documents (RAG)", "Поиск по вашим документам (RAG)"), t("Customisation for your tasks", "Настройка под ваши задачи"), t("Priority support for 12 months", "Приоритетная поддержка 12 месяцев")]},
            {'name': 'Enterprise', 'img': f'{root}assets/img/llm-ent.webp',
             'desc': t("Server infrastructure, training on your data and on-site support.", "Серверная инфраструктура, обучение на ваших данных и поддержка на месте."),
             'price': f'{t("From", "От")} $60,000', 'note': t("Custom quote", "Индивидуальный расчёт"),
             'list': [t("Multi-GPU servers", "Серверы с несколькими GPU"), t("Fine-tuning on your data", "Дообучение на ваших данных"), t("Integration with your systems", "Интеграция с вашими системами"), t("SLA and on-site support", "SLA и поддержка на месте")],
             'cta': t("Request a quote", "Запросить расчёт")},
        ],
        spec_rows=[
            (t("Deployment", "Размещение"), t("On your premises, fully offline; no cloud connection required", "У вас, полностью офлайн; подключение к облаку не нужно")),
            (t("Models", "Модели"), t("Current open-weight LLMs (e.g. Qwen, Llama, Mistral families), updated by us", "Актуальные открытые LLM (например, семейства Qwen, Llama, Mistral), обновляем мы")),
            (t("Interfaces", "Интерфейсы"), t("Web chat, OpenAI-compatible API, document search (RAG)", "Веб-чат, API, совместимый с OpenAI, поиск по документам (RAG)")),
            (t("Access", "Доступ"), t("Accounts, roles, HTTPS on your local network", "Учётные записи, роли, HTTPS в локальной сети")),
            (t("Basic / Pro hardware", "Оборудование Basic / Pro"), t("128 GB unified-memory appliance / workstation with a 96 GB professional GPU", "Сервер с 128 ГБ общей памяти / рабочая станция с профессиональной видеокартой 96 ГБ")),
            (t("Setup time", "Время запуска"), t("About 10 minutes after connecting to your network", "Около 10 минут после подключения к сети")),
        ],
        faqs=[
            (t("Does it work without the internet?", "Работает без интернета?"), t("Yes. LLM EdgeBox is fully offline; your data never leaves your network.", "Да. LLM EdgeBox работает полностью офлайн; данные не покидают вашу сеть.")),
            (t("What do I need to get started?", "Что нужно для запуска?"), t("Power and a connection to your local network. Everything is pre-installed.", "Питание и подключение к локальной сети. Всё уже установлено.")),
            (t("How does it compare to cloud AI?", "Чем это лучше облачного ИИ?"), t("No per-request fees, no data leaving the company and no dependency on a provider's rules — at the cost of a one-time hardware purchase.",
                                                                                   "Нет оплаты за каждый запрос, данные не покидают компанию и нет зависимости от правил провайдера — ценой разовой покупки оборудования.")),
            (t("Can it be adapted to our company?", "Можно адаптировать под нашу компанию?"), t("Yes: your terminology, tone of voice, document base and branding. Pro and Enterprise include deeper customisation.",
                                                                                             "Да: ваша терминология, стиль, база документов и фирменное оформление. В Pro и Enterprise — более глубокая настройка.")),
            (t("Why are prices higher than last year?", "Почему цены выше, чем в прошлом году?"), t("Memory and GPU prices rose sharply in 2026 because of the global memory shortage. In return, today's models are far more capable: Basic runs models that needed a server rack two years ago.",
                                                                                                 "В 2026 году цены на память и видеокарты резко выросли из-за мирового дефицита памяти. Зато современные модели намного сильнее: Basic запускает модели, для которых два года назад нужна была серверная стойка.")),
        ],
        subject='LLM EdgeBox',
        cta_title=t("See private AI in action", "Посмотрите приватный ИИ в работе"),
        cta_sub=t("Book a demo — we'll show EdgeBox on your kind of documents.", "Запишитесь на демонстрацию — покажем EdgeBox на ваших типовых документах."),
        nav_extra=[(t("Who it's for", "Для кого"), '#who')])
    # блок «для кого» после возможностей
    body = body.replace('<section id="pricing"', how + '<section id="pricing"', 1)
    return (t("LLM EdgeBox — private AI on your premises", "LLM EdgeBox — приватный ИИ у вас в офисе"),
            t("A ready-to-use, fully offline AI appliance: chat, document search and automation with your data staying in-house. From $9,900.",
              "Готовый ИИ-сервер, работающий полностью офлайн: чат, поиск по документам и автоматизация — данные остаются внутри компании. От $9,900."),
            nav, body)


def privacy(lang, root, key):
    t = L(lang)
    here = os.path.dirname(os.path.abspath(__file__))
    lines = open(os.path.join(here, 'legal', 'privacy-pl.txt'), encoding='utf-8').read().splitlines()[1:-1]
    lines += open(os.path.join(here, 'legal', 'cookies-pl.txt'), encoding='utf-8').read().splitlines()
    out = []
    for l in lines:
        l = l.strip()
        if not l or l in ('Ок', 'Cookie Policy'):
            continue
        l = l.replace('https://www.os.cakescats.com', 'https://' + SITES[key]['domain'])
        if l.isupper() and len(l) < 90:
            out.append(f'<h3>{ESC(l)}</h3>')
        else:
            out.append(f'<p>{ESC(l)}</p>')
    body = (f'<div class="hero"><div class="wrap" style="grid-template-columns:1fr"><div><span class="eyebrow">Legal</span>'
            f'<h1>Polityka prywatności i cookies</h1><p class="lead">{t("Privacy and cookie policy (in Polish). This site does not use tracking cookies or analytics.", "Политика конфиденциальности и cookie (на польском языке). Сайт не использует отслеживающие cookie и аналитику.")}</p></div></div></div>'
            + section('<div class="prose" lang="pl">' + ''.join(out) + '</div>'))
    nav = [(t("Home", "Главная"), f'{root}{ru(lang)}'), (t("Contact", "Контакты"), f'{TG}')]
    return ('Polityka prywatności — ' + SITES[key]['name'], 'Polityka prywatności i cookies', nav, body)
