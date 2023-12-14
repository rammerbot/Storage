from django.db import models

# Create your models here.


class Clients(models.Model):
    code = models.CharField("Codigo", max_length=50, unique=True)
    name = models.CharField("Nombre", max_length=50)
    last_name = models.CharField("Apellido", max_length=50)
    phone = models.CharField("Telefono", max_length=20, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self) -> str:
        return f"Cliente {self.name} {self.last_name} - Codigo: {self.code}"