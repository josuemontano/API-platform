import json
import requests

from demonstrare.auth.jwt import create_token
from demonstrare.models.core import User

from pyramid.view import view_config


@view_config(route_name='oauth2-google', renderer='json', request_method='POST')
def google(request):
    access_token_url = 'https://accounts.google.com/o/oauth2/token'
    people_api_url = 'https://www.googleapis.com/plus/v1/people/me/openIdConnect'
    payload = dict(client_id=request.json['clientId'],
                   redirect_uri=request.json['redirectUri'],
                   client_secret=request.registry.settings['GOOGLE_SECRET'],
                   code=request.json['code'],
                   grant_type='authorization_code')

    # Step 1. Exchange authorization code for access token.
    r = requests.post(access_token_url, data=payload)
    token = json.loads(r.text)
    headers = {'Authorization': 'Bearer {0}'.format(token['access_token'])}

    # Step 2. Retrieve information about the current user.
    r = requests.get(people_api_url, headers=headers)
    profile = json.loads(r.text)

    user = request.db_session.query(User).filter_by(google=profile['sub']).first()
    if user is None:
        user = User(display_name=profile['given_name'], google=profile['sub'])
        request.db_session.add(user)
        request.db_session.flush()
    
    token = create_token(user)
    return dict(token=token)


@view_config(route_name='oauth2-facebook', renderer='json', request_method='POST')
def facebook(request):
    access_token_url = 'https://graph.facebook.com/v2.3/oauth/access_token'
    graph_api_url = 'https://graph.facebook.com/v2.3/me'
    params = {
        'client_id': request.json['clientId'],
        'redirect_uri': request.json['redirectUri'],
        'client_secret': request.registry.settings['FACEBOOK_SECRET'],
        'code': request.json['code']
    }

    # Step 1. Exchange authorization code for access token.
    r = requests.get(access_token_url, params=params)
    access_token = json.loads(r.text)

    # Step 2. Retrieve information about the current user.
    r = requests.get(graph_api_url, params=access_token)
    profile = json.loads(r.text)

    user = request.db_session.query(User).filter_by(google=profile['sub']).first()
    if user is None:
        user = User(display_name=profile['given_name'], facebook=profile['sub'])
        request.db_session.add(user)
        request.db_session.flush()

    token = create_token(user)
    return dict(token=token)
