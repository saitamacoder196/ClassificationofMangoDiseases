import os
import cv2
import numpy as np
import sqlite3
from datetime import datetime
import tensorflow as tf
from settings import MODEL_PATH, IMG_HEIGHT, IMG_WIDTH, IMAGES_PATH, DATABASE_PATH

# Load pre-trained model
model = tf.keras.models.load_model(MODEL_PATH)

# Create a function to preprocess the image
def preprocess_image(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (IMG_WIDTH, IMG_HEIGHT))  # Resize to the input shape required by the model
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    image = image / 255.0  # Normalize the image
    return image

# Create a function to make predictions
def classify_image(image):
    processed_image = preprocess_image(image)
    predictions = model.predict(processed_image)
    predicted_class = np.argmax(predictions, axis=1)
    return predicted_class, predictions

# Save prediction to database
def save_prediction_to_db(image_path, predicted_class, predictions):
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS predictions
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  image_path TEXT,
                  predicted_class INTEGER,
                  predictions TEXT,
                  timestamp TEXT)''')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    c.execute('INSERT INTO predictions (image_path, predicted_class, predictions, timestamp) VALUES (?, ?, ?, ?)',
              (image_path, predicted_class, str(predictions), timestamp))
    conn.commit()
    conn.close()

# Save captured image
def save_captured_image(image, image_name):
    if not os.path.exists(IMAGES_PATH):
        os.makedirs(IMAGES_PATH)
    image_path = os.path.join(IMAGES_PATH, image_name)
    cv2.imwrite(image_path, image)
    return image_path

