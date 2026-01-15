from django import forms
from books.models import Editorial
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit

class EditorialCreate(forms.Form):
    nombre = forms.CharField(
        max_length=200,
        )
    direccion = forms.CharField(
        max_length=300,
        required=False
        )
    ciudad = forms.CharField(
        max_length=100,
        required=False
        )
    estado = forms.CharField(
        max_length=100,
        required=False
        )
    pais = forms.CharField(
        max_length=100,
        required=False
        )
    codigo_postal = forms.CharField(
        max_length=20,
        required=False
        )
    telefono = forms.CharField(
        max_length=20,
        required=False
        )
    email = forms.EmailField(
        required=False
    )
    sitio_web = forms.URLField(
        required=False
    )
    fecha_fundacion = forms.DateField(
        widget = forms.SelectDateWidget
    )


class EditorialModelFormCreate(ModelForm):
    class Meta:
        model = Editorial
        fields = ['nombre', 'email', 'fecha_fundacion', 'level']

   