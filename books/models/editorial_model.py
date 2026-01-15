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
    level_choices = {
        "1": "Nivel 1",
        "2": "Nivel 2",
        "3": "Nivel 3",
    }
        
    level = models.CharField(
        'Nivel',
        max_length=2,
        choices=level_choices, 
        default="1"
        ) 
    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('editorial:detail', kwargs={'pk': self.pk})

