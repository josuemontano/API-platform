from pyramid.security import Allow


class RootFactory(object):
    # TODO: Load from database
    __acl__ = [(Allow, 'admin', ('admin', 'view')),
               (Allow, 'user', 'view')]

    def __init__(self, request):
        self.request = request
