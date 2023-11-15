#!/usr/bin/python3
"""
This is a Flask web application.
"""

from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """ Display an HTML page listing states existing in storage """
    states = storage.all('State')
    return render_template("8-cities_by_states.html", states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """ Displays an HTML page with states that match the ID
    also displays the cities tied to that state. """
    for state in storage.all('State').values():
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html')


@app.teardown_appcontext
def teardown(exc):
    """ Ends the existing SQLAlchemy session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
