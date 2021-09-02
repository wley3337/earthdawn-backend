from flask import Blueprint, jsonify, request
from http import HTTPStatus
from flasgger import swag_from

login = Blueprint('login', __name__)


@login.route('/v1/login', methods=["POST"])
@swag_from(
    {'response': {
        HTTPStatus.OK.value: {
            'description': 'Login route',
        }
    }})
def login_user():
    """Logs a user into application and adds a JWT HTTP only cookie"""
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    return jsonify({
        "success": True,
        "username": username,
        "password": password
    })


# if username != "test" or password != 'test':
#     return jsonify({"msg": "Bad username or password"}), 401
# access_token = create_access_token(identity=username)
# return jsonify(access_token=access_token)
