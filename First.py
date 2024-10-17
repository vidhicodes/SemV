import streamlit as st
import os
import numpy as np
from keras.models import load_model
from keras.layers import DepthwiseConv2D
from keras.preprocessing import image
from keras.applications.mobilenet_v2 import preprocess_input  # Adjust according to your model

# Custom DepthwiseConv2D class to handle loading without 'groups' argument
class CustomDepthwiseConv2D(DepthwiseConv2D):
    def __init__(self, *args, **kwargs):
        # Remove unsupported 'groups' argument if present
        kwargs.pop('groups', None)
        super().__init__(*args, **kwargs)

# Function to load the model
def load_model_func():
    model_path = 'keras_model.h5'  # or provide the absolute path
    print(f"Trying to load model from: {model_path}")
    
    # Check if the model file exists
    if not os.path.isfile(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")
    
    # Load the model with custom_objects
    model = load_model(model_path, custom_objects={'DepthwiseConv2D': CustomDepthwiseConv2D})
    print("Model loaded successfully.")
    return model

# Load the labels from the labels file
def load_labels():
    labels_path = 'labels.txt'  # or provide the absolute path
    print(f"Trying to load labels from: {labels_path}")

    # Check if the labels file exists
    if not os.path.isfile(labels_path):
        raise FileNotFoundError(f"Labels file not found: {labels_path}")

    with open(labels_path, 'r') as file:
        labels = file.read().splitlines()
    print("Labels loaded successfully.")
    return labels

# Function to preprocess the uploaded image
def preprocess_image(uploaded_file):
    img = image.load_img(uploaded_file, target_size=(224, 224))  # Adjust according to your model's input size
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array = preprocess_input(img_array)  # Preprocess for your model (e.g., MobileNetV2)
    return img_array

# Check the current working directory
print("Current Working Directory:", os.getcwd())

# Load the model and labels when the app starts
model = None
labels = None

try:
    model = load_model_func()
except Exception as e:
    st.error(f"Error loading model: {e}")

try:
    labels = load_labels()
except Exception as e:
    st.error(f"Error loading labels: {e}")

# Streamlit app layout
st.title("Waste Classification App")
st.write("Upload an image of waste to classify it.")

# Image upload
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
    st.write("")
    st.success("Image uploaded successfully!")

    # Check if the model was loaded successfully before making predictions
    if model is not None and labels is not None:
        # Preprocess the image and make predictions using the model
        image_data = preprocess_image(uploaded_file)
        predictions = model.predict(image_data)
        predicted_label = labels[np.argmax(predictions)]
        
        # Display the predicted label
        st.write(f"Predicted label: {predicted_label}")
    else:
        st.error("Model or labels not available. Please check if they were loaded correctly.")
