from django.shortcuts import render

# Vistas generales de la aplicación

def autor_views(request):
    return render(request, 'autor/autor.html')