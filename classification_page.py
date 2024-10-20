import streamlit as st
import os
import numpy as np
from PIL import Image
from keras.models import load_model
from keras.layers import DepthwiseConv2D
from keras.preprocessing import image
from keras.applications.mobilenet_v2 import preprocess_input

# Custom DepthwiseConv2D class to handle loading without 'groups' argument
class CustomDepthwiseConv2D(DepthwiseConv2D):
    def __init__(self, *args, **kwargs):
        kwargs.pop('groups', None)
        super().__init__(*args, **kwargs)

# Function to load the model
def load_model_func():
    model_path = 'waste_classification.h5'
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

# Function to preprocess the uploaded image
def preprocess_image(uploaded_file):
    img = image.load_img(uploaded_file, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
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
            "Recycle plastic containers by rinsing and placing them in recycling bins.",
            "Consider using reusable bags instead of plastic ones.",
            "Upcycle plastic bottles into planters or storage containers."
        ],
        "Metal": [
            "Clean and recycle metal cans in your local recycling program.",
            "Use metal containers for storage instead of plastic.",
            "Donate old metal items instead of throwing them away."
        ],
        "Paper": [
            "Recycle paper products like newspapers and cardboard.",
            "Use both sides of paper before discarding.",
            "Shred sensitive documents and recycle the scraps."
        ],
        "Glass": [
            "Rinse glass jars and bottles before recycling them.",
            "Consider using glass containers for food storage.",
            "Repurpose glass jars as vases or decorative items."
        ],
        "Compost": [
            "Compost kitchen scraps to create nutrient-rich soil.",
            "Use compost bins or piles to reduce waste.",
            "Educate others about the benefits of composting."
        ],
        "Cardboard": [
            "Flatten cardboard boxes before recycling.",
            "Reuse cardboard for crafts or storage.",
            "Consider donating cardboard boxes to local schools or charities."
        ]
    }
    return suggestions.get(predicted_label, ["No specific suggestions available."])

# Show classification page
def show_classification_page():
    # Load the model and labels
    try:
        model = load_model_func()
        labels = load_labels()
    except Exception as e:
        st.error(f"Error loading model or labels: {e}")
        return

    # Set up the enhanced page style
    st.markdown(
        """
        <style>
        body {
            background-color: #F7FFF7; /* Light green for a refreshing look */
            font-family: 'Helvetica', sans-serif;
        }
        .title {
            text-align: center;
            font-size: 3.5em;
            color: #00A86B; /* Green shade for eco-friendliness */
            font-weight: 700;
            padding: 20px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        }
        .upload-section {
            background: #ffffff;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
            margin: 20px 0;
        }
        .classify-button {
            background-color: #228B22; /* Green color */
            color: #ffffff;
            padding: 12px 28px;
            font-size: 1.2em;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .classify-button:hover {
            background-color: #32CD32; /* Bright green */
        }
        .suggestion {
            margin-top: 15px;
            padding: 15px;
            background-color: #e7f9e7;
            border-radius: 8px;
            font-size: 1.1em;
            color: #006400;
            box-shadow: 0 4px 6px rgba(0, 128, 0, 0.15);
        }
        .footer-links a {
            color: #228B22;
            font-size: 1.1em;
            text-decoration: none;
            margin: 0 10px;
        }
        .footer-links a:hover {
            text-decoration: underline;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display enhanced title
    st.markdown('<div class="title">EcoSort 🌱</div>', unsafe_allow_html=True)
    st.write("### Capture or upload an image to classify waste type")

    # Webcam option
    option = st.radio("Choose an option:", ("Upload Image", "Use Webcam"))

    if option == "Use Webcam":
        st.markdown("<div class='camera-section'>", unsafe_allow_html=True)
        st.write("### Capture an Image Using Your Webcam")
        camera_input = st.camera_input("Take a picture")
        if camera_input is not None:
            img = Image.open(camera_input)
            st.image(img, caption='Captured Image', use_column_width=True)
            image_data = preprocess_image(camera_input)
            if model and labels:
                predicted_label = classify_image(model, labels, image_data)
                st.write(f"### Result: **{predicted_label}**")
                suggestions = get_suggestions(predicted_label)
                st.subheader("Recycling Suggestions:")
                for suggestion in suggestions:
                    st.markdown(f'<div class="suggestion">{suggestion}</div>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    else:  # Image upload option
        uploaded_file = st.file_uploader("Choose an image file...", type=["jpg", "jpeg", "png"])

        # Handle image upload and classification
        if uploaded_file is not None:
            st.markdown('<div class="upload-section">', unsafe_allow_html=True)
            img = Image.open(uploaded_file)
            st.image(img, caption="Uploaded Image", use_column_width=True)
            st.write("### Result:")

            # Add a classify button with interactivity
            if st.button("Classify Waste", key="classifyButton", help="Click to classify the waste image"):
                with st.spinner('Classifying... Please wait.'):
                    try:
                        image_data = preprocess_image(uploaded_file)
                        predicted_label = classify_image(model, labels, image_data)
                        st.success(f"Predicted label: **{predicted_label}** 🎉")
                        
                        # Show recycling suggestions
                        suggestions = get_suggestions(predicted_label)
                        st.subheader("Recycling Suggestions:")
                        for suggestion in suggestions:
                            st.markdown(f'<div class="suggestion">{suggestion}</div>', unsafe_allow_html=True)
                    except Exception as e:
                        st.error(f"Error during classification: {e}")
            st.markdown('</div>', unsafe_allow_html=True)


# Main application
if __name__ == "__main__":
    show_classification_page()
