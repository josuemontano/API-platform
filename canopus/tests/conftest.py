import pytest
import transaction
from pyramid import testing

from pyramid_jwt.policy import JWTAuthenticationPolicy

from canopus.auth import RootFactory
from canopus.models import User, Post
from canopus.tests.factory import UserFactory


@pytest.yield_fixture
def app_config():
    # TODO: Load settings from .ini file
    settings = {'sqlalchemy.url': 'postgresql+psycopg2://josuemontano:@127.0.0.1:5432/canopus_test'}
    config = testing.setUp(settings=settings)

    config.include('canopus.models')
    config.include('canopus.auth')
    config.set_root_factory(RootFactory)

    yield config
    testing.tearDown()


@pytest.yield_fixture
def dbsession(app_config):
    from canopus.models import get_engine, get_session_factory, get_tm_session

    engine = get_engine(app_config.get_settings())
    session_factory = get_session_factory(engine)
    _session = get_tm_session(session_factory, transaction.manager)

    from canopus.models.meta import Base
    Base.metadata.create_all(engine)

    yield _session

    _session.rollback()
    transaction.abort()
    Base.metadata.drop_all(engine)


@pytest.fixture
def request(dbsession, user):
    policy = JWTAuthenticationPolicy('secret')

    request = testing.DummyRequest(dbsession=dbsession, user=user)
    request.authorization = ('JWT', policy.create_token(user.id))
    request.jwt_claims = policy.get_claims(request)
    return request


@pytest.fixture
def user(dbsession):
    with transaction.manager:
        user = UserFactory()
        dbsession.add(user)

    return dbsession.query(User).first()
