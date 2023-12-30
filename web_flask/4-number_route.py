#!/usr/bin/python3

from flask import flask

app = flask(__name__)

app.route('/', strict_slashes=False)

def HELLO_HBNB():
    """displays HELLO_HBNB"""
    return "HELLO_HBNB"

app.route('/hbnb', strict_slashes=False)

def hbnb():
    """displays hbnb"""
    return "hbnb"

app.route('/c/<text', strict_slashes=False)
def c_with_text(text):
    formatted_text = text.replace('_',' ')
    return "c ()". format.formatted_text()

app.route('/python', defaults={'text: is cool'}, strict_slashes=False)
app.route('/python<text>', strict_slashes=False)