from uuid import UUID

from db_utils.utils.enshure_db_object_exists import enshure_db_object_exists
from src.notification__db.model.email_message_log import EmailMessageLog


def get_log_by_id(log_id: UUID) -> EmailMessageLog:
    log = EmailMessageLog.query.filter_by(id=log_id).first()
    return enshure_db_object_exists(EmailMessageLog, log)
