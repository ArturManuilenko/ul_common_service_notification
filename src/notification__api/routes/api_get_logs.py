from uuid import UUID

from api_utils.api_resource.api_resource import ApiResource
from api_utils.utils.constants import TJsonResponse

import src.conf.permissions as permissions
from src.conf.notification__api import api_sdk
from src.notification__db.helpers.get_log_by_id import get_log_by_id
from src.notification__db.helpers.get_log_list import get_log_list


@api_sdk.api_route_get('/logs')
@api_sdk.rest_api(many=True, access=permissions.PERMISSION__NFK_GET_LOGS_LIST)
def nfk_get_logs_list(api_resource: ApiResource) -> TJsonResponse:
    logs, total_count = get_log_list(
        limit=api_resource.pagination.limit,
        offset=api_resource.pagination.offset,
        filters=api_resource.filter_by.params,
        sorts=api_resource.sort_by.params
    )
    log_list = [log.to_dict() for log in logs]
    return api_resource.response_list_ok(list_of_obj=log_list, total_count=total_count)


@api_sdk.api_route_get('/logs/<uuid:log_id>')
@api_sdk.rest_api(many=False, access=permissions.PERMISSION__NFK_GET_LOG)
def nfk_get_log(api_resource: ApiResource, log_id: UUID) -> TJsonResponse:
    log = get_log_by_id(log_id)
    return api_resource.response_obj_ok(log.to_dict())
