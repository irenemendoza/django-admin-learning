from django.contrib import admin
from books.models import Autor, Editorial, Libro
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor
        fields = ('nombre', 'apellido')
        export_order = ('nombre', 'apellido')

class LibroInline(admin.StackedInline):
    model = Libro

@admin.register(Autor)
class AutorAdmin (ImportExportModelAdmin):
    resource_class = AutorResource
    list_display = ["nombre", "apellido", "fecha_nacimiento", "nacionalidad"]
    ordering = ["nombre"]

@admin.register(Editorial)
class EditorialAdmin (admin.ModelAdmin):
    list_display = ["nombre", "pais"]
    list_filter = ["fecha_fundacion"]
    inlines = [
        LibroInline
    ]


# Definir la acción personalizada
def set_out_of_stock(modeladmin, request, queryset):
    queryset.update(is_out_of_stock=True)
    modeladmin.message_user(request, "Los libros seleccionados han sido marcados como fuera de stock")

# Personalizar el nombre de la acción    
set_out_of_stock.short_description = "Marcar como fuera de stock"


# Definir la acción personalizada para exportar a CSV
def export_books_to_csv(modeladmin, request, queryset):
    import csv
    from django.http import HttpResponse

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment: filename="books.csv"'
    writer = csv.writer(response)
    
    writer.writerow(['Titulo', 'ISBN', 'Fecha de publicación', 'Número de páginas', 'Idioma'])
    for book in queryset:
        writer.writerow([book.titulo, book.isbn, book.fecha_publicacion, book.numero_paginas, book.idioma])
    return response

# Personalizar el nombre de la acción
export_books_to_csv.short_description = "Exportar libros seleccionados a CSV"

@admin.register(Libro)
class LibroAdmin (admin.ModelAdmin):
    list_display = ["titulo", "fecha_publicacion", "idioma", "editorial", "genero", "is_out_of_stock"]
    list_filter = ["editorial", "idioma", "is_out_of_stock"]
    search_fields = ["titulo", "autores__nombre"]
    filter_horizontal = ["autores"]
    actions = [set_out_of_stock, export_books_to_csv, ]

