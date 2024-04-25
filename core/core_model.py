import cv2
import numpy as np
from keras.models import load_model

def predict_skin_disease(image_path):

    def preprocess_image(image_path):
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (100, 100))  # Resize the image to match the input shape of the model
        img = img.reshape(-1, 100, 100, 1)  # Reshape for model input (add batch dimension and channel dimension)
        img = img.astype('float32') / 255.0  # Normalize pixel values between 0 and 1
        return img

    uploaded_image_path = image_path


    model = load_model('core/skin_disease_model_updated.h5')

    preprocessed_image = preprocess_image(uploaded_image_path)

    predictions = model.predict(preprocessed_image)

    predicted_class_index = np.argmax(predictions)

    class_labels = [
        " Eczema", " Melanoma", " Atopic Dermatitis",
        " Basal Cell Carcinoma (BCC)", "Melanocytic Nevi (NV)",
        " Benign Keratosis-like Lesions (BKL)",
        " Psoriasis pictures Lichen Planus and related diseases",
        " Seborrheic Keratoses and other Benign Tumors",
        " Tinea Ringworm Candidiasis and other Fungal Infections",
        " Warts Molluscum and other Viral Infections"
    ]

    predicted_class_label = class_labels[predicted_class_index]

    print("Predicted Class:", predicted_class_label)
    
    return predicted_class_label

