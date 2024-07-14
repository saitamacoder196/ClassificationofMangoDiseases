import os

# Đường dẫn tới model đã huấn luyện
MODEL_PATH = os.path.join(os.getcwd(), 'best_model.h5')

# Đường dẫn tới thư mục lưu hình ảnh
IMAGES_PATH = os.path.join(os.getcwd(), 'images/captured_images')

# Đường dẫn tới database
DATABASE_PATH = os.path.join(os.getcwd(), 'database/predictions.db')

# Kích thước hình ảnh đầu vào cho model
IMG_HEIGHT = 224
IMG_WIDTH = 224

