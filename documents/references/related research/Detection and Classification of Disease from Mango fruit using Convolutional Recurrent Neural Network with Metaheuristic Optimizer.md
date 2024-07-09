### Tóm tắt bài báo "Detection and Classification of Disease from Mango fruit using Convolutional Recurrent Neural Network with Metaheuristic Optimizer"

#### Tóm tắt:
Bài báo này tập trung vào việc phát hiện và phân loại các bệnh trên trái xoài thông qua việc sử dụng mạng nơ-ron tích chập hồi quy (Convolutional Recurrent Neural Network - CRNN) kết hợp với thuật toán tối ưu metaheuristic. Các bệnh trên trái xoài gây ra thiệt hại đáng kể cho sản lượng và chất lượng nông sản. Quá trình kiểm tra thủ công thường tốn nhiều thời gian và công sức, trong khi các phương pháp tự động có thể cung cấp độ chính xác cao hơn.

#### Phương pháp:
1. **Tiền xử lý dữ liệu**: Gồm hai bước chính là loại bỏ nền và tăng cường độ tương phản của hình ảnh.
2. **Phân đoạn đối tượng**: Sử dụng phương pháp phân đoạn để tách biệt các đặc điểm của hình ảnh.
3. **Trích xuất đặc trưng**: Các đặc trưng được trích xuất từ hình ảnh và đưa vào mạng CRNN_FOA.
4. **Phân loại**: Sử dụng mạng CRNN với thuật toán tối ưu FireFly (FOA) để phân loại các bệnh trên trái xoài.

#### Kết quả:
- Mô hình đề xuất đạt độ chính xác 97% trong việc phân loại các bệnh trên xoài.
- Mô hình này được đánh giá và xác thực thông qua các thử nghiệm thực tế, cho thấy hiệu quả vượt trội so với các phương pháp truyền thống.

#### Từ khóa:
- Mango fruit
- Optimization
- Background removal
- Instance segmentation
- CNN
- Disease classification

Bài báo nhấn mạnh tầm quan trọng của việc sử dụng các phương pháp học sâu và các thuật toán tối ưu hóa để nâng cao hiệu quả và độ chính xác trong việc phân loại bệnh trên trái xoài, đồng thời giảm bớt sự phụ thuộc vào lao động thủ công.