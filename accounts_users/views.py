from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from orders.mixins import  LoginRequiredMixin
from .forms import ProductInventoryForm
from products.models import Product
from orders.models import UserAdress, UserCheckout
from orders.forms import UserAddressForm
# Create your views here.

class SellersDashboard(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'dashboard/index.html', {})


class UserAddCreateView(CreateView):
    form_class = UserAddressForm
    template_name = 'dashboard/addres_add.html'
    success_url = "/accounts_users/address-list/"

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

class AccountAddress(LoginRequiredMixin, ListView):
    model = UserAdress
    template_name = 'dashboard/address_list.html'

    def get_queryset(self):
        user_check_id = self.request.user.id
        return super(AccountAddress, self).get_queryset().filter(user__user=user_check_id)

class AccountUpdate(LoginRequiredMixin, UpdateView):
    model = UserAdress
    template_name = 'dashboard/address_edit.html'
    fields = ['type', 'street', 'city', 'state', 'zipcode']

    success_url = '/accounts_users/address-list/'

class AccountsAddressDelete(LoginRequiredMixin, DeleteView):
    model = UserAdress
    success_url = '/accounts_users/address-list/'
