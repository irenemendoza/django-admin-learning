from django.db import models
from .editorial_model import Editorial
from .autor_model import Autor
from simple_history.models import HistoricalRecords
from django.urls import reverse

# Modelo para Libros
class Libro(models.Model):
    titulo = models.CharField(max_length=300)
    isbn = models.CharField(max_length=13, unique=True)
    fecha_publicacion = models.DateField(
        null = True,
        blank = True
    )
    numero_paginas = models.IntegerField(
        null = True,
        blank = True
    )
    lang_choices = (
        ("ES", "Español"),
        ("EN", "Inglés")
    )
            
    idioma = models.CharField(
        max_length=2,
        choices=lang_choices, 
        default="ES"
        )
    descripcion = models.TextField(
        null = True,
        blank = True
    )
    editorial = models.ForeignKey(
        Editorial, 
        on_delete=models.CASCADE,
        )
    autores = models.ManyToManyField(
        Autor,
        blank = True)
    genero = models.CharField(
        max_length=100,
        null = True,
        blank = True)
    precio = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        null = True,
        blank = True)
    history = HistoricalRecords()

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('libro:detail', kwargs={'pk': self.pk})