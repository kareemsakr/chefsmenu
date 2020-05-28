from flask import Flask
from marshmallow import Schema
from flask_restful import Api

from api.login_handler import LoginResource
from api.user_handler import UserResource
from api.meal_item_handler import MealItemResource
from api.LogoutResource import LogoutResource


from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    jwt_refresh_token_required, create_refresh_token,
    get_jwt_identity
)
from models import db


def create_app():
    app = Flask(__name__)
    app.config['JWT_TOKEN_LOCATION'] = ['cookies']

    # Only allow JWT cookies to be sent over https. In production, this
    # should likely be True
    app.config['JWT_COOKIE_SECURE'] = False
    app.config['JWT_ACCESS_COOKIE_PATH'] = '/'
    app.config['JWT_REFRESH_COOKIE_PATH'] = '/users/login'
    app.config['JWT_COOKIE_CSRF_PROTECT'] = True
    app.config['JWT_CSRF_IN_COOKIES'] = True
    app.config['JWT_SECRET_KEY'] = 'team-bluejay'
    jwt = JWTManager(app)

    # Database variables
    user = 'postgres'
    pw = '123456'
    url = 'localhost:5432'
    db_name = 'team-bluejay'

    DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
        user=user, pw=pw, url=url, db=db_name)

    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    api = Api(app)

    api.add_resource(UserResource, '/users')
    api.add_resource(LoginResource, '/users/login')
    api.add_resource(MealItemResource, '/meal_items')
    api.add_resource(LogoutResource, '/users/logout')

    return app
