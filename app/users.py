from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.schemas import UserSchema
from app.models import User


user_bp = Blueprint('users', __name__, url_prefix='/users')

@user_bp.get('/all')
@jwt_required()
def get_all_users():

    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=15, type=int)

    users = User.query.paginate(page=page, per_page=per_page)

    result = UserSchema().dump(users, many=True)

    return jsonify({"users": result}), 200
    