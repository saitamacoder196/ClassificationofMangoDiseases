Để kiểm tra và đánh giá một mô hình sau khi đã huấn luyện xong, các số liệu, bảng biểu, và biểu đồ sau đây là rất quan trọng:

### Số liệu (Metrics)
1. **Accuracy**: Độ chính xác của mô hình.
2. **Precision**: Độ chính xác khi dự đoán đúng lớp.
3. **Recall**: Khả năng của mô hình phát hiện đúng lớp.
4. **F1-Score**: Sự cân bằng giữa Precision và Recall.
5. **AUC-ROC Score**: Diện tích dưới đường cong ROC để đánh giá khả năng phân loại của mô hình.

### Bảng biểu (Tables)
1. **Classification Report**: Bảng báo cáo chi tiết về Precision, Recall, F1-Score cho từng lớp.
2. **Confusion Matrix**: Ma trận nhầm lẫn để xem xét chi tiết các trường hợp dự đoán đúng và sai của mô hình.

### Biểu đồ (Plots)
1. **Training and Validation Accuracy**: Biểu đồ thể hiện độ chính xác trên tập huấn luyện và tập kiểm tra qua từng epoch.
2. **Training and Validation Loss**: Biểu đồ thể hiện hàm mất mát trên tập huấn luyện và tập kiểm tra qua từng epoch.
3. **ROC Curve**: Đường cong ROC để xem xét khả năng phân loại của mô hình cho từng lớp.
4. **Precision-Recall Curve**: Đường cong Precision-Recall để đánh giá sự cân bằng giữa Precision và Recall.

### Bảng tóm tắt cần thiết
1. **Model Summary**: Tóm tắt kiến trúc mô hình, số lượng tham số.

### Mẫu Code cho Việc Kiểm tra và Đánh giá

#### Import Libraries
```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc, precision_recall_curve
from sklearn.preprocessing import label_binarize
import tensorflow as tf
```

#### Plot Training and Validation Accuracy and Loss
```python
def plot_history(history, model_name, augmented=False):
    base_path = get_model_save_path(model_name, augmented)
    
    # Plot training & validation accuracy values
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title(f'Model accuracy - {model_name}')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Validation'], loc='upper left')
    plt.savefig(os.path.join(base_path, 'accuracy.png'))
    plt.close()
    
    # Plot training & validation loss values
    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title(f'Model loss - {model_name}')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Validation'], loc='upper left')
    plt.savefig(os.path.join(base_path, 'loss.png'))
    plt.close()
```

#### Save Classification Report
```python
def save_classification_report(y_true, y_pred, class_names, base_path):
    report = classification_report(y_true, y_pred, target_names=class_names, output_dict=True)
    df = pd.DataFrame(report).transpose()
    df.to_csv(os.path.join(base_path, 'classification_report.csv'), index=True)
```

#### Save Confusion Matrix
```python
def save_confusion_matrix(y_true, y_pred, class_names, base_path):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(10, 7))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=class_names, yticklabels=class_names)
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.title('Confusion Matrix')
    plt.savefig(os.path.join(base_path, 'confusion_matrix.png'))
    plt.close()
```

#### Save ROC Curve
```python
def save_roc_curve(y_true, y_score, base_path, num_classes):
    y_true_binarized = label_binarize(y_true, classes=[i for i in range(num_classes)])
    
    fpr = dict()
    tpr = dict()
    roc_auc = dict()
    for i in range(num_classes):
        fpr[i], tpr[i], _ = roc_curve(y_true_binarized[:, i], y_score[:, i])
        roc_auc[i] = auc(fpr[i], tpr[i])

    # Plot ROC curve for each class
    plt.figure()
    for i in range(num_classes):
        plt.plot(fpr[i], tpr[i], lw=2, label='Class {0} (area = {1:0.2f})'.format(i, roc_auc[i]))
    
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic')
    plt.legend(loc='lower right')
    plt.savefig(os.path.join(base_path, 'roc_curve.png'))
    plt.close()
```

#### Save Precision-Recall Curve
```python
def save_precision_recall_curve(y_true, y_score, base_path, num_classes):
    y_true_binarized = label_binarize(y_true, classes=[i for i in range(num_classes)])
    
    precision = dict()
    recall = dict()
    for i in range(num_classes):
        precision[i], recall[i], _ = precision_recall_curve(y_true_binarized[:, i], y_score[:, i])

    # Plot Precision-Recall curve for each class
    plt.figure()
    for i in range(num_classes):
        plt.plot(recall[i], precision[i], lw=2, label='Class {0}'.format(i))
    
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision-Recall Curve')
    plt.legend(loc='lower right')
    plt.savefig(os.path.join(base_path, 'precision_recall_curve.png'))
    plt.close()
```

#### Evaluate Model
```python
def evaluate_model(model, valid_generator, model_name, augmented=False):
    base_path = get_model_save_path(model_name, augmented)
    y_true = valid_generator.classes
    y_pred = model.predict(valid_generator)
    y_pred_classes = np.argmax(y_pred, axis=1)
    
    save_classification_report(y_true, y_pred_classes, class_names, base_path)
    save_confusion_matrix(y_true, y_pred_classes, class_names, base_path)
    save_roc_curve(y_true, y_pred, base_path, num_classes=len(class_names))
    save_precision_recall_curve(y_true, y_pred, base_path, num_classes=len(class_names))
```

### Tóm tắt
Các số liệu, bảng biểu và biểu đồ nêu trên sẽ cung cấp cho bạn một cái nhìn toàn diện về hiệu suất của mô hình sau khi đã huấn luyện xong, giúp bạn hiểu rõ hơn về các điểm mạnh và điểm yếu của mô hình, từ đó có thể cải thiện và tối ưu hóa mô hình nếu cần thiết.