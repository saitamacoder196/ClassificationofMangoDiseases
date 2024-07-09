Dưới đây là phân tích về cách xây dựng mô hình của tác giả và các bước thực hiện, sau đó là sơ đồ Mermaid để mô tả quá trình này.

### Các bước thực hiện

1. **Nhập các thư viện cần thiết**:
   - Import các thư viện cần thiết như `numpy`, `pandas`, `tensorflow`, và `os`.

2. **Tải và chuẩn bị dữ liệu**:
   - Sử dụng `image_dataset_from_directory` để tải dữ liệu từ thư mục chứa hình ảnh.
   - Tiền xử lý dữ liệu bằng cách chuẩn hóa (normalize) giá trị pixel.

3. **Xây dựng mô hình CNN**:
   - Sử dụng `Sequential` để xây dựng mô hình CNN với các lớp `Conv2D`, `MaxPool2D`, `BatchNormalization`, `Flatten`, và `Dense`.

4. **Tóm tắt mô hình**:
   - Hiển thị cấu trúc mô hình bằng phương thức `model.summary()`.

5. **Biên dịch mô hình**:
   - Sử dụng `model.compile` với hàm mất mát `SparseCategoricalCrossentropy` và bộ tối ưu `Adam`.

6. **Huấn luyện mô hình**:
   - Sử dụng `model.fit` để huấn luyện mô hình trên tập dữ liệu trong 40 epochs.

### Sơ đồ Mermaid

```mermaid
graph TD;
    A[Nhập các thư viện cần thiết] --> B[Tải và chuẩn bị dữ liệu]
    B --> C[Xây dựng mô hình CNN]
    C --> D[Tóm tắt mô hình]
    D --> E[Biên dịch mô hình]
    E --> F[Huấn luyện mô hình]

    subgraph "Nhập các thư viện cần thiết"
    A1[import numpy as np]
    A2[import pandas as pd]
    A3[import tensorflow as tf]
    A4[import os]
    end

    subgraph "Tải và chuẩn bị dữ liệu"
    B1[image_dataset_from_directory]
    B2[Tiền xử lý dữ liệu]
    B2 --> B3[Normalize dữ liệu]
    end

    subgraph "Xây dựng mô hình CNN"
    C1[Sequential]
    C2[Conv2D]
    C3[MaxPool2D]
    C4[BatchNormalization]
    C5[Flatten]
    C6[Dense]
    end

    subgraph "Tóm tắt mô hình"
    D1["model.summary()"]
    end

    subgraph "Biên dịch mô hình"
    E1[model.compile]
    E2[SparseCategoricalCrossentropy]
    E3[Adam optimizer]
    end

    subgraph "Huấn luyện mô hình"
    F1[model.fit]
    F2[40 epochs]
    end

    classDef step fill:#ADD8E6,stroke:#000,stroke-width:2px,color:#fff;
    class A,B,C,D,E,F,A1,A2,A3,A4,B1,B2,B3,C1,C2,C3,C4,C5,C6,D1,E1,E2,E3,F1,F2 step;

```

### Mô tả sơ đồ

1. **Nhập các thư viện cần thiết**:
   - Nhập các thư viện cần thiết như `numpy`, `pandas`, `tensorflow`, và `os`.

2. **Tải và chuẩn bị dữ liệu**:
   - Sử dụng `image_dataset_from_directory` để tải dữ liệu từ thư mục chứa hình ảnh.
   - Tiền xử lý dữ liệu bằng cách chuẩn hóa giá trị pixel.

3. **Xây dựng mô hình CNN**:
   - Sử dụng `Sequential` để xây dựng mô hình CNN với các lớp `Conv2D`, `MaxPool2D`, `BatchNormalization`, `Flatten`, và `Dense`.

4. **Tóm tắt mô hình**:
   - Hiển thị cấu trúc mô hình bằng phương thức `model.summary()`.

5. **Biên dịch mô hình**:
   - Sử dụng `model.compile` với hàm mất mát `SparseCategoricalCrossentropy` và bộ tối ưu `Adam`.

6. **Huấn luyện mô hình**:
   - Sử dụng `model.fit` để huấn luyện mô hình trên tập dữ liệu trong 40 epochs.

Sơ đồ này mô tả chi tiết các bước trong quá trình xây dựng và huấn luyện mô hình CNN của tác giả, giúp bạn dễ dàng theo dõi và hiểu được quy trình thực hiện.