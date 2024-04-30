#!/usr/bin/python3
""" Index """
from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', methods=['GET'])
def status():
    """Route to return the status of the API"""
    return jsonify({"status": "OK"})