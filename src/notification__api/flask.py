from flask import Flask
from flask_mail import Mail

from src.conf.mail_conf import MailConfig
from src.conf.notification__api import api_sdk
from src.conf.notification__db import db_config

flask_app: Flask = api_sdk.flask_app

flask_app.config.from_object(MailConfig)

db_config.attach_to_flask_app(flask_app)

mail = Mail(flask_app)


__all__ = (
    'flask_app',
    'mail',
)
