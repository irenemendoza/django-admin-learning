from django import forms


class ContactForm(forms.Form):
    nombre = forms.CharField(
        label="Nombre:", 
        max_length=140)
    email = forms.EmailField(
        label="Email:"
    )
    comentario = forms.CharField(
        label="Comentario:", 
        max_length= 1000,
        widget=forms.Textarea
    )

    def clean_comentario(self):
        comentario = self.cleaned_data.get('comentario')
        if len(comentario)<5:
            raise forms.ValidationError("El comentario debe tener al menos 5 caracteres")
        return comentario
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if "prueba" in email:
            raise forms.ValidationError("El email no parece ser correcto")
        return email