#!/usr/bin/python3
'''this script will start a flask web apllication'''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    '''this function handles the home route'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''this function handles the hbnb route'''
    return 'HBNB'


@app.route('/c/<string:text>', strict_slashes=False)
def ctext(text):
    '''this function handles the ctect route'''
    return f"C {text.replace('_', ' ')}"


@app.route('/python', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def pthon_text(text):
    '''this function handles the python route'''
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    '''this function handles the number route'''
    return f'{n} is a number'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
