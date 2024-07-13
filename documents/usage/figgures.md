Để theo dõi và quan sát quá trình huấn luyện mô hình, chúng ta cần thu thập và hiển thị các số liệu, biểu đồ, và bảng biểu sau:

### 1. **Số liệu (Metrics)**
- **Accuracy**: Độ chính xác của mô hình trên tập huấn luyện và tập kiểm tra.
- **Loss**: Hàm mất mát của mô hình trên tập huấn luyện và tập kiểm tra.
- **Precision, Recall, F1-Score**: Các chỉ số về hiệu suất phân loại.
- **Confusion Matrix**: Ma trận nhầm lẫn để hiểu rõ hơn về cách mô hình đang phân loại dữ liệu.

### 2. **Biểu đồ (Plots)**
- **Training and Validation Accuracy**: Biểu đồ thể hiện độ chính xác trên tập huấn luyện và tập kiểm tra qua từng epoch.
- **Training and Validation Loss**: Biểu đồ thể hiện hàm mất mát trên tập huấn luyện và tập kiểm tra qua từng epoch.
- **Learning Rate Schedule**: Biểu đồ hiển thị sự thay đổi của learning rate (nếu có).

### 3. **Bảng biểu (Tables)**
- **Classification Report**: Báo cáo phân loại chi tiết từ sklearn, bao gồm Precision, Recall, F1-Score cho từng lớp.
- **Model Summary**: Tóm tắt kiến trúc mô hình.

### 4. **Lượt đồ (Diagrams)**
- **Model Architecture Diagram**: Sơ đồ kiến trúc mô hình, ví dụ sử dụng công cụ như `plot_model` của Keras.

### 5. **Biểu đồ bổ sung (Additional Charts)**
- **ROC Curve**: Đường cong ROC và AUC để đánh giá hiệu suất của mô hình phân loại.
- **Precision-Recall Curve**: Đường cong Precision-Recall để đánh giá cân bằng giữa Precision và Recall.
- **Training Time per Epoch**: Biểu đồ thời gian huấn luyện cho mỗi epoch.

### Mẫu Code cho Việc Hiển thị
Dưới đây là các mẫu code để tạo và hiển thị các biểu đồ và số liệu cần thiết:

#### 1. Import Libraries
```python
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc, precision_recall_curve
import pandas as pd
import numpy as np
```

#### 2. Plot Training and Validation Accuracy and Loss
```python
history = model.fit(...)  # Fit the model and save the history

# Plot training & validation accuracy values
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')

# Plot training & validation loss values
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()
```

#### 3. Confusion Matrix
```python
# Assuming y_true and y_pred are your true and predicted labels
cm = confusion_matrix(y_true, y_pred)
plt.figure(figsize=(10, 7))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=class_names, yticklabels=class_names)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()
```

#### 4. Classification Report
```python
report = classification_report(y_true, y_pred, target_names=class_names)
print(report)
```

#### 5. ROC Curve
```python
fpr, tpr, _ = roc_curve(y_true, y_score)
roc_auc = auc(fpr, tpr)

plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc='lower right')
plt.show()
```

#### 6. Precision-Recall Curve
```python
precision, recall, _ = precision_recall_curve(y_true, y_score)

plt.figure()
plt.plot(recall, precision, color='b', lw=2)
plt.fill_between(recall, precision, alpha=0.2, color='b')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.show()
```

#### 7. Model Summary
```python
model.summary()
```

#### 8. Model Architecture Diagram
```python
from tensorflow.keras.utils import plot_model
plot_model(model, to_file='model.png', show_shapes=True, show_layer_names=True)
```

### Tổng kết
Những số liệu, biểu đồ và bảng biểu trên sẽ giúp bạn theo dõi và quan sát chi tiết quá trình huấn luyện mô hình, từ đó có thể điều chỉnh và cải thiện mô hình hiệu quả hơn.