import os
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS


def create_app():
    """Factory function that creates the Flask App"""

    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])

    CORS(app, origins=["http://localHost:3000"])
    # Print ENV to console
    print(os.environ['APP_SETTINGS'])

    # Instantiate DataBase In App
    from api.services.database import db
    db.init_app(app)

    # Import models
    from api.models import user

    from api.routes.login import login
    app.register_blueprint(login)

    return app
