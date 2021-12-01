from accounts.models import User, Following
from accounts.models.exceptions import DoubleFollowException
from accounts.selectors import get_user, following_exists


def following_create(user: User, to_follow: User):
    user = get_user(user, True)
    user_to_follow = get_user(to_follow, True)
    if bool(following_exists(user, user_to_follow)):
        raise DoubleFollowException("Ya lo estas siguiendo")
    following = Following(user=user, to_follow=user_to_follow)
    following.full_clean()
    following.save()
    return following
