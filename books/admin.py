from django.contrib import admin
from books.models import Autor, Editorial, Libro

# Register your models here.

class LibroInline(admin.StackedInline):
    model = Libro

@admin.register(Autor)
class AutorAdmin (admin.ModelAdmin):
    list_display = ["nombre", "apellido", "fecha_nacimiento", "nacionalidad"]
    ordering = ["nombre"]

@admin.register(Editorial)
class EditorialAdmin (admin.ModelAdmin):
    list_display = ["nombre", "pais"]
    list_filter = ["fecha_fundacion"]
    inlines = [
        LibroInline
    ]


@admin.register(Libro)
class LibroAdmin (admin.ModelAdmin):
    list_display = ["titulo", "fecha_publicacion", "idioma", "editorial", "genero"]
    list_filter = ["editorial", "idioma"]
    search_fields = ["titulo", "autores__nombre"]
    filter_horizontal = ["autores"]