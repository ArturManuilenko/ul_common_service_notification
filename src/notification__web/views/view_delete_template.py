from typing import Tuple, Union
from uuid import UUID

from api_utils.api_resource.api_resource import ApiResource
from flask import redirect, url_for
from werkzeug import Response

from src.conf.notification__web import web_sdk
from src.conf.self_api import self_api


@web_sdk.api_route_get('/templates/delete/<id_template>')
@web_sdk.rest_api(many=False, access=web_sdk.ACCESS_PUBLIC)
def view_delete_template(api_resource: ApiResource, id_template: UUID) -> Union[Tuple[str, int], Response]:
    self_api.request_delete(f'/templates/{id_template}')
    return redirect(url_for('view_list_template'))
