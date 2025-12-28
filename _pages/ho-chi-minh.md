---
title: Hồ Chí Minh
layout: single
permalink: /ho-chi-minh
classes: wide
parent:
  label: Chuyện người xưa
  url: chuyen-nguoi-xua
categories: 
  - chuyen-nguoi-xua
---

![alt]({{ 'assets/images/ho-chi-minh.jpg' | absolute_url }})
>

## Danh sách
{% assign posts = site.posts | where_exp: "item", "item.categories contains 'ho-chi-minh'" %}
{% for post in posts %}
  {% include archive-single.html %}
{% endfor %}