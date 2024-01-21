import numpy as np
import cv2
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC  # Consider other classifiers if needed

#Load and Preprocess Images:
def load_and_preprocess_images(image_paths):
    images = []
    for image_path in image_paths:
        # Load image in grayscale
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        # Resize images to a consistent size (if needed)
        img = cv2.resize(img, (32, 32))  # Reshape for consistency
        # Flatten image into a feature vector
        features = img.flatten()
        images.append(features)
    return np.array(images)
  
#Load Data and Create Labels:
# Assuming you have image paths in two lists: plain_images and crossed_images
plain_features = load_and_preprocess_images(plain_images)
crossed_features = load_and_preprocess_images(crossed_images)
labels = np.array([0] * len(plain_images) + [1] * len(crossed_images))  # 0 for plain, 1 for crossed

#Split Data into Training and Testing Sets:
X_train, X_test, y_train, y_test = train_test_split(
    np.concatenate((plain_features, crossed_features)), labels, test_size=0.25
)

#Train a Machine Learning Model:
model = SVC()  # You can experiment with different classifiers
model.fit(X_train, y_train)

#Test the Model on New Images:
def predict_image(image_path):
    features = load_and_preprocess_images([image_path])[0]  # Preprocess single image
    prediction = model.predict(features)
    return "Plain" if prediction == 0 else "Crossed"

#Use the Model for Prediction:
new_image_path = "path/to/new/image.jpg"
prediction = predict_image(new_image_path)
print(prediction)  # Print "Plain" or "Crossed"

#To save the model:
from sklearn.externals import joblib
# After training your model (assuming it's named 'model')
model_file = "path/to/save/model.h5"  # Specify file path
joblib.dump(model, model_file)  # Save the model to the HDF5 file

#To Load the model:
from sklearn.externals import joblib
# When you need to use the model later
loaded_model = joblib.load(model_file)  # Load the model from the HDF5 file
# Use the loaded model for predictions
prediction = loaded_model.predict(new_data)  # Example usage
