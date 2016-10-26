from .config import configure


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    application = configure(settings).make_wsgi_app()
    return application
