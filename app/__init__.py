from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

# extensions
db = SQLAlchemy()
jwt = JWTManager()

def create_app():

    app = Flask(__name__)

    app.config.from_prefixed_env()

    # initialize extensions
    db.init_app(app)
    jwt.init_app(app)

    # import blueprints
    from app.auth import auth_bp
    from app.users import user_bp
    from app.jwt import jwt_bp

    # register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(jwt_bp)

    return app