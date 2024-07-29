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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
