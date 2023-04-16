"""empleado URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

app_name = "persona_app"

urlpatterns = [
    path(
            '',
            views.InicioView.as_view(),
            name='inicio'
    ),
    path(
        'listar-todo-empleados/',
        views.ListAllEmpleados.as_view(),
        name='empleados_all'
    ),
    path(
        'lista-by-area/<shortname>',
        views.ListByArea.as_view(),
        name='empleados_area'
    ),
    path(
        'lista-empleados-admin/',
        views.ListEmpleadosAdmin.as_view(),
        name='empleados_admin'
    ),
    path('buscar_empleado/', views.ListEmpleadoByKword.as_view()),
    path('listar_habilidad/', views.ListHabilidadEmpleados.as_view()),
    path(
        'ver-empleado/<pk>',
        views.DetalleEmpleado.as_view(),
        name='empleado_detalle'
    ),
    path(
        'add-empleado/',
        views.EmpleadoCreateView.as_view(),
        name='empleado_add'
    ),
    path(
        'success/',
        views.SuccessView.as_view(),
        name='correcto'
    ),
    path(
            'update-empleado/<pk>',
            views.EmpleadoUpdateView.as_view(),
            name='modificar_empleado'
    ),
    path(
            'delete-empleado/<pk>',
            views.EmpleadoDeleteView.as_view(),
            name='eliminar_empleado'
    ),
                ]