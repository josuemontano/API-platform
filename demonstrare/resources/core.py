from .pyr import SecuredResource

from demonstrare.auth.jwt import parse_token
from demonstrare.models.core import Post, User

from restless.preparers import FieldsPreparer
from sqlalchemy import desc


class ProfileResource(SecuredResource):
    def __init__(self, *args, **kwargs):
        super(ProfileResource, self).__init__(*args, **kwargs)

        self.http_methods.update({
            'custom': {
                'GET': 'custom',
            }
        })

    # GET /profile/
    def custom(self):
        request = self.request
        me = request.db_session.query(User).filter_by(id=self.user_id).first()

        return {
            'display_name': me.display_name,
        }

    @classmethod
    def as_list(cls, *init_args, **init_kwargs):
        return cls.as_view('custom', *init_args, **init_kwargs)


class PostResource(SecuredResource):
    preparer = FieldsPreparer(fields=Post.serializer())

    # GET /posts/
    def list(self):
        db_session = self.request.db_session
        return db_session.query(Post).filter_by(is_published=True).order_by(desc('created')).all()

    # GET /posts/<pk>
    def detail(self, pk):
        db_session = self.request.db_session
        return db_session.query(Post).get(pk)
