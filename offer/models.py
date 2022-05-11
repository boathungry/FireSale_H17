from django.db import models
from catalog.models import Item
from user.models import User
from django.core.validators import MinValueValidator


class Offer(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField(validators=[MinValueValidator(0.0)])
    itemid = models.ForeignKey(Item, on_delete=models.CASCADE)
    buyerid = models.ForeignKey(User, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"({self.id}) {self.amount} offered on {self.datetime}, Buyer: {self.buyerid}, Item: {self.itemid}"
