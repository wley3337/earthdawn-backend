from flask import Blueprint, jsonify, request
from http import HTTPStatus
from flasgger import swag_from
from flask_jwt_extended import unset_jwt_cookies

logout = Blueprint('logout', __name__)


@logout.route('/api/v1/logout', methods=["GET"])
@swag_from({
    'response': {
        HTTPStatus.OK.value: {
            'description':
            'Logs out a user by removing the JWT token in the cookies',
        }
    }
})
def logout_user():
    """Logs Out a user of the application and removes the JWT HTTP only cookie"""
    response = jsonify({
        "message": "log out successful",
    })
    unset_jwt_cookies(response)
    return response, 200
