import json
import logging
from datetime import datetime

from pyramid.httpexceptions import HTTPBadRequest, HTTPNotFound, HTTPNoContent
from pyramid.view import view_config
from sqlalchemy.exc import IntegrityError

from .base import BaseView
from ..services import QueryBuilder

log = logging.getLogger(__name__)


class CRUDBaseView(BaseView):
    resource = None
    schema_many = None
    schema = None
    query_builder = QueryBuilder

    # GET /<resource>?limit=20&offset=100&search=text
    def list(self):
        request = self.request
        builder = self.query_builder(self.resource, request)

        total = builder.total()
        total_count = total.count()
        self.request.response.headers['X-Total-Count'] = str(total_count)

        query = builder.all()
        return self.schema_many.dump(query.all()).data

    # POST /<resource>
    def create(self):
        item = self.load_object()
        self.request.dbsession.add(item)
        self.request.dbsession.flush()

        log.info('User %d created %s. Params => %s', self.current_user_id, item.__class__.__name__, self.request.json)

        return self.schema.dump(item).data

    # GET /<resource>/<id>
    def detail(self):
        pk = int(self.request.matchdict['id'])
        item = self.request.dbsession.query(self.resource).get(pk)
        if not item or item.deleted_at is not None:
            raise HTTPNotFound()

        return self.schema.dump(item).data

    # PUT /<resource>/<id>
    def update(self):
        pk = int(self.request.matchdict['id'])
        item = self.request.dbsession.query(self.resource).get(pk)
        if not item or item.deleted_at is not None:
            raise HTTPNotFound()

        data = self.load_object()
        self.populate_object(item, data)

        log.info('User %d updated %s. Params => %s', self.current_user_id, item.__class__.__name__, self.request.json)

        return self.schema.dump(item).data

    # DELETE /<resource>/<id>
    def delete(self):
        pk = int(self.request.matchdict['id'])
        request = self.request
        item = request.dbsession.query(self.resource).get(pk)
        if not item or item.deleted_at is not None:
            raise HTTPNotFound()

        try:
            request.dbsession.begin_nested()
            request.dbsession.delete(item)
            request.dbsession.flush()

            log.info('User %d deleted %s. Params => %s', self.current_user_id, item.__class__.__name__, request.params)
        except IntegrityError:
            request.dbsession.rollback()
            log.error('There are related records for %s. Params => %s. IT WON\'T BE HARD DELETED', item.__class__.__name__, request.params)
            self.delete_fallback(item)
        finally:
            return HTTPNoContent()

    def load_object(self):
        body = self.request.body.decode("utf-8")
        body = json.loads(body)

        data, errors = self.schema.load(body)
        if any(errors):
            raise HTTPBadRequest(body=json.dumps(errors))
        else:
            return data

    def populate_object(self, item, data):
        raise NotImplementedError()

    def delete_fallback(self, item):
        item.deleted_at = datetime.now()


class CRUDRegistrar(object):
    """
    Decorator meant to do all the view_config work for the CRUD services
    we expose, setting JSON as the render for these views.

    If route is provided the following attributes will be configured with
    these verbs
        detail: GET
        update: PUT
        delete: DELETE

    If collection_route is provided the attributes will be configured with
    these verbs
        create: GET
        list: POST

    :type route: str | None
    :type collection_route: str | None
    :type permissions: dict | {}
    """
    def __init__(self, route=None, collection_route=None, http_cache=(None, {'private': True}), **permissions):
        self.route = route
        self.collection_route = collection_route
        self.http_cache = http_cache
        self.permissions = permissions

        self.setup_permissions()

    def setup_permissions(self):
        """Set permissions for all views. If none was provided use the
        default one.
        """
        default_permission = self.permissions.get('default')

        self.permissions['list'] = self.permissions.get('list') or default_permission
        self.permissions['create'] = self.permissions.get('create') or default_permission
        self.permissions['detail'] = self.permissions.get('detail') or default_permission
        self.permissions['update'] = self.permissions.get('update') or default_permission
        self.permissions['delete'] = self.permissions.get('delete') or default_permission

    def __call__(self, cls):
        cls.item_route = self.route
        if self.collection_route:
            cls = view_config(_depth=1, renderer='json', http_cache=self.http_cache, permission=self.permissions['list'], attr='list', request_method='GET', route_name=self.collection_route)(cls)
            cls = view_config(_depth=1, renderer='json', http_cache=self.http_cache, permission=self.permissions['create'], attr='create', request_method='POST', route_name=self.collection_route)(cls)
        if self.route:
            cls = view_config(_depth=1, renderer='json', http_cache=self.http_cache, permission=self.permissions['detail'], attr='detail', request_method='GET', route_name=self.route)(cls)
            cls = view_config(_depth=1, renderer='json', http_cache=self.http_cache, permission=self.permissions['update'], attr='update', request_method='PUT', route_name=self.route)(cls)
            cls = view_config(_depth=1, renderer='json', http_cache=self.http_cache, permission=self.permissions['delete'], attr='delete', request_method='DELETE', route_name=self.route)(cls)
        return cls
