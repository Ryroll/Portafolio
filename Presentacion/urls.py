from django.urls import path
from . import views

app_name = 'Presentacion'

urlpatterns = [

    path(
        '',
        views.index,
        name='index'
    ),

    path(
        'proyectos/',
        views.proyectos,
        name='proyectos'
    ),

    path(
        'experiencia/',
        views.experiencia,
        name='experiencia'
    ),

    path(
        'herramientas/',
        views.herramientas,
        name='herramientas'
    ),

    path(
        'certificaciones/',
        views.certificaciones,
        name='certificaciones'
    ),

    path(
        'sobre-mi/',
        views.sobre_mi,
        name='sobre_mi'
    ),
    
    path(
        'contacto/',
        views.contacto,
        name='contacto'
    ),
]