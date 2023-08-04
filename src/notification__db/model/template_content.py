import uuid
from datetime import datetime
from enum import Enum

from db_utils import CustomQuery
from db_utils.modules.db import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy_serializer import SerializerMixin


class TemplateType(Enum):
    jinja2 = 'JINJA2'


class TemplateContent(db.Model, SerializerMixin):
    __tablename__ = 'template_content'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    date_created = db.Column(db.DateTime(), default=datetime.utcnow(), nullable=False)
    user_created_id = db.Column(UUID(as_uuid=True), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    type = db.Column(db.Enum(TemplateType), nullable=False)
    input_data_json_schema = db.Column(db.JSON(), nullable=False)
    default_data = db.Column(db.JSON(), nullable=False)
    template_id = db.Column(UUID(as_uuid=True), db.ForeignKey('template.id'), nullable=False)
    template = db.relationship(
        'Template',
        foreign_keys=[template_id],
        query_class=CustomQuery,
        uselist=False,
    )
