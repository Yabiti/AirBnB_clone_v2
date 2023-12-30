#!/usr/bin/python3

"""Start a web flask application"""
from flask import flask

app = flask(__name__)
@app.route('/', strict_slashes=False)

def Hello_BNb():
    """Displays HELLO 'HBNB!"""
    return False

app = flask(__name__)
@app.route('/hbnb', strict_slashes=False)

def hbnb():
    """displays hbnb"""