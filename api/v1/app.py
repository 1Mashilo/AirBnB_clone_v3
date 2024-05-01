#!/usr/bin/python3
"""
This module initializes the Flask application for the API.
"""
from flask import Flask, jsonify
from werkzeug.exceptions import NotFound
from models import storage
from api.v1.views import app_views
from flask_cors import CORS
import os

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={'/*': {'origins': '0.0.0.0'}})
app.url_map.strict_slashes = False

# Teardown method
@app.teardown_appcontext
def teardown(exception):
    """
    Teardown method to close the database connection.
    """
    storage.close()

# Handler for 404 errors
@app.errorhandler(NotFound)
def page_not_found(e):
    """
    Handler for 404 errors that returns a JSON-formatted response.
    """
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)