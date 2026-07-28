---
title: Thơ văn
permalink: /tho-van
classes: wide
---

![alt]({{ 'assets/images/liu-yunfang-mountains-river-boat.jpg' | absolute_url }})
> <cite>
刘云芳《小桥流水人家》- Lưu Vân Phương《Cầu nhỏ, nước chảy, nhà ai》
</cite>

## Danh sách
{% assign posts = site.posts | where_exp: "item", "item.tags contains 'tho-van'" %}
{% for post in posts %}
  {% include archive-single.html %}
{% endfor %}
