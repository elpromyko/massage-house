from django.contrib import admin

from .models import Item, Massage, Masseur, Client, Rating, Address, Order


class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'amount']


admin.site.register(Item, ItemAdmin)


class MassageAdmin(admin.ModelAdmin):
    list_display = ['name', 'kind', 'duration', 'price']


admin.site.register(Massage, MassageAdmin)


class MasseurAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'gender']


admin.site.register(Masseur, MasseurAdmin)


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname']


admin.site.register(Client, ClientAdmin)


class RatingAdmin(admin.ModelAdmin):
    list_display = ['rate', 'masseur']


admin.site.register(Rating, RatingAdmin)


class AddressAdmin(admin.ModelAdmin):
    list_display = ['street_name', 'city']


admin.site.register(Address, AddressAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'massage', 'masseur']


admin.site.register(Order, OrderAdmin)
