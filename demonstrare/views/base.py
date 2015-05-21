from demonstrare.auth.jwt import parse_token

from jwt import DecodeError, ExpiredSignature
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPUnauthorized


class register_views(object):
    def __init__(self, route=None, collection_route=None, custom=None):
        self.route = route
        self.collection_route = collection_route
        self.custom = custom

    def __call__(self, cls):
        cls.item_route = self.route
        if self.route:
            cls = view_config(_depth=1, renderer='json', attr='detail', request_method='GET', route_name=self.route)(cls)
            cls = view_config(_depth=1, renderer='json', attr='update', request_method='PUT', route_name=self.route)(cls)
            cls = view_config(_depth=1, renderer='json', attr='delete', request_method='DELETE', route_name=self.route)(cls)
        if self.collection_route:
            cls = view_config(_depth=1, renderer='json', attr='list', request_method='GET', route_name=self.collection_route)(cls)
        if self.custom:
            cls = view_config(_depth=1, renderer='json', attr=self.custom['attr'], request_method=self.custom['method'], route_name=self.custom['route'])(cls)
        return cls


class BaseView(object):
    item_cls = None
    schema_cls = None

    def __init__(self, request):
        self.request = request
        self.user_id = None
        # TODO:
        if not self.is_authenticated():
            raise HTTPUnauthorized()

    def is_authenticated(self):
        request = self.request
        if request.headers.get('Authorization'):
            try:
                payload = parse_token(request)
                # TODO: Integrate with pyramid's auth system?
                self.user_id = payload['sub']
                return True
            except DecodeError:
                request.response.status = 401
                print('Token is invalid', request)
            except ExpiredSignature:
                request.response.status = 401
                print('Token has expired', request)
        return False

    def list(self):
        # noinspection PyCallingNonCallable
        schema = self.schema_cls(many=True)
        ll = self.request.db_session.query(self.item_cls).all()
        return schema.dump(ll).data

    def detail(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
