from accounts.models import Following, User


def following_exists(user: User, to_follow: User):
    return Following.objects.filter(user=user, to_follow=to_follow).exists()



