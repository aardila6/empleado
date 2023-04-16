from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('home/', views.IndexView.as_view()),
    path('lista/', views.PruebaListView.as_view()),
    path('lista-prueba/', views.ModeloPruebaListView.as_view()),
    path('add/', views.PruebaCreateView.as_view(), name='prueba_add'),
    path(
        'resumenf/',
        views.ResFoundationView.as_view(),
        name='resumenf'
    ),
]
#urlpatterns = [
    # ... the rest of your URLconf goes here ...
#] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)