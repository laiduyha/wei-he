---
title: Trung Quốc
layout: single
permalink: /trung-quoc
classes: wide
---

![alt]({{ 'assets/images/tse-tsan-tai-this-situation-in-the-far-east.jpg' | absolute_url }})
> <cite>
<a target="_blank" href="https://en.m.wikipedia.org/wiki/File:%E6%97%B6%E5%B1%80%E5%9B%BE.jpg">
谢缵泰《时局图》- Tạ Toản Thái《Tình hình hiện tại (1904)》
</a>
</cite>

Laissons la Chine dormir, car quand elle se réveillera, le monde tremblera.\
 \
China is a sleeping dragon, let China sleep, for when she awakes, the world will tremble.
{: .notice--warning .text-justify}
> <cite>
Napoleon Bonaparte
</cite>

## Danh sách
{% assign posts = site.posts | where_exp: "item", "item.categories contains 'trung-quoc'" %}
{% for post in posts %}
  {% include archive-single.html %}
{% endfor %}