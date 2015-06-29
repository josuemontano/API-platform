from jwt import DecodeError, ExpiredSignature
from pyramid.interfaces import IAuthenticationPolicy
from pyramid.security import Authenticated, Everyone
from zope.interface import implementer

from .jwt import parse_token


@implementer(IAuthenticationPolicy)
class JWTAuthenticationPolicy(object):
    """
    A Pyramid authentication policy which obtains data from
    JWT authentication headers.
    """
    def __init__(self, callback):
        self.callback = callback

    def authenticated_userid(self, request):
        try:
            payload = parse_token(request)
            userid = payload['sub']
            if self.callback(userid, request) is not None:
                return userid
            return None
        except (DecodeError, ExpiredSignature):
            return None

    def unauthenticated_userid(self, request):
        try:
            payload = parse_token(request)
            return payload['sub']
        except (DecodeError, ExpiredSignature):
            return None

    def effective_principals(self, request):
        principals = [Everyone]
        try:
            payload = parse_token(request)
            userid = payload['sub']
            groups = self.callback(userid, request)
            if groups is not None:
                principals.append(Authenticated)
                principals.append(userid)
                principals.extend(groups)
        except (DecodeError, ExpiredSignature):
            pass
        finally:
            return principals

    def remember(self, request, principal, **kw):
        return []

    def forget(self, request):
        return []
