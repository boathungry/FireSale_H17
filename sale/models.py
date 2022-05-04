from django.db import models
from catalog.models import Item
from user.models import User


class Sale(models.Model):
    itemid = models.ForeignKey(Item, on_delete=models.CASCADE)
    sellerid = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sellerid')
    buyerid = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buyerid')
    price = models.PositiveIntegerField()
    shipped = models.DateField(blank=True)
    shipping_address = models.CharField(max_length=255)

    def __str__(self):
        return f"Item {self.itemid} sold to user {self.buyerid} for {self.price}"
