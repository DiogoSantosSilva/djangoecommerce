from django.contrib.admin.options import ModelAdmin
from django.contrib import admin
from .models import Cart, CartItem
# Register your models here.

class AdminCart(ModelAdmin):
    list_display = ('id', 'user', 'timestamp', 'updated')


admin.site.register(Cart, AdminCart)

class CartItemAdmin(ModelAdmin):
    list_display = ['cart', 'item', 'quantity']

admin.site.register(CartItem, CartItemAdmin)
