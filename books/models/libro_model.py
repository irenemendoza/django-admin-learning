from django.db import models
from .editorial_model import Editorial
from .autor_model import Autor
from simple_history.models import HistoricalRecords

# Modelo para Libros
class Libro(models.Model):
    titulo = models.CharField(max_length=300)
    isbn = models.CharField(max_length=13, unique=True)
    fecha_publicacion = models.DateField()
    numero_paginas = models.IntegerField()
    lang_choices = {
        "ES": "Español",
        "EN": "Inglés"
    }
    idioma = models.CharField(
        max_length=2,
        choices=lang_choices, 
        default="ES"
        )
    descripcion = models.TextField()
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    autores = models.ManyToManyField(Autor)
    genero = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    history = HistoricalRecords()

    def __str__(self):
        return self.titulo