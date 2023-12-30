#!/usr/bin/python3

from flask import flask

app = flask(__name__)

app.route('/', strict_slashes=False)