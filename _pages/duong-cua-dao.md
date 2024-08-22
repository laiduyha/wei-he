---
title: Đường của đạo
permalink: /duong-cua-dao/
classes: wide
---

![alt]({{ 'assets/images/tao-leng-yue-you-gu-qi-feng.jpg' | absolute_url }})
> <cite>
<a target="_blank" href="http://www.360doc.com/content/15/0914/22/15883912_499173466.shtml">
陶冷月《幽谷奇峰》- Đào Lãnh Nguyệt《Thung lũng và đỉnh núi》
</a>
</cite>

Tớ không hẳn là một người theo bất kỳ tôn giáo nào, nhưng tớ cảm nhận đạo lí của Đạo Giáo có vẻ phù hợp với nhân sinh quan của mình. 
Cả cuộc đời mình tớ muốn dành để `chảy` đi hết thế gian, nhìn thấy được nhiều thứ, ngộ ra được nhiều điều.

Và tớ cũng không muốn những điều này sẽ mất đi khi tớ không còn nữa. 
Thế nên tớ lưu vết lại nơi đây, để cho những ai có đi qua, tạt ngang con đường này sẽ thấy được cái thú vị của nó.

{% assign posts = site.posts | where_exp: "item", "item.tags contains 'duong-cua-dao'" %}
{% for post in posts %}
  - [{{ post.title }}]({{ post.url | relative_url }})
{% endfor %}