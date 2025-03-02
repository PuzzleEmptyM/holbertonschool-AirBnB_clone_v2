#!/usr/bin/python3
"""
This is a Flask web application.
"""

from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """ Display a list of states and cities from the storage """
    states = storage.all('State')
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """ Remove the current SQLAlchemy Session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
