from django.contrib.admin.options import ModelAdmin
from django.contrib import admin
from .models import Cart, CartItem
# Register your models here.

class AdminCart(ModelAdmin):
    list_display = ('id', 'user', 'timestamp', 'updated')


admin.site.register(Cart, AdminCart)
admin.site.register(CartItem)