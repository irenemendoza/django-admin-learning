from django.shortcuts import render#, redirect
# from books.forms import AutorModelFormCreate
from books.models import Autor

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy


class AutorListView(ListView):
    model = Autor
    template_name = "autor/Autores.html"
    context_object_name = "autores"


class AutorDetailView(DetailView):
    model = Autor
    template_name = "autor/AutorDetail.html"
    context_object_name = "autor"


class AutorCreateView(CreateView):
    model = Autor
    fields = ["nombre", "apellido", "fecha_nacimiento", "nacionalidad", "biografia", "email"]
    template_name = "autor/AutorCreate.html"


class AutorUpdateView(UpdateView):
    model = Autor
    fields = ["nombre", "apellido", "fecha_nacimiento", "nacionalidad", "biografia", "email"]
    template_name = "autor/AutorUpdate.html"
    context_object_name = "autor"


class AutorDeleteView(DeleteView):
    model = Autor
    success_url =reverse_lazy('autor:list')
    context_object_name = "autor"
    template_name = "autor/AutorDelete.html"
    
"""
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
    """