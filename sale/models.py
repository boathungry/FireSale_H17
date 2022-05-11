from django.db import models
from catalog.models import Item
from user.models import User
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField
from django.core.validators import MaxValueValidator, MinValueValidator


class Sale(models.Model):
    itemid = models.ForeignKey(Item, on_delete=models.CASCADE)
    sellerid = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sellerid')
    buyerid = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buyerid')
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    shipped = models.DateField(blank=True)
    shipping_address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    def __str__(self):
        return f"({self.id}) {self.itemid} sold to {self.buyerid} for {self.price}"


class Payment(models.Model):
    credit_card_name = models.CharField(max_length=255) 
    credit_card_number = CardNumberField(max_length=16)
    expiration_date = CardExpiryField(default=None)
    cvv = SecurityCodeField(default=None)
    address = models.CharField(max_length=255)
    

