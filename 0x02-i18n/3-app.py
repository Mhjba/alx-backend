#!/usr/bin/env python3
"""
Get locale from request
"""
from flask import Flask, request, render_template
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

class Config(object):
    """configure available languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

@babel.localeselector
def get_locale():
    """determine best match"""
    loc = request.args.get('locale')
    if loc in app.config['LANGUAGES']:
        return loc
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/', strict_slashes=False)
def index():
    """return a simple template"""
    return render_template('3-index.html')

if __name__ == '__main__':
    app.run(debug=True)

