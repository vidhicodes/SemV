import streamlit as st
import numpy as np
import os
import cv2
from keras.models import load_model
from keras.layers import DepthwiseConv2D
from keras.preprocessing import image
from keras.applications.mobilenet_v2 import preprocess_input  # Adjust according to your model
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
from PIL import Image, ImageOps

# Custom DepthwiseConv2D class to handle loading without 'groups' argument
class CustomDepthwiseConv2D(DepthwiseConv2D):
    def __init__(self, *args, **kwargs):
        kwargs.pop('groups', None)  # Remove unsupported 'groups' argument if present
        super().__init__(*args, **kwargs)

# Function to load the Keras model
@st.cache(allow_output_mutation=True)
def load_model_func():
    model_path = 'waste_classification.h5'  # or provide the absolute path
    if not os.path.isfile(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")
    model = load_model(model_path, custom_objects={'DepthwiseConv2D': CustomDepthwiseConv2D})
    return model

# Load the labels from the labels file
def load_labels():
    labels_path = 'labels.txt'
    if not os.path.isfile(labels_path):
        raise FileNotFoundError(f"Labels file not found: {labels_path}")
    with open(labels_path, 'r') as file:
        labels = file.read().splitlines()
    return labels

# Preprocess the uploaded image for the Keras model
def preprocess_image(uploaded_file):
    img = image.load_img(uploaded_file, target_size=(224, 224))  # Adjust according to model input size
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array = preprocess_input(img_array)  # Preprocess for your model (e.g., MobileNetV2)
    return img_array

# Function to preprocess the webcam image
def preprocess_webcam_image(image):
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array
    return data

# VideoTransformer for the webcam input
class VideoTransformer(VideoTransformerBase):
    def __init__(self, model, labels):
        self.model = model
        self.labels = labels

    def transform(self, frame):
        image = frame.to_ndarray(format="bgr24")
        image_resized = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
        image_normalized = preprocess_webcam_image(image_resized)
        prediction = self.model.predict(image_normalized)
        index = np.argmax(prediction)
        class_name = self.labels[index]
        confidence_score = prediction[0][index]
        cv2.putText(image, f"{class_name}: {confidence_score*100:.2f}%", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        return image

# Load the model and labels
try:
    model = load_model_func()
    labels = load_labels()
except Exception as e:
    st.error(f"Error loading model or labels: {e}")

# Streamlit app layout
st.title("Waste Classifier App")
st.write("Classify waste using either an image upload or live webcam input.")

# Option for image upload or webcam
option = st.radio("Select input type:", ('Image Upload', 'Webcam'))

if option == 'Image Upload':
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
        st.write("")
        st.success("Image uploaded successfully!")

        if model is not None and labels is not None:
            image_data = preprocess_image(uploaded_file)
            predictions = model.predict(image_data)
            predicted_label = labels[np.argmax(predictions)]
            st.write(f"Predicted label: **{predicted_label}**")
        else:
            st.error("Model or labels not available. Please check if they were loaded correctly.")

elif option == 'Webcam':
    if model is not None and labels is not None:
        webrtc_streamer(key="example", video_transformer_factory=lambda: VideoTransformer(model, labels))
    else:
        st.error("Model or labels not available. Please check if they were loaded correctly.")
