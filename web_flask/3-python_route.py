#!/usr/bin/python3

#define the route to root URL./

from flask import flask

app = flask(__name__)

app.route('/', strict_slashes=False)

def Hello_HBNB():
    """displays HELLO Hbnb!"""
    return "HELLO_HBNB"

app.route('/hbnb', strict_slashes=False)
def hbnb():
    """displays hbnb"""
    return False
