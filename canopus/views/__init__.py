import os
from datetime import date

from pyramid.response import FileResponse
from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/index.html')
def index(request):
    return {'year': date.today().year}


@view_config(route_name='robots')
def robots(request):
    here = os.path.abspath(os.path.dirname(__file__))
    response = FileResponse(here + '/../static/robots.txt', request=request)
    return response
