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

Tớ không hẳn là một người theo bất kỳ tôn giáo nào, nhưng với riêng tớ thì đạo lí của Đạo Giáo có vẻ là phù hợp nhất để hoàn thành ước nguyện của bản thân. Với tớ, mong ước lớn nhất là có thể dành cả cuộc đời mình để chảy đi khắp thế gian, nhìn thấy được nhiều thứ, ngộ ra được nhiều điều.
{: .text-justify}

Và tớ cũng không muốn những thứ mà tớ thấy, những điều mà tớ ngộ sẽ mất đi khi tớ không còn nữa. Thế nên tớ lưu vết nơi đây, để dấu lại cho người có duyên.
{: .text-justify}

## Danh sách
{% assign posts = site.posts | where_exp: "item", "item.categories contains 'duong-cua-dao'" %}
{% for post in posts %}
  {% include archive-single.html %}
{% endfor %}