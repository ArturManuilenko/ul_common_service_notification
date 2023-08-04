from jinja2 import Template
from db_utils.modules.db_context import db_context_transaction_commit
from flask_mail import Message
from unipipeline.worker.uni_worker import UniWorker
from unipipeline.worker.uni_worker_consumer_message import UniWorkerConsumerMessage

from src.notification__db.helpers.get_template_by_id import get_template_by_id
from src.conf.self_logging import self_logging
from src.notification__api.flask import flask_app, mail
from src.notification__db.helpers.add_message_log import add_email_message_log
from src.notification__uni_worker.messages.notification_input_message import NotificationInputV0Message

logger = self_logging.getLogger(__name__)


class NotificationInputWorker(UniWorker[NotificationInputV0Message, None]):
    @db_context_transaction_commit(flask_app)
    def handle_message(self, message: UniWorkerConsumerMessage[NotificationInputV0Message]) -> None:
        logger.info("%s -> NotificationWorker HANDLE MESSAGE", message)

        input_msg: NotificationInputV0Message = message.payload

        template = get_template_by_id(input_msg.template_id)
        template_content = Template(template.template_content.content)
        template_html = template_content.render(input_msg.template_data)

        sending_msg = Message(
            sender='no-reply@neroelectronics.com',
            recipients=[input_msg.email_to]
        )
        sending_msg.html = str(template_html)
        mail.send(sending_msg)

        add_email_message_log(
            user_created=input_msg.user_created_id,
            input_data=input_msg.template_data,
            result_content=template_html,
            email_to=input_msg.email_to,
            template_id=input_msg.template_id,
            template_content_id=template.current_content
        )
