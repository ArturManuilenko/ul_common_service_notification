"""empty message

Revision ID: 73f71698c503
Revises: 36eacc481a8b
Create Date: 2021-10-11 10:12:00.168851

"""
import json
from datetime import datetime
from alembic import op


# revision identifiers, used by Alembic.
revision = '73f71698c503'
down_revision = 'c1b455ed0562'
branch_labels = None
depends_on = None

TEMPLATE_ID = 'e3b81c7d-9643-467f-af5a-c1b69a43e836'
TEMPLATE_NAME = "pii_invite_template"
TEMPLATE_CONTENT_ID = '1a44b7df-7044-4565-bb58-5d4d839d8ffc'
USER_CREATE_ID = '6230d349-16b8-4aaa-825c-ab4bee6ccc77'
TEMPLATE_CONTENT_SCHEMA = {
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "auth_token": {
      "type": "string"
    }
  },
  "required": [
    "name",
    "auth_token"
  ]
}
TEMPLATE_CONTENT_DEFAULT_DATA = {
    "name": "-",
    "auth_token": "-"
}
TEMPLATE_CONTENT_HTML = '''
<h2 style="text-align: center;"><strong>Hello, {{name}} <br /><span class="VIiyi" lang="en"><span class="JLqJ4b ChMk0b" data-language-for-alternatives="en" data-language-to-translate-into="ru" data-phrase-index="0">you have been invited to be new member of Project Registry<br /></span></span></strong></h2>
<h2 style="text-align: center;">&nbsp;</h2>
<h2 style="text-align: center;"><strong>Your authorization token is:</strong></h2>
<h2 style="text-align: center;"><strong>{{auth_token}}</strong></h2>
<h2 style="text-align: center;">&nbsp;</h2>"
'''


def upgrade():
    dt_now = datetime.utcnow()
    op.execute("INSERT INTO template(id, user_created_id, user_modified_id, is_alive, "
                "date_created, date_modified, name, current_content) "
                f"VALUES ('{TEMPLATE_ID}', '{USER_CREATE_ID}', '{USER_CREATE_ID}', True, "
                f"'{dt_now}', '{dt_now}', '{TEMPLATE_NAME}', '{TEMPLATE_CONTENT_ID}')")
    op.execute("INSERT INTO template_content(id, date_created, user_created_id, "
                "content, type, input_data_json_schema, default_data, template_id) "
                f"VALUES ('{TEMPLATE_CONTENT_ID}', '{dt_now}', '{USER_CREATE_ID}', "
                f"'{TEMPLATE_CONTENT_HTML}', 'jinja2', '{json.dumps(TEMPLATE_CONTENT_SCHEMA)}', '{json.dumps(TEMPLATE_CONTENT_DEFAULT_DATA)}', '{TEMPLATE_ID}')")


def downgrade():
    pass
