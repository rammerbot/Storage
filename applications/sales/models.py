from django.db import models
from django.forms import model_to_dict

from ..clients.models import Clients
from ..inventory.models import Product
# Create your models here.


class Egress(models.Model):
    shipping_date = models.DateField(max_length=255)
    client = models.ForeignKey(Clients, on_delete=models.SET_NULL , null=True , related_name='clientee')
    total = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    pay = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    comment = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    ticket = models.BooleanField(default=True)
    detail = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=True , null=True)

    class Meta:
        verbose_name='Egreso'
        verbose_name_plural = 'Egresos'
        order_with_respect_to = 'shipping_date'
    
    def __str__(self):
        return str(self.id)
   

class EgressProduct(models.Model):
    egress = models.ForeignKey(Egress, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=2 , null=False)
    price = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    subtotal = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    iva = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    total = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    created = models.DateTimeField(auto_now_add=True)
    delivered = models.BooleanField(default=True)
    returned = models.BooleanField(default=False)

    class Meta:
        verbose_name='Producto egreso'
        verbose_name_plural = 'Productos egreso'
        order_with_respect_to = 'created'
    
    def __str__(self):
        return self.product
    
    def toJSON(self):
        item = model_to_dict(self, exclude=['created'])
        return item