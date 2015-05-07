from .pyr import SecuredResource

from demonstrare.auth.jwt import parse_token
from demonstrare.models.core import Post

from restless.preparers import FieldsPreparer


class PostResource(SecuredResource):
    preparer = FieldsPreparer(fields=Post.serializer())

    # GET /posts/
    def list(self):
        return self.request.db.query(Post).filter(Post.is_published == True).order_by('created desc').all()

    # GET /posts/<pk>
    def detail(self, pk):
        return self.request.db.query(Post).get(pk)
