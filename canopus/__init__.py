from .config import configure


def main(global_config, **settings):
    application = configure(settings).make_wsgi_app()
    return application
