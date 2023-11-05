---

title: "Anwendertreffen 2014 Bern"
year: 2014

---

# Anwendertreffen 2014 Bern

Das Anwendertreffen 2014 war das 5. Treffen der QGIS Anwendergruppe Schweiz und fand am 18. Juni 2014 in Bern statt.
{: .alert .alert-secondary :}

## Ziele

* Information über aktuelle Arbeiten im QGIS-Projekt
* Austausch unter QGIS Anwendern und Networking
* Kontakt zwischen Anwendern und Entwicklern
* Vorstellung der neuen Features in der aktuellen Entwickler-Version
* Vorstellung aktueller Case Studies
* Koordination zukünftiger Entwicklungen

## Organisation

**Veranstalter:** QGIS-Anwendergruppe Schweiz

**Kontakt:** info (at) qgis (dot) ch

**Datum:** Mittwoch, 18. Juni 2014, 9:00 bis 17:00

**Ort:** [Universität Bern, Gebäude UniS, Schanzeneckstrasse 1](http://www.bau.unibe.ch/plaene/hgexwiunis.htm){: .external-link :}

**Anreise:** Der Veranstaltungsort ist unmittelbar oberhalb des Hauptbahnhofs in Bern. Wir empfehlen die Anreise mit öffentlichen Verkehrsmitteln. Wenn Sie mit dem Auto anreisen können Sie das Parkhaus des Bahnhofs Bern benutzen.

Vom Hauptbahnhof den Ausgang West "Die Welle" benutzen und Richtung Schanzenstrasse/Länggasse gehen. Links in die Schanzeneckstrasse einbiegen. Das Gebäude ist im [Quartierplan](http://www.bau.unibe.ch/plaene/vorlaeng_areal2.gif) mit der Nr. 1 bezeichnet.

**Kosten:** Die Teilnahme an den Vorträgen/Präsentationen am Vormittag ist kostenfrei, für die Workshops wird eine kleine Workshopgebühr erhoben. MitgliederInnen der QGIS Anwendergruppe Schweiz: CHF 100.-, Nicht-Mitglieder: CHF 150.-, Studierende: CHF 50.- Die Workshop-Preise beinhalten einen kleinen Lunch (Sandwiches).

**Verpflegung:** Kaffeepausen am Vormittag und Nachmittag. Mittagessen (kleiner Lunch) für Workshopteilnehmer inbegriffen.

**Anmeldung:**  [Anmeldeformular](https://docs.google.com/spreadsheet/viewform?fromEmail=true&formkey=dHNoTTFHVGtMSjVmbHFsVERvR2lNVGc6MA){: .external-link :} (Google Docs) mit Zahlungsinformationen (Zahlung nur für Workshops)

## Programm

<table class="table table-striped">
  <thead>
    <tr>
      <th scope="col">Zeit</th>
      <th scope="col">Vortrag</th>
      <th scope="col">Referent(en)</th>
    </tr>
  </thead>
  <tbody>
{% for p in site.data.anwendertreffen-2014 %}
    <tr>
      <td>{{ p.time }}</td>
      {% if p.url %}
      <td>
        {% assign prefix = p.url | slice: 0,5 %}
        {% if prefix != "https" %}
        <a href="{% link {{ p.url }} %}" class="pdf-link">{{ p.presentation }}</a>
        {% else %}
        <a href="{{ p.url }}" class="external-link">{{ p.presentation }}</a>
        {% endif %}
      </td>
      {% else %}
      <td>{{ p.presentation }}</td>
      {% endif %}
      <td>{{ p.presenter }}</td>
    </tr> 
{% endfor %}
  </tbody>
</table>

## Workshops

Bitte bringen Sie zu den Workshops eigene Laptops mit vorinstalliertem QGIS 2.2 oder QGIS 2.3/2.4 (Entwicklerversion) mit.

### A: Tabellen, Formulare, Widgets und Datenbankrelationen

In QGIS 2.0 wurden die Attribut-Tabelle und die Formularansicht in ein gemeinsames Fenster zusammengelegt. Gleichzeitig wurden neue Filter- und Selektionsmöglichkeiten zur Verfügung gestellt. In QGIS 2.2 wurden 1:n Datenbankrelationen eingeführt und die zughörigen einbettbaren Formulare. In QGIS 2.4 wurde das Widgetsystem auf eine neue und flexiblere technologische Basis gestellt. Im Workshop wird der Umgang mit Tabellen, Formularen, Datenbankrelationen, Widgets, dem Feldrechner und Expressions gezeigt. Anhand eines Beispiels wird eine "Mini-Fachschale" mit einem einfachen Datenmodell erstellt. Im Workshop soll auch diskutiert werden in welche Richtung sich die Formular- und Datenbankrelations-Technik in zukünftigen QGIS-Versionen weiterentwickeln soll.

Workshop-Instruktoren: Matthias Kuhn, Denis Rouzaud

### B: Print Composer und Atlas-Seriendruck

Im Workshop wird gezeigt welche Neuerungen es im Print Composer in den Versionen 2.2 und 2.4 gegeben hat. Anhand von vorbereiten Beispielen wird die Erstellung von Kartenlayouts geübt. Es wird gezeigt wie mit der Seriendruckfunktion einfache "Atlanten" erstellt werden können. Atlanten können über alle Objekte einer Tabelle oder über eine vorbereitete Tabelle mit Blattschnitten erstellt werden. In Beispielen wird geübt wie im Atlas-Druck Objekte hervorgehoben oder weggefiltert werden können. Mit Hilfe der Atlas-Seriendruckfunktion können auch einfache Datenblätter oder Berichte generiert werden welche Text, Tabellen oder Fotos beinhalten. Mit Hilfe von HTML-Elementen können diese flexibel gestaltet werden. Es wird auch ein Ausblick auf zukünftige Funktionen geben, sowie eine Diskussion über gewünschte Funktionen in den Bereichen Kartenlayout, Seriendruck und Reporting.

Workshop-Instruktor: Andreas Neumann

### C: QGIS Cloud und QGIS Server

QGIS Server ist seit einiger Zeit nicht nur ein WMS-Server (fertig symbolsierte Karten), sondern auch ein WFS-Server (Web-Feature-Server für Original Vektordaten) und ein WCS (Web-Coverage Server für Original Rasterdaten). Bestehende QGIS Desktop-Projekte können bequem für die Publikation im Web-GIS oder Geowebdienste aus QGIS-Desktop heraus konfiguriert werden. Das QGIS Cloud Plugin erlaubt die Publikation eines QGIS-Projekts ohne eigene Serverinfrastruktur.

Workshop-Instruktoren: Pirmin Kalberer, Horst Düster, Marco Hugentobler