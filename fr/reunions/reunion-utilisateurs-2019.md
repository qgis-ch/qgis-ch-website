---

title: "Anwendertreffen 2019 Olten"
year: 2019

---

# Anwendertreffen 2019 Olten

Das Anwendertreffen 2019 war das 10. Treffen der QGIS Anwendergruppe Schweiz und fand am 13. Juni 2019 in Olten statt.
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

**Datum:** Donnerstag, 13. Juni 2019, 9:00 bis 17:00

**Ort:** FHNW Olten, Gebäude 4, Von Roll-Strasse 10, Hörsaal OVR B018 (Erdgeschoss).

![Lageplan FHNW Olten](/assets/img/lageplan_qgis_anwendertag_2023_olten.png){: .img-fluid :}

**Sprache:** gemischt (deutsch, französisch, englisch), je nach Herkunft des Referenten

**Anreise:** Der Veranstaltungsort ist gut zu Fuss vom Bahnhof Olten erreichbar. Wir empfehlen die Anreise mit öffentlichen Verkehrsmitteln.

**Kosten:** Die Teilnahme an den Vorträgen/Präsentationen am Vormittag ist kostenfrei, für die Workshops wird eine kleine Workshopgebühr erhoben. MitgliederInnen der QGIS Anwendergruppe Schweiz: CHF 100.-, Nicht-Mitglieder: CHF 150.-, Studierende: CHF 50.- Die Workshop-Preise beinhalten einen kleinen Lunch am Mittag.

**Verpflegung:** Kaffeepausen am Vormittag und Nachmittag. Mittagessen (kleiner Lunch) inbegriffen.

**Anmeldung:**  [Anmeldeformular via Google Docs](https://docs.google.com/forms/d/e/1FAIpQLSfM0NLQe7hcJq_Lrpy0ry8rbtRoM2_FZDzRKZ2Dc0xyEyp5HQ/viewform?usp=sf_link){: .external-link :}

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
{% for p in site.data.anwendertreffen-2019 %}
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

Workshop A: benötigt Laptop mit [QGIS 3.6](https://qgis.org/en/site/forusers/download.html){: .external-link :}, WLAN-Empfang und [PostGIS](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads){: .external-link :} (lokal installiert), Java, [ili2pg](http://www.eisenhutinformatik.ch/interlis/ili2pg/){: .external-link :}, [il2gpkg](http://www.eisenhutinformatik.ch/interlis/ili2gpkg/){: .external-link :} und [ilivalidator](https://github.com/claeis/ilivalidator/releases){: .external-link :}.

Workshops B+C: benötigt [QGIS 3.6](https://qgis.org/en/site/forusers/download.html){: .external-link :} und WLAN-Empfang. 

Workshop D: QGIS Desktop 3.6, ein Android Tablet or Telefon mit mindestens Android 6, WLAN und Netzwerkverbindung auf Laptop und Tablet/Telefon.
