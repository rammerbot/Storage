from django.urls import path
from .views import *


app_name = 'inventory_app'

urlpatterns = [

    path('',inventory_view, name='inventory' ),
    path('add_product/', add_product_view, name='add_product'),
    path('delete_product/', delete_product_view, name='delete_product'),
    path('edit_product/', edit_product_view, name='edit_product'),
]
