Dưới đây là nội dung cho một file README giới thiệu về tập dữ liệu huấn luyện MangoFruitDDS:

---

# MangoFruitDDS Dataset

## Giới thiệu

MangoFruitDDS là một tập dữ liệu về các bệnh trên quả xoài, được sử dụng để huấn luyện các mô hình nhận diện bệnh. Tập dữ liệu này chứa hình ảnh của các loại bệnh phổ biến trên quả xoài cũng như hình ảnh của các quả xoài khỏe mạnh. Các hình ảnh được chụp từ một vườn xoài ở Senegal, sử dụng camera điện thoại di động.

Tập dữ liệu được lấy từ [Kaggle](https://www.kaggle.com/datasets/warcoder/mangofruitdds) và được cung cấp dưới hai phiên bản:
- **SenMangoFruitDDS_original**: Phiên bản chứa các hình ảnh gốc.
- **SenMangoFruitDDS_bgremoved**: Phiên bản chứa các hình ảnh đã được loại bỏ nền.

## Nội dung tập dữ liệu

Tập dữ liệu bao gồm tổng cộng 1700 hình ảnh có kích thước 224x224 ở định dạng JPG, thuộc 5 danh mục sau:
- Alternaria
- Anthracnose (Thán Thư)
- Black Mould Rot (Mốc Đen)
- Healthy (Xoài Khỏe Mạnh)
- Stem end Rot (Thối Cuống)

## Số liệu về các danh mục

Dưới đây là số liệu về số lượng hình ảnh gốc và hình ảnh sau khi tăng cường dữ liệu của mỗi danh mục:

| Class             | Gốc | Tăng cường |
|-------------------|-----|------------|
| Alternaria        | 165 | 969        |
| Anthracnose       | 129 | 919        |
| Black Mould Rot   | 182 | 974        |
| Healthy           | 205 | 996        |
| Stem end Rot      | 157 | 990        |

## Giấy phép

Tập dữ liệu này được cấp phép dưới giấy phép [CC BY NC 3.0](https://creativecommons.org/licenses/by-nc/3.0/). Bạn có thể sử dụng dữ liệu này cho mục đích phi thương mại, với điều kiện là phải ghi nhận nguồn và giấy phép tương ứng.

## Liên kết

- [Tải xuống từ Kaggle](https://www.kaggle.com/datasets/warcoder/mangofruitdds)
