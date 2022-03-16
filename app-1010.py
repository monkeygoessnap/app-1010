import flask
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'TestTest'


@app.route('/home')
def home():
    return "YourHome"

if __name__ == "__main__":
    app.run()
