---
title: Nguyễn Du
layout: single
permalink: /nguyen-du
classes: wide
parent:
  label: Chuyện người xưa
  url: chuyen-nguoi-xua
categories: 
  - chuyen-nguoi-xua
---

![alt]({{ 'assets/images/nguyen-du.jpeg' | absolute_url }})
> <cite>
<a target="_blank" href="http://nguyendu.org.vn/vi/-nguyen-du---dai-thi-hao-dan-toc-viet-nam--FB689E800066581BBE66B1B8F8106905.html/i1439363111155/6/8">
Lê Anh Tuấn《Nguyễn Du - Đại thi hào dân tộc Việt Nam》
</a>
</cite>

Nguyễn Du (阮攸) tự Tố Như (素如), hiệu Thanh Hiên (清軒). Ông sinh năm 1766, mất năm 1820, thọ 54 tuổi. Ông sống vào thời khắc bước ngoặt lịch sử của nhà Hậu Lê, Tây Sơn và Chúa Nguyễn. Thuở nhỏ, tưởng chừng như cuộc đời ông không gặp nhiều trắc trở, khi cha ông làm tới chức tể tướng của Triều Lê. Tuy nhiên khi ông lên mười thì cha mất, mười ba tuổi thì mồ côi mẹ. Sau này rồi, chiến sự loạn lạc càng làm ông trở nên mất phương hướng. Vào thời buổi loạn lạc đó, vì những ràng buộc của tư tưởng Nho giáo mà ông bị kẹt trong gọng kiềm của sự trung thành với nhà Lê. Khi nhà Tây Sơn ra Bắc năm 1786, ông chọn thái độ không cộng tác, tìm đường sống ẩn dật, cam chịu cảnh nghèo khổ mà thanh cao.
{: .text-justify}

Nguyễn Du có mái tóc bạc sớm, mái tóc như biểu tượng của những chiêm nghiệm buồn thương và bế tắc. Nguyễn Du nổi tiếng với Truyện Kiều. Thế nhưng sâu thẳm bên trong ông lại có một tiếng nói khác. Một Nguyễn Du luôn hoài nghi, đau đáu về nhân sinh, về những trói buộc của thời cuộc, và cả tài năng của chính mình trong thời buổi loạn lạc ấy.
{: .text-justify}

## Danh sách
{% assign posts = site.posts | where_exp: "item", "item.categories contains 'Nguyen-Du'" %}
{% for post in posts %}
  {% include archive-single.html %}
{% endfor %}