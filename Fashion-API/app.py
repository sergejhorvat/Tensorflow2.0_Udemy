# Stage 1: Import project dependencies
import os
import requests
import numpy as np
import tensorflow as tf

from scipy.misc import imsave, imread

from flask import Flask, request, jsonify


# Stage 2: Load pretrained model
# Load model structure
with open("fashion_model_flask.json","r") as f:
    model_json = f.read()
    print(model_json)

model = tf.keras.models.model_from_json(model_json)

# Load model weights
model.load_weights("fashion_model_flask.h5")

# Stage 3: Create the Flask API
app = Flask(__name__)

@app.route("/api/v1/<string:img_name>" , methods=["POST"])
def classify_image(img_name):
    upload_dir = "uploads/"

    image = imread((upload_dir + img_name))
    #print("Image type: " + str(type(image)))

    # Define the list of class names
    classes = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

    # Reshape image to vector
    prediction = model.predict(image.reshape(1, 28 * 28))

    # Return classification to user with json that does marshaling
    return jsonify({"object_detected": classes[np.argmax(prediction[0])]})

# Start the Flask API and make prediction
app.run(port=5000, debug=False)

# Create client call in some Web api  framework like postman,
# Send the POST request to test API
# http://127.0.0.1:5000/api/v1/0.png