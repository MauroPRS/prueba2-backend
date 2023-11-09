from django import forms
from firstApp.models import Sala
class Formulario(forms.ModelForm):
    class Meta:
        model=Sala
        fields='__all__'