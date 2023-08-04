import uuid
from typing import Any, Dict, Optional
from uuid import UUID


from api_utils.errors.object_has_already_exists_error import ObjectHasAlreadyExistsError
from db_utils.modules.db import db

from src.notification__db.model.template import Template
from src.notification__db.model.template_content import TemplateContent, TemplateType


def add_new_template(
    name: str,
    user_created_id: UUID,
) -> Template:
    if template_dublicate := Template.query.filter_by(name=name).first():
        raise ObjectHasAlreadyExistsError(
            f"Template {template_dublicate.id} with name {template_dublicate.name} already exist"
        )

    template = Template(
        id=uuid.uuid4(),
        name=name,
    )
    template.mark_as_created(user_created_id)

    db.session.add(template)
    db.session.flush()
    return template


def add_new_template_content(
    content: str,
    type: TemplateType,
    input_data_json_schema: Dict[str, Any],
    default_data: Optional[Dict[str, Any]],
    user_created_id: UUID,
    template_id: UUID
) -> TemplateContent:
    template_content = TemplateContent(
        id=uuid.uuid4(),
        user_created_id=user_created_id,
        content=content,
        type=type,
        input_data_json_schema=input_data_json_schema,
        default_data=default_data,
        template_id=template_id
    )
    db.session.add(template_content)
    db.session.flush()
    return template_content


def attach_current_content_to_template(
    template: Template,
    template_content_id: UUID,
    user_modified_id: UUID
) -> None:
    template.current_content = template_content_id
    template.mark_as_modified(user_modified_id)
