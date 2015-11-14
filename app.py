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

if __name__ == '__main__':
    app.run(debug=True)
