import uuid
from datetime import datetime
from typing import Any, Dict, Optional, Tuple
from uuid import UUID

from db_utils.modules.db import db

from src.notification__db.helpers.get_template_by_id import get_template_by_id
from src.notification__db.model.template import Template
from src.notification__db.model.template_content import TemplateContent, TemplateType


def update_template(
    name: str,
    content: str,
    type: TemplateType,
    input_data_json_schema: Dict[str, Any],
    default_data: Optional[Dict[str, Any]],
    user_id: UUID,
    template_id: UUID
) -> Tuple[Template, TemplateContent]:
    template = get_template_by_id(template_id)
    template.name = name
    template.mark_as_modified(user_id)
    template_content = TemplateContent(
        id=uuid.uuid4(),
        date_created=datetime.utcnow(),
        user_created_id=user_id,
        content=content,
        type=type,
        input_data_json_schema=input_data_json_schema,
        default_data=default_data,
        template_id=template.id
    )
    db.session.add(template_content)
    return template, template_content
