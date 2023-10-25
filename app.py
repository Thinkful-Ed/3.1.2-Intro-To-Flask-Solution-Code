# app.py
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/error')
def trigger_error():
    raise ValueError("This is a deliberate error.")


if __name__ == '__main__':
    app.run(port=5001, debug=True)
