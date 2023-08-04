from typing import Any, Dict, Optional
from uuid import UUID

import jsonschema
from api_utils.api_resource.api_resource import ApiResource
from api_utils.errors.api_validate_error import ApiValidateError
from api_utils.utils.constants import TJsonResponse
from db_utils import transaction_commit
from pydantic import BaseModel

import src.conf.permissions as permissions
from src.conf.common import NOTIFICATION__SYS_USER_ID
from src.conf.notification__api import api_sdk
from src.notification__db.helpers.add_template import add_new_template, attach_current_content_to_template, add_new_template_content
from src.notification__db.helpers.delete_template_by_id import delete_template_by_id
from src.notification__db.helpers.update_template import update_template
from src.notification__db.model.template_content import TemplateType


class ApiCreateTemplate(BaseModel):
    name: str
    content: str
    type: TemplateType
    input_data_json_schema: Dict[str, Any] = ...    # type: ignore
    default_data: Optional[Dict[str, Any]] = ...    # type: ignore


@api_sdk.api_route_post('/templates')
@api_sdk.rest_api(many=False, access=permissions.PERMISSION__NFK_MK_TEMPLATE)
def nfk_mk_template(api_resource: ApiResource, body: ApiCreateTemplate) -> TJsonResponse:
    try:
        jsonschema.validate(object(), body.input_data_json_schema)
    except jsonschema.exceptions.SchemaError:
        raise ApiValidateError(
            code='validation_error',
            location='body.input_data_json_schema',
            msg_template="invalid input data json schema"
        )
    except jsonschema.exceptions.ValidationError:
        pass
    with transaction_commit():
        template = add_new_template(
            # user_created_id=api_resource.auth_token.user_id,
            user_created_id=UUID(NOTIFICATION__SYS_USER_ID),
            name=body.name,
        )
        template_content = add_new_template_content(
            user_created_id=UUID(NOTIFICATION__SYS_USER_ID),
            content=body.content,
            type=body.type,
            input_data_json_schema=body.input_data_json_schema,
            default_data=body.default_data,
            template_id=template.id
        )

    with transaction_commit():
        attach_current_content_to_template(
            template=template,
            template_content_id=template_content.id,
            user_modified_id=UUID(NOTIFICATION__SYS_USER_ID)
        )
    return api_resource.response_obj_created_ok(template.to_dict())


@api_sdk.api_route_put('/templates/<uuid:template_id>')
@api_sdk.rest_api(many=False, access=permissions.PERMISSION__NFK_MOD_TEMPLATE)
def nfk_mod_template(api_resource: ApiResource, template_id: UUID, body: ApiCreateTemplate) -> TJsonResponse:
    with transaction_commit():
        template, template_content = update_template(
            # user_id=api_resource.auth_token.user_id,
            user_id=UUID(NOTIFICATION__SYS_USER_ID),
            name=body.name,
            content=body.content,
            type=body.type,
            input_data_json_schema=body.input_data_json_schema,
            default_data=body.default_data,
            template_id=template_id,
        )

    with transaction_commit():
        attach_current_content_to_template(
            template=template,
            template_content_id=template_content.id,
            user_modified_id=UUID(NOTIFICATION__SYS_USER_ID)
        )
    return api_resource.response_obj_created_ok(template.to_dict())


@api_sdk.api_route_delete('/templates/<uuid:template_id>')
@api_sdk.rest_api(many=False, access=permissions.PERMISSION__NFK_DEL_TEMPLATE)
def nfk_del_template(api_resource: ApiResource, template_id: UUID) -> TJsonResponse:
    with transaction_commit():
        delete_template_by_id(template_id)
    return api_resource.response_obj_deleted_ok()
