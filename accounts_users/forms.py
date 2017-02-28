from django import forms

from django.forms.models import modelformset_factory

from products.models import Product

class ProductInventoryForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("__all__")
