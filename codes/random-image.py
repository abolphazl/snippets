from flask import Flask, jsonify, make_response
import random

app = Flask(__name__)

# List of image URLs
images = [
    "https://image1.jpg",
    "https://image2.jpg",
    "https://image3.jpg",
    "https://image4.jpg",
    "https://image5.jpg",
    "https://image6.jpg"
]

@app.route('/random-image', methods=['GET'])
def random_image():
    # Select a random image from the list
    image = random.choice(images)
    
    # Return the image URL as a JSON response
    return jsonify({'image_url': image})

if __name__ == '__main__':
    app.run(debug=True)
