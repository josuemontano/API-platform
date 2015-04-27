import jwt
import os

from datetime import datetime, timedelta


def parse_token(request):
    token = request.headers.get('Authorization').split()[1]
    return jwt.decode(token, os.environ.get('JWT_SECRET'))
