from django.shortcuts import render, #redirect
#from books.forms import EditorialModelFormCreate
from books.models import Editorial

#from django.urls import reverse

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy


class EditorialListView(ListView):
    model = Editorial
    template_name = "editorial/editoriales_ccbv.html"
    context_object_name = "editoriales"

class EditorialDetailView(DetailView):
    model = Editorial
    template_name = "editorial/editorial_detail_ccbv.html"
    context_object_name = "editorial"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Este es mi título añadido como contexto'
        return context

class EditorialCreateView(CreateView):
    model = Editorial
    fields = ["nombre", "email", "fecha_fundacion"]
    template_name = "editorial/editorial_create.html"


class EditorialUpdateView(UpdateView):
    model = Editorial
    fields = ["nombre", "email", "fecha_fundacion"]
    template_name = "editorial/editorial_update.html"
    context_object_name = "editorial"


class EditorialDeleteView(DeleteView):
    model = Editorial
    success_url =reverse_lazy('books:editorial_list')
    context_object_name = "editorial"
    template_name = "editorial/editorial_delete.html"

"""
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
    """