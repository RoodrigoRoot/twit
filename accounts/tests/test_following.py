import pytest
from accounts.models import Following, User
from faker import Faker

from accounts.models.exceptions import DoubleFollowException
from accounts.services import following_create

fake = Faker()


@pytest.mark.django_db
def tests_create_following_succesfully(following_factory):
    follow = following_factory
    follow.create()
    count = Following.objects.all().count()
    assert count == 1


@pytest.mark.django_db
def tests_create_following_fail_does_not_follow_your_self():
    user = User.objects.last()
    with pytest.raises(Exception):
        following_create(
            user=user,
            to_follow=user
        )


@pytest.mark.django_db
def tests_create_following_fail_following_already_exists(following_factory):
    follow = following_factory.create()
    with pytest.raises(DoubleFollowException):
        following_create(follow.user, follow.to_follow)
