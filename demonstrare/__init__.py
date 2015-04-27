from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from sqlalchemy.orm import scoped_session, sessionmaker
from zope.sqlalchemy import ZopeTransactionExtension


def db(request):
    """ Every request will have a session associated with it. If any exception
        happened in requests, session db_write will rollback automatically when cleanup
        https://github.com/Pylons/pyramid_cookbook/blob/master/database/sqlalchemy.rst
    """
    maker = request.registry.dbmaker
    session = maker()

    def cleanup(request):
        try:
            if request.exception is not None:
                session.rollback()
            else:
                session.commit()
        except:
            pass
        session.close()

    request.add_finished_callback(cleanup)
    return session


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    
    engine = engine_from_config(settings, prefix='sqlalchemy.')
    config.registry.dbmaker = scoped_session(sessionmaker(extension=ZopeTransactionExtension(), bind=engine))
    # Add db session to request
    # The reify parameter is used for putting the result of a method after the first call.
    # The function won't call second time ever.
    config.add_request_method(db, reify=True)

    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()

    return config.make_wsgi_app()
