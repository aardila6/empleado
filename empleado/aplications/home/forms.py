from django import forms

from .models import Prueba

class PruebaForm(forms.ModelForm):
    class Meta:
        model = Prueba
        fields = (
            'titulo',
            'subtitulo',
            'cantidad',
        )
        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'placeholder':'Ingrese Texto aqui'
                }
            )
        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad<10:
            raise forms.ValidationError('Ingrese numero mayor que 10')
        return cantidad