---

---

{% for post in site.posts %}
{% if post.lang == "fr" %}

<h2>{{ post.title }}</h2>

<p style="color: gray;"><i>publié le {{ post.date }}</i></p>

{{ post.excerpt }}

<a href="{{ post.url }}">Lien vers l'article</a>

{% endif %}
{% endfor %}
