#!/usr/bin/python3
"""
This is a simple Flask web application.
"""

from flask import Flask, escape, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    """ Replace underscores with spaces and display
    "C " followed by the value of the text variable """
    return 'C {}'.format(escape(text).replace('_', ' '))


@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text='is_cool'):
    """ Display "Python " followed by the value of the text variable
    with the default value of 'is_cool' """
    return 'Python {}'.format(escape(text).replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """ Display 'n is a number' only if n is an integer """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    """ Display the number directly, only if n is an integer """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_number_odd_or_even(n):
    """ Display an HTML page with H1 tag: 'Number: n is even|odd' only
    if n is an integer """
    return render_template('number_odd_or_even_template.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
