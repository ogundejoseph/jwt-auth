from flask import Blueprint, jsonify, request
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