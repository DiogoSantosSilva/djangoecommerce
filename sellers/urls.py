
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from .views import SellerProductsView, SellerAddView, SellerDetailView
from products.views import VariationListView

from .views import SellersDashboard

urlpatterns = [
    url(r'^$', SellersDashboard.as_view(), name='dashboard'),
    url(r'^products/$', SellerProductsView.as_view(), name='list'),
    url(r'^products/(?P<pk>[0-9]+)/$', SellerDetailView.as_view(), name='detail'),
    url(r'^products/(?P<pk>[0-9]+)/inventory/$', VariationListView.as_view(), name='seller_inventory'),
    url(r'^add/$', SellerAddView.as_view(), name='add_product')

]