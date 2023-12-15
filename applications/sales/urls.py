from django.urls import path
from . import views


app_name = 'sales_app'

urlpatterns = [

    #path('',sales_view, name='sales' ),
    path('sales/',views.add_sales.as_view(), name='sales'),
    path('export/', views.export_pdf_view, name="export_pdf" ),
    path('export/<id>/<iva>', views.export_pdf_view, name="export_pdf" ),
]
