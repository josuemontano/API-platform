import factory

from canopus.models import User, Role


class UserFactory(factory.Factory):
    class Meta:
        model = User

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.LazyAttribute(lambda user: '{0}.{1}@example.com'.format(user.first_name, user.last_name).lower())
    phone = factory.Faker('phone_number')
    enabled = True
    role = Role.USER
