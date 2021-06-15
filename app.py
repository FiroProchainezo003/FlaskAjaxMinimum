from flask import Flask, request, render_template, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_datetime', methods=['POST'])
def get_datetime():
    return jsonify({'date': datetime.now()})


if __name__ == '__main__':
    app.run()
