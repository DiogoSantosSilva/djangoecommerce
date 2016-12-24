from django.shortcuts import render
from django.views.generic import View
# Create your views here.


class SellersDashboard(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'dashboard/sellers.html', {})