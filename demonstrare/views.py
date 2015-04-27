from datetime import date
from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/index.html')
def index(request):
    return {'year': date.today().year}
