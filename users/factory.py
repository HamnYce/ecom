import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'users.User'

    email = factory.Sequence(lambda n: f'person{n}@example.com')
    has_profile = False
    password = factory.Faker('ean')
