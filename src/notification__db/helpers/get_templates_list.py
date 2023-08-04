from typing import Tuple, List, Dict, Any

from sqlalchemy import desc
from sqlalchemy.orm.exc import NoResultFound
from db_utils.utils.search.search import db_search
from src.notification__db.model.template import Template


def get_templates_list(
    limit: int,
    offset: int,
    filters: List[Dict[str, Any]] = [],  # noqa
    sorts: List[Tuple[str, str]] = [],  # noqa
) -> Tuple[List[Template], int]:
    template_query = Template.query.order_by(desc(Template.date_created))
    if not template_query:
        raise NoResultFound('No templates found')
    template_list = db_search(
        model=Template,
        initial_query=template_query,
        sorts=sorts,
        filters=filters,
        limit=limit,
        offset=offset
    ).all()
    total_count = db_search(
        model=Template,
        initial_query=template_query,
        filters=filters,
    ).count()
    return template_list, total_count
