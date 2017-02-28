
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from .views import SellerProductsView, SellerAddView, SellerDetailView, AccountAddress, AccountUpdate, AccountsAddressDelete
from products.views import VariationListView

from .views import SellersDashboard

urlpatterns = [
    url(r'^$', SellersDashboard.as_view(), name='dashboard'),
    url(r'^edit-address/(?P<pk>[0-9]+)/$', AccountUpdate.as_view(), name='address_edit'),
    url(r'^edit-address/(?P<pk>[0-9]+)/delete/$', AccountsAddressDelete.as_view(), name='address_delete'),
    url(r'^address-list/$', AccountAddress.as_view(), name='address_list'),

]
