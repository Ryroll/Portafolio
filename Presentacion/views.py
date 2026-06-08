from django.http import HttpResponse
import django.shortcuts
from .models import (
    Perfil,
    Herramienta,
    Proyecto,
    ExperienciaTrabajo,
    Certificacion,
    Skill
)

# INICIO

def index(request) -> HttpResponse:

    perfil = Perfil.objects.first()

    proyectos_destacados = Proyecto.objects.filter(
        destacado=True
    )[:3]

    context = {
        'perfil': perfil,
        'proyectos': proyectos_destacados,
    }

    return django.shortcuts.render(
        request,
        'index.html',
        context
    )

# PROYECTOS
def proyectos(request) -> HttpResponse:

    proyectos = Proyecto.objects.all().order_by(
        '-fecha_creacion'
    )

    context = {
        'proyectos': proyectos
    }

    return django.shortcuts.render(
        request,
        'proyectos.html',
        context
    )

# EXPERIENCIA
def experiencia(request) -> HttpResponse:

    experiencias = ExperienciaTrabajo.objects.all().order_by(
        '-fecha_inicio'
    )

    context = {
        'experiencias': experiencias
    }

    return django.shortcuts.render(
        request,
        'experiencia.html',
        context
    )

# HERRAMIENTAS
def herramientas(request) -> HttpResponse:

    herramientas = Herramienta.objects.all()

    context = {
        'herramientas': herramientas
    }

    return django.shortcuts.render(
        request,
        'herramientas.html',
        context
    )

# CERTIFICACIONES
def certificaciones(request) -> HttpResponse:

    certificaciones = Certificacion.objects.all().order_by(
        '-fecha'
    )

    context = {
        'certificaciones': certificaciones
    }

    return django.shortcuts.render(
        request,
        'certificaciones.html',
        context
    )

# SOBRE MÍ
def sobre_mi(request) -> HttpResponse:

    perfil = Perfil.objects.first()
    
    skills = Skill.objects.all()

    context = {
        'perfil': perfil,
        'skills': skills
    }

    return django.shortcuts.render(
        request,
        'sobre_mi.html',
        context
    )

# CONTACTO
def contacto(request) -> HttpResponse:

    perfil = Perfil.objects.first()

    context = {
        'perfil': perfil
    }

    return django.shortcuts.render(
        request,
        'contacto.html',
        context
    )