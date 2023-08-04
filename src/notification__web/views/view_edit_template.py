import json
from typing import Union, Tuple
from uuid import UUID

from api_utils.api_resource.api_resource import ApiResource
from flask import Response, request, redirect, url_for, render_template

from src.conf.notification__web import web_sdk
from src.conf.self_api import self_api


@web_sdk.api_route(['POST', 'GET'], '/templates/edit/<id_template>')
@web_sdk.rest_api(many=False, access=web_sdk.ACCESS_PUBLIC)
def view_edit_template(api_resource: ApiResource, id_template: UUID) -> Union[Tuple[str, int], Response]:
    if request.method == 'POST':
        try:
            json.loads(request.form.get('input_data_json_schema'))  # type: ignore
        except ValueError as e:
            return f"Error input_data_json_schema {e}", 400
        self_api.request_put(f'/templates/{id_template}', json={
            'name': request.form.get('name'),
            'content': request.form.get('content'),
            'type': request.form.get('type_template'),
            'input_data_json_schema': json.loads(request.form.get('input_data_json_schema')),  # type: ignore
            'default_data': json.loads(request.form.get('default_data')) if request.form.get('default_data') else [],  # type: ignore
        })
        return redirect(url_for('view_list_template'))  # type: ignore
    res = self_api.request_get(f'/templates/{id_template}')
    return render_template(
        'edit_template.html',
        title="Edit template",
        data=res.payload,
        input_data_json_schema=json.dumps(res.payload['template_content']['input_data_json_schema'], ensure_ascii=False),
    ), 200
