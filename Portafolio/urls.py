import django.contrib
import django.conf
import django.conf.urls.static
import django.urls

urlpatterns = [

    django.urls.path('admin/', django.contrib.admin.site.urls),

    # URLs de la app Presentacion
    django.urls.path('', django.urls.include('Presentacion.urls')),

]


# Archivos multimedia en modo DEBUG
if django.conf.settings.DEBUG:

    urlpatterns += django.conf.urls.static.static(
        django.conf.settings.MEDIA_URL,
        document_root=django.conf.settings.MEDIA_ROOT
    )