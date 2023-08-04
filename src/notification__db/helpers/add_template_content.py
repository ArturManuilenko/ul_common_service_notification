import uuid
from datetime import datetime
from typing import Any, Dict, Optional
from uuid import UUID

from db_utils.modules.db import db

from src.notification__db.model.template_content import TemplateContent, TemplateType


def add_new_template_content(
    content: str,
    template_id: UUID,
    type: TemplateType,
    input_data_json_schema: Dict[str, Any],
    default_data: Optional[Dict[str, Any]],
    user_created_id: UUID
) -> TemplateContent:
    template_content = TemplateContent(
        id=uuid.uuid4(),
        template_id=template_id,
        date_created=datetime.utcnow(),
        user_created_id=user_created_id,
        content=content,
        type=type,
        input_data_json_schema=input_data_json_schema,
        default_data=default_data,
    )
    db.session.add(template_content)
    return template_content
