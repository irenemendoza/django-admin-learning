from django.shortcuts import render#, redirect
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
    template_name = "editorial/Editoriales.html"
    context_object_name = "editoriales"


class EditorialDetailView(DetailView):
    model = Editorial
    template_name = "editorial/EditorialDetail.html"
    context_object_name = "editorial"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Este es mi título añadido como contexto'
        return context


class EditorialCreateView(CreateView):
    model = Editorial
    fields = ["nombre", "email", "fecha_fundacion"]
    template_name = "editorial/EditorialCreate.html"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class EditorialUpdateView(UpdateView):
    model = Editorial
    fields = ["nombre", "email", "fecha_fundacion"]
    template_name = "editorial/EditorialUpdate.html"
    context_object_name = "editorial"


class EditorialDeleteView(DeleteView):
    model = Editorial
    success_url =reverse_lazy('editorial:list')
    context_object_name = "editorial"
    template_name = "editorial/EditorialDelete.html"

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