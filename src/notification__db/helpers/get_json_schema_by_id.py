from typing import Any, Dict, Tuple
from uuid import UUID
from src.notification__db.model.template_content import TemplateContent


def get_json_schema(template_id: UUID) -> Tuple[Dict[str, Any], UUID]:
    template = TemplateContent.query.filter_by(template_id=template_id).first()
    return template.input_data_json_schema, template.user_created_id
