#!/usr/bin/env python
from flask import Blueprint, jsonify
import platform

api = Blueprint('api', __name__)

@api.route("/api/version")
def version():
    return jsonify({'version': '0.1'})

@api.route("/api/info")
def info():
    data = {
        'node': platform.node(),
        'runtime': platform.python_implementation(),
        'runtime_version': platform.python_version(),
    }
    return jsonify(data)
