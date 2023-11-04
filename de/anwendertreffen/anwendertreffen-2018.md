---

layout: plain-de
lang: de
title: "Anwendertreffen 2018 Olten"
year: 2018
date: "18.06.2018
von 08:30- 17:00"
location: "Olten, FHNW, Aula"

---

# Anwendertreffen 2018 Olten

Das Anwendertreffen 2018 war das 9. Treffen der QGIS Anwendergruppe Schweiz und fand am 18. Juni 2018 in Olten statt.
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

**Datum:** Montag, 18. Juni 2018, 9:00 bis 17:00

**Ort:** FHNW Olten, Aula Riggenbachstrasse 16 (Erdgeschoss).

![Lageplan FHNW Olten](/assets/img/lageplan_fhnw_aula_2018.png){: .img-fluid :}

**Sprache:** gemischt (deutsch, französisch, englisch), je nach Herkunft des Referenten

**Anreise:** Der Veranstaltungsort ist gut zu Fuss vom Bahnhof Olten erreichbar. Wir empfehlen die Anreise mit öffentlichen Verkehrsmitteln.

**Kosten:** Die Teilnahme an den Vorträgen/Präsentationen am Vormittag ist kostenfrei, für die Workshops wird eine kleine Workshopgebühr erhoben. MitgliederInnen der QGIS Anwendergruppe Schweiz: CHF 100.-, Nicht-Mitglieder: CHF 150.-, Studierende: CHF 50.- Die Workshop-Preise beinhalten einen kleinen Lunch am Mittag.

**Verpflegung:** Kaffeepausen am Vormittag und Nachmittag. Mittagessen (kleiner Lunch) inbegriffen.

**Anmeldung:**  [Anmeldeformular via Google Docs](https://docs.google.com/forms/d/e/1FAIpQLSczWV5iT916UeocLL5KPKS8ZtvZ3kwjqX9YXlkZD7N4Crzg5A/viewform?usp=sf_link){: .external-link :} - Besten Dank für Ihre Anmeldung!

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
{% for p in site.data.anwendertreffen-2018 %}
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

Workshop A: benötigt Laptop mit QGIS 3.x, WLAN-Empfang und Postgis (lokal installiert)

Workshop B: benötigt QGIS 3.x und 1 Android-Tablet (oder Telefon mit grösserem Bildschirm), Verbindungskabel zwischen Laptop und mobilem Gerät oder drahtlose Kommunikation.
