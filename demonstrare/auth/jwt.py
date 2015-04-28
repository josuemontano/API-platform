import jwt
import os

from datetime import datetime, timedelta


def create_token(user):
    payload = {
        'sub': user.id,
        'iat': datetime.now(),
        'exp': datetime.now() + timedelta(days=1)
    }

    token = jwt.encode(payload, os.environ.get('JWT_SECRET'))
    return token.decode('unicode_escape')


def parse_token(request):
    token = request.headers.get('Authorization').split()[1]
    return jwt.decode(token, os.environ.get('JWT_SECRET'))
