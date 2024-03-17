from flask import Blueprint, jsonify, request
from flask_jwt_extended import (
    create_access_token, 
    create_refresh_token, 
    jwt_required, 
    get_jwt,
    get_jwt_identity, 
    current_user
    )
from app.models import User

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.post('/register')
def register_user():
    data = request.get_json()
    
    user = User.get_username(username=data.get('username'))

    if user:
        return jsonify({"error": "Username is taken. Please choose a different username"}), 403
    
    email = User.get_email(email=data.get('email'))

    if email:
        return jsonify({"error": "Email already exists"}), 403
     
    new_user = User(
        username = data.get('username'),
        email = data.get('email')
    )
    new_user.set_password(password=data.get('password'))
    new_user.save()

    return jsonify({"message": "User created"}), 201


@auth_bp.post('login')
def login_user():
    data = request.get_json()
    user = User.get_username(username=data.get('username'))

    if user and (user.check_password(password=data.get('password'))):
        access_token = create_access_token(identity=user.username)
        refresh_token = create_refresh_token(identity=user.username)

        return jsonify(
            {
                "message":"logged in",
                "tokens":{
                    "access":access_token,
                    "refresh":refresh_token
                }
            }
        ), 200
    
    return jsonify({"error": "Invalid username or password"}), 400