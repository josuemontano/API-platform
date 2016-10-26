import json

import requests
from pyramid.view import view_config, view_defaults
from pyramid.httpexceptions import HTTPNotFound

from ..models import User
from ..auth import TokenFactory


@view_defaults(renderer='json', request_method='POST')
class Authenticator(object):
    def __init__(self, request):
        self.request = request

    @view_config(route_name='oauth2-google')
    def google(self):
        profile_api_url = 'https://www.googleapis.com/plus/v1/people/me/openIdConnect'
        profile = self.get_profile(profile_api_url)

        try:
            return self.issue_access_token(profile['email'])
        except:
            raise HTTPNotFound()

    @view_config(route_name='oauth2-facebook')
    def facebook(self):
        profile_api_url = 'https://graph.facebook.com/v2.5/me?fields=id,email'
        profile = self.get_profile(profile_api_url)

        try:
            return self.issue_access_token(profile['email'])
        except:
            raise HTTPNotFound()

    @view_config(route_name='oauth2-windows')
    def windows(self):
        profile_api_url = 'https://apis.live.net/v5.0/me'
        profile = self.get_profile(profile_api_url)

        try:
            return self.issue_access_token(profile['emails']['account'])
        except:
            raise HTTPNotFound()

    def issue_access_token(self, email):
        user = self.request.dbsession.query(User).filter_by(
                email=email).filter(
                User.deleted.is_(None)).one()
        factory = TokenFactory(self.request, user)
        return factory.create_access_token()

    def get_profile(self, profile_api_url):
        """Verify with the social provider the token is valid and who the user is """
        token = self.request.POST['access_token']
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        response = requests.get(profile_api_url, headers=headers)
        profile = json.loads(response.text)

        return profile
