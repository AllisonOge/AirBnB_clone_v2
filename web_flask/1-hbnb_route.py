#!/usr/bin/python3
"""
a script that starts a Flask web application that displays
“HBNB” if the URL is /hbnb
"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello_world():
    """prints Hello HBNB!"""
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    """prints HBNB"""
    return 'HBNB'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
