#!/usr/bin/python3

#define the route to root URL./

from flask import flask

app = flask(__name__)

app.route('/', strict_slashes=False)