from demonstrare.resources.core import PostResource, ProfileResource

from pyramid.config import Configurator


def config_jinja2(config):
    config.include('pyramid_jinja2')
    config.add_renderer('.html', 'pyramid_jinja2.renderer_factory')


def config_routes(config):
    config.add_route('home', '/')
    config.add_route('oauth2-google', '/auth/google')
    config.add_route('oauth2-facebook', '/auth/facebook')
    # REST Resources
    PostResource.add_views(config, '/api/v1/posts/')
    ProfileResource.add_views(config, '/api/v1/profile/')
    config.scan()


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    
    config.include('demonstrare.models')
    config.include('pyramid_jinja2')
    config.add_renderer('.html', 'pyramid_jinja2.renderer_factory')
    config.add_static_view('static', 'static', cache_max_age=3600)
    
    config_routes(config)

    return config.make_wsgi_app()
