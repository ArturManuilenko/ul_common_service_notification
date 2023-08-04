from uuid import UUID

from db_utils.utils.enshure_db_object_exists import enshure_db_object_exists
from src.notification__db.model.template import Template


def get_template_by_id(template_id: UUID) -> Template:
    template = Template.query.filter_by(id=template_id).first()
    return enshure_db_object_exists(Template, template)
