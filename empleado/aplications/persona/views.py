
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)
# Importo el modelo de Empleados
from .models import Empleado
# forms
from .forms import EmpleadoForm

# Create your views here.

class InicioView(TemplateView):
    """Vista inicial"""
    template_name = 'inicio.html'


class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4
    ordering = 'first_name'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            full_name__icontains=palabra_clave
        )
        return lista

class ListEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado


class ListByArea(ListView):
    """ Lista de empleados por area """
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'
    model = Empleado

    def get_queryset(self):
        """
        EL CODIGO PROPIO PERSONALIZASO
        Return the list of items for this view.
        The return value must be an iterable and may be an instance of
        `QuerySet` in which case `QuerySet` specific behavior will be enabled.
        """
        area = self.kwargs['shortname']
        lista = Empleado.objects.filter(
            departamento__short_name=area
        )
        return lista

class ListEmpleadoByKword(ListView):
    """Lista de Empleados con parámetro de palabras claves o letras"""
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print('***************')
        palabra_clave = self.request.GET.get('kword','')
        lista = Empleado.objects.filter(
            first_name=palabra_clave
        )
        return lista

class ListHabilidadEmpleados(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=1)
        return empleado.habilidades.all()

class DetalleEmpleado(DetailView):
    model = Empleado
    template_name = "persona/detalle_empleado.html"
    
    def get_context_data(self, **kwargs):
        context = super(DetalleEmpleado, self).get_context_data(**kwargs)
        # Lo que le ponemos a hacer, el proceso
        context['titulo'] = 'Empleado del mes'
        return context

class SuccessView(TemplateView):
    template_name = "persona/success.html"

class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = 'persona/add.html'
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:empleados_admin')

    def form_valid(self, form):
        #Logica de codigo
        empleado = form.save(commit = False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView,self).form_valid(form)

class EmpleadoUpdateView(UpdateView):
    template_name = "persona/update.html"
    model = Empleado
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    success_url = reverse_lazy('persona_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print("********METODO POST**********")
        print("=============================")
        print(request.POST)
        print(request.POST['first_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        #Logica de codigo
        print("********METODO FORM VALID**********")
        print("******************************")
        return super(EmpleadoUpdateView,self).form_valid(form)

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:empleados_admin')
            
