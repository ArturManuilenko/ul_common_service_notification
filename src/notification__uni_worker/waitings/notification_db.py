from unipipeline.waiting.uni_postgres_waiting import UniPostgresWaiting

from src.conf.notification__db import db_config


class NotificationDbWaiting(UniPostgresWaiting):
    def get_connection_uri(self) -> str:
        return db_config.uri
