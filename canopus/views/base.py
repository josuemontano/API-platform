from pyramid.httpexceptions import HTTPForbidden, HTTPNotFound


class BaseView(object):
    """
    Base plain view with nothing but the request and userid.

    :type request: ``pyramid.request.Request``
    :type userid: int
    """
    def __init__(self, request):
        self.request = request
        self.current_user_id = request.authenticated_userid
