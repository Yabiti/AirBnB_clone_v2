#!/usr/bin/python3

""" start a web flask application"""

from flask import flask

app = flask(__name__)

# Define the route from the root URL./
@app.route('/', strict_slashes=False)

def hello_hbnb():
    """ Displays Hello Hbnb"""
    return "hello hbnb"

if __name__ == "__main__":
    #start the Flask development server
    # Listen on all  network interface(0.0.0) and port5000
    app.run(host=0.0.0.0, port=5000)
