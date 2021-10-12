from flask import Blueprint, jsonify, request
from http import HTTPStatus
from flasgger import swag_from
from flask_jwt_extended import jwt_required

from api.models.talent import Talent, talent_schema, talents_schema

talents = Blueprint('talents', __name__, url_prefix='/api/v1/talents')


@talents.route('/', methods=["GET"])
@swag_from(
    {'response': {
        HTTPStatus.OK.value: {
            'description': 'Get all talents'
        }
    }})
@jwt_required()
def get_all_talents():
    """Returns all talents in the database sorted by id"""
    all_talents = Talent.all()
    return jsonify(talents_schema.dump(all_talents)), 200
