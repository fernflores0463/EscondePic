#!/usr/bin/env python

__authors__ = [
    "Dor Rondel",
    "James Spann",
    "Jane Chen",
    "Renzhentaxi Baerde"
]

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', text="Hello HackRPI")

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
