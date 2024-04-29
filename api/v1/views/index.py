from flask import jsonify
import app_views from api.v1.views

@app_views.route('/status')
def get_status():
    """Returns a JSON response indicating the API status as 'OK'."""
    data = {'status': 'OK'}
    return jsonify(data)
