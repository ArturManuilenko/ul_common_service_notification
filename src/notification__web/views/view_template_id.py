from typing import Tuple
from uuid import UUID

from api_utils.api_resource.api_resource import ApiResource
from flask import render_template

from src.conf.notification__web import web_sdk
from src.conf.self_api import self_api


@web_sdk.api_route_get('/templates/<id_template>')
@web_sdk.html_view(many=False, access=web_sdk.ACCESS_PUBLIC)
def view_template_id(api_resource: ApiResource, id_template: UUID) -> Tuple[str, int]:
    res = self_api.request_get(f'/templates/{id_template}', q={})
    return render_template(
        'template.html',
        active="templates",
        title='Templates',
        data=res.payload,
    ), 200
