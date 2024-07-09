### Phương pháp 1:
```mermaid
graph TD;
    A[Thu thập dữ liệu] --> B[Tiền xử lý và gán nhãn]
    B --> C[Phân chia tập dữ liệu]
    C --> D1[Train Set]
    C --> D2[Test Set]
    C --> D3[Validation Set]
    D1 --> E1[Huấn luyện mô hình CNN 1]
    D1 --> E2[Huấn luyện mô hình CNN 2]
    D1 --> E3[Huấn luyện mô hình CNN 3]
    E1 --> F[Thực nghiệm trên tập dữ liệu Test]
    E2 --> F
    E3 --> F
    F --> G[Ghi nhận kết quả]

    classDef step fill:#ADD8E6,stroke:#000,stroke-width:2px,color:#fff;
    class A,B,C,D1,D2,D3,E1,E2,E3,F,G step;
```

### Phương pháp 2:
```mermaid
graph TD;
    A[Thu thập dữ liệu] --> B[Tiền xử lý và gán nhãn]
    B --> C[Phân chia tập dữ liệu]
    C --> D1[Train Set]
    C --> D2[Validation Set]
    C --> D3[Test Set]
    D1 --> E1[Tăng cường dữ liệu Train]
    D2 --> E2[Tăng cường dữ liệu Validation]
    E1 --> F1[Huấn luyện mô hình CNN 1]
    E1 --> F2[Huấn luyện mô hình CNN 2]
    E1 --> F3[Huấn luyện mô hình CNN 3]
    E2 --> F1
    E2 --> F2
    E2 --> F3
    F1 --> G[Thực nghiệm trên tập dữ liệu Test]
    F2 --> G
    F3 --> G
    G --> H[Ghi nhận kết quả]

    classDef step fill:#ADD8E6,stroke:#000,stroke-width:2px,color:#fff;
    class A,B,C,D1,D2,D3,E1,E2,F1,F2,F3,G,H step;
```

### Phương pháp 3:
```mermaid
graph TD;
    A[Thu thập dữ liệu] --> B[Tiền xử lý và gán nhãn]
    B --> C[Phân chia tập dữ liệu]
    C --> D1[Train Set]
    C --> D2[Validation Set]
    C --> D3[Test Set]
    D1 --> E1[Tăng cường dữ liệu Train]
    D2 --> E2[Tăng cường dữ liệu Validation]
    E1 --> F1[Sử dụng OpenCV cắt vùng quan trọng]
    E2 --> F2[Sử dụng OpenCV cắt vùng quan trọng]
    F1 --> G1[Huấn luyện mô hình CNN 1]
    F1 --> G2[Huấn luyện mô hình CNN 2]
    F1 --> G3[Huấn luyện mô hình CNN 3]
    F2 --> G1
    F2 --> G2
    F2 --> G3
    G1 --> H[Thực nghiệm trên tập dữ liệu Test]
    G2 --> H
    G3 --> H
    H --> I1[Sử dụng OpenCV phát hiện vùng bệnh trên ảnh test]
    I1 --> I2[Nhận diện bệnh với mô hình CNN 1]
    I1 --> I3[Nhận diện bệnh với mô hình CNN 2]
    I1 --> I4[Nhận diện bệnh với mô hình CNN 3]
    I2 --> J[Ghi nhận kết quả]
    I3 --> J
    I4 --> J

    classDef step fill:#ADD8E6,stroke:#000,stroke-width:2px,color:#fff;
    class A,B,C,D1,D2,D3,E1,E2,F1,F2,G1,G2,G3,H,I1,I2,I3,I4,J step;
```

### Demo

```mermaid
graph TD;
    A[Kết nối DroidCam từ điện thoại đến máy tính] --> B[Sử dụng điện thoại để chụp mẫu]
    B --> C[Cắt lấy vùng có dấu hiệu bệnh]
    C --> D[Đưa vào mô hình nhận diện]
    D --> E[Đưa ra kết quả]

    F[Sử dụng Streamlit để hiển thị hình ảnh từ camera điện thoại] --> G[Hiển thị hình ảnh đã chụp trên Streamlit]
    G --> H[Phát hiện dấu hiệu bệnh bằng OpenCV]
    H --> I[Hiển thị hình ảnh cùng bounding box trên Streamlit]
    I --> J[Nhận diện kết quả từ mô hình]
    J --> K[Hiển thị kết quả trên Streamlit]

    K --> L[Button nhận diện đúng hoặc sai]
    L --> M[Button gán nhãn lại cho bệnh]
    M --> N[Button lưu vào folder có nhãn tương ứng]

    classDef step fill:#ADD8E6,stroke:#000,stroke-width:2px,color:#fff;
    class A,B,C,D,E,F,G,H,I,J,K,L,M,N step;
```

Sơ đồ này mô tả các bước triển khai demo cho việc nhận diện bệnh trên xoài, từ kết nối DroidCam, chụp ảnh, cắt vùng có dấu hiệu bệnh, đưa vào mô hình nhận diện và hiển thị kết quả trên Streamlit. Các bước được liên kết một cách tuần tự và logic để dễ dàng theo dõi và triển khai. Các button trên Streamlit cho phép gán nhãn lại cho bệnh và lưu vào folder tương ứng, hỗ trợ việc cải thiện dữ liệu và mô hình nhận diện.