import factory
from users.models import User


class UserProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'profiles.UserProfile'

    username = factory.Sequence(lambda n: f'user{n}')
    email = factory.Iterator(User.objects.all())
    gender = factory.Faker('boolean')
