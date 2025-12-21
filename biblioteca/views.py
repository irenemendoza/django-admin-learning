from django.shortcuts import render
from django.contrib import messages
from django.utils.translation import gettext as _
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.utils import translation
from books.models import Autor, Libro, Editorial
from books.forms import SearchForm
from .form import ContactForm


# Vistas generales de la aplicación

def home_view(request):
    messages.info(request, "Este es un mensaje informativo")
    return render(request, 'general/home.html')

# def contact_view(request):
#     if request.POST:
#         nombre = request.POST['nombre']
#         email = request.POST['email']
#         comentario = request.POST['comentario']
#         print(f'Se ha enviado un correo a {nombre} al correo {email} con el texto {comentario}')
#     return render(request, 'general/contact.html')

def search_view(request):

    if request.GET:

        formulario = SearchForm(request.GET)

        busqueda = formulario.data["q"]

        autores = Autor.objects.filter(nombre__icontains=busqueda)
        editoriales = Editorial.objects.filter(nombre__icontains=busqueda)
        libros = Libro.objects.filter(titulo__icontains=busqueda)

        context = {
            "autores": autores,
            "editoriales": editoriales,
            "libros": libros,
            "formulario": formulario,
        }
        return render(request, 'general/search.html', context)
    
    else:
        formulario = SearchForm()

    context = {
        "formulario": formulario
    }
    
    # if request.GET:
    #     busqueda = request.GET["q"]
       

        # autores = Autor.objects.filter(nombre__icontains=busqueda)
        # print(autores)
        # editoriales = Editorial.objects.filter(nombre__icontains=busqueda)
        # libros = Libro.objects.filter(titulo__icontains=busqueda)

        # context = {
        #     "autores": autores,
        #     "editoriales": editoriales,
        #     "libros": libros,
        # }
        # return render(request, 'general/search.html', context)
    return render(request, 'general/search.html', context)

def contact_view(request):
    if request.POST:
        formulario = ContactForm(request.POST)

        if formulario.is_valid():
            nombre = formulario.cleaned_data['nombre']
            email = formulario.cleaned_data['email']
            comentario = formulario.cleaned_data['comentario']
            print(f'Se ha enviado un correo a {nombre} al correo {email} con el texto {comentario}')

            context = {
                "formulario": formulario,
            }
            messages.info(request, _("El correo se ha enviado correctamente"))


            return render(request, 'general/contact.html', context)
        else:
            context = {
                "formulario": formulario
            }
            return render(request, 'general/contact.html', context)
    formulario = ContactForm()
    context = {
        "formulario": formulario
    }
    return render(request, 'general/contact.html', context)

class SetLanguageView(View):
    def post(self, request, *args, **kwargs):
        # Obtenemos el idioma seleccionado del formulario
        language = request.POST.get('language', None)

        # Si se seleccionó un idioma, lo activamos
        if language:
            translation.activate(language)
            
        # Redirigimos a la página desde donde se hizo la petición
        next_url = request.POST.get('next', '/')
        return HttpResponseRedirect(next_url)