from django.db import models
from user.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.id})"


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=510, blank=True)
    buyout = models.PositiveIntegerField()
    catid = models.ForeignKey(Category, on_delete=models.CASCADE)
    sellerid = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.id}), seller id: {self.sellerid}"

