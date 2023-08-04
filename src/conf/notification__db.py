import os

from db_utils import DbConfig


db_config = DbConfig(
    uri=os.environ['NOTIFICATION__DB_URI'],
)
