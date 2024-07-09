
## Tóm tắt
Nghiên cứu này đề cập đến việc phân loại và sắp xếp xoài Carabao dựa trên hình dạng và kích thước sử dụng xử lý hình ảnh và mạng nơ-ron xác suất (PNN). Trọng tâm là phân loại xoài thành ba kích thước: nhỏ, vừa và lớn.

## Giới thiệu
Xoài là một trong những loại trái cây xuất khẩu chính của Philippines, với xoài Carabao được xem là một trong những giống tốt nhất thế giới. Quá trình phân loại và sắp xếp sau thu hoạch ảnh hưởng lớn đến việc xuất khẩu xoài. Việc phân loại dựa trên chất lượng của trái cây, và chất lượng cao sẽ có giá trị và nhu cầu cao hơn trên thị trường.

## Phương pháp
### Khung khái niệm
1. **Thu thập mẫu xoài**: Sử dụng camera để thu thập hình ảnh của xoài.
2. **Tiền xử lý hình ảnh**: Tách xoài ra khỏi nền, chuyển đổi thành ảnh xám, và sau đó chuyển đổi thành ảnh nhị phân để loại bỏ sự biến đổi màu sắc.
3. **Trích xuất đặc trưng**: Bao gồm diện tích, màu sắc và vùng đốm đen.
4. **Phân loại bằng PNN**: Sử dụng các đặc trưng đã trích xuất để phân loại xoài vào một trong ba kích thước hoặc các loại khác.

### Hệ thống
- **Phần cứng**: Arduino microcontroller kết nối với máy tính để điều khiển các cảm biến, động cơ DC, và động cơ Servo.
- **Quy trình**: Xoài được đặt vào khay và di chuyển trên băng chuyền. Hình ảnh của xoài được chụp và tiền xử lý, sau đó được phân loại dựa trên các đặc trưng đã trích xuất và phân loại bằng PNN. Kết quả phân loại sẽ điều khiển các lá chắn trên băng chuyền để chuyển hướng xoài vào đúng loại của nó.

## Kết quả và thảo luận
- **Độ chính xác**: Độ chính xác của hệ thống là 87.5%, được xác nhận bằng ma trận nhầm lẫn. 
- **Phân tích**: Sử dụng T-test hai phía để xác minh tính khả thi của phương pháp, kết quả cho thấy không có sự khác biệt đáng kể giữa trọng lượng đo được và trọng lượng tính toán.
- **Hạn chế**: Hệ thống gặp khó khăn trong việc xác định các loại xoài khác nhau, đặc biệt là các loại không thuộc ba kích thước chính.

## Kết luận
Nghiên cứu đã phát triển thành công một hệ thống phân loại và sắp xếp xoài Carabao dựa trên hình dạng và kích thước sử dụng PNN. Hệ thống có thể được triển khai trong thực tế để hỗ trợ quá trình phân loại sau thu hoạch, tăng giá trị và nhu cầu của sản phẩm trên thị trường.

【12:0†020065_1_online.pdf】.