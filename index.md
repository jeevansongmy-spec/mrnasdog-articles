---
layout: article
title: MrNasdog Research
description: Mirror of MrNasdog crypto research — coin supply, demand and inflation analyses. Originals on mrnasdog.com.
canonical_url: https://mrnasdog.com/
---

# MrNasdog Research

Should you buy a coin, sell it, or wait? Each coin page answers it with the law of supply and demand — new supply,
demand, price drivers and the questions people ask, with dated numbers. Each page here is a copy; the original, always
up to date, is on [mrnasdog.com](https://mrnasdog.com).

## Coin pages

{% assign hubs = site.pages | where_exp: "p", "p.content_type == 'coin_hub'" | sort: "title" %}
<ul>
{% for p in hubs %}<li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
{% endfor %}
</ul>

## Supply deep-dives and articles

{% assign items = site.pages | where_exp: "p", "p.path contains 'crypto/'" | where_exp: "p", "p.content_type != 'coin_hub'" | sort: "title" %}
<ul>
{% for p in items %}<li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
{% endfor %}
</ul>
