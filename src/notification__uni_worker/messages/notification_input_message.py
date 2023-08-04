from typing import Dict, Any
from uuid import UUID

from unipipeline.message.uni_message import UniMessage


class NotificationInputV0Message(UniMessage):
    template_data: Dict[str, Any]
    email_to: str
    template_id: UUID
    user_created_id: UUID
