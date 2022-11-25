import json
from flask import Flask, render_template
from flask import request, redirect, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registrace')
def registrace():
    return render_template('registrace.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=8080, debug=False)