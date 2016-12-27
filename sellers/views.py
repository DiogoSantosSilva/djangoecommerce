from django.shortcuts import render
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from .forms import ProductInventoryForm
from products.models import Product
# Create your views here.

class SellersDashboard(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'dashboard/sellers.html', {})


class SellerProductsView(ListView):
    model = Product
    template_name = 'dashboard/products_list.html'

class SellerDetailView(DetailView):
    model = Product
    template_name = 'dashboard/product_detail.html'

class SellerAddView(CreateView):
    model = Product
    template_name = 'dashboard/add_product.html'
    form_class = ProductInventoryForm
    success_url = ("{% products:list %}")