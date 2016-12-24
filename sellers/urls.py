
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

from .views import SellersDashboard

urlpatterns = [
    url(r'^$', SellersDashboard.as_view(), name='dashboard'),
]