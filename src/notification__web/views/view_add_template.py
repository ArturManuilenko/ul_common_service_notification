import json
from typing import Tuple

from api_utils.api_resource.api_resource import ApiResource
from flask import request, redirect, url_for, render_template

from src.conf.notification__web import web_sdk
from src.conf.self_api import self_api


@web_sdk.api_route(['POST', 'GET'], '/templates/add')
@web_sdk.rest_api(many=False, access=web_sdk.ACCESS_PUBLIC)
def view_add_template(api_resource: ApiResource) -> Tuple[str, int]:
    if request.method == 'POST':
        self_api.request_post('/templates', json={
            'name': request.form.get('name'),
            'content': request.form.get('content'),
            'type': request.form.get('type_template'),
            'input_data_json_schema': json.loads(request.form['input_data_json_schema']),
            'default_data': json.loads(request.form.get('default_data', [])),  # type: ignore
        })
        redirect(url_for('view_list_template'))
    return render_template(
        'add_template.html',
        title="Add template",
    ), 200
