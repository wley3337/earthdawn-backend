from flask import Blueprint, jsonify, request
from http import HTTPStatus
from flasgger import swag_from

from api.models.talent import Talent, talent_schema, talents_schema

talents = Blueprint('talents', __name__)


@talents.route('/v1/talents', methods=["GET"])
@swag_from(
    {'response': {
        HTTPStatus.OK.value: {
            'description': 'Get all talents'
        }
    }})
def get_all_talents():
    """Returns all talents in the database sorted by id"""
    all_talents = Talent.all()
    return jsonify(talents_schema.dump(all_talents)), 200
