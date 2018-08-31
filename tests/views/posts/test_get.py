import pytest

from tests import factories
from tests.helpers import sign_in


class TestPostViewGET:
    @pytest.fixture(autouse=True)
    def populate_db(self, dbsession):
        posts = factories.PostFactory.build_batch(30)
        dbsession.add_all(posts)
        dbsession.commit()

    def test_forbids_anonymous_users(self, app):
        response = app.get('/api/v1/posts', expect_errors=True)

        assert response.content_type == 'text/plain'
        assert response.status_code == 403

    def test_allows_users(self, app, mocker, user):
        jwt_header = sign_in(mocker, user)
        headers = dict(authorization=jwt_header)
        response = app.get('/api/v1/posts', headers=headers)

        assert response.content_type == 'application/json'
        assert response.status_code == 200

    def test_allows_admins(self, app, mocker, admin):
        jwt_header = sign_in(mocker, admin)
        headers = dict(authorization=jwt_header)
        response = app.get('/api/v1/posts', headers=headers)

        assert response.content_type == 'application/json'
        assert response.status_code == 200
