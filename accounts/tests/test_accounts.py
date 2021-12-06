import pytest
from accounts.models import User


@pytest.mark.django_db
def tests_create_account(user_factory):
    user = user_factory.create()
    count = User.objects.all().count()
    assert count == 1
    assert user.username is not None
    assert user.date_birth is not None





