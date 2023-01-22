from ssl import create_default_context
from django.db import models

# Create your models here.

class Catalogo(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    revista = models.FileField(upload_to = "catalogos/")
    imagen = models.ImageField(upload_to = "catalogos/")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

