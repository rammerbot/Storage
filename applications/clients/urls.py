from django.urls import path
from .views import *

app_name = 'clients_app'

urlpatterns = [

    path('',clients_view, name='clients' ),
    path('add_client/', add_client_view, name='add_client'),
    path('edit_client/', edit_client_view, name='edit_client'),
     path('delete_client/', delete_client_view, name='delete_client'),
]
