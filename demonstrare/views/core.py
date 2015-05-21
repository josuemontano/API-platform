import logging

from .base import BaseView, register_views

from demonstrare.models.core import Post
from demonstrare.schema.core import PostSchema

from datetime import date
from pyramid.view import view_config
from sqlalchemy import desc

log = logging.getLogger(__name__)


@view_config(route_name='home', renderer='templates/index.html')
def index(request):
    return {'year': date.today().year}


@register_views(route='post', collection_route='posts')
class PostsView(BaseView):
    # GET /posts
    def list(self):
        schema = PostSchema(many=True, only={'id', 'title'})
        ll = self.request.db_session.query(Post).filter_by(is_published=True).order_by(desc(Post.created)).all()
        return schema.dump(ll).data

    # GET /posts/<pk>
    def detail(self):
        pk = int(self.request.matchdict['id'])

        schema = PostSchema()
        item = self.request.db_session.query(Post).get(pk)
        return schema.dump(item).data
