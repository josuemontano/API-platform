import pytest

from canopus.models import Role
from canopus.tests import factories


@pytest.fixture
def user(dbsession):
    user = factories.UserFactory(role=Role.USER)
    dbsession.add(user)
    dbsession.commit()
    return user


@pytest.fixture
def admin(dbsession):
    user = factories.UserFactory(role=Role.ADMIN)
    dbsession.add(user)
    dbsession.commit()
    return user
