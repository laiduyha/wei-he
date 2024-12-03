---
title: Lý Quang Diệu
layout: single
permalink: /ly-quang-dieu
classes: wide
parent:
  label: Chuyện người xưa
  url: chuyen-nguoi-xua
categories: 
  - chuyen-nguoi-xua
---

![alt]({{ 'assets/images/lee-kuan-yew-one-man-view-the-world.jpg' | absolute_url }})
> <cite>
Lee Kuan Yew《One man's view of the world》- Lý Quang Diệu《Ông già nhìn ra thế giới》
</cite>

Lý Quang Diệu (李光耀) là thủ tướng đầu tiên và là người đặt nền móng, kiến trúc sư trưởng cho đất nước Singapore ngày nay. Ông sinh năm 1923, mất năm 2015, thọ 92 tuổi. Sự thịnh vượng hiện tại của Singapore được thừa hưởng nhiều từ góc nhìn sắc sảo, sự kiên định và quyết liệt trong việc thực hiện hóa ý tưởng của ông.
{: .text-justify}

Với những bài viết dưới đây của ông, cậu sẽ biết được góc nhìn của ông về thế giới, về các cường quốc đã từng và đang trỗi dậy. Hầu hết những bài viết này của ông là vào những năm cuối đời (2010) khi tình hình thế giới đang có diễn biến mới. Nền văn minh Phương Tây đang có dấu hiệu chững lại và sự vươn lên của Trung Quốc ngày một rõ nét.
{: .text-justify}

## Danh sách
{% assign posts = site.posts | where_exp: "item", "item.categories contains 'ly-quang-dieu'" %}
{% for post in posts %}
  {% include archive-single.html %}
{% endfor %}