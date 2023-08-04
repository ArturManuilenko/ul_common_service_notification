from typing import Tuple

from api_utils.api_resource.api_resource import ApiResource
from flask import render_template, request

from src.conf.notification__web import web_sdk
from src.conf.self_api import self_api


@web_sdk.api_route(['GET', 'POST'], '/send_message')
@web_sdk.html_view(many=False, access=web_sdk.ACCESS_PUBLIC)
def view_send_message(api_resource: ApiResource) -> Tuple[str, int]:
    if request.method == 'GET':
        return render_template(
            'send_message.html',
            active='send_message',
            title='Send message',
        ), 200

    if request.method == 'POST':
        template_data = request.form.to_dict()
        [template_data.pop(key, None) for key in ['email', 'template']]

        self_api.request_post(f'/templates/{request.form.get("template")}/emails', json={
            'email_to': request.form.get('email'),
            'template_data': template_data,
        })

        return render_template(
            'send_message.html',
            active='send_message',
            title='Send message',
        ), 200

    raise NotImplementedError()
