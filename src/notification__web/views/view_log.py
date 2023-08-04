from typing import Tuple
from uuid import UUID

from api_utils.api_resource.api_resource import ApiResource
from flask import render_template

from src.conf.notification__web import web_sdk
from src.conf.self_api import self_api


@web_sdk.api_route_get('/logs/<log_id>')
@web_sdk.html_view(many=False, access=web_sdk.ACCESS_PUBLIC)
def view_log(api_resource: ApiResource, log_id: UUID) -> Tuple[str, int]:
    res = self_api.request_get(f'/logs/{log_id}')
    if not res.ok:
        return render_template('errors/invalid_request_400.html'), 400
    return render_template(
        'log.html',
        title=f"Log {log_id}",
        data=res.payload,
    ), 200
