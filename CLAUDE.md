# CLAUDE.md

Blog Jekyll (theme minimal-mistakes), nội dung tiếng Việt. Bài viết nằm ở `_posts/`, trang tổng hợp series ở `_pages/`.

## Định dạng series truyện dài

Áp dụng cho mọi bài thuộc một series nhiều kỳ (hiện có: `pbc-*` Phan Bội Châu, `lky-*` Lý Quang Diệu, `dcstq-*` Chính trường TQ thời lập quốc) và mọi series mở mới sau này.

### 1. Khối trích — chọn biến thể `notice` theo ngữ nghĩa

Mỗi biến thể có đúng một vai. Không dùng biến thể chỉ vì "cho đổi màu".

| Class | Vai | Dùng cho |
|---|---|---|
| `.notice` | **Lời nói** | Lời thoại, phát ngôn trực tiếp của nhân vật. Mặc định cho mọi câu nói. |
| `.notice--warning` | **Văn bản** | Điện tín, thư từ, mệnh lệnh, tuyên ngôn, chỉ thị, thơ, câu liễn — thứ được *viết ra* chứ không phải *nói ra*. |
| `.notice--info` | **Ngoại đề** | Ghi chú nền của người kể: đoạn dẫn nhập mở bài, tiểu sử nhân vật phụ, bối cảnh sự kiện, chuyện hậu kỳ, chú thích ảnh dài (liệt kê người trong ảnh). Không phải lời của ai cả. |
| `.notice--danger` | **Bước ngoặt** | Câu/đoạn đánh dấu tổn thất hoặc điểm không thể quay đầu của kỳ đó. **Tối đa 1 khối mỗi bài.** Nếu phân vân thì dùng `.notice` hoặc `.notice--warning`. |

Không dùng `.notice--success`.

### 2. Cấu trúc khối — bất biến

```markdown
Đoạn dẫn kết bằng dấu hai chấm:
{: .text-justify}

> Nội dung trích.
{: .notice .text-justify}
```

- Khối trích **luôn** là blockquote — mọi dòng bắt đầu bằng `> `. Không có khối `{: .notice*}` nào gắn vào đoạn văn trần.
- Dòng attribute **luôn** đủ hai class, có dấu chấm trước mỗi class: `{: .notice--warning .text-justify}`. Không bao giờ viết `{: .notice text-justify}`.
- Đoạn dẫn ngay trước khối trích luôn có `{: .text-justify}` riêng.
- Ngăn cách các đoạn *bên trong* một khối bằng dòng `>  \` (dấu `>`, hai space, backslash), và kết thúc đoạn trên bằng `\`:

```markdown
> Đoạn thứ nhất.\
>  \
> Đoạn thứ hai.
{: .notice--info .text-justify}
```

### 3. Đối thoại

**Một lời thoại đơn** — người nói nêu ở đoạn dẫn, khối chứa lời trần, **không ngoặc kép** (khung notice đã đóng vai ngoặc kép):

```markdown
Mao dặn dò cấp dưới bằng một câu gọn lỏn:
{: .text-justify}

