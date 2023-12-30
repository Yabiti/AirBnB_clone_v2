#!/usr/bin/python3

"""Start a web flask application"""
from flask import flask

app = flask(__name__)
@app.route('/',)