---

layout: threecol-de
lang: de
title: "Anwendertreffen 2023 Olten"
year: 2023
date: "07.06.2022
von 09:00 - 12:30"
location: "Olten"

---

# Anwendertreffen 2023

Das Anwendertreffen 2023 war das 15. Treffen der QGIS Anwendergruppe Schweiz und fand am 7. Juni 2023 in Olten statt.
{: .alert .alert-secondary :}

## Ziele

* Information über aktuelle Arbeiten im QGIS-Projekt
* Austausch unter QGIS Anwendern und Networking
* Kontakt zwischen Anwendern und Entwicklern
* Vorstellung der neuen Features in der aktuellen Entwickler-Version
* Vorstellung aktueller Case Studies
* Koordination zukünftiger Entwicklungen

## Organisation

**Veranstalter:** QGIS Anwendergruppe Schweiz

**Kontakt:** info (at) qgis (dot) ch

**Datum:** Mittwoch, 07. Juni 2023, 8:55 bis 17:00

**Ort:** FHNW Olten, Gebäude 4, Von-Roll-Strasse 10, Hörsaal OVR A022 (Erdgeschoss)

![](/assets/img/lageplan_qgis_anwendertag_2023_olten.png){: .img-fluid :}

**Sprache:** gemischt (deutsch, französisch, englisch), je nach Herkunft des Referenten

**Anreise:** Der Veranstaltungsort ist gut zu Fuss vom Bahnhof Olten erreichbar. Wir empfehlen die Anreise mit öffentlichen Verkehrsmitteln.

**Kosten:**  Die Teilnahme an den Vorträgen/Präsentationen am Vormittag ist kostenfrei, für die Workshops wird eine kleine Workshopgebühr erhoben. MitgliederInnen der QGIS Anwendergruppe Schweiz: CHF 99.-, Nicht-Mitglieder: CHF 199.-, Studierende: gratis. Die Workshop-Preise beinhalten einen kleinen Lunch (Sandwiches).

**Verpflegung:** Kaffeepausen am Vormittag und Nachmittag. Mittagessen (kleiner Lunch) für Workshopteilnehmer inbegriffen.

**Anmeldung:** [Google Forms Link](https://forms.gle/NFbZfc5gbdMvHz8Z6)

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
{% for p in site.data.anwendertreffen-2023 %}
    <tr>
      <td>{{ p.time }}</td>
      {% if p.url %}
      <td>
        <a href="{{ p.url }}">{{ p.presentation }}</a>
      </td>
      {% else %}
      <td>{{ p.presentation }}</td>
      {% endif %}
      <td>{{ p.presenter }}</td>
    </tr>
{% endfor %}
  </tbody>
</table>
