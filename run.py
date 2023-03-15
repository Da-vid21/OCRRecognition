import os

from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from src import OCRConversion
app = Flask(__name__)


app.config["UPLOAD_FOLDER"] = "pics/"

@app.route('/')
def upload_file():
    return render_template('index.html')


@app.route('/display', methods = ['GET', 'POST'])
def display_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)

        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        
        content = OCRConversion.actualConversion(app.config['UPLOAD_FOLDER'] + filename)
        
        if(len(content) == 0):
          content = "<Response 440 bytes [200 OK]>"
          
    
    content = content.replace("\n", "<br>")
    os.remove(app.config['UPLOAD_FOLDER'] + filename)
    return jsonify({"result": content})
    return render_template('content.html', content=content) 

@app.route('/noLines', methods = ['GET', 'POST'])
def noLines():
  return render_template("index.html")
if __name__ == '__main__':
    app.run(port=5000, debug = True, host="127.0.0.1")