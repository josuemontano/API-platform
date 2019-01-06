from marshmallow import ValidationError
from pyramid.httpexceptions import HTTPBadRequest, HTTPNotFound
from pyramid.request import Request
from webargs import fields
from webargs.pyramidparser import use_args, use_kwargs

from ..models.query import CollectionQueryBuilder


class BaseView:
    collection_schema = None
    model = None
    query_builder = CollectionQueryBuilder
    schema = None

    def __init__(self, request: Request, context=None):
        self.request = request
        self.dbsession = request.dbsession
        self.current_user = request.user

    @use_args(
        {
            'page': fields.Int(missing=1),
            'per_page': fields.Int(missing=25),
            'search': fields.String(),
            'sort_by': fields.String(),
        }
    )
    def collection_get(self, args):
        query_builder = self.query_builder(
            self.model, self.dbsession, self.current_user, args
        )
        query, page, total = query_builder.build()

        items = self.collection_schema.dump(query.all())
        return dict(total=total, page=page, items=items)

    def collection_post(self):
        instance = self.load_json_body()

        self.dbsession.add(instance)
        self.dbsession.flush()

        self.request.response.status_code = 201
        return self.schema.dump(instance)

    @use_kwargs({'instance_id': fields.Int(data_key='id', location='matchdict')})
    def get(self, instance_id: int):
        instance = self.dbsession.query(self.model).get(instance_id)

        if instance:
            return self.schema.dump(instance)
        else:
            return HTTPNotFound()

    @use_kwargs({'instance_id': fields.Int(data_key='id', location='matchdict')})
    def put(self, instance_id: int):
        instance = self.dbsession.query(self.model).get(instance_id)

        if instance:
            self.load_json_body(instance=instance)
            return self.schema.dump(instance)
        else:
            return HTTPNotFound()

    @use_kwargs({'instance_id': fields.Int(data_key='id', location='matchdict')})
    def delete(self, instance_id: int):
        instance = self.dbsession.query(self.model).get(instance_id)

        if instance:
            self.dbsession.delete(instance)
            return self.schema.dump(instance)
        else:
            return HTTPNotFound()

    def load_json_body(self, instance=None, extra_attrs=None):
        if extra_attrs is None:
            extra_attrs = {}
        extra_attrs.update(self.request.json)

        try:
            return self.schema.load(
                extra_attrs, instance=instance, session=self.dbsession
            )
        except ValidationError as error:
            raise HTTPBadRequest(json_body=error.messages)
