#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Hello world to Dona3</h1>'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)


