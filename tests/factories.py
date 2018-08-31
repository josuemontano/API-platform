import factory

from canopus.models import Post, User


class PostFactory(factory.Factory):
    class Meta:
        model = Post

    title = factory.Faker('catch_phrase')
    body = factory.Faker('text')


class UserFactory(factory.Factory):
    class Meta:
        model = User

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    phone = factory.Faker('msisdn')
