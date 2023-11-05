---

title: "Anwendertreffen 2016 Bern"
year: 2016

---

# Anwendertreffen 2016 Bern

Das Anwendertreffen 2016 war das 7. Treffen der QGIS Anwendergruppe Schweiz und fand am 15. Juni 2016 in Bern statt.
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

**Datum:** Mittwoch, 15. Juni 2016, 9:00 bis 17:00

**Ort:** [Universität Bern, Gebäude UniS, Schanzeneckstrasse 1](http://www.bau.unibe.ch/plaene/hgexwiunis.htm){: .external-link :}

**Sprache:** gemischt (deutsch, französisch, englisch), je nach Herkunft des Referenten

**Anreise:** Der Veranstaltungsort ist unmittelbar oberhalb des Hauptbahnhofs in Bern. Wir empfehlen die Anreise mit öffentlichen Verkehrsmitteln. Wenn Sie mit dem Auto anreisen können Sie das Parkhaus des Bahnhofs Bern benutzen.

Vom Hauptbahnhof den Ausgang West "Die Welle" benutzen und Richtung Schanzenstrasse/Länggasse gehen. Links in die Schanzeneckstrasse einbiegen. Das Gebäude ist im [Quartierplan](http://www.bau.unibe.ch/plaene/vorlaeng_areal2.gif) mit der Nr. 1 bezeichnet.

**Kosten:** Die Teilnahme an den Vorträgen/Präsentationen am Vormittag ist kostenfrei, für die Workshops wird eine kleine Workshopgebühr erhoben. MitgliederInnen der QGIS Anwendergruppe Schweiz: CHF 100.-, Nicht-Mitglieder: CHF 150.-, Studierende: CHF 50.- Die Workshop-Preise beinhalten einen kleinen Lunch (Sandwiches).

**Verpflegung:** Kaffeepausen am Vormittag und Nachmittag. Mittagessen (kleiner Lunch) für Workshopteilnehmer inbegriffen.

**Anmeldung:**  [Anmeldeformular](https://docs.google.com/forms/d/1dTnfQrI2xFbZwptgy3qXwDN0HFJZtbYZNVPgsgP1XK8/viewform?usp=send_form){: .external-link :} (Google Docs) mit Zahlungsinformationen (Zahlung nur für Workshops)

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
{% for p in site.data.anwendertreffen-2016 %}
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

Bitte bringen Sie zu den Workshops eigene Laptops mit vorinstalliertem QGIS 2.14 mit.

Workshop A: benötigt neben QGIS (2.14 oder Master Nightly oder Weekly Build) auch eine PostGIS Installation, Java und ili2pg. [Die Unterlagen für diesen Workshop finden Sie hier](https://sogeo.services/slides/qgis_anwendertreffen/2016-qgis-ili2pg-workshop_v02_11pt.pdf){: .external-link :}.

Workshop B: bitte bringen Sie falls möglich parallel zu QGIS 2.14 eine Snapshot-Version von QGIS 2.15 an den Workshop mit (Entwicklerversion, Preview von Version 2.16). Einige Beispiele im Workshop werden auf diese Version abzielen. [Bitte installieren Sie die neueste Weekly Version](http://qgis.org/downloads/weekly/?C=M;O=D){: .external-link :} möglichst kurz vor dem Workshop.
