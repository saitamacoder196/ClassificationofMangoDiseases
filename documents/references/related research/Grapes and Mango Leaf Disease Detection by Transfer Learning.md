### Tóm tắt bài báo: "Deep Learning Precision Farming: Grapes and Mango Leaf Disease Detection by Transfer Learning"

#### Tác giả và nơi công bố
- **Tác giả:** U Sanath Rao, R Swathi, V Sanjana, L Arpitha, K Chandrasekhar, Chinmayi, Pramod Kumar Naik
- **Nơi công bố:** Global Transitions Proceedings, 2 (2021) 535-544
- **DOI:** [10.1016/j.gltp.2021.08.002](https://doi.org/10.1016/j.gltp.2021.08.002)

#### Nội dung chính
Bài báo này tập trung vào việc ứng dụng học sâu (Deep Learning) và chuyển giao học tập (Transfer Learning) để phát hiện bệnh trên lá nho và lá xoài. Mục tiêu chính là phát hiện và phân loại bệnh trên lá cây, sử dụng mạng nơ-ron tích chập (CNN) và kiến trúc AlexNet đã được huấn luyện trước.

#### Các bước thực hiện
1. **Thu thập dữ liệu:**
   - Sử dụng bộ dữ liệu Plant Village và thu thập thêm từ các trang trại.
   - Tổng cộng 8,438 hình ảnh của lá nho và lá xoài bị bệnh và khỏe mạnh được sử dụng.

2. **Xử lý dữ liệu:**
   - Tiền xử lý hình ảnh để cải thiện chất lượng và dán nhãn dữ liệu.
   - Phân chia dữ liệu thành tập huấn luyện (80%) và tập kiểm tra (20%).

3. **Mô hình học sâu:**
   - Sử dụng mạng nơ-ron tích chập (CNN) AlexNet cho việc trích xuất đặc trưng và phân loại.
   - Mạng AlexNet được tinh chỉnh để phù hợp với bài toán phân loại bệnh trên lá cây.

4. **Kết quả:**
   - Độ chính xác đạt 99% cho lá nho và 89% cho lá xoài.
   - Một ứng dụng trên Android có tên "JIT CROPFIX" được phát triển để triển khai mô hình trên điện thoại thông minh.

#### Các loại bệnh được phát hiện
- **Lá xoài:**
  - Bệnh thán thư (Anthracnose)
  - Bệnh đốm đen
  - Bệnh đốm trắng

- **Lá nho:**
  - Bệnh đốm đen
  - Bệnh đốm lá
  - Bệnh nấm mốc bột

#### Kết luận
- Hệ thống phát hiện bệnh trên lá cây giúp cải thiện chất lượng và sản lượng nông sản, giảm thiểu tổn thất kinh tế và nâng cao độ chính xác trong phát hiện bệnh.
- Ứng dụng AlexNet với chuyển giao học tập chứng minh hiệu quả cao trong việc phân loại hình ảnh lá cây bị bệnh và khỏe mạnh.
- Phát triển ứng dụng di động để triển khai mô hình học sâu trên thiết bị di động, hỗ trợ nông dân trong việc giám sát và quản lý bệnh trên cây trồng.

#### Hạn chế và hướng phát triển
- Cần mở rộng tập dữ liệu để bao gồm nhiều loại bệnh và điều kiện ánh sáng khác nhau.
- Phát triển mô hình để nhận diện sớm các dấu hiệu bệnh, cải thiện khả năng xử lý trong điều kiện thực tế như ánh sáng thay đổi và các yếu tố ngoại cảnh.

Bài báo này cho thấy tiềm năng lớn của việc áp dụng học sâu và chuyển giao học tập trong nông nghiệp chính xác, đặc biệt là trong việc phát hiện và quản lý bệnh trên cây trồng.