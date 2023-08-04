import os


class MailConfig(object):
    MAIL_SERVER = os.environ['NOTIFICATION__MAIL_SERVER']
    MAIL_USERNAME = os.environ['NOTIFICATION__MAIL_USERNAME']
    MAIL_PASSWORD = os.environ['NOTIFICATION__MAIL_PASSWORD']
    MAIL_PORT = os.environ['NOTIFICATION__MAIL_PORT']
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
