# Jakob Kohlbrenner: Projektstand und offene Punkte

Stand: 27. Oktober 2026. Die neue Seite läuft auf GitHub Pages (koojaa92.github.io/Jakob-Kohlbrenner). Unter jakob-kohlbrenner.de ist weiter die Squarespace-Seite live.

## Was steht
- Mehrseitige statische Website (HTML, CSS, JS) aus `_content/*.html`, `_tools/projekte.json` und `_tools/build.py`.
- Bisherige Seiten mit alten Pfaden, Projektgalerie mit 7 echten Projekten und 2 Platzhaltern, alle 90 Bilder der alten Seite.
- Neu: Seite `strategische-visualisierung` (Entwurf aus den bisherigen Texten).

## Offene Punkte
- [ ] Neues Repo anlegen und diese Dateien dorthin übernehmen. Dort `CLAUDE.md` nach dem Playbook.
- [ ] Strategische Visualisierung: Was genau bietest du an (Formate, Dauer, Preislogik)? Aktuell nur Umstellung vorhandener Texte, nichts Neues erfunden.
- [ ] Harvesting „Tonspur“ (Zusammenfassung): in eigenen Worten beschreiben.
- [ ] Zahlen für „seit 2017“: Einsätze, Orte, Kunden (nur echte Zahlen).
- [ ] Projektbilder und Projektinfos (Anlass, Ort, Kunde, Jahr, Teilnehmende, Freigaben).
- [ ] Marktanalyse der Kolleginnen und Kollegen, Keyword-Auswertung.
- [ ] Domain: Registrar prüfen (Squarespace), Search Console prüfen, erst dann umziehen.
- [ ] Datenschutz und Impressum rechtlich prüfen.
- [ ] Schreibweisen klären: Siepmann/Siebmann, „Führungskolleg“.

## Entschieden (27.10.)
- Entwurf gefällt (modern, schneller greifbar). Feinschliff bei Farben, Abständen und klaren Angeboten kommt später, Jakob meldet sich.
- „Kulturentwicklung“ ist als Schlagwort nicht stark. Stattdessen „Organisationsentwicklung“ prüfen (Seitenname, Menü, Titel). Pfad `/kulturentwicklung` bleibt wegen der Google-Platzierung bestehen.
- SEO für Graphic Recording in Freiburg und Süddeutschland, dazu Vergleich mit Kolleginnen und Kollegen (Marktanalyse, Keywords).
- Essential Guidance vorerst raus, kommt später mit anderem Titel als Verlinkung zurück.

## Marktanalyse (noch offen)
- Region Freiburg: Nils Theurer, Lumilla Bartsch, Christina (Nachname offen).
- Deutschsprachig: Kommunikationslotsen, Visual Facilitators, Malte von Diesenhausen, Robin Hutz, Marie-Pascal Gaffinen, Sabina Söder.
- Ziel: Keywords (Graphic Recording, Live-Visualisierung, Live-Zeichner, Scribing, Sketchnotes u. a.), was die Seiten zeigen und was fehlt. Google Trends: Interesse an „Graphic Recording“ seit 2022 stabil, „Sketchnotes“ seit 2021 stark gefallen.

## Design-Runde 28.10. (umgesetzt)
- Ruhigere Farben: Petrol als einzige Akzentfarbe, Sandton für Hervorhebungen, dünne ockerfarbene Fortschrittslinie unter dem Menü.
- Jede Seite startet mit einem Vollbild-Hintergrundbild. Bild und Text nebeneinander sind gleich hoch. Abschnitte wechseln automatisch zwischen hell und grau.
- Schriften kleiner, Stimmen ruhiger. Aufruf am Ende und Fuß bilden einen dunklen Block mit Bild.
- Logo nur als Name in einer Zeile. Startseite zeigt bis zu 6 Projekte.
- Projektseiten haben Platz für Abschnitte (`abschnitte` in `_tools/projekte.json`) und eine Kundenstimme (`stimme`).

## Offen für längere Projektbeschreibungen
- [ ] Pro Projekt: Anlass, Aufgabe, Vorgehen, Ergebnis, Zitat, Zahl der Teilnehmenden, Jahr, Freigaben. Ohne diese Angaben bleiben die Texte bei den bisherigen kurzen Beschreibungen.
- [ ] Weitere Projekte samt Bildern (Ordner je Projekt mit `info.txt`).
