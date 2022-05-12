import datetime
import json
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from catalog.models import Item
from offer.models import Offer
from user.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from FireSale import settings


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
        offer.amount = float(request_data['amount'])  # get the offer amount from the POST request
        offer.buyerid = user
        offer.datetime = datetime.datetime.now()
        offer.save()
        send_email(request, offer, 'Offer made')
        return redirect(f'/catalog/{id}')


def cancel_offer(request, id):
    if request.method == 'POST':
        delete_offer(id)
        return redirect('my_offers')


def cancel_offer_itempage(request, id, itemid):
    if request.method == 'POST':
        delete_offer(id)
        return redirect('item_details', itemid)


def delete_offer(offerid):
    Offer.objects.get(id=offerid).delete()


def get_offers_for_item(request, itemid):
    item = Item.objects.get(id=itemid)
    offers = Offer.objects.filter(itemid=item)
    return render(request, 'Offer/offer_list.html', {'offers': offers, 'item': item})


def accept_offer(request, offerid):
    offer = Offer.objects.get(id=offerid)
    offer.accepted = True
    offer.save()
    item = offer.itemid
    item.offer_accepted = True
    item.save()
    send_email(request, offer, 'Offer accepted')
    send_email(request, offer, 'Item sold')
    return render(request, 'Offer/offer_accepted.html')


def send_email(request, offer, message_type):
    message_type_options = {
        'Offer made': f'Dear {offer.buyerid.name.capitalize()},\n\n'
                      f'An offer has been made on your item "{offer.itemid.name}" for the amount: {offer.amount:.2f}.\n\n'
                      f'If you wish to accept the offer, log in to your account and accept.\n\n'
                      f'All the best,\n\n'
                      f'FireSale Team',
        'Offer accepted': f'Dear {offer.buyerid.name.capitalize()}\n'
                          f'Your offer on item "{offer.itemid.name}" for the amount {offer.amount:.2f} has been accepted!\n'
                          f'Please log into your account to finish the checkout process.',
        'Item sold': f'Unfortunately, the item "{offer.itemid.name}" you made an offer on has had another offer '
                     f'accepted.\n'
                     f'Better luck next time!'
    }
    message_name = message_type
    if message_name == 'Item sold':
        buyer_list = Offer.objects.filter(itemid=offer.itemid).exclude(buyerid=offer.buyerid).values_list('buyerid')
        receiver_email = [buyer.email for buyer in buyer_list]
        if receiver_email == [] :
            return
    else:
        receiver_email = [offer.itemid.sellerid.email]
    message = message_type_options[message_type]
    send_mail(
        message_name + f': {offer.itemid.name}',  # subject
        message,  # message
        settings.EMAIL_HOST_USER,  # from email
        receiver_email  # to email
    )
    return HttpResponse("Email notification sent.")
