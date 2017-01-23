"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

import os

import flask

app = flask.Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'mysecretkey')


@app.route('/')
def home():
  """Render website's home page."""
  return 'hello world'


if __name__ == '__main__':
    app.run(debug=True)
