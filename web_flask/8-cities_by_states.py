#!/usr/bin/python3
"""
This is a Flask web application.
"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ Display a list of states and cities from the storage """
    states = storage.all(State).values()

    for state in states:
        if storage.__class__.__name__ == "DBStorage":
            state.cities = state.cities()

    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exception):
    """ Remove the current SQLAlchemy Session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
