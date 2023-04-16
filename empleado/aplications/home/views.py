from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Prueba
from .forms import PruebaForm

# Create your views here.

class IndexView(TemplateView):
    template_name = 'home/home.html'

class ResFoundationView(TemplateView):
    template_name = 'home/resfoundation.html'

class PruebaListView(ListView):
    template_name = 'home/lista.html'
    queryset = ['A','B','C']
    context_object_name = 'lista_prueba'

class ModeloPruebaListView(ListView):
    model = Prueba
    template_name = 'home/pruebas.html'
    context_object_name = 'lista_prueba'

class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba
    form_class = PruebaForm
    succes_url = "/"

