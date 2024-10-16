from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import streamlit as st 

# Define the model loading function
@st.cache_resource  # Cache the model to avoid reloading it each time
def load_keras_model():
    # Load the Keras model from the provided h5 file
    return load_model("keras_model.h5", compile=False)

# Waste classification function using Teachable Machine model
def classify_waste(img):
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = load_keras_model()

    # Load the updated labels
    class_names = open("labels.txt", "r").readlines()

    # Create the array of the right shape to feed into the Keras model
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    
    # Convert the image to RGB (in case it's in another mode)
    image = img.convert("RGB")

    # Resize the image to 224x224 pixels
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # Convert the image to a numpy array and normalize it
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the data array
    data[0] = normalized_image_array

    # Perform prediction using the loaded model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index].strip()  # Clean the label from extra spaces or newline characters
    confidence_score = prediction[0][index]

    return class_name, confidence_score

# Streamlit configuration
st.set_page_config(layout='wide')

st.title("Waste Classifier Sustainability App")

# Upload an image file for classification
input_img = st.file_uploader("Enter your image", type=['jpg', 'png', 'jpeg'])

if input_img is not None:
    if st.button("Classify"):
        
        col1, col2 = st.columns([1, 1])

        with col1:
            st.info("Your uploaded Image")
            st.image(input_img, use_column_width=True)

        with col2:
            st.info("Your Result")
            image_file = Image.open(input_img)
            label, confidence_score = classify_waste(image_file)
            
            # Classification results
            if "cardboard" in label.lower():
                st.success("The image is classified as CARDBOARD.")                 
            elif "metal" in label.lower():
                st.success("The image is classified as METAL.")
            elif "plastic" in label.lower():
                st.success("The image is classified as PLASTIC.")
            elif "glass" in label.lower():
                st.success("The image is classified as GLASS.")
            elif "paper" in label.lower():
                st.success("The image is classified as PAPER.")
            elif "compost" in label.lower():
                st.success("The image is classified as COMPOST.")
            else:
                st.error("The image is not classified as any relevant class.")
