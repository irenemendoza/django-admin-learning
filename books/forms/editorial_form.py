from django import forms

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
