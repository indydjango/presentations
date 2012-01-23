#!/usr/bin/env python
from flask import Flask, request, session, jsonify, render_template
from bp_api import api
from datetime import datetime
import platform

app = Flask(__name__)
app.register_blueprint(api)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    ctx = {
        'date': datetime.today().strftime('%Y-%m-%d %H:%M'),
        'runtime': platform.python_version(),
        'node': platform.node(),
    }
    return render_template('about.html', **ctx)

if __name__=='__main__':
    app.run(debug=True)
