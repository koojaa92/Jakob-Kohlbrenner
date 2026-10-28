#!/usr/bin/env python3
"""Baut die Website aus _content/*.html, _tools/projekte.json und den Vorlagen unten.

  python3 _tools/build.py          Vorschau-Links mit .html (zum lokalen Ansehen)
  python3 _tools/build.py --prod   Links ohne .html, wie die bisherigen Adressen
"""
import html, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROD = "--prod" in sys.argv
BASE = "https://www.jakob-kohlbrenner.de"
VERSION = "3"  # bei Änderungen an styles.css oder main.js hochzählen
NAME = "Jakob Kohlbrenner"
FONTS = ("https://fonts.bunny.net/css?family=bricolage-grotesque:500,700|instrument-sans:400,500,600&display=swap"
         if PROD else
         "https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700&family=Instrument+Sans:wght@400;500;600&display=swap")

# Titel (bis ca. 60 Zeichen) und Beschreibung (bis ca. 155 Zeichen) je Seite
PAGES = [
    ("", "index", "Graphic Recording & Facilitation in Freiburg | Jakob Kohlbrenner",
     "Graphic Recording, Generative Scribing und Dialog-Facilitation für Konferenzen, Workshops und Teamprozesse in Freiburg, Baden-Württemberg und Süddeutschland.",
     "img/jakob-graphic-recording-f-hrungskolleg.jpg"),
    ("graphic-recording", "graphic-recording", "Graphic Recording Freiburg & Süddeutschland | Jakob Kohlbrenner",
     "Live-Visualisierung und Generative Scribing für Konferenzen, Workshops und Teamtage in Freiburg, Baden-Württemberg und München. Digitale Scans inklusive.",
     "img/persta-250509-142.jpg"),
    ("strategische-visualisierung", "strategische-visualisierung", "Strategische Visualisierung für Teams | Jakob Kohlbrenner",
     "Strategien, Visionen und Veränderungsprozesse als Bild: strategische Visualisierung mit Graphic Recording und Harvesting für Teams und Organisationen in Freiburg und Süddeutschland.",
     "img/66-dscf6422.jpg"),
    ("facilitation", "facilitation", "Dialog-Facilitation & Art of Hosting | Jakob Kohlbrenner",
     "Dialog-Facilitation und Art of Hosting für Konferenzen, Workshops und Großgruppen: Begegnungsräume für tragfähige Entscheidungen. Freiburg und Süddeutschland.",
     "img/img-2810.jpg"),
    ("kulturentwicklung", "kulturentwicklung", "Kulturentwicklung für Organisationen | Jakob Kohlbrenner",
     "Kulturentwicklung, die nicht nach dem Workshop aufhört: Kulturdiagnose, Formatentwicklung und Führungskultur für Teams und Organisationen.",
     "img/persta-250509-457-kopie.jpg"),
    ("about", "about", "Über Jakob Kohlbrenner | Facilitator in Freiburg",
     "Jakob Kohlbrenner begleitet seit über acht Jahren Organisationen mit Facilitation, Graphic Recording und Kulturentwicklung. Arbeitsort Freiburg.",
     "img/jakob-kohlbrenner-about.png"),
    ("projektgalerie", "projektgalerie", "Projekte: Graphic Recording & Facilitation | Jakob Kohlbrenner",
     "Projekte aus Freiburg, München und darüber hinaus: Graphic Recording, Generative Scribing und Facilitation bei Konferenzen und Teamprozessen.",
     "img/jobrad-m-nchen-567.jpg"),
    ("kontakt", "kontakt", "Kontakt & Erstgespräch | Jakob Kohlbrenner",
     "Kostenfreies Erstgespräch zu Graphic Recording, Facilitation und Kulturentwicklung. Telefon, E-Mail oder direkt einen Termin buchen.",
     "img/jakob-kohlbrenner-about-f4eb.png"),
    ("impressum", "impressum", "Impressum | Jakob Kohlbrenner", "Impressum von Jakob Kohlbrenner.", None),
    ("datenschutz", "datenschutz", "Datenschutz | Jakob Kohlbrenner", "Datenschutzerklärung von Jakob Kohlbrenner.", None),
]
NOINDEX = {"impressum", "datenschutz"}
NAV = [("graphic-recording", "Graphic Recording"), ("strategische-visualisierung", "Strategische Visualisierung"), ("facilitation", "Facilitation"),
       ("kulturentwicklung", "Kulturentwicklung"), ("projektgalerie", "Projekte"), ("about", "Über mich")]

