from django.db import models
from django.contrib.auth import get_user_model


class Tweet(models.Model):

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='tweets')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user.email

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Tweet"
        verbose_name_plural = "Tweets"

