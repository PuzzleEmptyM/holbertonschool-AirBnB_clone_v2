#!/usr/bin/python3
"""
This is a Flask web application.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ Display a list of states and cities from the storage """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)

    for state in sorted_states:
        if storage.__class__.__name__ == "DBStorage":
            state.cities = state.cities()

    return render_template('7-cities_by_states.html', states=sorted_states)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """ Remove the current SQLAlchemy Session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
