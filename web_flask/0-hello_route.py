#!/usr/bin/python3

""" start a web flask application"""

from flask import flask

app = flask(__name__)

# Define the route from the root URL./
@app.route('/', strict_slashes=False)

def hello_hbnb():
