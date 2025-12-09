# create_data.py
import os
import django

# CONFIGURAR DJANGO
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblioteca.settings')
django.setup()
from books.models import Editorial, Autor, Libro
from datetime import date

# Crear datos
print("Creando datos...")

# Autores
autor1 = Autor.objects.create(
    nombre="Gabriel García Márquez",
    fecha_nacimiento="1927-03-06",
    biografia="Escritor colombiano, premio Nobel de literatura"
)

autor2 = Autor.objects.create(
    nombre="Isabel Allende",
    fecha_nacimiento="1942-08-02",
    biografia="Escritora chilena"
)

# Editorial
editorial = Editorial.objects.create(
    nombre="Penguin Random House",
    pais="España",
    fecha_fundacion="1927-01-01"
)

# Libros
libro1 = Libro.objects.create(
    titulo="Cien años de soledad",
    isbn="9780307474728",
    editorial=editorial,
    fecha_publicacion="1967-06-05"
)
libro1.autores.add(autor1)

libro2 = Libro.objects.create(
    titulo="La casa de los espíritus",
    isbn="9788401242267",
    editorial=editorial,
    fecha_publicacion="1982-01-01"
)
libro2.autores.add(autor2)

print("✅ Datos creados exitosamente!")

# Para crear datos random:
"""
from books.models import Editorial, Autor, Libro
from datetime import date


editoriales = [
    Editorial(
        nombre=f"Editorial {i}",
        direccion=f"Dirección {i}",
        ciudad="Ciudad",
        estado="Estado",
        pais="País",
        codigo_postal=f"0000{i}",
        telefono=f"123456789{i}",
        email=f"editorial{i}@example.com",
        sitio_web=f"http://editorial{i}.com",
        fecha_fundacion=date(2000 + i, 1, 1),
    )
    for i in range(1, 11)
]
Editorial.objects.bulk_create(editoriales)

autores = [
    Autor(
        nombre=f"Nombre {i}",
        apellido=f"Apellido {i}",
        fecha_nacimiento=date(1970 + i, 1, 1),
        nacionalidad="Nacionalidad",
        biografia=f"Biografía del autor {i}",
        email=f"autor{i}@example.com",
        telefono=f"987654321{i}",
        sitio_web=f"http://autor{i}.com",
        premios=f"Premio {i}",
    )
    for i in range(1, 11)
]
Autor.objects.bulk_create(autores)


editoriales = Editorial.objects.all()
autores = Autor.objects.all()

libros = [
    Libro(
        titulo=f"Título del Libro {i}",
        isbn=f"123456789012{i}",
        fecha_publicacion=date(2010 + i, 1, 1),
        numero_paginas=100 + i,
        idioma="Idioma",
        descripcion=f"Descripción del libro {i}",
        editorial=editoriales[i % len(editoriales)],
        genero="Género",
        precio=19.99 + i,
    )
    for i in range(1, 11)
]
Libro.objects.bulk_create(libros)

import random

for libro in Libro.objects.all():
    libro.autores.add(Autor.objects.get(pk=random.randint(1, Autor.objects.count())))
    libro.autores.add(Autor.objects.get(pk=random.randint(1, Autor.objects.count())))
    libro.autores.add(Autor.objects.get(pk=random.randint(1, Autor.objects.count())))
    libro.save()
"""