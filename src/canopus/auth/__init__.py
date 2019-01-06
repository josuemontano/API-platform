import os

from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.security import Allow, ALL_PERMISSIONS

from ..models import User, Role


class RootFactory(object):
    """Permission definitions"""

    __acl__ = [(Allow, Role.USER, 'view'), (Allow, Role.ADMIN, ALL_PERMISSIONS)]

    def __init__(self, request):
        self.request = request


def groupfinder(userid, request):
    user = request.user
    if user is not None:
        return [user.role]
    return None


def get_current_user(request):
    user_id = request.unauthenticated_userid
    return (
        request.dbsession.query(User)
        .filter_by(id=user_id, is_enabled=True)
        .filter(User.deleted_at.is_(None))
        .one_or_none()
    )


def includeme(config):
    config.include('pyramid_jwt')

    config.set_authorization_policy(ACLAuthorizationPolicy())

    jwt_secret = os.environ.get('JWT_SECRET', 'secret')
    config.set_jwt_authentication_policy(jwt_secret, callback=groupfinder)

    config.add_request_method(get_current_user, name='user', reify=True)
