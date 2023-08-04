from typing import Any, Dict
import uuid
from datetime import datetime
from uuid import UUID

from db_utils.modules.db import db

from src.notification__db.model.email_message_log import EmailMessageLog


def add_email_message_log(
    user_created: UUID,
    input_data: Dict[str, Any],
    result_content: str,
    email_to: str,
    template_id: UUID,
    template_content_id: UUID,
) -> None:
    new_log = EmailMessageLog(
        id=uuid.uuid4(),
        date_created=datetime.utcnow(),
        user_created=user_created,
        input_data=input_data,
        result_content=result_content,
        email_to=email_to,
        template_id=template_id,
        template_content_id=template_content_id
    )
    db.session.add(new_log)
