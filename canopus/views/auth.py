import json
from datetime import timedelta

import pendulum
import requests
from pyramid.request import Request
from pyramid.view import view_config, view_defaults
from pyramid.httpexceptions import HTTPNotFound, HTTPUnprocessableEntity

from ..models import User
from ..schema import UserSchema


@view_defaults(renderer='json', request_method='POST')
class AuthenticatorView:
    def __init__(self, request: Request):
        self.request = request

    def issue_access_token(self, email: str=None, user: User=None):
        if email:
            user = self.request.dbsession.query(User).filter_by(email=email, is_enabled=True).one_or_none()

        if user:
            now = pendulum.now()
            expire_in = timedelta(days=7)
            expires_at = now.add(days=7)
            access_token = self.request.create_jwt_token(user.id, expiration=expire_in)
            user.last_signed_in_at = now

            return dict(user=UserSchema().dump(user), access_token=access_token, expires=expires_at.format(pendulum.constants.ISO8601))
        else:
            return HTTPUnprocessableEntity()


class SocialAuthenticatorView(AuthenticatorView):
    @view_config(route_name='auth-google')
    def google(self):
        profile_api_url = 'https://www.googleapis.com/plus/v1/people/me/openIdConnect'
        profile = self.fetch_profile_from_provider(profile_api_url)
        email = profile['email']

        return self.issue_access_token(email=email)

    @view_config(route_name='auth-windows')
    def windows(self):
        profile_api_url = 'https://apis.live.net/v5.0/me'
        profile = self.fetch_profile_from_provider(profile_api_url)
        email = profile['emails']['account']

        return self.issue_access_token(email=email)

    def fetch_profile_from_provider(self, profile_api_url: str, fetch_method=requests.get):
        """Verify with the social provider the token is valid and who the user is"""
        access_token = self.request.json['access_token']
        headers = {'Authorization': f'Bearer {access_token}'}
        response = fetch_method(profile_api_url, headers=headers)
        profile = json.loads(response.text)

        return profile
