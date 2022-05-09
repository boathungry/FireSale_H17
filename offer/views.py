import datetime
import json
from catalog.models import Item
from offer.models import Offer
from user.models import User


def make_offer(request, id):
    if request.method == 'POST':
        item = Item.objects.get(id=id)
        user = User.objects.get(auth=request.user.id)
        offer = Offer()
        offer.itemid = item
        request_data = json.loads(request.body)
        offer.amount = int(request_data['amount'])  # get the offer amount from the POST request
        offer.buyerid = user
        offer.datetime = datetime.datetime.now()
        offer.save()
        return request
