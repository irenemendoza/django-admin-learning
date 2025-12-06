from django.shortcuts import render, redirect
from books.forms import AutorModelFormCreate
from books.models import Autor

from django.urls import reverse
# Vistas generales de la aplicación

def autor_views(request):

    autores = Autor.objects.all()
    
    context = {
        "autores": autores,
    }
    return render(request, 'autor/autor.html', context)

def autor_detail(request, id):
    
    autor = Autor.objects.get(pk=id)    


    context = {
        'autor': autor
    }
    return render(request, 'autor/autor_detail.html', context)

def autor_create_views(request):
    if request.POST:
        form = AutorModelFormCreate(request.POST)
        if form.is_valid():
            nuevo_autor = Autor.objects.create(
                nombre = form.cleaned_data['nombre'],
                nacionalidad = form.cleaned_data['nacionalidad'],
                email = form.cleaned_data['email'],
                sitio_web = form.cleaned_data['sitio_web'],
            )
        return redirect(reverse('books:autor_detail', kwargs={'id': nuevo_autor.pk}))
            
    else:
        form = AutorModelFormCreate()
    
    context = {
        'form': form
    }
    return render(request, 'autor/autor_create.html', context)