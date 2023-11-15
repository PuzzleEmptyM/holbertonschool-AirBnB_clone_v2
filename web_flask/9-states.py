#!/usr/bin/python3
"""
This is a Flask web application.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """ Display a list of states """
    states = storage.all(State).values()
    return render_template("9-states.html", states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    """ Display information about a specific state by ID """
    state = storage.get(State, id)
    if state:
        return render_template("9-states_by_id.html", state=state)
    else:
        return render_template("9-states_not_found.html")


@app.teardown_appcontext
def teardown(exception):
    """ Remove the current SQLAlchemy Session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
