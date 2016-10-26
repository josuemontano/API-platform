from datetime import datetime, timedelta

from ..schema import UserSchema


class TokenFactory(object):
    def __init__(self, request, user):
        self.user = user
        self.request = request

    def create_access_token(self):
        user = self.user
        if user.last_signed_in is None:
            user.welcome()
        user.last_signed_in = datetime.now()

        token = self.request.create_jwt_token(user.id, expiration=timedelta(days=7))
        user_schema = UserSchema(exclude=('enabled',))

        return dict(token=token, user={})
