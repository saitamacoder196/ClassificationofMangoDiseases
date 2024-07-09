Dưới đây là cách xây dựng mô hình của tác giả từ đoạn code được cung cấp, kèm theo sơ đồ Mermaid mô tả các bước thực hiện:

### Các bước thực hiện

1. **Nhập các thư viện cần thiết**:
   - Import các thư viện cần thiết như `numpy`, `pandas`, `tensorflow`, `os`, và `matplotlib`.

2. **Tải và chuẩn bị dữ liệu**:
   - Xác định các thư mục chứa hình ảnh của các loại bệnh khác nhau.
   - Liệt kê và kiểm tra số lượng hình ảnh trong mỗi thư mục.
   - Sử dụng `train_test_split` để chia dữ liệu thành tập huấn luyện và tập kiểm tra.

3. **Hiển thị hình ảnh mẫu**:
   - Sử dụng `matplotlib` để hiển thị một số hình ảnh mẫu từ các tập dữ liệu.

4. **Xây dựng mô hình CNN**:
   - Sử dụng `Sequential` để xây dựng mô hình CNN với các lớp `Conv2D`, `MaxPooling2D`, `Flatten`, `Dropout`, và `Dense`.

5. **Biên dịch mô hình**:
   - Sử dụng `model.compile` với hàm mất mát `categorical_crossentropy` và bộ tối ưu `RMSprop`.

6. **Tăng cường dữ liệu**:
   - Sử dụng `ImageDataGenerator` để tăng cường dữ liệu cho tập huấn luyện và tập kiểm tra.

7. **Huấn luyện mô hình**:
   - Sử dụng `model.fit` để huấn luyện mô hình trên tập dữ liệu trong 30 epochs.

8. **Đánh giá mô hình và hiển thị kết quả**:
   - Sử dụng `matplotlib` để vẽ đồ thị kết quả huấn luyện và kiểm tra.

### Sơ đồ Mermaid

```mermaid
graph TD;
    A[Nhập các thư viện cần thiết] --> B[Tải và chuẩn bị dữ liệu]
    B --> C[Hiển thị hình ảnh mẫu]
    C --> D[Xây dựng mô hình CNN]
    D --> E[Biên dịch mô hình]
    E --> F[Tăng cường dữ liệu]
    F --> G[Huấn luyện mô hình]
    G --> H[Đánh giá mô hình và hiển thị kết quả]

    subgraph "Nhập các thư viện cần thiết"
    A1[import numpy as np]
    A2[import pandas as pd]
    A3[import tensorflow as tf]
    A4[import os]
    A5[import matplotlib.pyplot as plt]
    A6[import matplotlib.image as mpimg]
    end

    subgraph "Tải và chuẩn bị dữ liệu"
    B1[Xác định thư mục chứa hình ảnh]
    B2[Liệt kê và kiểm tra số lượng hình ảnh]
    B3[Sử dụng train_test_split]
    end

    subgraph "Hiển thị hình ảnh mẫu"
    C1[Sử dụng matplotlib để hiển thị hình ảnh]
    end

    subgraph "Xây dựng mô hình CNN"
    D1[Sequential]
    D2[Conv2D]
    D3[MaxPooling2D]
    D4[Flatten]
    D5[Dropout]
    D6[Dense]
    end

    subgraph "Biên dịch mô hình"
    E1[model.compile]
    E2[categorical_crossentropy]
    E3[RMSprop optimizer]
    end

    subgraph "Tăng cường dữ liệu"
    F1[ImageDataGenerator]
    F2[flow_from_dataframe]
    end

    subgraph "Huấn luyện mô hình"
    G1[model.fit]
    G2[30 epochs]
    end

    subgraph "Đánh giá mô hình và hiển thị kết quả"
    H1[import matplotlib.pyplot as plt]
    H2[Vẽ đồ thị kết quả]
    end

    classDef step fill:#ADD8E6,stroke:#000,stroke-width:2px,color:#fff;
    class A,B,C,D,E,F,G,H,A1,A2,A3,A4,A5,A6,B1,B2,B3,C1,D1,D2,D3,D4,D5,D6,E1,E2,E3,F1,F2,G1,G2,H1,H2 step;
```

### Mô tả sơ đồ

1. **Nhập các thư viện cần thiết**:
   - Nhập các thư viện cần thiết như `numpy`, `pandas`, `tensorflow`, `os`, và `matplotlib`.

2. **Tải và chuẩn bị dữ liệu**:
   - Xác định các thư mục chứa hình ảnh của các loại bệnh khác nhau.
   - Liệt kê và kiểm tra số lượng hình ảnh trong mỗi thư mục.
   - Sử dụng `train_test_split` để chia dữ liệu thành tập huấn luyện và tập kiểm tra.

3. **Hiển thị hình ảnh mẫu**:
   - Sử dụng `matplotlib` để hiển thị một số hình ảnh mẫu từ các tập dữ liệu.

4. **Xây dựng mô hình CNN**:
   - Sử dụng `Sequential` để xây dựng mô hình CNN với các lớp `Conv2D`, `MaxPooling2D`, `Flatten`, `Dropout`, và `Dense`.

5. **Biên dịch mô hình**:
   - Sử dụng `model.compile` với hàm mất mát `categorical_crossentropy` và bộ tối ưu `RMSprop`.

6. **Tăng cường dữ liệu**:
   - Sử dụng `ImageDataGenerator` để tăng cường dữ liệu cho tập huấn luyện và tập kiểm tra.

7. **Huấn luyện mô hình**:
   - Sử dụng `model.fit` để huấn luyện mô hình trên tập dữ liệu trong 30 epochs.

8. **Đánh giá mô hình và hiển thị kết quả**:
   - Sử dụng `matplotlib` để vẽ đồ thị kết quả huấn luyện và kiểm tra.

Sơ đồ này mô tả chi tiết các bước trong quá trình xây dựng và huấn luyện mô hình CNN của tác giả, giúp bạn dễ dàng theo dõi và hiểu được quy trình thực hiện.