import os
from datetime import date

from pyramid.httpexceptions import HTTPBadRequest
from pyramid.response import FileResponse
from pyramid.view import view_config
from sqlalchemy.exc import IntegrityError


@view_config(route_name='home', renderer='templates/index.html')
def index(request):
    return {'year': date.today().year}


@view_config(route_name='robots')
def robots(request):
    here = os.path.abspath(os.path.dirname(__file__))
    response = FileResponse(here + '/../static/robots.txt', request=request)
    return response


@view_config(context=KeyError)
@view_config(context=IntegrityError)
def bad_request(exc, request):
    raise HTTPBadRequest()
