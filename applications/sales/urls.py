from django.urls import path
from .views import *


app_name = 'sales_app'

urlpatterns = [

    path('',sales_view, name='sales' ),
    #path('', include('applications.product.urls')),
]
