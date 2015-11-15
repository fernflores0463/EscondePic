#!/usr/bin/env python

__authors__ = [
    "Dor Rondel",
    "Jane Chen",
    "Renzhentaxi Baerde",
    "James Spann"
]

from flask import (Flask, redirect, g, url_for, render_template,
                    send_from_directory, request)
from werkzeug import secure_filename
from encrypt import *
import os
#from forms import HideForm, RevealForm

'''''''''''''''''''''''''''''''''''''''''
'''''''''''''''' Setup ''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''

UPLOAD_FOLDER = '/home/dor/CompSci/github/EscondePic/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


'''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''APP ''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        message = request.form['user-message']
        password = request.form['user-password']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            if message and password:
                encrypt(file.filename, message, password, outputName=file.filename)
            elif message is None or message == "":
                decrypt(file, password)
                print decrypt(file.filename, password)
            else: pass
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return render_template('index.html')

@app.route('/uploads/<filename>/')
def uploaded_file(filename):
    return render_template("result.html", userimage="/shabat_shalom.png")

@app.route('/reveal/')
def reveal():
    return render_template("reveal.html")

########################################
############ Error Handling ############
########################################

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

@app.errorhandler(500)
def internal_error(e):
    return render_template("500.html")

if __name__ == '__main__':
    app.run(debug=True)
