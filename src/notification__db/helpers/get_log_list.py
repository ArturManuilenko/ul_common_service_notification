from typing import Tuple, List, Dict, Any

from db_utils.utils.search.search import db_search
from sqlalchemy import desc

from src.notification__db.model.email_message_log import EmailMessageLog


def get_log_list(
    limit: int,
    offset: int,
    filters: List[Dict[str, Any]] = [],  # noqa
    sorts: List[Tuple[str, str]] = [],  # noqa
) -> Tuple[List[EmailMessageLog], int]:
    log_list_query = EmailMessageLog.query.order_by(desc(EmailMessageLog.date_created))
    log_list = db_search(
        model=EmailMessageLog,
        initial_query=log_list_query,
        sorts=sorts,
        filters=filters,
        limit=limit,
        offset=offset
    ).all()
    total_count = db_search(
        model=EmailMessageLog,
        initial_query=log_list_query,
        filters=filters,
    ).count()
    return log_list, total_count
