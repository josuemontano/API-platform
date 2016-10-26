from pyramid.config import Configurator

from .auth import RootFactory


def configure(settings=None):
    # Actually setup our Pyramid Configurator with the values pulled in from
    # the environment as well as the ones passed in to the configure function.
    config = Configurator(settings=settings, root_factory=RootFactory)

    config.include('.auth')
    config.include('.models')
    config.include('.tasks')
    config.include('.mailer')
    config.include('.routes')

    config.include('pyramid_jinja2')
    config.include('rollbar.contrib.pyramid')

    # Use Jinja2 for .html templates
    config.add_renderer('.html', 'pyramid_jinja2.renderer_factory')
    # Scan everything for configuration
    config.scan()

    return config
