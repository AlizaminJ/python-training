from flask import Flask, jsonify, render_template, request
import webbrowser
import time
import random

app = Flask(__name__)


@app.route('/random', methods=['GET'])
def random_stuff():
    result = random.randint(0, 10)
    return jsonify('random_number: {}'.format(result))


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
