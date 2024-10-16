---
title: Học hành
permalink: /hoc-hanh
classes: wide
---

![alt]({{ 'assets/images/zheng-wu-chang-deng-shan-guan-pu.jpg' | absolute_url }})
> <cite>
<a target="_blank" href="https://auction.artron.net/paimai-art37790702/">
郑午昌《登山观瀑图》- Trịnh Ngọ Xương《Leo núi ngắm thác》
</a>
</cite>

## Danh sách
{% assign posts = site.posts | where_exp: "item", "item.categories contains 'hoc-hanh'" %}
{% for post in posts %}
  {% include archive-single.html %}
{% endfor %}