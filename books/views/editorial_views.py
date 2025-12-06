from django.shortcuts import render, redirect
from books.forms import EditorialModelFormCreate
from books.models import Editorial

from django.urls import reverse

def editorial_views(request):
    editoriales = Editorial.objects.all()

    context = {
        'editoriales': editoriales
    }

    return render(request, 'editorial/editorial.html', context)

def editorial_detail_views(request, id):
     
    editorial = Editorial.objects.get(pk=id)

    context = {
        'editorial': editorial
    }
    

    return render(request, 'editorial/editorial_detail.html', context)

def editorial_create_views(request):
    if request.POST:
        form = EditorialModelFormCreate(request.POST)
        if form.is_valid():
            nueva_editorial = Editorial.objects.create(
                nombre = form.cleaned_data['nombre'],
                fecha_fundacion = form.cleaned_data['fecha_fundacion']
            )
        return redirect(reverse('books:editorial_detail', kwargs={'id': nueva_editorial.pk}))
            
    else:
        form = EditorialModelFormCreate()
    
    context = {
        'form': form
    }
    return render(request, 'editorial/editorial_create.html', context)