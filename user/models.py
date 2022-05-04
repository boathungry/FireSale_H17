from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    bio = models.CharField(max_length=510)
    rating = models.PositiveIntegerField()
    image = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.id})"
