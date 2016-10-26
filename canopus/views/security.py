from pyramid.security import Allow

from ..models.auth import User


def groupfinder(userid, request):
    user = request.dbsession.query(User).get(userid)
    if user is not None:
        return [user.role.name]


class RootFactory(object):
    # TODO: Load from database
    __acl__ = [(Allow, 'admin', ('admin', 'view')),
               (Allow, 'user', 'view')]

    def __init__(self, request):
        self.request = request
