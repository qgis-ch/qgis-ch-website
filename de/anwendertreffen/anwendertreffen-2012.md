---

title: "Anwendertreffen 2012 Bern"
year: 2012
date: "04.06.2012
von 09:00- 17:00"
location: "Bern"

---

# Anwendertreffen 2012 Bern

Das Anwendertreffen 2012 war das 3. Treffen der QGIS Anwendergruppe Schweiz und fand am 04. Juni 2012 in Bern statt.
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

**Datum:** Montag, 4. Juni 2012, 9:00 bis 17:00

**Ort:** Universität Bern, Gebäude UniS, Schanzeneckstrasse 1.

**Anreise:** Der Veranstaltungsort ist unmittelbar oberhalb des Hauptbahnhofs in Bern. Wir empfehlen die Anreise mit öffentlichen Verkehrsmitteln. Wenn Sie mit dem Auto anreisen können Sie das Parkhaus des Bahnhofs Bern benutzen.

Vom Hauptbahnhof den Ausgang West "Die Welle" benutzen und Richtung Schanzenstrasse/Länggasse gehen. Links in die Schanzeneckstrasse einbiegen. Das Gebäude ist im Quartierplan mit der Nr. 1 bezeichnet.

**Kosten:** Die Teilnahme an den Vorträgen/Präsentationen am Vormittag ist kostenfrei, für die Workshops wird eine Workshopgebühr von CHF 100.- erhoben.

**Verpflegung:** Begrüssungskaffee am Morgen, Kaffeepausen am Vormittag und Nachmittag (kostenfrei, gesponsert). Mittagessen (kleiner Lunch) für Workshopteilnehmer inbegriffen.

**Sponsoren:** Firma [Sourcepole](http://www.sourcepole.ch/) (Zürich), Firma [Camptocamp](http://www.camptocamp.com/) (Lausanne)

**Anmeldung:** nicht mehr aktiv.

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
{% for p in site.data.anwendertreffen-2012 %}
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

Am Nachmittag finden 3 Workshops zu je 2.5-3 Stunden statt. Dafür wird eine Workshop-Gebühr eingehoben, die zur Finanzierung der Raummiete und für die teilweise Rückvergütung von Fahrtspesen von Referenten verwendet wird.

Folgende Workshops werden angeboten:

* Kartografie, Symbolisierung und Kartenlayout mit QGIS (A. Neumann, O. Dassau) - im Computerlab der Uni Bern
* QGIS Python Plugin Entwicklung (H. Düster, M. Walker)  - eigenen Laptop mitnehmen!
* QGIS Server und QGIS Webclient (M. Hugentobler, P. Kalberer) - Rechner werden zur Verfügung gestellt.
* Lab-Session: QGIS auf Android (Tablets, Telefone) (M. Bernasocchi) - eigene Android-Geräte mitbringen!

Für den Workshop "Python Plugin Entwicklung" bringen Sie bitte eigene Laptops mit. Für die beiden anderen Workshops werden Rechner zur Verfügung gestellt. Für die Lab-Session "QGIS auf Android" bringen Sie bitte eigene Tablets und Android-Telefone mit.