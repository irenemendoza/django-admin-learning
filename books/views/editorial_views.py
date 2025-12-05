from django.shortcuts import render
from books.forms import EditorialCreate
from books.models import Editorial

def editorial_views(request):
    return render(request, 'editorial/editorial.html')

def editorial_create_views(request):
    if request.POST:
        form = EditorialCreate(request.POST)
        if form.is_valid():
            Editorial.objects.create(
                nombre = form.cleaned_data['nombre'],
                fecha_fundacion = form.cleaned_data['fecha_fundacion']
            )
    else:
        form = EditorialCreate()
    
    context = {
        'form': form
    }
    return render(request, 'editorial/editorial_create.html', context)