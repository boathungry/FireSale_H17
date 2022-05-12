from django.db import models
from django.contrib.auth.models import User as AuthUser


class User(models.Model):
    name = models.CharField(max_length=255)
    bio = models.CharField(max_length=510)
    rating = models.PositiveIntegerField(default=0)
    image = models.ImageField(null=True, default="static/images/default_pic.jpg")
    email = models.EmailField(max_length=255, blank=True)
    auth = models.ForeignKey(AuthUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.id})"


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviewer")
    rating = models.PositiveIntegerField()
    review = models.CharField(max_length=999)

    def __str__(self):
        return f"{self.rating} stars from {self.reviewer}"
