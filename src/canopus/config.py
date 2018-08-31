from pyramid.config import Configurator

from .auth import RootFactory


def configure(settings=None):
    config = Configurator(settings=settings, root_factory=RootFactory)

    config.include('cornice')
    config.include('pyramid_jinja2')
    config.commit() # pyramid_jinja2_webpack requires a jinja2 environment
    config.include('pyramid_jinja2_webpack')
    config.include('rollbar.contrib.pyramid')

    config.include('.models')
    config.include('.auth')
    config.include('.routes')

    # Scan everything for configuration
    config.scan()

    return config
