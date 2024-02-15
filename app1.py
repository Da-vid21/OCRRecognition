from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import requests
import json

app = Flask(__name__)

# Set the Azure server endpoint
endpoint = 'http://127.0.0.1:5000'

# Set the allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return 'No file selected'
    file = request.files['file']
    if file.filename == '':
        return 'No file selected'
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(filename)
        # Pass the image to the Azure server for OCR conversion
        with open(filename, 'rb') as f:
            image_data = f.read()
        headers = {'Content-Type': 'application/octet-stream'}
        response = requests.post(endpoint, data=image_data, headers=headers, timeout=60)
        text = response.json()['text']
        return text
    else:
        return 'Invalid file extension'

if __name__ == '__main__':
    app.run(debug=True)
