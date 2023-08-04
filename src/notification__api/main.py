from src.conf.notification__api import api_sdk
from src.notification__api.flask import flask_app

api_sdk.load_routes()

__all__ = (
    'flask_app',
)
