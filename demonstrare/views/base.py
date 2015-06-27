class BaseView(object):
    def __init__(self, request):
        self.request = request
        self.userid = request.authenticated_userid
