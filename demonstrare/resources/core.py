from demonstrare.models import Post
from restless.preparers import FieldsPreparer
from restless.pyr import PyramidResource


class PostResource(PyramidResource):
    preparer = FieldsPreparer(fields=Post.serializer())

    # GET /posts/
    def list(self):
        return self.request.db.query(Post).filter(Post.is_published == True).order_by('created desc').all()

    # GET /posts/<pk>
    def detail(self, pk):
        return self.request.db.query(Post).get(pk)
