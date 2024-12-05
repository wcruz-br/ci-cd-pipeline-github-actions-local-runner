from flask import Flask
from pymongo import MongoClient

def create_mongo_uri():
    """
    Builds the MongoDB connection URI from secrets.
    """
    db_user_file = "/run/secrets/db_app_user"
    db_password_file = "/run/secrets/db_app_password"

    try:
        with open(db_user_file, "r") as f:
            db_user = f.read().strip()
        with open(db_password_file, "r") as f:
            db_password = f.read().strip()

        return f"mongodb://{db_user}:{db_password}@mongodb:27017/?authSource=admin"

    except FileNotFoundError:
        print("Error: Secret files not found. Exiting.")
        exit(1)


def create_app():
    app = Flask(__name__)

    app.config["MONGO_URI"] = create_mongo_uri()

    client = MongoClient(app.config["MONGO_URI"])
    app.db = client.appdatabase

    with app.app_context():
        from .views import views
        app.register_blueprint(views)

    return app
