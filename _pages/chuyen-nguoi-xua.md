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

Người xưa chí lớn hào hùng,\
Người xưa muôn kiếp, muôn đường trầm luân.\
Người xưa trác tuyệt phong vân,\
Người xưa với cõi hồng trần oán than.\
 \
Ta lần theo vết mây tan,\
Vết xưa khắc lại giới quan của người.\
Giờ đây vật đổi sao dời,\
Vết xưa dấu ấy vẫn còn ở đây!

> <cite>
<a target="_blank" href="https://wei-he.xyz">Wéi Hé</a>
</cite>

## Danh sách
{% assign pages = site.pages | where_exp: "item", "item.categories contains 'chuyen-nguoi-xua'" %}
{% for post in pages %}
  {% include archive-single.html %}
{% endfor %}