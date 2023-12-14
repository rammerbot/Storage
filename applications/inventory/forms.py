from django import forms
from .models import Product

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('code', 'product', 'description', 'image', 'price', 'stock')
        labels ={
            'code':'Codigo de producto: ',
            'product':'Nombre de Producto: ',
            'description': 'Descripcion: ',
            'image':'Imagen: ',
            'price':'Precio: ',
            'stock':'Cantidad'
        }
        
        widget = {
            'description': forms.Textarea(),
            'image': forms.ClearableFileInput()
        }

class EditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product', 'description', 'image', 'price', 'stock')
        labels = {
            'product': 'Producto: ',
            'description':'Detalles: ',
            'image':'Imagen: ',
            'price':'Precio: ',
            'stock':'Inventario: '
        }
        widgets = {
            'product': forms.TextInput(attrs={ 'id':'edit_product'}),
            'description': forms.TextInput(attrs={'id':'edit_description'}),
            'image': forms.ClearableFileInput(attrs={'id':'edit_image'}),
            'price': forms.NumberInput(attrs={'id':'edit_price'}),
            'stock': forms.NumberInput(attrs={'id':'edit_stock'}),
        }