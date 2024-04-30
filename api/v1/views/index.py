#!/usr/bin/python3
""" Index """

from models import storage
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def status():
    """Route to return the status of the API"""
    return jsonify({"status": "OK"})


@app_views.route('/api/v1/stats', methods=['GET'])
def number_objects():
    """ Retrieves the number of each objects by type """
    classes = [Amenity, City, Place, Review, State, User]
    names = ["amenities", "cities", "places", "reviews", "states", "users"]

    num_objects = {}
    for i, cls in enumerate(classes):
        count = storage.count(cls)
        num_objects[names[i]] = count

    return jsonify(num_objects)