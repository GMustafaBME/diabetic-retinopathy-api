from flask import Flask, request, jsonify
import numpy as np
from PIL import Image
import io
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import Layer
from tensorflow.keras import backend as K
from pyngrok import ngrok  # Import Ngrok to start it manually
import os

# ✅ Step 1: Define Custom Functions & Layers (If Used in Model)
def f1(y_true, y_pred):
    precision = tf.keras.metrics.Precision()(y_true, y_pred)
    recall = tf.keras.metrics.Recall()(y_true, y_pred)
    return 2 * ((precision * recall) / (precision + K.epsilon()))

class CastLayer(Layer):
    def __init__(self, target_dtype='float32', **kwargs):
        super(CastLayer, self).__init__(**kwargs)
        self.target_dtype = target_dtype

    def call(self, inputs):
        return tf.cast(inputs, self.target_dtype)

# ✅ Step 2: Load Model with Custom Objects
custom_objects = {"f1": f1, "Cast": CastLayer}
model_path = "/content/model/DenseNet_DR.h5"

if os.path.exists(model_path):
    model = load_model(model_path, custom_objects=custom_objects)
    print("✅ Model loaded successfully!")
else:
    print("❌ ERROR: Model file not found. Please check the path.")

# ✅ Step 3: Initialize Flask App
app = Flask(__name__)

# ✅ Step 4: Manually Start Ngrok & Get Public URL
from pyngrok import ngrok

# ✅ Step 4: Authenticate Ngrok and Start Tunnel
ngrok.set_auth_token("WRITE IT HERE")  # Replace with your token
public_url = ngrok.connect(5000).public_url
print(f"🌍 Flask App is Running on: {public_url}")


# ✅ Step 5: Preprocessing Function for Images
def preprocess_image(image):
    image = image.convert("RGB")  # Ensure it has 3 channels
    image = image.resize((256, 256))  # Resize to match model input
    image = np.array(image) / 255.0  # Normalize pixel values
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image.astype(np.float32)  # Ensure correct data type

# ✅ Step 6: Define API Routes
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Diabetic Retinopathy Detection API!"})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        file = request.files['file']
        image = Image.open(io.BytesIO(file.read()))
        processed_image = preprocess_image(image)

        # Make Prediction
        prediction = model.predict(processed_image)
        prediction_score = float(prediction[0][0])
        result = {
            "prediction": "Diabetic Retinopathy Detected" if prediction_score > 0.5 else "No Diabetic Retinopathy",
            "confidence_score": prediction_score
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)})

# ✅ Step 7: Run Flask App
if __name__ == '__main__':
    app.run()
