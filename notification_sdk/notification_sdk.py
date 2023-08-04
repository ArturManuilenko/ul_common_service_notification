from typing import Dict, Any
from uuid import UUID

import requests

from api_utils.modules.api_sdk_jwt import ApiSdkJwt     # noqa: E0401
from notification_sdk.notification_sdk_config import NotificationSdkConfig


class NotificationSdk:

    def __init__(self, config: NotificationSdkConfig) -> None:
        self._config = config

    def send_email_message(self, template_id: UUID, template_data: Dict[str, Any], email_to: str, token: ApiSdkJwt) -> Dict[str, Any]:
        auth_header = {'Authorization': f'Bearer {token}'}
        template_payload = {
            'template_data': template_data,
            'email_to': email_to,
        }
        result = requests.post(
            f'{self._config.api_url}/'
            f'api/v1/templates/{template_id}/emails',
            json=template_payload,
            headers=auth_header,
        )
        result.raise_for_status()
        return result.json()