FAQ = {
    "graphic-recording": [
        ("Was ist der Unterschied zwischen Graphic Recording und Generative Scribing?",
         "Graphic Recording dokumentiert in Echtzeit das Gesagte und macht komplexe Themen sichtbar. Generative Scribing geht einen Schritt weiter: Es hält nicht nur fest, sondern entwickelt – es spiegelt Stimmungen, Dynamiken und das Gemeinte hinter den Worten. So entstehen Bilder, die Prozesse vertiefen und neue Perspektiven eröffnen."),
        ("Welche Voraussetzungen braucht der Raum für die Visualisierung?",
         "Idealerweise gibt es eine lange, glatte Wand, an der ich Papier anbringen kann. Alle weiteren Materialien bringe ich mit. Falls nötig, kann ich gegen eine Mietgebühr auch meine Graphic Wall mitbringen – eine mobile, besonders lange Pinnwand für große Formate."),
        ("Bekommen wir digitale Scans und wie ist es mit den Bildrechten?",
         "Ja, alle Bildrechte liegen im Nachgang bei euch. Ihr erhaltet von mir aufbereitete digitale Scans direkt nach der Veranstaltung – zur freien Verwendung in Präsentationen, Berichten oder Social Media. Visualisierungen sind dafür da, geteilt und gesehen zu werden. Ich freue mich, wenn ihr meinen Namen und meine Website mit anführt."),
        ("Arbeitest du auch digital?",
         "Ja, ich arbeite auch digital – zum Beispiel über Zoom, Teams oder Google Meet. Auf dem iPad visualisiere ich live und integriere die Zeichnungen ideal in Online-Workshops, Summits oder Konferenzen. Besonders wirkungsvoll ist die Kombination mit Miro oder MURAL Boards, denn so entsteht ein gemeinsamer Raum, in dem Visualisierung eine wichtige Lücke der Kommunikation schließt, die im Online-Format oft verloren geht."),
        ("Gibst du auch Visualisierungs-Workshops?",
         "Ja, ich biete Visualisierungs-Workshops für Gruppen von 5 bis etwa 30 Personen an. Dabei geht es vor allem um einen intuitiven Zugang zum Zeichnen: mit einfachen Materialien, klaren Strukturen und der Möglichkeit, innere Themen sichtbar zu machen. So entsteht Klarheit, Kreativität und oft auch eine neue Form der Reflexion. Meine Workshops eignen sich besonders gut für Teambuilding, persönliche Entwicklung und für die Frage, was im jeweiligen Kontext wirklich wesentlich ist. Wenn du Interesse hast, melde dich gerne – gemeinsam finden wir das passende Format."),
    ],
    "facilitation": [
        ("Was ist der Unterschied zwischen Moderation und Facilitation?",
         "Moderation bedeutet, ein vorbereitetes Programm durchzuführen. Facilitation heißt dagegen „erleichtern“ (vom Latein facilitare): Ich öffne Räume für echte Gespräche, entwickle ein Prozessdesign und arbeite mit interaktiven Methoden. Ich bin kein klassischer Moderator für Podiumsdiskussionen, sondern Gestalter von Dialogräumen."),
        ("Was kostet eine Begleitung?",
         "Ich arbeite in der Regel mit Tagessätzen. Jedes Projekt ist individuell – nach einem ersten Gespräch erhältst du ein maßgeschneidertes Angebot, passend zu deinem Kontext und Umfang."),
        ("Mit wie vielen Leuten arbeitest du?",
         "Von kleinen Teams mit 3–5 Personen über Workshops mit 15–30 bis hin zu Großgruppen mit 100–300 Teilnehmenden. Je größer die Gruppe, desto wichtiger sind Vorbereitung, Prozessdesign und eine klare Organisation."),
    ],
}

FAQ["strategische-visualisierung"] = [FAQ["graphic-recording"][i] for i in (2, 3, 4)]

SERVICE_AREA = [{"@type": "City", "name": "Freiburg im Breisgau"}, {"@type": "AdministrativeArea", "name": "Baden-Württemberg"},
                {"@type": "City", "name": "München"}, {"@type": "Country", "name": "Deutschland"}]


