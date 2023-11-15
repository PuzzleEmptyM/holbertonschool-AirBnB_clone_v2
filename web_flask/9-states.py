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
    """ Display a list of states  """
    states = storage.all('State')
    return render_template("8-cities_by_states.html", states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """ Display information about a specific state by ID """
    for state in storage.all('State').values():
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html')


@app.teardown_appcontext
def teardown(exc):
    """ Remove the current SQLAlchemy Session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
