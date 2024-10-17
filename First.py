import streamlit as st
import os
import numpy as np
from keras.models import load_model
from keras.layers import DepthwiseConv2D
from keras.preprocessing import image
from keras.applications.mobilenet_v2 import preprocess_input
from PIL import Image

# Custom DepthwiseConv2D class to handle loading without 'groups' argument
class CustomDepthwiseConv2D(DepthwiseConv2D):
    def __init__(self, *args, **kwargs):
        kwargs.pop('groups', None)  # Remove unsupported 'groups' argument if present
        super().__init__(*args, **kwargs)

# Function to load the model
@st.cache(allow_output_mutation=True)
def load_model_func():
    model_path = 'keras_model.h5'  # or provide the absolute path
    if not os.path.isfile(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")
    
    # Load the model with custom_objects
    model = load_model(model_path, custom_objects={'DepthwiseConv2D': CustomDepthwiseConv2D})
    return model

# Load the labels from the labels file
def load_labels():
    labels_path = 'labels.txt'  # or provide the absolute path
    if not os.path.isfile(labels_path):
        raise FileNotFoundError(f"Labels file not found: {labels_path}")

    with open(labels_path, 'r') as file:
        labels = file.read().splitlines()
    return labels

# Function to preprocess the uploaded image
def preprocess_image(uploaded_file):
    img = image.load_img(uploaded_file, target_size=(224, 224))  # Adjust according to model input size
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array = preprocess_input(img_array)  # Preprocess for your model (e.g., MobileNetV2)
    return img_array

# Function to classify an image
def classify_image(model, labels, image_data):
    predictions = model.predict(image_data)
    predicted_label = labels[np.argmax(predictions)]
    return predicted_label

# Function to handle webcam capture and classification
def handle_webcam_capture(model, labels):
    st.write("### Use your webcam to classify waste")
    camera_input = st.camera_input("Take a picture")
    
    if camera_input is not None:
        # Open the image from the camera input
        image_data = Image.open(camera_input)  # Convert camera input to PIL Image

        # Display the captured image
        st.image(image_data, caption='Captured Image', use_column_width=True)
        st.write("")

        # Preprocess the image and make predictions using the model
        image_data = preprocess_image(camera_input)  # Use the camera input directly
        if model is not None and labels is not None:
            predicted_label = classify_image(model, labels, image_data)
            st.write(f"Predicted label: {predicted_label}")
        else:
            st.error("Model or labels not available. Please check if they were loaded correctly.")

# Show classification page
def show_classification_page():
    # Streamlit app layout
    st.title("Waste Classification App")
    st.write("Upload an image of waste to classify it, or use your webcam.")

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

    # Image upload
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display uploaded image
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
        st.write("")

        # Preprocess the image and make predictions using the model
        image_data = preprocess_image(uploaded_file)
        if model is not None and labels is not None:
            predicted_label = classify_image(model, labels, image_data)
            st.write(f"Predicted label: {predicted_label}")
        else:
            st.error("Model or labels not available. Please check if they were loaded correctly.")

    # Call the function to handle webcam input
    handle_webcam_capture(model, labels)

# Run the Streamlit app
if __name__ == "__main__":
    show_classification_page()
