import os

import jwt
import pendulum


def sign_in(mocker, user):
    secret = os.environ.get('JWT_SECRET', 'secret')
    claims = dict(sub=user.id, iat=pendulum.now(), exp=pendulum.tomorrow())
    mocker.patch.object(jwt, 'decode', return_value=claims)

    access_token = jwt.encode(claims, secret).decode("utf-8")
    return f'JWT {access_token}'
