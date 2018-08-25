from canopus.tests import factories


class TestUser:
    def test_full_name(self):
        user = factories.UserFactory(first_name='John', last_name='Smith')
        assert user.full_name == "John Smith"
