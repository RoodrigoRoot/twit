from accounts.models import User
from typing import Union

from accounts.selectors import get_user


def user_create(data: dict) -> User:
    data.pop('password2')
    user = User(**data)
    user.full_clean()
    user.save()
    return user


def user_delete(username: str) -> Union[bool, str]:
    user = get_user(username)
    if user:
        user.delete()
        return True, "Usuario eliminado"
    return False, "No se pudo eleminar al usuario"


def user_update(username: str, data: dict) -> User:

    user = get_user(username)

    user.update(username=data["username"], first_name=data["first_name"], last_name=data["last_name"],
                description=data["description"])
    return user
