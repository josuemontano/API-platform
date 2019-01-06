from sqlalchemy.orm import Session
from sqlalchemy.orm.query import Query
from sqlalchemy_searchable import search

from .meta import Base
from .user import User


class CollectionQueryBuilder:
    def __init__(self, model: Base, dbsession: Session, current_user: User, params):
        self.model = model
        self.dbsession = dbsession
        self.current_user = current_user
        self.params = params

    def build(self):
        query = self.search(self.filter(self.build_base_query()))
        total = query.count()

        return (*self.paginate(query), total)

    def build_base_query(self):
        return self.dbsession.query(self.model)

    def filter(self, query: Query):
        return query

    def search(self, query: Query):
        params = self.params
        search_text = (
            params['search'].replace('.', ' ').strip() if 'search' in params else None
        )

        if search_text:
            search_by, search_query = self.get_search_query(search_text)
            search_expression = self.get_search_vector_for_field(
                query, search_by, search_query
            )

            if type(search_expression) is Query:
                return search_expression
            else:
                return search(query, search_query, vector=search_expression)
        else:
            return self.sort(query)

    def paginate(self, query: Query):
        params = self.params
        per_page = params['per_page'] if 'per_page' in params else 25
        page = params['page'] if 'page' in params else 1

        return query.limit(per_page).offset((page - 1) * per_page), page

    def sort(self, query: Query):
        params = self.params
        if 'sort_by' in params:
            sort_by = params['sort_by']
            sort_column = getattr(self.model, sort_by, None)
        else:
            sort_column = self.get_default_sort_column()

        if sort_column is not None:
            return query.order_by(*sort_column)
        else:
            return query

    def get_search_query(self, search_text):
        search_params = search_text.split(':', 1)
        search_by = search_params[0].strip() if len(search_params) == 2 else None
        search_query = search_params[1] if len(search_params) == 2 else search_params[0]
        search_query = search_query.strip()

        return search_by, search_query

    def get_search_vector_for_field(self, query, search_by: str, search_query: str):
        vector = getattr(self.model, f'{search_by}_search_vector', None)
        if vector:
            return vector
        else:
            return self.get_default_search_vector()

    def get_default_search_vector(self):
        return None

    def get_default_sort_column(self):
        return (getattr(self.model, 'name', None),)
