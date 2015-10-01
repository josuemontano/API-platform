import json
import logging

from pyramid.exceptions import HTTPBadRequest
from pyramid.view import view_defaults, view_config
from sqlalchemy import desc

from .base import BaseView
from demonstrare.models.core import Post
from demonstrare.schema.core import PostSchema

log = logging.getLogger(__name__)


@view_defaults(route_name='post', renderer='json', permission='view')
class PostsView(BaseView):
    # GET /posts
    @view_config(request_method='GET', route_name='posts')
    def list(self):
        schema = PostSchema(many=True, only=('id', 'title'))
        ll = self.request.db_session.query(Post).filter_by(is_published=True).order_by(desc(Post.created)).all()
        return schema.dump(ll).data

    # GET /posts/<id>
    @view_config(request_method='GET')
    def detail(self):
        pk = int(self.request.matchdict['id'])

        schema = PostSchema()
        item = self.request.db_session.query(Post).get(pk)
        return schema.dump(item).data

    # PUT /posts/<id>
    @view_config(request_method='PUT')
    def update(self):
        pk = int(self.request.matchdict['id'])
        body = self.request.body.decode("utf-8")
        body = json.loads(body)

        data, errors = PostSchema(only=('title', 'body')).load(body)
        if any(errors):
            return HTTPBadRequest(body=json.dumps(errors))

        log.info('User %d is updating the post "%s"', self.userid, data.title)
        post = self.request.db_session.query(Post).get(pk)
        post.title = data.title
        post.body = data.body

        schema = PostSchema()
        return schema.dump(post).data
