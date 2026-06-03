from django.contrib import admin
from .models import *

#REGISTRO DE MODELOS EN EL ADMINISTRADOR DE DJANGO
admin.site.register(Perfil)
admin.site.register(Herramienta)
admin.site.register(Categoria)
admin.site.register(Proyecto)
admin.site.register(ExperienciaTrabajo)
admin.site.register(Certificacion)
admin.site.register(Skill)