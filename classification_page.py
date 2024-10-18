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
    img = image.load_img(uploaded_file, target_size=(224, 224))  # Adjust according to your model's input size
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array = preprocess_input(img_array)  # Preprocess for your model (e.g., MobileNetV2)
    return img_array

# Function to classify an image
def classify_image(model, labels, image_data):
    predictions = model.predict(image_data)
    predicted_label = labels[np.argmax(predictions)]
    return predicted_label

# Function to get recycling suggestions based on the predicted label
def get_suggestions(predicted_label):
    suggestions = {
        "Plastic": [
            "1. Recycle plastic containers by rinsing and placing them in recycling bins.",
            "2. Consider using reusable bags instead of plastic ones.",
            "3. Upcycle plastic bottles into planters or storage containers."
        ],
        "Metal": [
            "1. Clean and recycle metal cans in your local recycling program.",
            "2. Use metal containers for storage instead of plastic.",
            "3. Donate old metal items instead of throwing them away."
        ],
        "Paper": [
            "1. Recycle paper products like newspapers and cardboard.",
            "2. Use both sides of paper before discarding.",
            "3. Shred sensitive documents and recycle the scraps."
        ],
        "Glass": [
            "1. Rinse glass jars and bottles before recycling them.",
            "2. Consider using glass containers for food storage.",
            "3. Repurpose glass jars as vases or decorative items."
        ],
        "Compost": [
            "1. Compost kitchen scraps to create nutrient-rich soil.",
            "2. Use compost bins or piles to reduce waste.",
            "3. Educate others about the benefits of composting."
        ],
        "Cardboard": [
            "1. Flatten cardboard boxes before recycling.",
            "2. Reuse cardboard for crafts or storage.",
            "3. Consider donating cardboard boxes to local schools or charities."
        ]
    }
    return suggestions.get(predicted_label, ["No specific suggestions available."])

# Show classification page
def show_classification_page():
    # Set background image and styles
    st.markdown(
        """
        <style>
        body {
            background-image: url("https://png.pngtree.com/thumb_back/fh260/background/20220217/pngtree-green-simple-atmospheric-waste-classification-illustration-background-image_953325.jpg");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
            background-repeat: no-repeat;
            color: #333;
            font-family: 'Arial', sans-serif;
        }
        .title {
            text-align: center;
            font-size: 2.5em;
            color: #fff;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.7);
        }
        .button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1.2em;
            transition: background-color 0.3s ease;
        }
        .button:hover {
            background-color: #45a049;
        }
        .suggestion {
            background-color: #00A86B;
            border-radius: 8px;
            padding: 10px;
            margin-top: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Streamlit app layout
    st.markdown('<div class="title">Waste Classification App</div>', unsafe_allow_html=True)
    st.write("Select an option to classify waste:")

    # Add radio button for choosing the input method
    option = st.radio("Choose input method:", ("Upload Image", "Use Webcam"))

    # Load the model and labels when the app starts
    model, labels = None, None

    try:
        model = load_model_func()
        st.success("Model loaded successfully!", icon="✅")
    except Exception as e:
        st.error(f"Error loading model: {e}")

    try:
        labels = load_labels()
        st.success("Labels loaded successfully!", icon="✅")
    except Exception as e:
        st.error(f"Error loading labels: {e}")

    # Handle image upload
    if option == "Upload Image":
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            # Display uploaded image
            st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
            st.write("")

            # Preprocess the image and make predictions using the model
            image_data = preprocess_image(uploaded_file)
            if model and labels:
                predicted_label = classify_image(model, labels, image_data)
                st.write(f"Predicted label: **{predicted_label}**", unsafe_allow_html=True)

                # Display recycling suggestions
                suggestions = get_suggestions(predicted_label)
                st.subheader("Recycling Suggestions:")
                for suggestion in suggestions:
                    st.markdown(f'<div class="suggestion">{suggestion}</div>', unsafe_allow_html=True)
            else:
                st.error("Model or labels not available. Please check if they were loaded correctly.")

    # Handle webcam capture
    if option == "Use Webcam":
        st.write("### Use your webcam to classify waste")
        camera_input = st.camera_input("Take a picture")
        
        if camera_input is not None:
            # Display the captured image
            st.image(camera_input, caption='Captured Image', use_column_width=True)
            st.write("")

            # Preprocess the image and make predictions using the model
            image_data = preprocess_image(camera_input)
            if model and labels:
                predicted_label = classify_image(model, labels, image_data)
                st.write(f"Predicted label: **{predicted_label}**", unsafe_allow_html=True)

                # Display recycling suggestions
                suggestions = get_suggestions(predicted_label)
                st.subheader("Recycling Suggestions:")
                for suggestion in suggestions:
                    st.markdown(f'<div class="suggestion">{suggestion}</div>', unsafe_allow_html=True)
            else:
                st.error("Model or labels not available. Please check if they were loaded correctly.")

# Main application
if __name__ == "__main__":
    show_classification_page()
