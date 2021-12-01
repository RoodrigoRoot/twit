from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    description = models.TextField(blank=True, null=True)
    date_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username

    @property
    def followers_count(self) -> int:
        return self.followers.all().count()



