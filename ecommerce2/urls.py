from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from carts.views import CartView, ItemCountView, CheckOutView, CheckOutFinalView
from orders.views import AddressSelectFormView, UserAdressCreateView, OrdersList, OrderDetailView


urlpatterns = [
    # Examples:
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^contact/$', 'newsletter.views.contact', name='contact'),
    url(r'^about/$', 'ecommerce2.views.about', name='about'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^products/', include('products.urls')),
    url(r'^categories/', include('products.urls_categories')),

    url(r'^orders/$', OrdersList.as_view(), name='order_list'),
    url(r'^orders/(?P<pk>\d+)/$', OrderDetailView.as_view(), name='order_detail'),

    url(r'^cart/$', CartView.as_view(), name='cart'),
    url(r'^cart/count/$', ItemCountView.as_view(), name='item_count'),

    url(r'^checkout/$', CheckOutView.as_view(), name='checkout'),
    url(r'^checkout/address/$', AddressSelectFormView.as_view(), name='order_address'),
    url(r'^checkout/address/add/$',UserAdressCreateView.as_view(), name='user_address_create'),
    url(r'^checkout/final/$', CheckOutFinalView.as_view(), name='checkout_final'),


    url(r'^seller/', include('sellers.urls', namespace='sellers')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
