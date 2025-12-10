from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Modelo para Editoriales
class Editorial(models.Model):
    nombre = models.CharField(
        max_length=200
        )
    direccion = models.CharField(
        max_length=300,
        blank=True,
        null=True
        )
    ciudad = models.CharField(
        max_length=100,
        blank=True,
        null=True
        )
    estado = models.CharField(
        max_length=100,
        blank=True,
        null=True
        )
    pais = models.CharField(
        max_length=100,
        blank=True,
        null=True
        )
    codigo_postal = models.CharField(
        max_length=20,
        blank=True,
        null=True
        )
    telefono = models.CharField(
        max_length=20,
        blank=True,
        null=True
        )
    email = models.EmailField()
    sitio_web = models.URLField(
        blank=True,
        null=True
    )
    fecha_fundacion = models.DateField()
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('editorial:detail', kwargs={'pk': self.pk})

