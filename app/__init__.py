from flask import Flask
from pymongo import MongoClient
import os

def create_app():
    app = Flask(__name__)

    # MongoDB Configuration
    app.config["MONGO_URI"] = os.environ.get("CONN_STR")
    
    # Initializes the connection to MongoDB
    client = MongoClient(app.config["MONGO_URI"])
    app.db = client.mydatabase
    
    # Other initializations
    with app.app_context():
        from .views import views
        app.register_blueprint(views)

    return app
