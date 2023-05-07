---

layout: threecol-de
lang: de
title: "Anwendertreffen Online 2020"
year: 2020
date: "23.06.2022
von 08:55 - 12:30"
location: "Online"

---

# Anwendertreffen Online 2020

Das Online Anwendertreffen 2020 ist das 11. Treffen der Schweizer QGIS-Anwender.
{: .alert .alert-secondary :}

## Organisation

**Veranstalter:** QGIS Anwendergruppe Schweiz

**Kontakt:** info (at) qgis (dot) ch

**Datum:** Dienstag, 23. Juni 2020, 8:55 bis 12:30

**Ort:** [Online - Link (inkl. Registrierung) für das Webinar](https://www.edudip.com/de/webinar/qgis-user-meeting-online-2020-anwendertreffen-reunion-des-utilisateurs/331482).

**Softwareanforderungen:** Moderner Webbrowser mit Video/Audio/WebRTC Support (prinzipiell alle modernen Browser). Internet Explorer ist nicht unterstützt. MS Edge sollte funktionieren. Es ist keine Zusatzsoftware notwendig. Mikrofon und Kamera sind notwendig für Referenten oder Teilnehmer die Fragen stellen wollen. Es ist kein Login erforderlich.

[Testlink für Browser- und Firewall](https://webinartrainer.edudip.com/selftestwebrtc)

**Sprache:** hauptsächlich englisch dieses Mal (internationale Referenten)

**Kosten:** die Teilnahme ist kostenfrei

**Weiteres:** Die Veranstaltung kann im Umfang eines halben Tages (4h) als Fortbildung für Ingenieur-Geometerinnen und -Geometer angerechnet werden. Bei Interesse melden Sie sich bitte bei kassier@qgis.ch für eine Teilnahmebestätigung.

## Programm

Für dieses Online Meeting (Webinar) konzentrieren wir uns auf QGIS Desktop Themen. Falls das Format gut aufgenommen wird, sind weitere Online Meetings zu anderen Themen (wie QGIS Server, Mobile, Web Clients; Infrastruktur; QGIS in der Ausbildung; etc.) geplant.

Die Video-Aufzeichnungen sind unten im Programm verlinkt.

<table class="table table-striped">
  <thead>
    <tr>
      <th scope="col">Zeit</th>
      <th scope="col">Vortrag</th>
      <th scope="col">Referent(en)</th>
    </tr>
  </thead>
  <tbody>
{% for p in site.data.anwendertreffen-online-2020 %}
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
