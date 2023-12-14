from django.db import models

# Create your models here.

class Product(models.Model):
    code = models.CharField("Codigo", max_length=50, unique=True)
    product = models.CharField("Producto", max_length=100)
    description = models.CharField("Descripcion", max_length=255)
    image = models.ImageField("Imagen", upload_to='products')
    price = models.DecimalField("Precio", max_digits=10, decimal_places=2)
    stock = models.IntegerField("Inventario")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return f"{self.product} {self.code}"