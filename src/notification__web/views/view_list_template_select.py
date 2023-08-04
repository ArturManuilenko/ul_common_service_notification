from typing import Tuple

from api_utils.api_resource.api_resource import ApiResource

from src.conf.notification__web import web_sdk
from src.conf.self_api import self_api


@web_sdk.api_route_get('/templates-select')
@web_sdk.rest_api(many=False, access=web_sdk.ACCESS_PUBLIC)
def view_list_template_select(api_resource: ApiResource) -> Tuple[str, int]:
    res = self_api.request_get("/templates")
    return res.result_json
