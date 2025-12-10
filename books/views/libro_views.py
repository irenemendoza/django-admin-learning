from django.shortcuts import render

from books.models import Libro

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy


class LibroListView(ListView):
    model = Libro
    template_name = "libro/Libros.html"
    context_object_name = "libros"


class LibroDetailView(DetailView):
    model = Libro
    template_name = "libro/LibroDetail.html"
    context_object_name = "libro"


class LibroCreateView(CreateView):
    model = Libro
    fields = ["titulo", "isbn", "editorial", "precio"]
    template_name = "libro/LibroCreate.html"


class LibroUpdateView(UpdateView):
    model = Libro
    fields = ["titulo", "isbn", "editorial", "precio"]
    template_name = "libro/LibroUpdate.html"
    context_object_name = "libro"


class LibroDeleteView(DeleteView):
    model = Libro
    success_url =reverse_lazy('libro:list')
    context_object_name = "libro"
    template_name = "libro/LibroDelete.html"