---

layout: plain-de
lang: de

---

# QGIS Model Baker

Model Baker ist ein [QGIS plugin](https://plugins.qgis.org/plugins/QgisModelBaker/), welches das schnelle Erstellen von QGIS Projekten aus physischen Datenmodellen erlaubt. Ausserdem lässt es mittels graphischen Ansteuerung der [ili2db](https://github.com/claeis/ili2db/blob/master/docs/ili2db.rst) Tools [INTERLIS](https://www.interlis.ch/) Modelle und Daten bequem in QGIS importieren, exportieren und validieren.

Model Baker verwendet ili2db, um ein INTERLIS-Modell in eine physische Datenbank zu importieren und die vorhandene Datenstruktur sowie Metainformationen für die Konfiguration des QGIS Projekts mit Legende, Formularlayouts, Relationen und vielem mehr. Diese Automatisierung reduziert den Konfigurationsaufwand massiv.

* [QGIS Model Baker Dokumentation](https://opengisch.github.io/QgisModelBaker/de/){: target="BLANK"}

* [QGIS Model Baker Code Repository](https://github.com/opengisch/QgisModelBaker){: target="BLANK"}

* [Kurzpräsentation QGIS Model Baker]({% link /assets/themen/2019-06-13_QGIS-Model-Baker.pdf %}){: target="BLANK"} vom Anwendertreffen 2019

# TEKSI

[www.teksi.ch](https://www.teksi.ch/)

# Swiss Locator

Swiss Locator ist ein Plugin für QGIS zur Suche von Geodaten und Orte vom Online Geoportal [https://map.geo.admin.ch](https://map.geo.admin.ch):

* Orte
  * Kantone, Städte und Gemeinden
  * alle Lokalisationen, wie sie auf der Landeskarte gedruckt sind (SwissNames)
  * Adressen und Postleitzahlen
  * Katasterparzellen
* WMS-Ebenen aus dem Geoportal des Bundes oder von [opendata.swiss](https://opendata.swiss), welche als neue Layer in das Kartenfenster hinzugefügt werden können

* [Swiss Locator Code Repository](https://github.com/opengisch/qgis-swiss-locator)
