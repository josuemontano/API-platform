from datetime import date, datetime, timedelta
from freezegun import freeze_time

from canopus.auth import TokenFactory


class TestTokenFactory(object):
    def test_create_access_token(self, mocker, request, user):
        request.create_jwt_token = lambda x, expiration: None
        user.last_signed_in = date.today()
        mock = mocker.patch.object(request, 'create_jwt_token', return_value='token')

        factory = TokenFactory(request, user)
        factory.create_access_token()

        mock.assert_called_once_with(user.id, expiration=timedelta(7))

    def test_create_access_token_set_last_signed_in(self, request, user):
        request.create_jwt_token = lambda x, expiration: None
        user.last_signed_in = date.today() - timedelta(7)

        with freeze_time('2016-10-10'):
            factory = TokenFactory(request, user)
            factory.create_access_token()

            assert user.last_signed_in == datetime(2016, 10, 10)
