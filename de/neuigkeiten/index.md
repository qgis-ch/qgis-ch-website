---

---

{% for post in site.posts %}
{% if post.lang == "de" %}

<h2>{{ post.title }}</h2>

<p style="color: gray;"><i>veröffentlicht am {{ post.date }}</i></p>

{{ post.excerpt }}

<a href="{{ post.url }}">Link zum Artikel</a>

{% endif %}
{% endfor %}
