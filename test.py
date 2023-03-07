from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
from src import OCRConversion
app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "pics/"

@app.route('/')
def upload_file():
    return render_template('index.html')
@app.route('/upload', methods=['GET', 'POST'])
def handle_upload():
    # handle the file upload and processing here
    file = request.files['file']
    filename = secure_filename(file.filename)

    file.save(app.config['UPLOAD_FOLDER'] + filename)
    # do something with the file
    content = OCRConversion.actualConversion(app.config['UPLOAD_FOLDER'] + filename)
        
    
    return jsonify({"result": content})
  # change to your own logic
if __name__ == '__main__':
    app.run(port=5000, debug = True)