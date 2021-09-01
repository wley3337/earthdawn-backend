from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager
from routes.login import login

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "one-ring"  # change this
jwt = JWTManager(app)

app.register_blueprint(login)

# @app.route('/v1/login', methods=["POST"])
# def login():
#     username = request.json.get("username", None)
#     password = request.json.get("password", None)
#     if username != "test" or password != 'test':
#         return jsonify({"msg": "Bad username or password"}), 401
#     access_token = create_access_token(identity=username)
#     return jsonify(access_token=access_token)

if __name__ == "__main__":
    app.run(debug=True)
