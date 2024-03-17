from flask import Blueprint, jsonify
from app.extensions import jwt

jwt_bp = Blueprint('jwt', __name__)

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