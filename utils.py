import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image

# Preprocess the uploaded or webcam image for the Keras model
def preprocess(image, target_size=(224, 224)):
    """
    Preprocess the input image for model prediction.
    - Convert RGBA to RGB if needed.
    - Resize to the expected input size of the model.
    - Convert the image to a numpy array.
    - Normalize pixel values.
    
    Args:
        image (PIL Image): Input image to preprocess.
        target_size (tuple): The size expected by the model.
        
    Returns:
        numpy array: Preprocessed image ready for model prediction.
    """
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    image = image.resize(target_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = image / 255.0  # Normalize the pixel values
    
    return image

# Load the pre-trained Keras model
def load_model_func(model_path='keras.h5'):
    """
    Load the pre-trained Keras model from the provided path.
    
    Args:
        model_path (str): Path to the .h5 Keras model file.
        
    Returns:
        model: Loaded Keras model.
    """
    model = load_model(model_path)  # Load the model
    return model

# Generate class labels for the waste types
def load_labels():
    """
    Generate labels for the classes. Update these to match the classes from your model.
    
    Returns:
        list: Class labels.
    """
    return ["Cardboard", "Glass", "Metal", "Paper", "Plastic", "Compost"]  # Update if needed
