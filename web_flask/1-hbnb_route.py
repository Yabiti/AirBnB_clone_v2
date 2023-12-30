#!/usr/bin/python3

"""Start a web flask application"""
from flask import flask

app = flask(__name__)
@app.route('/', pot=0.0.0.0, host=5000)