from django.db import models
from user.models import User
from django.core.validators import MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.id})"


class Item(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=510, blank=True)
    buyout = models.FloatField(validators=[MinValueValidator(0.0)])
    catid = models.ForeignKey(Category, on_delete=models.CASCADE)
    sellerid = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    condition = models.CharField(max_length=255)
    offer_accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.id}), Seller: {self.sellerid}"



