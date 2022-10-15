#!/usr/bin/python3
""" Starts a Flask web application 

The application listens on 0.0.0.0, port 5000.
Routes:
    /states_list: HTML page with a list of all State objects in DBStorage.
"""


from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """List all the states in the database"""
    states = storage.all('State')
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """close current sqlalchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
