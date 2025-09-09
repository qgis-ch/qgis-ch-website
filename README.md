# Webseite QGIS Anwendergruppe Schweiz

In diesem Repository wird die [Webseite der QGIS Anwendergruppe Schweiz](https://www.qgis.ch) gepflegt und weiter entwickelt.
Die Webseite wird mit [Jekyll](https://jekyllrb.com/) umgesetzt.

## Organisation der Webseite

Die Webseite ist zweisprachig mit Deutsch und Französisch umgesetzt. Hinzufügen von weiteren Sprachen ist technisch vorbereitet.

Sämtliche deutschen Seiten sind im Verzeichnis *de* organisiert. Jedes Unterverzeichnis von *de* entspricht einem Menüpunkt der Seite.

Analog dazu sind auch die französischen Seiten im Verzeichnis *fr* strukturiert.

### Publizieren von Neuigkeiten

Neuigkeiten werden wie folgt publiziert:

* Übersicht der Artikeln mit Einleitungstext auf der Startseite
* als Artikel unter *YYYY/mm/dd/title.html*
* im Atom Feed unter *feed.xml* zweisprachig

Um einen neuen Eintrag hinzuzufügen, muss für jede Sprache eine neue Seite unter *_posts* erstellt werden mit einem Dateinamen gemäss folgendem Schema: *YYYY-mm-dd-deutscher-kurz-titel.md* für deutsch und *YYYY-mm-dd-titre-court-francais.md* für französisch.

In diesen Seiten müssen im Dateikopf noch die entsprechenden Metadaten gesetzt werden:

```
---
lang: fr
excerpt: >-
  Nous avons le plaisir d'annoncer la sortie de QGIS 3.34 Prizren !
  Les installateurs pour Windows et Linux sont déjà disponibles.
title: QGIS 3.34 Prizren sortie!
---
```

Erklärung der Parameter:

* *lang*: *de* oder *fr* für die Sprache
* *excerpt*: Einleitungstext, welcher auf der Übersichtsseite erscheint
* *title*: Titel des Eintrags

### Publizieren von neuen Kurs- oder Veranstaltungsdaten

Im Menüpunkt *Kurse* werden Kurse oder Veranstaltungen über QGIS publiziert, welche **nicht** vom Verein angeboten oder durchgeführt werden. Es dürfen auch "QGIS-verwandte" Veranstaltungen eingetragen werden wie z.B. Kurse zu PostGIS.

Kurse können von Anbieter direkt eingetragen werden, dazu kann die Tabelle _data/kurse-cours.csv direkt im Repository bearbeitet werden und anschliessend ein Pull Request gestellt werden.

Die Tabelle ist im CSV Format:

1. Spalte *date*: Datum im Format dd.mm.YYYY
2. Spalte *title_de*: Kurzbeschreibung auf Deutsch
3. Spalte *title_fr*: Kurzbeschreibung auf Französisch
4. Spalte *url*: Link zu Webseite des Anbieters mit mehr Informationen

Wichtig: Falls die Kurzbeschreibung ein Komma beinhaltet, muss diese in Anführungszeichen stehen!

## Lokal testen und erweitern

### Mit lokaler Installation

* Installation von Jekyll gemäss [Jekyll Dokumentation](https://jekyllrb.com/docs/installation/).
* Kopieren des Quellcodes von GitHub: `git clone git@github.com:qgis-ch/qgis-ch-website.git`
* Wechseln in Verzeichnis der Webseite: `cd qgis-ch-website`
* Starten des Webservers: `bundle exec jekyll serve --livereload`
* Anschliessend ist die Website unter [localhost:4000](http://localhost:4000/) erreichbar.

### Mit Docker

* Kopieren des Quellcodes von GitHub: `git clone git@github.com:qgis-ch/qgis-ch-website.git`
* Wechseln in Verzeichnis der Webseite: `cd qgis-ch-website`
* Baue das Docker Image mit `docker compose build`
* Starte den Docker Container im Verzeichnis mit `docker compose up`
* Öffne im Browser die Website unter [localhost:4000](http://localhost:4000/)

## Deployment

Die Seite wird mit jedem *Push* in den *main* Branch neu gebaut und direkt auf den Webserver kopiert.



