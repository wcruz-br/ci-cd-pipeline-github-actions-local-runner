from flask import Flask
from pymongo import MongoClient
import os

def create_app():
    app = Flask(__name__)

    # Configurações do MongoDB
    app.config["MONGO_URI"] = os.environ.get("CONN_STR")
    
    # Inicializa a conexão com o MongoDB
    client = MongoClient(app.config["MONGO_URI"])
    app.db = client.mydatabase
    
    # Outras inicializações
    with app.app_context():
        from .views import views
        app.register_blueprint(views)

    return app
