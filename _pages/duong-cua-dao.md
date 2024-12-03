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

Chuyện trên đời phân phải trái, trắng đen.\
Muốn rạch ròi ở cả từng chi tiết,\
Chẳng khác nào tự lấy dây buộc lại,\
Trói cả chân và che cả mắt mình.

Chỉ muốn biết những gì đã từng biết,\
Luôn muốn nghe những gì vẫn hằng nghe,\
Và lại tin những gì trước giờ tin,\
Rồi mắc kẹt trong vũng lầy ngộ nhận.

Đi loanh quanh trong mê cung nhận thức,\
Bước luẩn quẩn mà không biết điểm ra.\
Cho dù có ánh mặt trời dẫn dắt,\
Thì cũng tắt ở giữa bầu trời đêm.

Kỳ thực là thế gian lại muôn màu,\
Không có đúng mà cũng chẳng có sai.\
Trắng và Đen bản chất thuộc về một,\
Hà cớ gì lại phải tách làm hai?

Chỉ đến khi thấy rõ được bản nguyên,\
Trong thế giới mà nhị nguyên làm chủ.\
Thì đường mòn rồi cũng sẽ hiện ra,\
Dẫn lối thoát khỏi mê cung nhận thức.

> <cite>
<a target="_blank" href="https://wei-he.xyz">Wéi Hé</a>
</cite>

## Danh sách
{% assign posts = site.posts | where_exp: "item", "item.categories contains 'duong-cua-dao'" %}
{% for post in posts %}
  {% include archive-single.html %}
{% endfor %}