from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from .config import Config  # Configurações da app

db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Configurações do config.py

    db.init_app(app)
    bcrypt.init_app(app)

    # Regista as rotas
    from . import routes
    app.register_blueprint(routes)

    return app
