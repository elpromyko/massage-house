from django.contrib import admin

from .models import Item, Massage, Masseur


class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'amount']


admin.site.register(Item, ItemAdmin)


class MassageAdmin(admin.ModelAdmin):
    list_display = ['name', 'kind', 'duration', 'price']


admin.site.register(Massage, MassageAdmin)


class MasseurAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname']


admin.site.register(Masseur, MasseurAdmin)
