import os

import pendulum
from pyramid.response import FileResponse
from pyramid.view import view_config


@view_config(route_name='home', renderer='../templates/home.jinja2')
@view_config(route_name='login', renderer='../templates/home.jinja2')
def login(request):
    settings = request.registry.settings
    google_app_id = settings['google.app_id']
    windows_app_id = settings['windows.app_id']

    return {
        'year': pendulum.today().year,
        'google_app_id': google_app_id,
        'windows_app_id': windows_app_id,
    }


@view_config(name='robots.txt')
def robots(request):
    here = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(here, '..', 'static', 'robots.txt')
    return FileResponse(path, request=request)
