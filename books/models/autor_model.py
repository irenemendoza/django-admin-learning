from django.db import models
from simple_history.models import HistoricalRecords

# Modelo para Autores
class Autor(models.Model):
    nombre = models.CharField(
        max_length=200
        )
    apellido = models.CharField(
        max_length=200
        )
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(
        max_length=100
        )
    biografia = models.TextField()
    email = models.EmailField()
    telefono = models.CharField(
        max_length=20,
        blank=True,
        null=True)
    sitio_web = models.URLField(
        blank=True,
        null=True
    )
    premios = models.TextField(
        blank=True,
        null=True
    )
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'

    def get_absolute_url(self):
        return reverse('books:autor_detail', kwargs={'pk': self.pk})
