import json
import logging

import requests
from pyramid.httpexceptions import HTTPNotFound
from pyramid.view import view_config
from sqlalchemy.orm.exc import NoResultFound

from demonstrare.auth.jwt import create_token
from demonstrare.models.auth import Role, User

log = logging.getLogger(__name__)


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

    try:
        user = request.db_session.query(User).filter_by(google=profile['sub']).one()
    except NoResultFound:
        user = create_user(request.db_session, profile['email'], _google=profile['sub'])
        if user is None:
            raise HTTPNotFound()

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

    try:
        user = request.db_session.query(User).filter_by(facebook=profile['id']).one()
    except NoResultFound:
        user = create_user(request.db_session, profile['email'], _facebook=profile['id'])
        if user is None:
            raise HTTPNotFound()

    token = create_token(user)
    return dict(token=token)


@view_config(route_name='oauth2-live', renderer='json', request_method='POST')
def live(request):
    body = request.body.decode("utf-8")
    body = json.loads(body)

    access_token_url = 'https://login.live.com/oauth20_token.srf'
    profile_url = 'https://apis.live.net/v5.0/me?access_token='
    payload = {
        'client_id': request.json['clientId'],
        'redirect_uri': request.json['redirectUri'],
        'client_secret': request.registry.settings['LIVE_SECRET'],
        'code': body['code'],
        'grant_type': 'authorization_code',
    }

    # Step 1. Exchange authorization code for access token.
    r = requests.post(access_token_url, data=payload)
    token = json.loads(r.text)

    # Step 2. Retrieve information about the current user.
    r = requests.get(profile_url + token['access_token'])
    profile = json.loads(r.text)

    try:
        user = request.db_session.query(User).filter_by(live=profile['id']).one()
    except NoResultFound:
        user = create_user(request.db_session, profile['emails']['account'], _live=profile['id'])
        if user is None:
            raise HTTPNotFound()

    token = create_token(user)
    return dict(token=token)


def create_user(db_session, email, _google=None, _facebook=None, _live=None):
    log.info('Request to create user for email %s', email)
    user = db_session.query(User).filter_by(email=email).one()
    if user is None:
        role = db_session.query(Role).filter_by(is_default=True).one()
        user = User(email, role)
        db_session.add(user)

    if _google is not None:
        user.google = _google
    elif _facebook is not None:
        user.facebook = _facebook
    elif _live is not None:
        user.live = _live

    return user
