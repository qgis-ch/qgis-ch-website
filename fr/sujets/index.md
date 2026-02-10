---

title: Sujets

---

# Sujets

Les thèmes et projets suivants présentent un intérêt particulier pour
l'association et sont soutenus en conséquence.

## QGIS Model Baker

Model Baker est un
[QGIS plugin](https://plugins.qgis.org/plugins/QgisModelBaker/){: .external-link :}
qui permet de créer rapidement des projets QGIS à partir de modèles de données
physiques.
En outre, il permet d'importer, d'exporter et de valider facilement des
[modèles et des données INTERLIS](https://www.interlis.ch/){: .external-link :}
dans QGIS par le biais d'une commande graphique des programmes
[ili2db](https://github.com/claeis/ili2db/blob/master/docs/ili2db.rst){: .external-link :}.

Model Baker utilise ili2db pour importer un modèle INTERLIS dans une base de
données physique et la structure de données existante ainsi que les
méta-informations pour la configuration du projet QGIS avec les légendes, les
mises en page de formulaires, les relations et bien plus encore. Cette
automatisation réduit massivement les efforts de configuration.

* [QGIS Model Baker Dokumentation](https://opengisch.github.io/QgisModelBaker/fr/){: .external-link :}

* [QGIS Model Baker Code Repository](https://github.com/opengisch/QgisModelBaker){: .external-link :}

* [Brève présentation de QGIS Model Baker]({% link /assets/themen/2019-06-13_QGIS-Model-Baker.pdf %}){: .pdf-link :}
  lors de la réunions des utilisateurs 2019

# TEKSI

[www.teksi.ch](https://www.teksi.ch/){: .external-link :}

 Le module TESKI assainissement & PGEE est un projet de développement d'un module métier pour la gestion des eaux usées et des plans généraux d'évacuation des eaux usées (PGEE).

![GEP Netzwerk]({% link assets/img/network_cadastral-1.png %}){: .img-fluid max-width="70%" }

Démarré en 2012 en raison d'un manque d'outils professionnels satisfaisants, des communes suisses et des bureaux d'ingénieurs se sont regroupés pour offrir une solution basée sur des logiciels libres et open-source. Ce groupe rassemble des experts en ingénierie des réseaux d'eaux usées, des gestionnaires, des concepteurs de modèles de données du domaine, des développeurs ainsi que des utilisateurs finaux des
solutions SIG.

Initialement sous-groupe de l’association QGIS Suisse, ce projet est depuis 2022 sous l’égide de l’association à but non lucratif TEKSI qui a pour but de mettre à disposition des gestionnaires d’infrastructures publiques des outils professionnels open source pour piloter leurs activités. Plus d’informations sur le [site web de TEKSI](https://www.teksi.ch/){: .external-link :}

Le module TEKSI assainissement est une sélection d’outils QGIS et une implémentation de base de donnée PostgreSQL/PostGIS qui vous permet de:

* gérer et cartographier les données de votre réseau d’assainissement avec tous   ses composants comme par exemple les collecteurs, les chambres, les déversoirs   d’orage, les bassins de rétention des eaux pluviales, les exutoires, etc.
* indiquer les caractéristiques des objets du réseau sous forme d’attributs comme   le diamètre, le matériau, la profondeur de pose, les défauts, la date de pose, etc.
* produire des plans et extraire des statistiques de la base de données comme la   valeur du réseau, la longueur totale des conduites, l’identification des   futures interventions, etc.
* Exporter les données géographiques en accord avec les standards suisses

![TEKSI GEP Formular]({% link assets/img/form_collecteur.png %}){: .img-fluid max-width="70%" }
 
### Les principales fonctionnalités de TEKSI assainissement sont

* multilingue: les versions anglaise, française et allemande sont d'ores et déjà disponibles
* respecte les standards suisses: Model VSA-DSS. Import et export au format INTERLIS SIA 405, VSA-SDEE et VSA-KEK.
* edition du réseau d'eau usée
* outils de construction CAD
* poursuite de réseau (vers l'aval ou l'amont ou entre 2 noeuds)
* vue en profil des conduites et des chambres
* symbologie et impression avancées des cartes et des profils
* interface avec des logiciels de modélisation
* outils maintenance et de planning (comme pour l'inspection TV, les réparations, etc.)

Le modèle de données est basé sur le standard suisse VSA-SDEE et est implémenté dans une base de données PostGIS. L'interface graphique est intégrée dans QGIS et bénéficie de l’ensemble des fonctionnalités natives de QGIS pour l’édition.
Un plugin est disponible pour accéder à certaines fonctionnalités de suivi réseau.
Les améliorations sont toujours intégrées en priorité dans le cœur de QGIS.

Pour participer au développement de ce projet, nous vous remercions de considérer l'idée de rejoindre l’association TEKSI.


### Organisation

TEKSI est une association sœur du groupe suisse d'utilisateurs de QGIS et est supervisée par un comité de pilotage, pour plus d'informations, consulter
[https://www.teksi.ch/communaute/](https://www.teksi.ch/communaute/){: .external-link :}.

En cas de questions, merci de contacter info@teksi.ch ou d’utiliser le 
[formulaire de contact](https://www.teksi.ch/contact/){: .external-link :}.


# Swiss Locator

Swiss Locator est un plugin pour QGIS pour la recherche de géodonnées et de
lieux sur le géoportail [https://map.geo.admin.ch](https://map.geo.admin.ch){: .external-link :}:

* des lieux
  * des cantons, villes et communes
  * toutes les localisations telles qu'elles sont imprimées sur la carte
    nationale (SwissNames)
  * des adresses et codes postaux
  * les parcelles cadastrales
* Couches WMS provenant du géoportail de la Confédération ou d'
[opendata.swiss](https://opendata.swiss){: .external-link :}, qui peuvent être
ajoutées comme nouvelles couches dans la fenêtre de carte.

* [Swiss Locator Code Repository](https://github.com/opengisch/qgis-swiss-locator){: .external-link :}

# DXF Export

Das [DXF bzw. DWG Format](https://de.wikipedia.org/wiki/Drawing_Interchange_Format){: .external-link :} ist für Ingenieurbüros, Kommunen und Kantone zentral für den Austausch von Geodaten mit Architekten und Planern. Gemeinden und Werkleitungsbetreiber in der Schweiz unterstützten daher gemeinsam die Entwicklung einer guten DXF Exportfunktion direkt aus QGIS, welche einfach zu bedienen ist. Das vorrangige Ziel ist der Export von Leitungs- und Vermessungsdaten.

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