def esc(s): return html.escape(s, quote=True)


def depth_prefix(path):  # path wie "projektgalerie/x/y" -> "../../"
    return "../" * path.count("/")


def link(name, R):
    if PROD:
        return R + name if name else (R or "./")
    return R + (name + ".html" if name else "index.html")


def read(p):
    with open(os.path.join(ROOT, p), encoding="utf-8") as f:
        return f.read()


def write(p, s):
    full = os.path.join(ROOT, p)
    os.makedirs(os.path.dirname(full) or ROOT, exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(s)


def projekte():
    return json.load(open(os.path.join(ROOT, "_tools/projekte.json"), encoding="utf-8"))["projekte"]


def tile(p, R):
    meta = " · ".join(x for x in [p.get("ort"), p["filter"][0] if p.get("filter") else None] if x)
    cats = "|".join(p.get("filter", []))
    if p.get("platzhalter"):
        return (f'<div class="tile platzhalter" data-cats="{esc(cats)}"><figure class="ph r43 is-missing" data-label="Bild folgt"></figure>'
                f'<div class="meta">Platzhalter</div><h3>{esc(p["titel"])}</h3><p>{esc(p["zitat"])}</p></div>')
    thumb = f'<figure class="ph"><img src="{R}img/{p["thumb"]}" alt="{esc(p["titel"])}" loading="lazy"></figure>'
    return (f'<a class="tile" href="{link(p["pfad"], R)}" data-cats="{esc(cats)}">{thumb}'
            f'<div class="meta">{esc(meta)}</div><h3>{esc(p["titel"])}</h3><p>„{esc(p["zitat"])}“</p></a>')


def cta(t, text, btn, R):
    return (f'<section class="cta"><div class="wrap"><h2>{t}</h2><p>{text}</p>'
            f'<div class="btns"><a class="btn" href="{link("kontakt", R)}">{btn}</a>'
            f'<a class="btn ghost" href="tel:+4915775353250">Anrufen</a></div></div></section>')


def faq_html(key):
    return "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in FAQ[key])


def jsonld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + "</script>"


def person_ld():
    return {"@context": "https://schema.org", "@graph": [
        {"@type": "Person", "@id": BASE + "/#jakob", "name": NAME, "url": BASE + "/",
         "jobTitle": "Graphic Recorder und Facilitator", "email": "kontakt@jakob-kohlbrenner.de", "telephone": "+4915775353250",
         "address": {"@type": "PostalAddress", "addressLocality": "Ehrenkirchen", "postalCode": "79238", "addressCountry": "DE"},
         "sameAs": ["https://linkedin.com/in/jakob-kohlbrenner-58133414a"],
         "knowsAbout": ["Graphic Recording", "Generative Scribing", "Dialog-Facilitation", "Art of Hosting", "Theory U", "Kulturentwicklung"]},
        {"@type": "ProfessionalService", "@id": BASE + "/#service", "name": "Jakob Kohlbrenner – Graphic Recording & Facilitation",
         "url": BASE + "/", "founder": {"@id": BASE + "/#jakob"}, "areaServed": SERVICE_AREA,
         "telephone": "+4915775353250", "email": "kontakt@jakob-kohlbrenner.de",
         "address": {"@type": "PostalAddress", "addressLocality": "Ehrenkirchen", "postalCode": "79238", "addressCountry": "DE"},
         "makesOffer": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": n}} for n in
                        ["Graphic Recording", "Generative Scribing", "Dialog-Facilitation", "Kulturentwicklung"]]}]}


def faq_ld(key):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ[key]]}


