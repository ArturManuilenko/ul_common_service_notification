from typing import Tuple
from uuid import UUID

from api_utils.api_resource.api_resource import ApiResource

from src.conf.notification__web import web_sdk
from src.conf.self_api import self_api


@web_sdk.api_route_get('/templates-select/<id_template>')
@web_sdk.rest_api(many=False, access=web_sdk.ACCESS_PUBLIC)
def view_template_select_id(api_resource: ApiResource, id_template: UUID) -> Tuple[str, int]:
    res = self_api.request_get(f"/templates/{id_template}")
    return res.result_json
