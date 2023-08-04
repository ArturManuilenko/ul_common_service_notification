import uuid
from datetime import datetime

from db_utils import CustomQuery
from db_utils.modules.db import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy_serializer import SerializerMixin

from src.notification__db.model.template import Template
from src.notification__db.model.template_content import TemplateContent


class EmailMessageLog(db.Model, SerializerMixin):
    __tablename__ = 'email_message_log'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    date_created = db.Column(db.DateTime(), default=datetime.utcnow(), nullable=False)
    user_created = db.Column(UUID(as_uuid=True), nullable=False)
    input_data = db.Column(db.JSON(), nullable=False)
    result_content = db.Column(db.Text(), nullable=False)
    email_to = db.Column(db.String(1000), nullable=False)
    serialize_rules = ("-template_id", "-template.template_content", "-template_content.template")

    template_content_id = db.Column(UUID(as_uuid=True), db.ForeignKey('template_content.id'), nullable=False)
    template_content = db.relationship(
        TemplateContent,
        foreign_keys=[template_content_id],
        query_class=CustomQuery,
        uselist=False,
    )
    template_id = db.Column(UUID(as_uuid=True), db.ForeignKey('template.id'), nullable=False)
    template = db.relationship(
        Template,
        foreign_keys=[template_id],
        query_class=CustomQuery,
        uselist=False,
    )
