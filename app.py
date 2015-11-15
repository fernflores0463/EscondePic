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
import encrypt
import os
#from forms import HideForm, RevealForm

'''''''''''''''''''''''''''''''''''''''''
'''''''''''''''' Setup ''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''

UPLOAD_FOLDER = '/home/dor/CompSci/webdev/deletemebruh'
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
        print message
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return render_template('index.html')

@app.route('/uploads/<filename>/')
def uploaded_file(filename):
    #add encryption
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)



@app.route('/result')
def result():
    return render_template('result.html', text="Hello HackRPI")

@app.route('/reveal')
def revealMessage():
    return render_template('reveal.html', text="Hello HackRPI")

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
