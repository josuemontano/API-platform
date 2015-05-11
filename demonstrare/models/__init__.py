from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from zope.sqlalchemy import register


def includeme(config):
    """ Add db session to request
        https://metaclassical.com/what-the-zope-transaction-manager-means-to-me-and-you/
    """
    # TODO: Separate session into read-only and writable sessions for scalability (basis
    # http://cjltsod.logdown.com/posts/257665-sqlalchemy-readonly-session-maker-with-pyramid)
    settings = config.get_settings()
    engine = engine_from_config(settings)
    
    maker = sessionmaker()
    register(maker)
    maker.configure(bind=engine)

    config.add_request_method(lambda request: maker(), 'db_session', reify=True)
