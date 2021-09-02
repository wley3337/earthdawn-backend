from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager
from api.routes.login import login

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "one-ring"  # change this
jwt = JWTManager(app)

app.register_blueprint(login)

if __name__ == "__main__":
    app.run(debug=True)
