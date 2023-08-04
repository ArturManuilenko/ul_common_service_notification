from db_utils import CustomQuery
from db_utils.model.base_user_log_model import BaseUserLogModel
from db_utils.modules.db import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy_serializer import SerializerMixin


class Template(BaseUserLogModel, SerializerMixin):
    __tablename__ = 'template'

    serialize_rules = ("-template_content.template",)
    name = db.Column(db.String(255), unique=True, nullable=False)
    current_content = db.Column(UUID(as_uuid=True), db.ForeignKey('template_content.id'), nullable=True)
    template_content = db.relationship(
        'TemplateContent',
        order_by='desc(TemplateContent.date_created)',
        foreign_keys=[current_content],
        query_class=CustomQuery,
        uselist=False,
    )
