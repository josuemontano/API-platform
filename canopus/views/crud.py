import json
import logging
from datetime import datetime

from pyramid.httpexceptions import HTTPBadRequest, HTTPNotFound
from pyramid.view import view_config
from sqlalchemy import asc
from sqlalchemy.exc import IntegrityError

from .base import BaseView

log = logging.getLogger(__name__)


class CRUDBaseView(BaseView):
    resource = None
    schema_many = None
    schema = None

    # GET /<resource>?limit=20&offset=100&search=text
    def list(self):
        request = self.request
        total, query = self.list_queries(request)
        try:
            limit = int(request.GET['limit'])
            offset = int(request.GET['offset'])

            if 'search' in request.GET and request.GET['search']:
                search_query = "%{0}%".format(request.GET['search'])
                exp = self.search_expression(search_query)
                if exp is not None:
                    query = query.filter(exp)
                    total = total.filter(exp)
            query = query.limit(limit).offset(offset)
        except KeyError:
            log.warn('No limit/offset keys found, will return the whole set of %s', self.resource)

        total = total.count()
        return {'meta': {'total': total}, 'data': self.schema_many.dump(query.all()).data}

    # POST /<resource>
    def create(self):
        data = self.load_object()
        log.info('User %d is creating %s %s', self.userid, data.__class__.__name__, data)
        self.request.dbsession.add(data)

        return self.schema.dump(data).data

    # GET /<resource>/<id>
    def detail(self):
        pk = int(self.request.matchdict['id'])
        requested = self.request.dbsession.query(self.resource).get(pk)
        if not requested:
            raise HTTPNotFound()

        return self.schema.dump(requested).data

    # PUT /<resource>/<id>
    def update(self):
        data = self.load_object()
        item = self.request.dbsession.query(self.resource).get(data.id)
        if not item:
            raise HTTPNotFound()
        
        log.info('User %d is updating %s %s', self.userid, item.__class__.__name__, item)

        self.populate_object(item, data)
        return self.schema.dump(item).data

    # DELETE /<resource>/<id>
    def delete(self):
        pk = int(self.request.matchdict['id'])
        request = self.request
        item = request.dbsession.query(self.resource).get(pk)
        if not item:
            raise HTTPNotFound()

        try:
            request.dbsession.begin_nested()
            request.dbsession.delete(item)
            request.dbsession.flush()

            return self.schema.dump(item).data
        except IntegrityError:
            request.dbsession.rollback()
            log.warn('There are related records for %s {pk:%s}. WON\'T BE DELETED', item.__class__.__name__, pk)
            self.delete_fallback(item)

    def list_queries(self, request):
        return request.dbsession.query(self.resource.id).filter_by(deleted_at=None), \
            self.order_expression(request.dbsession.query(self.resource)).filter_by(deleted_at=None)

    def order_expression(self, query):
        try:
            return query.order_by(asc(self.resource.name))
        except AttributeError:
            return query
    
    def search_expression(self, search_term):
        try:
            return self.resource.name.ilike(search_term)
        except AttributeError:
            return None
    
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
    :type permission: str | None
    """
    def __init__(self, route=None, collection_route=None, permission=None):
        self.route = route
        self.collection_route = collection_route
        self.permission = permission

    def __call__(self, cls):
        cls.item_route = self.route
        if self.route:
            cls = view_config(_depth=1, renderer='json', permission=self.permission, attr='detail', request_method='GET', route_name=self.route)(cls)
            cls = view_config(_depth=1, renderer='json', permission=self.permission, attr='update', request_method='PUT', route_name=self.route)(cls)
            cls = view_config(_depth=1, renderer='json', permission=self.permission, attr='delete', request_method='DELETE', route_name=self.route)(cls)
        if self.collection_route:
            cls = view_config(_depth=1, renderer='json', permission=self.permission, attr='list', request_method='GET', route_name=self.collection_route)(cls)
            cls = view_config(_depth=1, renderer='json', permission=self.permission, attr='create', request_method='POST', route_name=self.collection_route)(cls)
        return cls