def shell(path, name, title, desc, body, og=None, extra="", noindex=False, refresh=None):
    R = depth_prefix(path)
    canon = BASE + ("/" + name if name else "/")
    nav = "".join(f'<a href="{link(n, R)}"{" aria-current=page" if n == name else ""}>{t}</a>' for n, t in NAV)
    robots = '<meta name="robots" content="noindex,follow">' if noindex else ""
    ogimg = f'<meta property="og:image" content="{BASE}/{og}">' if og else ""
    refresh_tag = f'<meta http-equiv="refresh" content="0; url={refresh}">' if refresh else ""
    m_cta = re.search(r'<section class="cta">.*?</section>', body, re.S)
    cta_html = m_cta.group(0) if m_cta else ""
    main_body = body.replace(cta_html, "") if m_cta else body
    foot_nav = "".join(f'<li><a href="{link(n, R)}">{t}</a></li>' for n, t in NAV)
    out = f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canon}">
{robots}{refresh_tag}
<meta property="og:type" content="website"><meta property="og:locale" content="de_DE">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{canon}">
{ogimg}
<link rel="icon" href="{R}favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="{FONTS.split('/css')[0]}" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="{R}css/styles.css?v={VERSION}">
{extra}
</head>
<body>
<header class="kopf"><div class="wrap">
  <a class="logo" href="{link("", R)}">{NAME}</a>
  <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav">Menü</button>
  <nav class="nav" id="nav" aria-label="Hauptmenü">{nav}<a class="btn" href="{link("kontakt", R)}">Anfragen</a></nav>
<div class="progress" aria-hidden="true"><span></span></div></header>
<main>
{main_body}
</main>
<div class="endblock">
<figure class="endbg"><img src="{R}img/konferenz-menschen-fokus-beteiligung.jpg" alt="" loading="lazy"></figure>
{cta_html}
<footer><div class="wrap">
  <div><b>{NAME}</b>Graphic Recording, Facilitation und Kulturentwicklung in Freiburg, Baden-Württemberg und Süddeutschland.</div>
  <div><b>Seiten</b><ul>{foot_nav}<li><a href="{link("kontakt", R)}">Kontakt</a></li></ul></div>
  <div><b>Kontakt</b><ul><li><a href="mailto:kontakt@jakob-kohlbrenner.de">kontakt@jakob-kohlbrenner.de</a></li><li><a href="tel:+4915775353250">+49 157 75353250</a></li><li><a href="https://linkedin.com/in/jakob-kohlbrenner-58133414a" rel="noopener">LinkedIn</a></li></ul></div>
  <div class="small">© {NAME} · <a href="{link("impressum", R)}">Impressum</a> · <a href="{link("datenschutz", R)}">Datenschutz</a></div>
</div></footer>
</div>
<script src="{R}js/main.js?v={VERSION}"></script>
</body>
</html>
'''
    return out


def fill(body, R):
    prs = [p for p in projekte()]
    reale = [p for p in prs if not p.get("platzhalter")]
    body = re.sub(r"\{\{L:([^}]*)\}\}", lambda m: link(m.group(1), R), body)
    body = body.replace("{{PROJEKT_TEASER}}", "".join(tile(p, R) for p in reale[:6]))
    body = body.replace("{{PROJEKT_ALLE}}", "".join(tile(p, R) for p in prs))
    body = re.sub(r"\{\{FAQ:([^}]*)\}\}", lambda m: faq_html(m.group(1)), body)
    body = re.sub(r"\{\{CTA:([^|}]*)\|([^|}]*)\|([^}]*)\}\}", lambda m: cta(m.group(1), m.group(2), m.group(3), R), body)
    return body.replace("{{R}}", R)


def project_page(i, p, reale):
    R = depth_prefix(p["pfad"])
    aside = ""
    for label, key in [("Ort", "ort"), ("Format", "format"), ("Zeitraum", "zeit")]:
        if p.get(key):
            aside += f"<div><b>{label}</b>{esc(p[key])}</div>"
    tags = "".join(f"<span>{esc(f)}</span>" for f in p["filter"])
    paras = "".join(f"<p>{esc(a)}</p>" for a in p["absaetze"])
    pics = "".join(f'<figure class="ph"><img src="{R}img/{fn}" alt="{esc(p["titel"])}" loading="lazy"></figure>' for fn in p["bilder"])
    prev, nxt = reale[i - 1], reale[(i + 1) % len(reale)]
    stimme = ""
    if p.get("stimme"):
        st = p["stimme"]
        stimme = f'<figure class="quote stimme"><p>„{esc(st["text"])}“</p><cite><b>{esc(st["von"])}</b>{esc(st["rolle"])}</cite></figure>'
    sections = "".join(f'<h2>{esc(h)}</h2><p>{esc(t)}</p>' for h, t in p.get("abschnitte", []))
    body = f'''<section class="hero">
  <figure class="hero-bg"><img src="{R}img/{p["thumb"]}" alt="{esc(p["titel"])}" fetchpriority="high"></figure>
  <div class="wrap"><div>
    <a class="backlink" href="{link("projektgalerie", R)}">← Alle Projekte</a>
    <h1>{esc(p["titel"])}</h1><div class="tags">{tags}</div>
  </div></div>
