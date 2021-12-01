from django.db import models
from accounts.models import User
from accounts.models.exceptions import FollowItSelfException


class Following(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers")
    to_follow = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')

    def clean(self):
        if self.user == self.to_follow:
            raise FollowItSelfException('No te puedes seguir a ti mismo')

    def __str__(self) -> str:
        return self.user.username

