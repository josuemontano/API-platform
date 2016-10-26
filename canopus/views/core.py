from sqlalchemy import asc, desc

from .base import CRUDBaseView, CRUDRegistrar
from ..models.core import Post
from ..schema.core import PostSchema


@CRUDRegistrar(route='post', collection_route='posts', permission='view')
class PostsView(CRUDBaseView):
    resource = Post
    schema_many = PostSchema(many=True, only=('id', 'title'))
    schema = PostSchema()

    def search_expression(self, search_term):
        return Post.title.ilike(search_term)

    def order_expression(self, query):
        return query.order_by(desc(Post.created_at)).order_by(asc(Post.title))

    def populate_object(self, post, data):
        post.title = data.title
        post.body = data.body
        post.is_published = data.is_published
