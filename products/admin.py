from django.contrib.admin.options import ModelAdmin
from django.contrib import admin
from .models import Product, Variation, ProductImage, Category, ProductFeatured, SubCategory

class AdminProduct(ModelAdmin):
    list_display = ('title', 'default', 'price', 'active')

class AdminVariation(ModelAdmin):
    list_display = ('product', 'title', 'active', 'inventory')

class AdminCategory(ModelAdmin):
    list_display = ('title', 'timestamp', 'active')

# Register your models here.
admin.site.register(Category,AdminCategory)
admin.site.register(SubCategory)
admin.site.register(Product, AdminProduct)
admin.site.register(ProductFeatured)
admin.site.register(ProductImage)
admin.site.register(Variation, AdminVariation)
