from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import UserCheckout, UserAdress, Order

# Register your models here.
admin.site.register(UserCheckout)
admin.site.register(UserAdress)

class OrderAdmin(ModelAdmin):
    list_display = ['id','cart', 'user']

admin.site.register(Order, OrderAdmin)
