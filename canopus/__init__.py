from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.config import Configurator

from .auth.policy import JWTAuthenticationPolicy
from .views.security import groupfinder, RootFactory


def config_routes(config):
    """
    Add home, auth routes and RESTful routes

    :param config: The pyramid ``Configurator`` object for your app.
    :type config: ``pyramid.config.Configurator``
    """
    config.add_route('home', '/')
    config.add_route('oauth2-google', '/auth/google')
    config.add_route('oauth2-facebook', '/auth/facebook')
    config.add_route('oauth2-live', '/auth/live')
    # REST Resources
    config.add_route('posts', '/api/v1/posts')
    config.add_route('post', '/api/v1/posts/{id}')

    config.scan()


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
    config.include('pyramid_jinja2')

    config.add_renderer('.html', 'pyramid_jinja2.renderer_factory')
    config.add_static_view('static', 'static', cache_max_age=3600)

    config_routes(config)

    return config.make_wsgi_app()
