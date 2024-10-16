---
title: Đường của đạo
permalink: /duong-cua-dao
classes: wide
---

![alt]({{ 'assets/images/tao-leng-yue-you-gu-qi-feng.jpg' | absolute_url }})
> <cite>
<a target="_blank" href="http://www.360doc.com/content/15/0914/22/15883912_499173466.shtml">
陶冷月《幽谷奇峰》- Đào Lãnh Nguyệt《Thung Lũng và Đỉnh Núi》
</a>
</cite>

## Danh sách
{% assign posts = site.posts | where_exp: "item", "item.categories contains 'duong-cua-dao'" %}
{% for post in posts %}
  {% include archive-single.html %}
{% endfor %}