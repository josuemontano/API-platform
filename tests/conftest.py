import configparser
import os

import transaction
from alembic import command
from alembic.config import Config
from pyramid import testing

from .fixtures import *

PG_USER = os.environ.get('PGUSER', None)
PG_PASSWORD = os.environ.get('PGPASSWORD', None)


def pytest_addoption(parser):
    parser.addoption(
      '--config', action='store', default='pytest.ini',
      help='.ini configuration used to initialize the application for testing'
    )


@pytest.fixture(scope='session')
def ini_filepath(request):
    """Returns the argument specified by pytest --config=<ini_filepath>"""
    return request.config.getoption('--config')


@pytest.fixture(scope='session')
def ini_config(ini_filepath: str):
    """Returns a ConfigParser object created from ini_filepath"""
    config = configparser.ConfigParser()
    config.read(ini_filepath)

    # Setup database URL for Codeship
    if PG_USER and PG_PASSWORD:
        connection_url = f'postgresql+psycopg2://{PG_USER}:{PG_PASSWORD}@127.0.0.1:5432/test'
        config['app:main']['sqlalchemy.url'] = connection_url
        config['alembic']['sqlalchemy.url'] = connection_url

    return config


@pytest.fixture(scope='session')
def alembic_head(request, ini_filepath: str):
    alembic_config = Config(ini_filepath)

    # Setup database URL for Codeship
    if PG_USER and PG_PASSWORD:
        connection_url = f'postgresql+psycopg2://{PG_USER}:{PG_PASSWORD}@127.0.0.1:5432/test'
        alembic_config.set_main_option('sqlalchemy.url', connection_url)

    command.upgrade(alembic_config, 'head')

    def alembic_base():
        command.downgrade(alembic_config, 'base')

    request.addfinalizer(alembic_base)


@pytest.fixture(scope='class')
def app(request, ini_config, ini_filepath, alembic_head):
    """ returns pyramid app object initialized as a webtest.TestApp object """
    from webtest import TestApp

    global_config = {
        '__file__': ini_filepath,
        'here': 'canopus'
    }

    settings = ini_config['app:main']

    from canopus import main
    app = main(global_config, **settings)
    return TestApp(app)


@pytest.fixture
def dbsession(ini_config, alembic_head):
    """Creates a new database session for a test"""
    settings = ini_config['app:main']
    config = testing.setUp(settings=settings)
    config.include('canopus.models')

    session_factory = config.registry['dbsession_factory']
    session = session_factory()

    yield session

    session.close()
    testing.tearDown()


@pytest.fixture(autouse=True)
def cleanup(dbsession):
    from canopus.models import Post, User

    with transaction.manager:
        dbsession.query(Post).delete()
        dbsession.query(User).delete()
