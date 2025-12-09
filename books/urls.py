from django.urls import path, include

app_name = "books"

urlpatterns = [
    path('editorial/', include('books.urls.editoriales_urls')),
    path('libro/', include('books.urls.libros_urls')),
    path('editorial/', include('books.urls.autores_urls')),
] 

