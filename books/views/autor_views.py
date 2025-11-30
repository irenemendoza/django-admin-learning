from django.shortcuts import render

from books.models import Autor

# Vistas generales de la aplicación

def autor_views(request):

    autores = Autor.objects.all()
    
    context = {
        "autores": autores,
        "titulo": "Pepito"
    }
    return render(request, 'autor/autor.html', context)

def autor_detail(request, id):

    autores = [
        {
            "id": 1, 
            "nombre": "Antonio"
        },
            {
            "id": 2, 
            "nombre": "Felipe"
        },
        {
            "id": 3, 
            "nombre": "Matilde"
        },
    ]
     
    context = {
            "autor": None,
        }
    

    for autor in autores:
        if autor["id"] == id:
              context["autor"] = autor

    return render(request, 'autor/autor_detail.html', context)