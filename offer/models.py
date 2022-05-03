from django.db import models
from catalog.models import Item
from user.models import User


class Offer(models.Model):
    datetime = models.DateTimeField()
    amount = models.PositiveIntegerField()
    itemid = models.ForeignKey(Item, on_delete=models.CASCADE)
    buyerid = models.ForeignKey(User, on_delete=models.CASCADE)