</section>
<section><div class="wrap projekt-body">
  <aside>{aside}</aside>
  <div class="prose"><p class="zitat">„{esc(p["zitat"])}“</p>{paras}{sections}{stimme}</div>
</div></section>
<section><div class="wrap"><div class="masonry">{pics}</div>
  <div class="prevnext"><a href="{link(prev["pfad"], R)}">← {esc(prev["titel"])}</a><a href="{link(nxt["pfad"], R)}">{esc(nxt["titel"])} →</a></div></div></section>
{cta("Ein ähnliches Projekt?", "Erzähl mir von deiner Veranstaltung. Das Erstgespräch ist kostenfrei.", "Jetzt anfragen →", R)}'''
    title = f'{p["titel"]} | {NAME}'
    desc = (p["absaetze"][0][:150].rsplit(" ", 1)[0] + " …") if len(p["absaetze"][0]) > 155 else p["absaetze"][0]
    og = f'img/{p["thumb"]}'
    return shell(p["pfad"], p["pfad"], title, desc, body, og=og)


def main():
    urls = []
    for path, content, title, desc, og in PAGES:
        R = depth_prefix(path)
        body = fill(read(f"_content/{content}.html"), R)
        extra = ""
        if content == "index":
            extra = jsonld(person_ld())
        elif content in FAQ:
            extra = jsonld(faq_ld(content))
        out = shell(path, path, title, desc, body, og=og, extra=extra, noindex=content in NOINDEX)
        write((path or "index") + ".html", out)
        if content not in NOINDEX:
            urls.append(path)
    reale = [p for p in projekte() if not p.get("platzhalter")]
    for i, p in enumerate(reale):
        write(p["pfad"] + ".html", project_page(i, p, reale))
        urls.append(p["pfad"])
    # Alte Adresse /angebote-1 war eine Kopie von /graphic-recording
    write("angebote-1.html", shell("angebote-1", "graphic-recording", "Graphic Recording | Jakob Kohlbrenner", "Weiterleitung zu Graphic Recording.",
          f'<section><div class="wrap"><p><a class="textlink" href="{link("graphic-recording", "")}">Weiter zu Graphic Recording</a></p></div></section>',
          noindex=True, refresh=link("graphic-recording", "")))
    write("404.html", shell("404", "404", "Seite nicht gefunden | " + NAME, "Diese Seite gibt es nicht.",
          f'<section><div class="wrap narrow"><h1>Diese Seite gibt es nicht.</h1><p class="lead" style="margin-top:16px">Vielleicht hilft dir der Weg über die <a class="textlink" href="{link("", "/")}">Startseite</a> oder die <a class="textlink" href="{link("projektgalerie", "/")}">Projekte</a>.</p></div></section>',
          noindex=True))
    # Sitemap, robots, llms.txt
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sm += [f"<url><loc>{BASE}/{u}</loc></url>" for u in urls]
    sm.append("</urlset>")
    write("sitemap.xml", "\n".join(sm) + "\n")
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
    write("llms.txt", f"""# Jakob Kohlbrenner

> Graphic Recording, Generative Scribing, Dialog-Facilitation und Kulturentwicklung für Konferenzen, Workshops und Organisationen. Arbeitsort Freiburg (Ehrenkirchen), tätig in Baden-Württemberg und Süddeutschland, auch digital.

## Angebote
- Graphic Recording und Generative Scribing (Live-Visualisierung): {BASE}/graphic-recording
- Dialog-Facilitation und Art of Hosting: {BASE}/facilitation
- Kulturentwicklung: {BASE}/kulturentwicklung
- Projekte: {BASE}/projektgalerie

## Kontakt
- kontakt@jakob-kohlbrenner.de, +49 157 75353250
- Kostenfreies Erstgespräch: {BASE}/kontakt
""")
    print("gebaut:", len(urls), "Seiten", "(prod)" if PROD else "(Vorschau)")


if __name__ == "__main__":
    main()
