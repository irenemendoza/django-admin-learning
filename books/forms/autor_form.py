from books.models import Autor
from django.forms import ModelForm

class AutorModelFormCreate(ModelForm):
    class Meta:
        model = Autor
        fields = [
            'nombre', 
            'nacionalidad',
            'email', 
            'sitio_web',
            ]