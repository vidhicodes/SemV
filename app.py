from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import streamlit as st 
from dotenv import load_dotenv 
import os
import openai

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API Key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Define the model loading function
@st.cache_resource  # Cache the model to avoid reloading it each time
def load_keras_model():
    # Load the Keras model from the provided h5 file
    return load_model("keras_model.h5", compile=False)

# Waste classification function
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

# Generate carbon footprint information using OpenAI API
def generate_carbon_footprint_info(label):
    waste_type = label.strip()
    prompt = f"What is the approximate carbon footprint generated from {waste_type}? I need an approximate number for environmental awareness, focusing on typical waste disposal practices. Elaborate in about 100 words."
    
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=600,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response['choices'][0]['text']

# Streamlit configuration
st.set_page_config(layout='wide')

st.title("Waste Classifier Sustainability App")

# Upload an image file for classification
input_img = st.file_uploader("Enter your image", type=['jpg', 'png', 'jpeg'])

if input_img is not None:
    if st.button("Classify"):
        
        col1, col2, col3 = st.columns([1, 1, 1])

        with col1:
            st.info("Your uploaded Image")
            st.image(input_img, use_column_width=True)

        with col2:
            st.info("Your Result")
            image_file = Image.open(input_img)
            label, confidence_score = classify_waste(image_file)
            
            col4, col5 = st.columns([1, 1])
            
            # Classification results and display corresponding SDG images
            if label == "0 cardboard":
                st.success("The image is classified as CARDBOARD.")                
                with col4:
                    st.image("sdg goals/12.png", use_column_width=True)
                    st.image("sdg goals/13.png", use_column_width=True)
                with col5:
                    st.image("sdg goals/14.png", use_column_width=True)
                    st.image("sdg goals/15.png", use_column_width=True) 
            elif label == "1 metal":
                st.success("The image is classified as METAL.")
                with col4:
                    st.image("sdg goals/3.png", use_column_width=True)
                    st.image("sdg goals/6.jpg", use_column_width=True)
                with col5:
                    st.image("sdg goals/12.png", use_column_width=True)
                    st.image("sdg goals/14.png", use_column_width=True) 
            elif label == "2 plastic":
                st.success("The image is classified as PLASTIC.")
                with col4:
                    st.image("sdg goals/6.jpg", use_column_width=True)
                    st.image("sdg goals/12.png", use_column_width=True)
                with col5:
                    st.image("sdg goals/14.png", use_column_width=True)
                    st.image("sdg goals/15.png", use_column_width=True) 
            elif label == "3 glass":
                st.success("The image is classified as GLASS.")
                with col4:
                    st.image("sdg goals/12.png", use_column_width=True)
                with col5:
                    st.image("sdg goals/14.png", use_column_width=True)
            elif label == "4 paper":
                st.success("The image is classified as PAPER.")
                with col4:
                    st.image("sdg goals/12.png", use_column_width=True)
                with col5:
                    st.image("sdg goals/14.png", use_column_width=True)
            elif label == "5 compost":
                st.success("The image is classified as COMPOST.")
                with col4:
                    st.image("sdg goals/13.png", use_column_width=True)
                    st.image("sdg goals/15.png", use_column_width=True)
            else:
                st.error("The image is not classified as any relevant class.")

        with col3:
            result = generate_carbon_footprint_info(label)
            st.success(result)
