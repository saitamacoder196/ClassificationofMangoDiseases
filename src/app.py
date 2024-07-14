import streamlit as st
import cv2
from helper import classify_image, save_prediction_to_db, save_captured_image

# Streamlit interface
st.title("Image Classification Demo")

# Capture image from DroidCam
camera = cv2.VideoCapture('http://<DroidCam_URL>/video')

if not camera.isOpened():
    st.error("Error: Could not open camera.")
else:
    ret, frame = camera.read()
    if ret:
        st.image(frame, caption="Captured Image", use_column_width=True)
        predicted_class, predictions = classify_image(frame)
        
        # Display the predictions
        st.write("Predicted Class:", predicted_class)
        st.write("Predictions:", predictions)
        
        # Save the image and predictions
        image_name = "captured_image.jpg"
        image_path = save_captured_image(frame, image_name)
        save_prediction_to_db(image_path, predicted_class, predictions)
    else:
        st.error("Error: Could not capture image.")

camera.release()

