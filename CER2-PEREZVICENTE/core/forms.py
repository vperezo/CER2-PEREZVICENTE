from django import forms
from django.contrib.auth.forms import AuthenticationForm 
from .models import LugarPatrimonial

class LugarForm(forms.ModelForm):
    class Meta:
        model = LugarPatrimonial
        fields = ['nombre', 'descripcion', 'ubicacion', 'anio_construccion', 'imagen', 'categoria']


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'