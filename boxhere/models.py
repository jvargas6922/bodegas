from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BodegaTipo(models.Model):
    tipo = models.CharField(max_length=255, unique=True)
    metros = models.PositiveIntegerField()
    quimicos = models.BooleanField(default=False)
    organicos = models.BooleanField(default=False)
    hermetico = models.BooleanField(default=False)
    precio = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.tipo} - {self.metros}m² / ${self.precio}"
    
class Bodega(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    tipo_bodega = models.ForeignKey(BodegaTipo, on_delete=models.CASCADE)
    disponible = models.BooleanField(default=True) #Se agregó disponible de acuerdo al requerimiento, no estaba en el modelo de datos

    def __str__(self):
        return f"{self.tipo_bodega} - {self.codigo}"

class Noticia(models.Model):
    titulo = models.CharField(max_length=45)
    cuerpo = models.TextField()
    imagen_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.titulo

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'noticia')