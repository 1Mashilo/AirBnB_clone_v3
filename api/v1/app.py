from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)

# Register the blueprint
app.register_blueprint(app_views)

# Define a method to handle teardown_appcontext
@app.teardown_appcontext
def close_storage(error):
    """Close the current SQLAlchemy session."""
    storage.close()

if __name__ == "__main__":
    # Run the Flask server
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)