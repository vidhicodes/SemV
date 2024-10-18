from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image

def preprocess(image):
    """
    Preprocess the input image for model prediction.
    - Convert RGBA to RGB if needed.
    - Resize to the expected input size of the model.
    - Convert the image to a numpy array.
    - Normalize pixel values (if required).
    """
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    target_size = (224, 224)  # Match the size of the Teachable Machine model
    image = image.resize(target_size)
    
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = image / 255.0  # Normalize the pixel values
    
    return image

def model_arc():
    """
    Load the pre-trained Teachable Machine model from 'keras.h5'.
    """
    model = load_model('keras.h5')  # Replace this with the path to your downloaded model
    return model

def gen_labels():
    """
    Generate labels for the classes. Update these to match the classes from Teachable Machine.
    """
    return ["Cardboard", "Glass", "Metal", "Paper", "Plastic", "Compost"]  # Adjust if needed
