---

title: "Herzlich Willkommen"

---

<div class="row">
<div class="col-md-12">

<div id="carouselExampleIndicators" class="carousel slide">
  <div class="carousel-indicators">
    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="3" aria-label="Slide 4"></button>
  </div>
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="{% link /assets/main/image1.png %}" class="d-block w-100" alt="dkdk">
      <div class="carousel-caption d-none d-md-block">
        <h5>Solarkataster der Stadt Olten</h5>
      </div>
    </div>
    <div class="carousel-item">
      <img src="{% link /assets/main/image2.jpeg %}" class="d-block w-100" alt="...">
      <div class="carousel-caption d-none d-md-block">
        <h5>Fix-Punkte Protokoll Mezzovico - Basis Orthofoto</h5>
      </div>
    </div>
    <div class="carousel-item">
      <img src="{% link /assets/main/image3.png %}" class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="{% link /assets/main/image4.png %}" class="d-block w-100" alt="dkdk">
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>

  </div>
</div>
<div class="row">
  <div class="col-md-12 text-center">
    <h1>QGIS Anwendergruppe Schweiz</h1>
  </div>
</div>
<div class="row">
  <div class="col-md-12 text-center fw-bold mt-2 mb-2">
Die QGIS Anwendergruppe Schweiz (kurz QGIS-CH) ist eine unabhängige, nicht
profitorientierte Vereinigung von QGIS Benutzer zur Förderung und Koordination
von Weiterentwicklungen von QGIS sowie zum Erfahrungsaustausch und
Vernetzung unter Vereinsmitglieder.
  </div>
  <div class="col-md-12 text-center mt-2 mb-5">Die Anwendergruppe ist
ein Verein im Sinne des schweizerischen Zivilgesetzbuches Artikel 60 bis 79.
Derzeit gibt es über 100 Mitglieder aus Behörden, Firmen, Universitäten und
Einzelpersonen. Sie ist ein stimmberechtigtes Mitglied der internationalen
<a href="https://qgis.org/en/site/getinvolved/governance/charter/index.html" class="external-link">QGIS.ORG Association</a>.
  </div>
</div>
<div class="row">
  <div class="col-md-8">  
    <div class="row">
      <div class="col-md-12">
        <h2>Über QGIS</h2>
      </div>  
      <div class="col-md-12">
QGIS ist eine GIS Plattform bestehend aus den Komponenten Desktop-GIS, Server-GIS,
Web-GIS Client und Mobile-GIS. QGIS Desktop ist eine benutzerfreundliche GIS
Anwendung für das Erstellen von Karten und Layouts, das Bearbeiten und Analysieren
von Geodaten. Bisher ist es beschränkt auf 2d und 2.5d Daten und Darstellungen.
Es bestehen erste 3D-Komponenten, diese sind jedoch noch als experimentell zu
bezeichnen. QGIS ist erweiterbar mit Hilfe der Sprachen Python und C++ und basiert
auf der qt-Bibliothek von Digia.
      </div>
    </div>
  </div>
  <div class="col-md-4 font-size-sm">
    <div class="row">
      <div class="col-md-12">
        <h2>Neuigkeiten</h2>
      </div>
      <div class="col-md-12">
        {% for post in site.posts %}
        {% if post.lang == "de" %}
        <h3>{{ post.title }}</h3>
        <p style="color: gray;"><i>veröffentlicht am {{ post.date }}</i></p>
        {{ post.excerpt }}
        <a href="{{ post.url }}">Link zum Artikel</a>
        {% endif %}
        {% endfor %}
      </div>
    </div>
  </div>
</div>
