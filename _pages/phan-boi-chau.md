---
title: Phan Bội Châu (阮攸)
layout: single
permalink: /phan-boi-chau
classes: wide
parent:
  label: Chuyện người xưa
  url: chuyen-nguoi-xua
categories: 
  - chuyen-nguoi-xua
---

![alt]({{ 'assets/images/phan-boi-chau-va-cuong-de.jpg' | absolute_url }})
> <cite>
<a target="_blank" href="https://baotanglichsu.vn/vi/Articles/3097/14624/phong-trao-djong-du-1905-1908-mot-hinh-thuc-xay-dung-luc-luong-cach-mang-nhung-nam-djau-the-ky-xx.html">
《Phan Bội Châu (người ngồi) và Kỳ ngoại Hầu Cường Để》
</a>
</cite>

## Danh sách
{% assign posts = site.posts | where_exp: "item", "item.categories contains 'Phan-Boi-Chau'" %}
{% for post in posts %}
  {% include archive-single.html %}
{% endfor %}