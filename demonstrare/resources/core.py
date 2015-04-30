from demonstrare.auth.jwt import parse_token
from demonstrare.models.core import Post
from restless.preparers import FieldsPreparer
from restless.pyr import PyramidResource


class PostResource(PyramidResource):
    preparer = FieldsPreparer(fields=Post.serializer())

    def is_authenticated(self):
        request = self.request
        if request.headers.get('Authorization'):
            try:
                payload = parse_token(request)
                # TODO: Integrate with pyramid's auth system?
                return True
            except DecodeError:
                print('Token is invalid')
            except ExpiredSignature:
                print('Token has expired')
        return False

    # GET /posts/
    def list(self):
        return self.request.db.query(Post).filter(Post.is_published == True).order_by('created desc').all()

    # GET /posts/<pk>
    def detail(self, pk):
        return self.request.db.query(Post).get(pk)
