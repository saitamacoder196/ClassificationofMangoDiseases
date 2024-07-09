

## Tóm Tắt
Bài viết giới thiệu một mô hình mạng nơ-ron tích chập hoàn chỉnh (FrCNnet) để phân đoạn và nhận diện bệnh trên lá xoài. Mô hình được đánh giá trên bộ dữ liệu thời gian thực do viện nghiên cứu xoài ở Multan, Pakistan cung cấp và so sánh hiệu suất phân đoạn với các mô hình hiện đại khác như Vgg16, Vgg-19, và Unet. Kết quả cho thấy mô hình FrCNnet đạt độ chính xác phân đoạn 99.2%, cao hơn các mô hình khác.

## Giới Thiệu
Bệnh trên cây trồng gây thiệt hại lớn cho kinh tế của các nước nông nghiệp, đặc biệt là xoài, loại trái cây quan trọng của Pakistan. Việc phân đoạn chính xác vùng bệnh là yếu tố then chốt để nhận diện bệnh. Bài viết đề xuất mô hình FrCNnet dựa trên CNN để phân đoạn phần bệnh trên lá xoài, giúp nhận diện bệnh như Anthracnose và Apical Necrosis.

## Phương Pháp
### Quy Trình
1. **Thu Thập Dữ Liệu**: Bộ dữ liệu gồm hình ảnh lá xoài bị bệnh từ các vùng sản xuất xoài ở Pakistan.
2. **Tiền Xử Lý Hình Ảnh**: Gồm thay đổi kích thước, tăng cường độ tương phản và tạo mặt nạ chân thực.
3. **Mô Hình FrCNnet**: Một phiên bản tùy chỉnh của mô hình U-net, loại bỏ bước ghép nối để giữ lại độ phân giải đầy đủ của các đặc trưng.
4. **Trích Xuất và Kết Hợp Đặc Trưng**: Trích xuất các đặc trưng màu sắc, kết cấu và hình học, sau đó kết hợp chúng bằng phương pháp CCA và giảm chiều bằng NCA.
5. **Huấn Luyện và Kiểm Tra**: Huấn luyện mô hình trên bộ dữ liệu đã qua tiền xử lý và kiểm tra độ chính xác phân đoạn và phân loại.

## Kết Quả và Thảo Luận
- **Phân Đoạn**: Mô hình FrCNnet đạt độ chính xác phân đoạn 99.2%, cao hơn so với Vgg-16 (77.4%), Vgg-19 (73%), và Unet (91.7%).
- **Phân Loại**: Sau khi trích xuất và kết hợp đặc trưng, áp dụng 10 bộ phân loại khác nhau, kết quả cho thấy Quadratic-SVM và Cubic-SVM đạt độ chính xác cao nhất 98.9%.

## Kết Luận
Mô hình FrCNnet đã chứng minh khả năng phân đoạn và nhận diện bệnh trên lá xoài hiệu quả, vượt trội hơn các mô hình hiện tại. Kết quả cho thấy hệ thống tự động này có thể hỗ trợ đắc lực cho các nhà nông học và nông dân trong việc phát hiện và quản lý bệnh trên cây trồng. 

## Cảm Ơn
Tác giả cảm ơn viện nghiên cứu xoài Multan và công ty Tara Crop Sciences vì đã cung cấp dữ liệu hình ảnh.

## Tài Liệu Tham Khảo
Bài viết trích dẫn nhiều nghiên cứu trước đó về phân loại và nhận diện bệnh cây trồng sử dụng các kỹ thuật AI khác nhau. 

【23:0†Nguồn: TSP_CMC_17700.pdf】.