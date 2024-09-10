from flask import Flask, request, redirect, url_for, render_template
from app.models import db
from dotenv import load_dotenv
from flask_migrate import Migrate
import os

load_dotenv()

migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    migrate = Migrate(app, db, render_as_batch=True)
    db.init_app(app)
    migrate.init_app(app, db)

    from .portfolio.routes import portfolio
    app.register_blueprint(portfolio)


    with app.app_context():
        db.create_all()

    return app