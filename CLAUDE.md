# Hinweise für Änderungen an dieser Website (jakob-kohlbrenner.de)

- Live ist der Branch `main` (GitHub Pages). Domain bleibt `jakob-kohlbrenner.de`; sie zeigt bis zur Umstellung noch auf Squarespace. Nicht am DNS ändern, bevor Jakob es sagt.
- **Adressen dürfen sich nicht ändern** (Google-Platzierung). Alle bisherigen Pfade der Squarespace-Seite bleiben bestehen, auch `projektgalerie/blog-post-title-four-yzrk6…`. Neue Projekte bekommen sprechende Pfade.
- Aufbau: Seiten stehen als Fragmente in `_content/*.html`, Projekte in `_tools/projekte.json`, gemeinsame Vorlage (Kopf, Fuß, Titel, SEO-Daten, FAQ) in `_tools/build.py`. Die HTML-Dateien im Hauptordner werden daraus erzeugt: nie direkt bearbeiten.
- Bauen: `python3 _tools/build.py --prod` für die Live-Version (Links ohne `.html`). Ohne `--prod` entsteht die Vorschau mit `.html`-Links.
- Bei Änderungen an `css/styles.css` oder `js/main.js` `VERSION` in `_tools/build.py` hochzählen.
- Änderungen immer bei 1280 px (Desktop) und 390 px (Handy) prüfen.
- Fokus der Seite: Graphic Recording (Hauptgeschäft, SEO-Schwerpunkt Freiburg, Baden-Württemberg, Süddeutschland). Darunter Facilitation, Kulturentwicklung, strategische Visualisierung.
- Seit 2017 tätig. Schreibweise: „seit 2017“, nicht „zehn Jahre“, bis 2027.
- Essential Guidance ist vorerst nicht verlinkt (kommt später mit anderem Titel zurück).
- Inhaltstexte nie ungefragt umschreiben, nur Vorschläge machen. Bestehende Texte stammen von der alten Squarespace-Seite.
- Projekte brauchen echte Angaben (Ort, Kunde, Jahr, Teilnehmende) und Freigaben für Namen, Logos und erkennbare Personen. Nichts erfinden.
- FAQ-Texte stehen in `_tools/build.py` und werden zusätzlich als FAQPage-JSON-LD ausgegeben. Beides kommt aus derselben Quelle.
- Mail: kontakt@jakob-kohlbrenner.de. Telefon +49 157 75353250. Buchung: Calendly-Link in `_content/kontakt.html`.
- Impressum: USt-ID nur eintragen, wenn Jakob sie liefert. Keine Nummern erfinden. Datenschutz ist ein Entwurf und braucht rechtliche Prüfung.
- Projektstand und offene To-dos: `_projekt/STAND.md` (Unterstrich: wird nicht ausgeliefert, aber das Repo ist öffentlich, keine Geheimnisse hineinschreiben).
