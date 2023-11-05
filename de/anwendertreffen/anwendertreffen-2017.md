---

title: "Anwendertreffen 2017 Bern"
year: 2017
date: "21.06.2017
von 08:30- 17:00"
location: "Bern"

---

# Anwendertreffen 2017 Bern

Das Anwendertreffen 2017 war das 8. Treffen der QGIS Anwendergruppe Schweiz und
fand am 21. Juni 2017 in Bern statt.
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

**Datum:** Mittwoch, 21. Juni 2017, 9:00 bis 17:00

**Ort:** [Universität Bern, Gebäude UniS, Schanzeneckstrasse 1](http://www.bau.unibe.ch/plaene/hgexwiunis.htm){: .external-link :}

**Sprache:** gemischt (deutsch, französisch, englisch), je nach Herkunft des Referenten

**Anreise:** Der Veranstaltungsort ist unmittelbar oberhalb des Hauptbahnhofs in
Bern. Wir empfehlen die Anreise mit öffentlichen Verkehrsmitteln. Wenn Sie mit
dem Auto anreisen können Sie das Parkhaus des Bahnhofs Bern benutzen.

Vom Hauptbahnhof den Ausgang West "Die Welle" benutzen und Richtung
Schanzenstrasse/Länggasse gehen. Links in die Schanzeneckstrasse einbiegen. Das
Gebäude ist im [Quartierplan](http://www.bau.unibe.ch/plaene/vorlaeng_areal2.gif){: .external-link :}
mit der Nr. 1 bezeichnet.

**Kosten:** Die Teilnahme an den Vorträgen/Präsentationen am Vormittag ist kostenfrei, für die Workshops wird eine kleine Workshopgebühr erhoben. MitgliederInnen der QGIS Anwendergruppe Schweiz: CHF 100.-, Nicht-Mitglieder: CHF 150.-, Studierende: CHF 50.- Die Workshop-Preise beinhalten einen kleinen Lunch (Sandwiches).

**Verpflegung:** Kaffeepausen am Vormittag und Nachmittag. Mittagessen (kleiner Lunch) für Workshopteilnehmer inbegriffen.

**Anmeldung:**  [Anmeldeformular mit Zahlungsinformationen](https://docs.google.com/forms/d/e/1FAIpQLSeaywil8HXvpJrP7EEMKjeK0rU9Ya_pLEzvxL7NMO8DdmPI8A/viewform){: .external-link :} (Google Forms)

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
{% for p in site.data.anwendertreffen-2017 %}
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

Bitte bringen Sie zu den Workshops eigene Laptops mit vorinstalliertem QGIS mit.

Workshop A: benötigt QGIS 2.18 und 1 Android-Tablet (oder Telefon mit grösserem
Bildschirm)

Workshop B: benötigt QGIS 2.18
