from canopus.models import User
from canopus.schema import UserSchema
from canopus.tests.factory import UserFactory


class TestUserSchema(object):
    def test_dump(self, user):
        schema = UserSchema()
        result = schema.dump(user)

        assert result.data == {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'role': user.role,
            'phone': user.phone,
            'enabled': True
        }

    def test_load(self, user):
        schema = UserSchema()
        payload = {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'role': user.role,
            'phone': user.phone,
            'enabled': True
        }

        deserialized, errors = schema.load(payload)
        assert errors == {}

        assert isinstance(deserialized, User)
        assert deserialized.id == user.id
        assert deserialized.first_name == user.first_name
        assert deserialized.last_name == user.last_name
        assert deserialized.email == user.email
        assert deserialized.phone == user.phone
        assert deserialized.enabled == True

    def test_load_validation(self, user):
        schema = UserSchema()
        payload = {}

        deserialized, errors = schema.load(payload)

        assert not isinstance(deserialized, User)

        assert len(errors) == 3
        assert errors['first_name']
        assert errors['last_name']
        assert errors['role']


    def test_load_empty_email(self, user):
        schema = UserSchema()
        payload = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'role': user.role
        }

        deserialized, errors = schema.load(payload)
        assert errors == {}

        assert isinstance(deserialized, User)
        assert deserialized.email == None
