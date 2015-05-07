from demonstrare.resources.core import PostResource

from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from zope.sqlalchemy import register


def config_db(config, settings):
    """ Add db session to request
        https://metaclassical.com/what-the-zope-transaction-manager-means-to-me-and-you/
    """
    engine = engine_from_config(settings, prefix='sqlalchemy.')
    maker = sessionmaker()
    register(maker)
    maker.configure(bind=engine)
    # The reify parameter is used for putting the result of a method after the first call.
    # The function won't call second time ever.
    config.add_request_method(lambda request: maker(), 'db_session', reify=True)


def config_jinja2(config):
    config.include('pyramid_jinja2')
    config.add_renderer('.html', 'pyramid_jinja2.renderer_factory')


def config_routes(config):
    config.add_route('home', '/')
    config.add_route('oauth2-google', '/auth/google')
    config.add_route('oauth2-facebook', '/auth/facebook')
    # REST Resources
    PostResource.add_views(config, '/api/v1/posts/')
    config.scan()


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    
    # TODO: Separate session into read-only and writable sessions for scalability (basis
    # http://cjltsod.logdown.com/posts/257665-sqlalchemy-readonly-session-maker-with-pyramid)
    config_db(config, settings)
    config_jinja2(config)
    config_routes(config)
    config.add_static_view('static', 'static', cache_max_age=3600)

    return config.make_wsgi_app()
