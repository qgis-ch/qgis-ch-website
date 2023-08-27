---

layout: plain-de
lang: de
title: "Anwendertreffen Online Herbst 2020"
year: 2020
date: "24.11.2020
von 08:55 - 12:30"
location: "Online (Eduip)"

---

# Anwendertreffen Online Herbst 2020

Das Online Anwendertreffen Herbst 2020 war das 12. Treffen der Schweizer QGIS-Anwender und fand am 24. November 2020 online statt.
{: .alert .alert-secondary :}

Schwerpunkte: QGIS Server, Web Clients, Mobile Anwendungen und Synchronisation

## Organisation

**Veranstalter:** QGIS-Anwendergruppe Schweiz

**Kontakt:** info (at) qgis (dot) ch

**Datum:** Dienstag, 24. November 2020, 8:55 bis 12:30

**Ort:** [Online - Link (inkl. Registrierung) für das Webinar](https://www.edudip.com/de/webinar/qgis-user-meeting-online-2020-anwendertreffen-reunion-des-utilisateurs/331482){: .external-link :}

**Softwareanforderungen:** Moderner Webbrowser mit Video/Audio/WebRTC Support (prinzipiell alle modernen Browser). Internet Explorer ist nicht unterstützt. MS Edge sollte funktionieren. Es ist keine Zusatzsoftware notwendig. Mikrofon und Kamera sind notwendig für Referenten oder Teilnehmer die Fragen stellen wollen. Es ist kein Login erforderlich.

[Testlink für Browser- und Firewall](https://webinartrainer.edudip.com/selftestwebrtc){: .external-link :}

**Sprache:** englisch (internationale Referenten)

**Kosten:** die Teilnahme ist kostenfrei

## Programm

Für dieses Online Meeting (Webinar) konzentrieren wir uns auf die Themen QGIS Server, Web Clients, Mobile Lösungen und Synchronisation.

Die Video-Aufzeichnungen werden später im Programm verlinkt.

<table class="table table-striped">
  <thead>
    <tr>
      <th scope="col">Zeit</th>
      <th scope="col">Vortrag</th>
      <th scope="col">Referent(en)</th>
    </tr>
  </thead>
  <tbody>
{% for p in site.data.anwendertreffen-online-herbst-2020 %}
    <tr>
      <td>{{ p.time }}</td>
      {% if p.url %}
      <td>
        {% assign prefix = p.url | slice: 0,5 %}
        {% if prefix != "https" %}
        <a href="{% link {{ p.url }} %}">{{ p.presentation }}</a>
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
