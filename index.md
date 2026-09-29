---
layout: article
title: MrNasdog Research
description: Mirror of MrNasdog crypto research — coin supply, demand and inflation analyses. Originals on mrnasdog.com.
canonical_url: https://mrnasdog.com/
---

# MrNasdog Research

Coin supply, demand and inflation analyses by MrNasdog. Each page is a copy; the original, always up to date, is on
[mrnasdog.com](https://mrnasdog.com).

{% assign items = site.pages | where_exp: "p", "p.path contains 'crypto/'" | sort: "title" %}
<ul>
{% for p in items %}<li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
{% endfor %}
</ul>
