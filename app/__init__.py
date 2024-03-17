from flask import Flask
from app.extensions import db, jwt

def create_app():

    app = Flask(__name__)

    app.config.from_prefixed_env()

    # initialize extensions
    db.init_app(app)
    jwt.init_app(app)

    # import blueprints
    from app.auth import auth_bp

    # register blueprints
    app.register_blueprint(auth_bp)

    return app