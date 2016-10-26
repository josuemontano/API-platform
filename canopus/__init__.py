from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.config import Configurator

from .auth.policy import JWTAuthenticationPolicy
from .views.security import groupfinder, RootFactory


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings,
                          authentication_policy=JWTAuthenticationPolicy(callback=groupfinder),
                          authorization_policy=ACLAuthorizationPolicy(),
                          root_factory=RootFactory)

    config.include('.models')
    config.include('.tasks')
    config.include('.mailer')
    config.include('.routes')

    config.include('pyramid_jinja2')
    config.add_renderer('.html', 'pyramid_jinja2.renderer_factory')

    config.scan()

    return config.make_wsgi_app()
