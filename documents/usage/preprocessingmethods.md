Dưới đây là bảng trình bày các phương pháp tiền xử lý ảnh sau khi đã thu thập:

| #   | Phương Pháp                  | Mô Tả                                                                                                      | Lợi Ích                                                                                                    |
|-----|------------------------------|------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| 1   | Chuyển đổi màu sắc           | Chuyển đổi hình ảnh sang thang độ xám hoặc các không gian màu khác như HSV.                                 | Giảm bớt dữ liệu không cần thiết, làm nổi bật các đặc trưng quan trọng.                                    |
| 2   | Cân bằng sáng                | Điều chỉnh độ sáng của hình ảnh để đảm bảo hình ảnh có độ tương phản tốt.                                   | Tăng độ tương phản và làm rõ các chi tiết trong hình ảnh.                                                  |
| 3   | Lọc nhiễu                    | Sử dụng các bộ lọc để loại bỏ nhiễu (noise) từ hình ảnh, như bộ lọc Gaussian, Median, hoặc Bilateral.       | Giảm nhiễu, làm mịn hình ảnh, cải thiện chất lượng hình ảnh.                                               |
| 4   | Cắt ảnh (Cropping)           | Cắt bỏ các phần không cần thiết của hình ảnh, chỉ giữ lại phần chứa thông tin quan trọng.                   | Tập trung vào vùng chứa đối tượng cần nhận diện, giảm kích thước dữ liệu.                                  |
| 5   | Thay đổi kích thước          | Thay đổi kích thước hình ảnh để đồng nhất kích thước các ảnh đầu vào.                                        | Đảm bảo tất cả các hình ảnh đầu vào có cùng kích thước, thuận tiện cho quá trình huấn luyện mô hình.      |
| 6   | Tăng cường dữ liệu           | Sử dụng các kỹ thuật như xoay, lật, dịch chuyển, phóng to/thu nhỏ, để tạo thêm các mẫu từ dữ liệu hiện có. | Tăng số lượng mẫu huấn luyện, giảm hiện tượng overfitting, cải thiện độ chính xác của mô hình.            |
| 7   | Chuẩn hóa (Normalization)    | Chuẩn hóa giá trị pixel của hình ảnh về một khoảng cố định, thường là [0, 1] hoặc [-1, 1].                   | Đảm bảo tính nhất quán về giá trị pixel, giúp mô hình học nhanh hơn và hiệu quả hơn.                       |
| 8   | Tách nền (Background Removal)| Loại bỏ nền của hình ảnh, chỉ giữ lại đối tượng cần nhận diện.                                              | Loại bỏ nhiễu từ nền, tập trung vào đối tượng cần phân loại.                                                |
| 9   | Phát hiện biên (Edge Detection) | Sử dụng các thuật toán như Canny, Sobel để phát hiện các biên của đối tượng trong hình ảnh.                  | Làm nổi bật các đặc trưng quan trọng, hỗ trợ quá trình phân loại và nhận diện.                              |
| 10  | Chuyển đổi định dạng         | Chuyển đổi hình ảnh sang các định dạng khác nhau như JPEG, PNG, BMP tùy thuộc vào yêu cầu của hệ thống.     | Đảm bảo hình ảnh ở định dạng phù hợp với các bước xử lý tiếp theo và yêu cầu của hệ thống.                 |

Bảng này liệt kê các phương pháp tiền xử lý ảnh phổ biến, mô tả chi tiết và lợi ích của từng phương pháp, giúp bạn dễ dàng lựa chọn và áp dụng trong quá trình xử lý ảnh thu thập được.