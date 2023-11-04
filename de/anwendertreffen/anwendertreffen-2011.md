---

title: "Anwendertreffen 2011 Rapperswil"
year: 2011
date: "06.05.2011
von 08:30- 17:00"
location: "Rapperswil"

---

# Anwendertreffen 2011 Rapperswil

Das Anwendertreffen 2011 war das 2. Treffen der QGIS Anwendergruppe Schweiz und fand am 06. Mai 2011 in Rapperswil statt.
{: .alert .alert-secondary :}

Am 6. Mai 2011 fand an der HSR Rapperswil das 2. deutschsprachige QGIS-Anwendertreffen statt. Am Vormittag fanden in 2 Blöcken Präsentationen statt die über Neuigkeiten, Entwicklungstrends und Anwendungsmöglichkeiten berichteten. Es kamen gegen 80 Teilnehmer, über 40 nahmen auch an den Workshops teil. Der Anlass wurde von der QGIS Anwendergruppe Schweiz organisiert. Wir danken allen Mitorganisatoren, Referenten, Workshop-Instruktoren und Teilnehmern! Zudem danken wird dem Institut für Software und der HSR für die Gastfreundschaft und die Mithfilfe bei der Organisation. Das Datum des nächsten Anlasses in ca. einem Jahr wird auf der QGIS-Homepage, dem Geowebforum und über Email bekanntgegeben.

Nachfolgend finden Sie noch das Programm und die Folien als PDF-Dateien. Die Teilnehmer haben zudem eine Email erhalten mit einem Link zu einer Teilnehmerumfrage zu QGIS und dem QGIS-Anwendertreffen. Fotos vom Anlass finden Sie unter diesem [Flickr-Link](http://www.flickr.com/photos/pifx/sets/72157626750120332/){: .external-link :}.

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
{% for p in site.data.anwendertreffen-2011 %}
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

Am Nachmittag fanden 3 Workshops zu je 3 Stunden statt.

Die folgenden 3 Workshops wurden angeboten:

* QGIS Anfängerworkshops (für Neueinsteiger), Instruktoren: Otto Dassau, Werner Macho, Andreas Neumann
* QGIS 1.6 und 1.7 - Was gibt es an neuer Funktionalität?, Instruktoren: Pirmin Kalberer, Anita Graser, Mathias Walker
* QGIS Plugins mit Python programmieren, Instruktoren: Cédric Möri, Stefan Ziegler, (Horst Düster)
