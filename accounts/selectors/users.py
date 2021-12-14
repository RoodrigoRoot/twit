from typing import Optional

from accounts.models import User


def get_user_by_id(id: int) -> User:
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        raise Exception("No existe el usuario")
    return user


def get_user(username: str, one_or_row: Optional[bool]=False) -> User:
    try:
        user = User.objects.filter(username=username)
        if one_or_row:
            user = user.first()
    except User.DoesNotExist:
        raise Exception("No existe el usuario")
    return user


def user_exists(username: str) -> bool:
    return User.objects.filter(username=username).exists()


def user_email_exists(email: str) -> bool:
    return User.objects.filter(email=email).exists()

