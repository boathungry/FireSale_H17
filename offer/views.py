import datetime
import json
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from catalog.models import Item
from offer.models import Offer
from user.models import User


def make_offer(request, id):
    if request.method == 'POST':
        item = Item.objects.get(id=id)
        user = User.objects.get(auth=request.user.id)
        try:
            prev_offer = Offer.objects.get(buyerid=user.id, itemid=item.id)
            prev_offer.delete()
        except ObjectDoesNotExist:
            pass
        offer = Offer()
        offer.itemid = item
        request_data = json.loads(request.body)
        offer.amount = int(request_data['amount'])  # get the offer amount from the POST request
        offer.buyerid = user
        offer.datetime = datetime.datetime.now()
        offer.save()
        return redirect(f'/catalog/{id}')


def cancel_offer(request, id):
    if request.method == 'POST':
        Offer.objects.get(id=id).delete()
        return redirect('my_offers')
