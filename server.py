import os
from flask import Flask


def create_app():
    """Factory function that creates the Flask App"""

    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])

    from flask_cors import CORS
    CORS(app, origins=["http://localHost:3000"])
    # Print ENV to console
    print(os.environ['APP_SETTINGS'])

    # Instantiate JWT In App
    from api.services.jwt import jwt
    jwt.init_app(app)

    # Instantiate DataBase In App
    from api.services.database import db
    db.init_app(app)

    # Instantiate Marshmallow to app
    from api.services.marshmallow import ma
    ma.init_app(app)

    # Import models
    from api.models import user
    from api.models import talent

    # Import Routes
    from api.routes.login import login
    app.register_blueprint(login)

    from api.routes.talents import talents
    app.register_blueprint(talents)

    return app
