from django.shortcuts import render
from ..inventory.models import Product

# Create your views here.


def sales_view(request):
    products = Product.objects.all()
    context = {"products" : products}

    return render(request,'sales/sales.html', context)