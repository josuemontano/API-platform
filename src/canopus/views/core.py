from cornice.resource import resource

from .base import BaseView
from ..auth import RootFactory
from ..models import Post
from ..schema import PostSchema


@resource(collection_path='/api/v1/posts', path='/api/v1/posts/{id}', factory=RootFactory, permission='view')
class PostsView(BaseView):
    model = Post
    model_schema = PostSchema()
    collection_schema = PostSchema(many=True, only=('id', 'title'))
