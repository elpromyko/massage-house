from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render
from .models import Item, Client, Rating
from django.db.models import Avg


def index(request):
    items = Item.objects.exclude(amount=0)
    clients = Client.objects.filter(favorites__name='Jan', favorites__surname='Kowalski')
    masseur_rates = Rating.objects.filter(masseur__name='Jan', masseur__surname='Kowalski').aggregate(Avg('rate'))

    return render(request, 'massage/index.html', {'items': items,
                                                  'clients': clients,
                                                  'masseur_rates': masseur_rates['rate__avg']})


def item_detail(request, id):
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        raise Http404('This item does not exist')
    return render(request, 'massage/item_detail.html', {'item': item})
