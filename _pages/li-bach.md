---
title: Lí Bạch
layout: single
permalink: /li-bach
classes: wide
parent:
  label: Chuyện người xưa
  url: chuyen-nguoi-xua
categories: 
  - chuyen-nguoi-xua
---

![alt]({{ 'assets/images/li-bai.jpg' | absolute_url }})
>

## Danh sách
{% assign posts = site.posts | where_exp: "item", "item.categories contains 'li-bach'" %}
{% for post in posts %}
  {% include archive-single.html %}
{% endfor %}