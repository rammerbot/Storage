from django.shortcuts import render, redirect
from .models import Product
from .forms import AddProductForm, EditProductForm
from django.contrib import messages

# Create your views here.

def inventory_view(request):
    products = Product.objects.all()
    add_product_form = AddProductForm
    edit_product_form = EditProductForm

    context = {
        'products':products,
        'add_product_form':add_product_form,
        'edit_product_form':edit_product_form
    }
    return render(request, 'inventory/inventory.html', context)

def add_product_view(request):
    if request.POST:
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid:
            try:
                form.save()
            except:
                messages(request, "Error al agregar el Producto nuevo")
                return redirect('inventory_app:inventory')
        else:
            messages(request, "Error al agregar el Producto nuevo")
            return redirect('inventory_app:inventory')
    return redirect('inventory_app:inventory')

def edit_product_view(request):
    if request.POST:
        product = Product.objects.get(pk=request.POST.get('edit_product_id'))
        form = EditProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid:
            try:
                form.save()
            except:
                messages(request, "Error al agregar el producto nuevo")
                return redirect('inventory_app:inventory')

    return redirect('inventory_app:inventory')


def delete_product_view(request):
    
    if request.POST:
        client = Product.objects.get(pk=request.POST.get('delete_product_id'))
        client.delete()

    return redirect('inventory_app:inventory')