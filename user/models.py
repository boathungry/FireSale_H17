from django.db import models
from django.contrib.auth.models import User as AuthUser


class User(models.Model):
    name = models.CharField(max_length=255)
    bio = models.CharField(max_length=510)
    rating = models.PositiveIntegerField(default=0)
    image = models.ImageField(default="default_pic.img", upload_to='profile_pics')
    email = models.EmailField(max_length=255, blank=True)
    auth = models.ForeignKey(AuthUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.id})"