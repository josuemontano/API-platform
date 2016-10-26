from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.config import Configurator

from .auth.policy import JWTAuthenticationPolicy
from .views.security import groupfinder, RootFactory


def configure(settings=None):
    # Actually setup our Pyramid Configurator with the values pulled in from
    # the environment as well as the ones passed in to the configure function.
    config = Configurator(settings=settings,
                          authentication_policy=JWTAuthenticationPolicy(callback=groupfinder),
                          authorization_policy=ACLAuthorizationPolicy(),
                          root_factory=RootFactory)

    config.include('.models')
    config.include('.tasks')
    config.include('.mailer')
    config.include('.routes')

    config.include('pyramid_jinja2')

    # Use Jinja2 for .html templates
    config.add_renderer('.html', 'pyramid_jinja2.renderer_factory')
    # Scan everything for configuration
    config.scan()

    return config
