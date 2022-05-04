from django.db import models
from catalog.models import Item
from user.models import User


class Offer(models.Model):
    datetime = models.DateTimeField()
    amount = models.PositiveIntegerField()
    itemid = models.ForeignKey(Item, on_delete=models.CASCADE)
    buyerid = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.amount} offered on {self.datetime}, buyer id: {self.buyerid}, item id: {self.itemid}"
