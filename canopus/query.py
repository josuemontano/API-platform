from sqlalchemy import asc, desc, or_


class QueryBuilder(object):
    def __init__(self, resource, request):
        self.resource = resource
        self.request = request
        self.params = request.GET

    def total(self):
        return self.search(self.filter(self.request.dbsession.query(self.resource.id)))

    def all(self):
        query = self.search(self.filter(self.order(self.request.dbsession.query(self.resource))))
        return self.limit(query)

    def limit(self, query):
        limit = int(self.params['limit']) if 'limit' in self.params else 20
        offset = int(self.params['offset']) if 'offset' in self.params else 0
        return query.limit(limit).offset(offset)

    def filter(self, query):
        return query.filter_by(deleted_at=None)

    def search(self, query):
        if 'search' in self.params and self.params['search']:
            text = "%{0}%".format(self.params['search'])
            exp = self.search_in(text)
            if exp is not None:
                return query.filter(exp)

        return query

    def search_in(self, text):
        try:
            return self.resource.name.ilike(text)
        except AttributeError:
            return None

    def order(self, query):
        try:
            return query.order_by(asc(self.resource.name))
        except AttributeError:
            return query
