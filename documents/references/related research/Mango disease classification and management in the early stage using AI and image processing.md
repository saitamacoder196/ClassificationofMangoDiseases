### Tóm tắt bài báo: "Mango disease classification and management in the early stage using AI and image processing"

#### Tác giả và nơi công bố
- **Tác giả:** Mr. Vishwa Senevirathne
- **Giám sát:** Mr. Sudharshana Welihinda
- **Nơi công bố:** Trường Đại học Westminster, 2022

#### Giới thiệu
- **Mục tiêu**: Phát hiện và phân loại sớm sáu loại bệnh trên xoài sử dụng kỹ thuật xử lý hình ảnh và các thuật toán học sâu.
- **Bối cảnh**: Nông nghiệp là một trong những ngành kinh tế chính ở các nước Nam Á, và trồng xoài là một phần quan trọng trong hoạt động nông nghiệp. Tuy nhiên, việc tư vấn chuyên gia để xác định bệnh trên cây trồng có thể mất nhiều thời gian và chi phí cao, cùng với sự thiếu hụt các chuyên gia giàu kinh nghiệm.

#### Phương pháp
- **Công nghệ sử dụng**: Ứng dụng tầm nhìn máy tính và trí tuệ nhân tạo để giải quyết các vấn đề nông nghiệp, đặc biệt là phát hiện bệnh trên cây trồng.
- **Mô hình học sâu**: Sử dụng học chuyển tiếp (transfer learning) dựa trên mô hình đã được huấn luyện trước trên ImageNet, cụ thể là sử dụng MobileNet.
- **Triển khai trên thiết bị di động**: Mô hình TensorFlow Lite được sử dụng vì hoạt động tốt trên các thiết bị di động và có khả năng xử lý cục bộ.

#### Dữ liệu và tiền xử lý
- **Dữ liệu**: Bộ dữ liệu gồm khoảng 1200 hình ảnh lá xoài, bao gồm sáu loại bệnh: Phoma blight, Sooty mould, Scab, Anthracnose, Bacterial Canker, và lá khỏe mạnh.
- **Tăng cường dữ liệu**: Áp dụng các kỹ thuật tăng cường dữ liệu để xử lý thiếu hụt dữ liệu hình ảnh.

#### Kết quả
- **Độ chính xác mô hình**: Mô hình đạt độ chính xác khoảng 75% trong giai đoạn kiểm tra và đánh giá.
- **F1 Score**:
  - Anthracnose: 94%
  - Phoma blight: 64%
  - Scab: 64%
  - Sooty mould: 58%
  - Bacterial Canker: 75%
  - Healthy: 94%

#### Từ khóa
- Tầm nhìn máy tính, Học chuyển tiếp, Mạng nơ-ron tích chập, Phát hiện trên di động, Phát hiện bệnh trên xoài

### Kết luận
Bài báo này trình bày một hệ thống sử dụng trí tuệ nhân tạo và xử lý hình ảnh để phát hiện và phân loại sớm các bệnh trên xoài. Hệ thống sử dụng MobileNet và TensorFlow Lite để đảm bảo khả năng xử lý nhanh chóng và hiệu quả trên thiết bị di động, giúp nông dân phát hiện và quản lý bệnh cây trồng một cách hiệu quả hơn.