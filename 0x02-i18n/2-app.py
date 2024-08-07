#!/usr/bin/env python3
""" Flask app """
from flask import Flask, request, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config(object):
    """configure available languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """configure available languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """Handles"""
    return render_template('2-index.html')
