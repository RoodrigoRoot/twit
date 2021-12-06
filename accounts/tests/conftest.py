import pytest
from pytest_factoryboy import register
from accounts.tests.factories import UserFactory, FollowingFactory


register(UserFactory)
register(FollowingFactory)


@pytest.fixture
def new_user(db, user_factory):
    user = user_factory.create()
    return user


@pytest.fixture
def new_user2(db, user_factory):
    user = user_factory.create()
    return user
