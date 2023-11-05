---

title: "Anwendertreffen 2015 Bern"
year: 2015

---

# Anwendertreffen 2015 Bern

Das Anwendertreffen 2015 war das 6. Treffen der QGIS Anwendergruppe Schweiz und fand am 10. Juni 2015 in Bern statt.
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

**Datum:** Mittwoch, 10. Juni 2015, 9:00 bis 17:00

**Ort:** [Universität Bern, Gebäude UniS, Schanzeneckstrasse 1](http://www.bau.unibe.ch/plaene/hgexwiunis.htm){: .external-link :}

**Anreise:** Der Veranstaltungsort ist unmittelbar oberhalb des Hauptbahnhofs in Bern. Wir empfehlen die Anreise mit öffentlichen Verkehrsmitteln. Wenn Sie mit dem Auto anreisen können Sie das Parkhaus des Bahnhofs Bern benutzen.

Vom Hauptbahnhof den Ausgang West "Die Welle" benutzen und Richtung Schanzenstrasse/Länggasse gehen. Links in die Schanzeneckstrasse einbiegen. Das Gebäude ist im [Quartierplan](http://www.bau.unibe.ch/plaene/vorlaeng_areal2.gif) mit der Nr. 1 bezeichnet.

**Kosten:** Die Teilnahme an den Vorträgen/Präsentationen am Vormittag ist kostenfrei, für die Workshops wird eine kleine Workshopgebühr erhoben. MitgliederInnen der QGIS Anwendergruppe Schweiz: CHF 100.-, Nicht-Mitglieder: CHF 150.-, Studierende: CHF 50.- Die Workshop-Preise beinhalten einen kleinen Lunch (Sandwiches).

**Verpflegung:** Kaffeepausen am Vormittag und Nachmittag. Mittagessen (kleiner Lunch) für Workshopteilnehmer inbegriffen.

**Anmeldung:**  [Anmeldeformular](https://docs.google.com/forms/d/1O5axIuC7FdFIgnm_oRagx1wPdLH08hSaU_Zb3ztw6es/viewform?usp=send_form){: .external-link :} (Google Docs) mit Zahlungsinformationen (Zahlung nur für Workshops)

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
{% for p in site.data.anwendertreffen-2015 %}
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

Bitte bringen Sie zu den Workshops eigene Laptops mit vorinstalliertem QGIS 2.8 mit.

### Workshop A: QGIS Processing Workshop

In diesem Workshop wird der "Verarbeitungs"-(Analyse)-Teil von QGIS eingeführt. Die Werkzeugkiste erlaubt das Ausführen von Analysen und Algorithmen von anderen Open Source GIS Projekten wie GRASS, SAGA oder anderen. Zusätzlich wird der grafische Modellierer vorgestellt und beübt. Damit können verschiedene Arbeitsschritte automatisiert werden und auf verschiedenen Datensätzen angewandt werden.

Workshop-Instruktor: Andreas Neumann

### Workshop B: Digitalisier- und Konstruktionsworkshop, inkl. Qualitätsprüfung

Es werden die verfügbaren Digitalisier- und Konstruktionswerkzeuge, sowie die Fangeinstellungen im QGIS Kern gezeigt und beübt. Ausserdem werden ausgewählte Plugins (wie Digitizing Tools, CAD Input) vorgestellt. Schliesslich wird gezeigt wie ausgewählte Qualitätsprüfungen durchgeführt werden können.

Workshop-Instruktor: Bernhard Ströbl
