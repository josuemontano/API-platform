import json
import requests

from demonstrare.auth.jwt import create_token
from demonstrare.models import User

from pyramid.view import view_config


@view_config(route_name='oauth2-google', renderer='json', request_method='POST')
def oauth2_google(request):
    access_token_url = 'https://accounts.google.com/o/oauth2/token'
    people_api_url = 'https://www.googleapis.com/plus/v1/people/me/openIdConnect'
    # TODO: get client secret from config, GOOGLE_SECRET
    payload = dict(client_id=request.json['clientId'],
                   redirect_uri=request.json['redirectUri'],
                   client_secret='rz2X3aNud-THRric-a6_9udm',
                   code=request.json['code'],
                   grant_type='authorization_code')

    # Step 1. Exchange authorization code for access token.
    r = requests.post(access_token_url, data=payload)
    token = json.loads(r.text)
    headers = {'Authorization': 'Bearer {0}'.format(token['access_token'])}

    # Step 2. Retrieve information about the current user.
    r = requests.get(people_api_url, headers=headers)
    profile = json.loads(r.text)

    user = request.db.query(User).filter_by(google=profile['sub']).first()
    if user:
        token = create_token(user)
        return dict(token=token)
    else:
        error_dict = {'error': 'User not found'}
        request.response.status = 400
        return {'errors': error_dict}
