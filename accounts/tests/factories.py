import factory
from faker import Faker
from accounts.models import User, Following


fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    username = factory.Faker('user_name')
    is_staff = True
    description = fake.text()
    date_birth = str(fake.date())


class FollowingFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Following

    user = factory.SubFactory(UserFactory)
    to_follow = factory.SubFactory(UserFactory)
