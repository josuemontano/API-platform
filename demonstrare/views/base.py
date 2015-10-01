class BaseView(object):
    """ Base plain view with nothing but the request and userid.
    """
    def __init__(self, request):
        self.request = request
        self.userid = request.authenticated_userid
