from demonstrare.auth.jwt import parse_token

from restless.pyr import PyramidResource


class SecuredResource(PyramidResource):
    def is_authenticated(self):
        request = self.request
        if request.headers.get('Authorization'):
            try:
                payload = parse_token(request)
                # TODO: Integrate with pyramid's auth system?
                self.user_id = payload['sub']
                return True
            except DecodeError:
                print('Token is invalid')
            except ExpiredSignature:
                print('Token has expired')
        return False
