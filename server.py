from flask import Flask, request, jsonify
import io
import pytesseract
from PIL import Image

app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def ocr():
    image_data = request.data
    image = Image.open(io.BytesIO(image_data))
    text = pytesseract.image_to_string(image)
    return jsonify({'text': text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)