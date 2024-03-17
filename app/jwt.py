from flask import Blueprint, jsonify
from app.extensions import jwt
from app.models import User

jwt_bp = Blueprint('jwt', __name__)

# load user

@jwt.user_lookup_loader
def user_lookup_callback(jwt_header, jwt_data):
    identity = jwt_data['sub']

    return User.query.filter_by(username=identity).one_or_none()

# additional claims

@jwt.additional_claims_loader
def make_additional_claims(identity):
    if identity == "johndoe":
        '''
        users that meet this condition is_staff will be set to True
        in this case johndoe
        '''
        return {"is_staff": True}
    
    return {"is_staff": False}

# error handlers

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_data):
    return jsonify(
        {
            "message": "Token has expired", 
            "error": "token_expired"
        }
    ), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify(
        {
            "message": "Signature verification failed", 
            "error": "invalid_token"
        }
    ), 401

@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify(
        {
            "message": "Request doesnt contain valid token", 
            "error": "authorization_header"
        }
    ), 401