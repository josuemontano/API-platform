from tests import factories


class TestUser:
    def test_name(self):
        user = factories.UserFactory(first_name='John', last_name='Smith')
        assert user.name == "John Smith"
