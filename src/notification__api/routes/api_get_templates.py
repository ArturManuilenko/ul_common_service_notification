from uuid import UUID

from api_utils.api_resource.api_resource import ApiResource
from api_utils.utils.constants import TJsonResponse

import src.conf.permissions as permissions
from src.conf.notification__api import api_sdk
from src.notification__db.helpers.get_template_by_id import get_template_by_id
from src.notification__db.helpers.get_templates_list import get_templates_list


@api_sdk.api_route_get('/templates')
@api_sdk.rest_api(many=True, access=permissions.PERMISSION__NFK_GET_TEMPLATES_LIST)
def nfk_get_templates_list(api_resource: ApiResource) -> TJsonResponse:
    templates, total_count = get_templates_list(
        limit=api_resource.pagination.limit,
        offset=api_resource.pagination.offset,
        filters=api_resource.filter_by.params,
        sorts=api_resource.sort_by.params
    )
    templates_list = [template.to_dict() for template in templates]
    return api_resource.response_list_ok(list_of_obj=templates_list, total_count=total_count)


@api_sdk.api_route_get('/templates/<uuid:template_id>')
@api_sdk.rest_api(many=False, access=permissions.PERMISSION__NFK_GET_TEMPLATE)
def nfk_get_template(api_resource: ApiResource, template_id: UUID) -> TJsonResponse:
    template = get_template_by_id(template_id)
    return api_resource.response_obj_ok(template.to_dict())
