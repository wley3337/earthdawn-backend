from flask import Blueprint, jsonify, request
from http import HTTPStatus
from flasgger import swag_from
from flask_jwt_extended import create_access_token, set_access_cookies

from api.models.user import User
from api.utils.password_helpers import create_password_digest, password_matches

login = Blueprint('login', __name__)


@login.route('/api/v1/login', methods=["POST"])
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
    user = User.find_by_username(username)
    password_digest = user.password_digest

    if password_matches(password, password_digest):
        # create jwt with user.id
        additional_claims = {"user_id": user.id}
        access_token = create_access_token(identity=user.id,
                                           additional_claims=additional_claims)
        response = jsonify({
            "username": username,
            "password": password,
        })
        set_access_cookies(response, access_token)
        return response, 200
    else:
        return jsonify({"message": "Username or Password is incorrect."}), 404
