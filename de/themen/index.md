---

layout: plain-de
lang: de

---

# QGIS Model Baker

Model Baker ist ein [QGIS plugin](https://plugins.qgis.org/plugins/QgisModelBaker/){: .external-link target="BLANK"}, welches das schnelle Erstellen von QGIS Projekten aus physischen Datenmodellen erlaubt. Ausserdem lässt es mittels graphischen Ansteuerung der [ili2db](https://github.com/claeis/ili2db/blob/master/docs/ili2db.rst){: .external-link target="BLANK"} Tools [INTERLIS](https://www.interlis.ch/){: .external-link target="BLANK"} Modelle und Daten bequem in QGIS importieren, exportieren und validieren.

Model Baker verwendet ili2db, um ein INTERLIS-Modell in eine physische Datenbank zu importieren und die vorhandene Datenstruktur sowie Metainformationen für die Konfiguration des QGIS Projekts mit Legende, Formularlayouts, Relationen und vielem mehr. Diese Automatisierung reduziert den Konfigurationsaufwand massiv.

* [QGIS Model Baker Dokumentation](https://opengisch.github.io/QgisModelBaker/de/){: .external-link target="BLANK"}

* [QGIS Model Baker Code Repository](https://github.com/opengisch/QgisModelBaker){: .external-link target="BLANK"}

* [Kurzpräsentation QGIS Model Baker]({% link /assets/themen/2019-06-13_QGIS-Model-Baker.pdf %}){: .pdf-link target="BLANK"} vom Anwendertreffen 2019

# TEKSI

[www.teksi.ch](https://www.teksi.ch/){: .external-link target="BLANK"}

# Swiss Locator

Swiss Locator ist ein Plugin für QGIS zur Suche von Geodaten und Orte vom Online Geoportal [https://map.geo.admin.ch](https://map.geo.admin.ch){: .external-link target="BLANK"}:

* Orte
  * Kantone, Städte und Gemeinden
  * alle Lokalisationen, wie sie auf der Landeskarte gedruckt sind (SwissNames)
  * Adressen und Postleitzahlen
  * Katasterparzellen
* WMS-Ebenen aus dem Geoportal des Bundes oder von [opendata.swiss](https://opendata.swiss){: .external-link target="BLANK"}, welche als neue Layer in das Kartenfenster hinzugefügt werden können

* [Swiss Locator Code Repository](https://github.com/opengisch/qgis-swiss-locator){: .external-link target="BLANK"}

# DXF Export

Das [DXF bzw. DWG Format](https://de.wikipedia.org/wiki/Drawing_Interchange_Format){: .external-link target="BLANK"} ist für Ingenieurbüros, Kommunen und Kantone zentral für den Austausch von Geodaten mit Architekten und Planern. Gemeinden und Werkleitungsbetreiber in der Schweiz unterstützten daher gemeinsam die Entwicklung einer guten DXF Exportfunktion direkt aus QGIS, welche einfach zu bedienen ist. Das vorrangige Ziel ist der Export von Leitungs- und Vermessungsdaten.

Die Exportfunktion kann über das Menü _Projekt_ => _Import/Export_ => _Projekt als DXF speichern_ aufgerufen werden.

Die bisher erreichten Ziele sind:

* Auswahl welche Gruppen und Ebenen exportiert werden sollen
* Export wahlweise über alle Daten oder den aktuellen Kartenausschnitt
* Übernahme der Ebenenbezeichnungen wahlweise aus den QGIS Layernamen oder von einem Attribut (z.b. für den Export nach der SIA Geo405 Norm)
* Verschiedene Symbolisierungsoptionen:
  * Keine Darstellung (nur Geometrien mit default Symbologie)
  * Objektdarstellung (nur eine Geometrie pro Feature, keine vollständige Reproduktion bei komplexer Symbologie)
  * Symbollayerdarstellung (mehrere Geometrien pro Objekt, bildet komplexe Symbologie besser ab)
* Festlegung des Massstabs welcher für Filter, Symbologie und Beschriftungseinstellungen verwendet wird - Achtung: die Geometrien bleiben im Massstab 1:1, die Massstabszahl wird nur für Filter und Regeln angewandt
* Festlegen der Kodierung (Default ist CP1252) relevant für Umlaute und Sonderzeichen
* Unterstützung von "Sichtbarkeitsvoreinstellungen" (Lesezeichen für Kombinationen von Ebenensichtbarkeiten und Styles). So können z.b. Lesezeichen auf alle Gruppen/Ebenen der Leitungsdaten ohne Vermessungsdaten gesetzt werden.
* Unterstützung des Exports von Beschriftungen, inklusive mehrzeilige Beschriftungen und Textattribute
* Automatische Konvertierung von Einfachen Symbolen und SVG Symbolen zu DXF-Blöcken
* Unterstützung von Füllungen (nur Farbfüllungen und sind derzeit unterstützt)
* Unterstützung von Stricheigenschaften wie Strichstärke, Strichfarbe und Strichlierung
* Unterstützung von transparenten Füllungen
* Unterstützung von gemischten Einheiten (mm und Karteneinheiten) und Linienoffsets

![Export Dialog]({% link assets/img/1316c0fb-0220-4c32-994d-ab777de27d0d.png %}){: .img-fluid height="auto" max-width="100%" }

Explizit nicht unterstützt sind derzeit:

* Rasterebenen
* Komplexe Füllungen wie:
  * Punktmusterfüllungen
  * Linienmusterfüllungen
  * SVG-Füllungen
  * Rasterfüllungen
  * Shapeburstsymbolisierung
* Ebeneneffekte

Im untenstehenden Bild sehen Sie den gleichen Datenausschnitt links im Original in QGIS und rechts das Rendering in Autodesk TrueView:

![Vergleich QGIS und Autodesk TrueView]({% link assets/img/dxf_export_qgis_autodesk_trueview.png %}){: .img-fluid height="auto" max-width="100%" }

Das Projekt wird von verschiedenen Kommunen und vom Verein im Rahmen der Förderprojekte weiterentwickelt.
