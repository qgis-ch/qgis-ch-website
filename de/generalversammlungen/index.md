---

layout: threecol-de
lang: de

---

# Generalversammlungen

QGIS ist eine GIS Plattform bestehend aus den Komponenten Desktop-GIS, Server-GIS, Web-GIS Client und Mobile-GIS. QGIS Desktop ist eine benutzerfreundliche GIS Anwendung für das Erstellen von Karten und Layouts, das Bearbeiten und Analysieren von Geodaten. Bisher ist es beschränkt auf 2d und 2.5d Daten und Darstellungen. Es bestehen erste 3D-Komponenten, diese sind jedoch noch als experimentell zu bezeichnen. QGIS ist erweiterbar mit Hilfe der Sprachen Python und C++ und basiert auf der qt-Bibliothek von Digia.

Die QGIS Anwendergruppe Schweiz ist ein Verein der QGIS Anwender in der Schweiz. Es ist ein Verein im Sinne des schweizerischen Zivilgesetzbuches gemäss Artikel 60-79. Derzeit gibt es circa 50 Mitglieder aus Behörden, Firmen, Universitäten und Einzelpersonen.

<iframe width="560" height="315" src="https://www.youtube.com/embed/rYqGYfUMfiw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

{% for p in site.pages %}
  {% if p.path contains "veranstaltungen" %}
    {{ p.title }} {{ p.url }}
  {% endif %}
{% endfor %}

