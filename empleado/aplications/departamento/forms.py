from django import forms

class NewDepartamentoForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellidos = forms.CharField(max_length=35)
    departamento = forms.CharField(max_length=30)
    shortname = forms.CharField(max_length=20)

