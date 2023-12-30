#!/usr/bin/python3

from flask import flask

app = flask(__name__)

#Dispalys the route to root URL/
app.route('/', strict_slashes=False)

def Hello_HBNB():