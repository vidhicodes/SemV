import streamlit as st
import numpy as np
from PIL import Image, ImageOps
from tensorflow.keras.models import load_model

# Load the model
model = load_model('keras_model.h5')

# Load the class names from labels.txt
with open('labels.txt', 'r') as f:
    class_names = [line.strip() for line in f.readlines()]

# Function to preprocess the image
def preprocess(image):
    size = (224, 224)  # Image size required by the model
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array
    return data

# Streamlit UI
st.title("Waste Classification App")
st.write("Upload an image to classify the type of waste.")

# Image uploader in Streamlit
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open and preprocess the image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write("")
    st.write("Classifying...")

    # Preprocess the image and make predictions
    data = preprocess(image)
    prediction = model.predict(data)

    # Get the index with the highest confidence
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Output the result
    st.write(f"**Class:** {class_name}")
    st.write(f"**Confidence Score:** {confidence_score:.2f}")
