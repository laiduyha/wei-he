---
title: Chuyện người xưa
permalink: /chuyen-nguoi-xua
classes: wide
---

![alt]({{ 'assets/images/zhang-da-qian-kan-song-tu.jpg' | absolute_url }})
> <cite>
<a target="_blank" href="https://en.wikipedia.org/wiki/Chang_Dai-chien">
张大千《看松图》- Trương Đại Thiên《Dưới gốc Tùng》
</a>
</cite>

Người xưa chí lớn can trường,\
Người xưa số kiếp trăm đường trầm luân.\
Người xưa trác tuyệt phong vân,\
Người xưa với cõi hồng trần trách than.\
 \
Ta qua một kiếp mê man,\
Ta đi theo vết kiến quang trần đời.\
Ta tìm trong khắp đất trời,\
Ta ghi chép lại chuyện đời tích xưa.

> <cite>
<a target="_blank" href="https://wei-he.xyz">Wéi Hé</a>
</cite>

## Danh sách
{% assign pages = site.pages | where_exp: "item", "item.categories contains 'chuyen-nguoi-xua'" %}
{% for post in pages %}
  {% include archive-single.html %}
{% endfor %}