#!/usr/bin/python3

from flask import flask

app = flask(__name__)

#Define the route to root URL/
app.route('/', strict_slashes=False)

def Hello_HBNB():
    """Displays Hello HBNB!”"""
    return "HBNB"

#Define the route to root URL/
app.route('/hbnb', strict_slashes=False)

def hbnb():
    """didpalys hbnb"""
    return 

#Define the route for /c/<text>
app.route('/c/<text', strict_slashes=False)

def c_with_tex(text):
    formatted_text = text.replace()