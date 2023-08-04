from typing import Any, Dict
from uuid import UUID

import jsonschema
from api_utils.api_resource.api_resource import ApiResource
from api_utils.errors.api_simple_validate_error import ApiSimpleValidateError
from api_utils.utils.constants import TJsonResponse
from pydantic import BaseModel

from src.conf.notification__api import api_sdk
from src.conf.notification_service_input_worker import WORKER_NAME
from src.notification__db.helpers.get_json_schema_by_id import get_json_schema
from src.notification__uni_worker.lib import uni
from src.notification__uni_worker.messages.notification_input_message import NotificationInputV0Message
import src.conf.permissions as permissions


class ApiSendMessageQueryModel(BaseModel):
    template_data: Dict[str, Any]
    email_to: str


uni.init_consumer_worker(WORKER_NAME)
uni.initialize()


@api_sdk.api_route_post('/templates/<uuid:template_id>/emails')
@api_sdk.rest_api(many=False, access=permissions.PERMISSION__NFK_MK_MESSAGE_EMAIL)
def nfk_mk_message_email(api_resource: ApiResource, body: ApiSendMessageQueryModel, template_id: UUID) -> TJsonResponse:
    input_data_json_schema, user_created_id = get_json_schema(template_id)
    try:
        jsonschema.validate(body.template_data, input_data_json_schema)
    except jsonschema.exceptions.SchemaError:
        raise ApiSimpleValidateError("invalid input data json schema")
    except jsonschema.exceptions.ValidationError:
        raise ApiSimpleValidateError("invalid template data")
    message = NotificationInputV0Message(
        template_data=body.template_data,
        email_to=body.email_to,
        template_id=template_id,
        user_created_id=user_created_id,
    )
    uni.send_to(WORKER_NAME, message)
    return api_resource.response_obj_ok(None)
