import os
from datetime import datetime, timedelta

import jwt
from jwt import DecodeError


def create_token(user):
    payload = {
        'sub': user.id,
        'iat': datetime.now(),
        'exp': datetime.now() + timedelta(days=20),
    }

    token = jwt.encode(payload, os.environ.get('JWT_SECRET'))
    return token.decode('unicode_escape')


def parse_token(request):
    auth_token = request.headers.get('Authorization', None)
    if auth_token is None:
        raise DecodeError()
    else:
        token = auth_token.split()[1]
        return jwt.decode(token, os.environ.get('JWT_SECRET'))
