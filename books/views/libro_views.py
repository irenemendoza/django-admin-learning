from django.shortcuts import render

from books.models import Libro

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

def libro_views(request):
    return render(request, 'libro/libro.html')

class LibroList(ListView):
    model = Libro
    template_name = "libro/libros_ccbv.html"
    context_object_name = "libros"

class LibroDetail(DetailView):
    model = Libro
    template_name = "libro/libro_detail_ccbv.html"
    context_object_name = "libro"

class LibroCreateView(CreateView):
    model = Libro
    fields = ["titulo", "isbn", "editorial", "precio"]
    template_name = "libro/libro_create.html"
    success_url ="/"