> Ta đổi mũ rất nhanh, nhưng ta vẫn là Cộng sản.
{: .notice .text-justify}
```

**Đối đáp nhiều lượt** — gộp trong *một* khối, mỗi lượt mở đầu bằng em dash `— `, các lượt ngăn bằng `>  \`. Ghi người nói (nếu cần) đặt sau lời thoại, ngăn bằng en dash ` – `:

```markdown
> — Tôi lớn lên ở Đông Bắc – Chu Ân Lai tự giới thiệu.\
>  \
> — Tôi biết – Trương Học Lương đáp – Thầy Trương Bá Linh cho tôi hay điều đó.
{: .notice .text-justify}
```

Không dùng các kiểu sau nữa: `"Lời thoại" – Người nói.`, `Người nói: "Lời thoại"` bên trong khối, hay lời thoại có ngoặc kép trong khối notice.

**Phỏng vấn hỏi–đáp** (series `lky`): `**Hỏi:**` và `**Đáp:**` — dấu hai chấm **nằm trong** cặp `**`.

### 4. Dấu gạch ngang — mỗi dấu một nhiệm vụ

| Dấu | Dùng cho | Ví dụ |
|---|---|---|
| `—` em dash | **Chỉ** mở lượt thoại trong khối đối đáp | `> — Ân Lai, anh là bộ hạ của ta.` |
| `–` en dash, có space hai bên | Mệnh đề chen giữa câu; ngăn lời thoại với ghi chú người nói | `ba tỉnh Đông Bắc – Liêu Ninh, Cát Lâm và Hắc Long Giang – lần lượt rơi vào tay giặc` |
| `-` hyphen, có space hai bên | Nối cặp danh từ đối xứng; địa danh + đơn vị hành chính; cặp địa danh chỉ tuyến đường | `Mao - Tưởng`, `Quốc - Cộng`, `đường sắt Bình - Hán`, `Hoàng Sơn - An Huy`, `bay Tây An - Diên An` |

Phép thử: nếu bỏ phần sau dấu gạch đi mà câu vẫn đủ nghĩa thì đó là mệnh đề chen → `–`. Nếu hai vế phải đi liền nhau mới thành một cái tên → `-`.

Hai ngoại lệ giữ hyphen vì là bảng chứ không phải câu: khoảng năm/số (`1917 - 1955`, `tr.164 - 165`) và danh sách mốc thời gian trong trang series (`* 1884 (17 tuổi) - Pháp chiếm Hà Nội`).

Tiêu đề bài thơ trong khối trích ghi `**Tên bài – Tác giả**` (en dash, vì là ghi công tác giả).

### 5. Ngoặc kép và nhấn mạnh

- Chỉ dùng ngoặc kép **thẳng** `"`. Không dùng `“ ”`, `« »`.
- Trích nội tuyến trong đoạn văn xuôi (lời nói ngắn, tên tác phẩm, khẩu hiệu, thành ngữ): `*"..."*` — nghiêng bọc ngoài ngoặc kép thẳng. Không dùng `**"..."**`.
- Tên báo, tên tổ chức, biệt danh dẫn trong văn xuôi: ngoặc kép thẳng, không nghiêng — `tờ "Tân Hoa nhật báo"`.
- Không lặp ngoặc kép bên trong khối `notice` cho chính nội dung được trích.

### 6. Tiêu đề bài

Frontmatter `title:` luôn theo dạng `<Nhãn>: <Tên>`, bọc trong dấu nháy kép (bắt buộc, vì có dấu hai chấm):

```yaml
title: "Kỳ 8: Mây mù vần vũ"
title: "Ngoại truyện: Thư gửi cụ Tây Hồ"
title: "Hoa Kỳ: Nhiều trở ngại nhưng vẫn giữ vị trí số 1"
```

Nếu bản thân tên kỳ còn có phụ đề thì ngăn bằng en dash: `"Kỳ 7: Hợp tác lần hai – Tưởng Giới Thạch diễn kịch"`.

Link trong trang series ở `_pages/` phải trùng khít chuỗi này, kể cả chữ hoa/thường.

### 7. Ảnh và nguồn

Ảnh kèm nguồn luôn theo đúng khuôn này:

```markdown
![alt]({{ 'assets/images/ten-file.jpg' | absolute_url }})
> <cite>
<a href="URL" target="_blank">Chú thích ảnh</a>
</cite>
```

### 8. Checklist trước khi commit một kỳ mới

- [ ] Mọi khối `{: .notice*}` đều đứng ngay sau một dòng `>`.
- [ ] Mọi attribute đều có `.text-justify`, mọi class đều có dấu chấm đứng trước.
- [ ] Mọi đoạn văn xuôi đều có `{: .text-justify}`.
- [ ] Không còn `“`, `”` trong file.
- [ ] Biến thể notice khớp vai ở mục 1; `.notice--danger` không quá 1 lần.
- [ ] Gạch ngang dùng đúng theo mục 4.
- [ ] `title:` theo dạng `"<Nhãn>: <Tên>"` (mục 6).
- [ ] Đã thêm link kỳ mới vào trang series trong `_pages/`, chuỗi link trùng khít `title:`.
- [ ] Câu trích lấy từ nguồn thì đối chiếu lại nguyên văn trong `assets/docs/` trước khi rút gọn.
