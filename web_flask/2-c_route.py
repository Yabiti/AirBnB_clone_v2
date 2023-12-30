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

