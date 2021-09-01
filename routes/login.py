from flask import Blueprint, jsonify, request

login = Blueprint('login', __name__)


@login.route('/v1/login', methods=["POST"])
def login_user():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    return jsonify({"succes": True})
    # if username != "test" or password != 'test':
    #     return jsonify({"msg": "Bad username or password"}), 401
    # access_token = create_access_token(identity=username)
    # return jsonify(access_token=access_token)
