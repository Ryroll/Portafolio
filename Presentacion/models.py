import django.db.models
import django.core.validators
import sys
import io
import django.db.models
import django.core.files.uploadedfile
import PIL


# PERFIL PERSONAL
class Perfil(django.db.models.Model):

    nombre = django.db.models.CharField(
        max_length=100
    )

    descripcion = django.db.models.TextField()

    foto = django.db.models.ImageField(
        upload_to='perfil/',
        null=True,
        blank=True
    )

    github = django.db.models.URLField(
        blank=True
    )

    linkedin = django.db.models.URLField(
        blank=True
    )

    correo = django.db.models.EmailField()

    cv = django.db.models.FileField(
        upload_to='cv/',
        null=True,
        blank=True
    )

    creado = django.db.models.DateTimeField(
        auto_now_add=True
    )

    actualizado = django.db.models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

    def __str__(self):
        return self.nombre
    
    # COMPRESIÓN DINÁMICA DE LA FOTO ANTES DE GUARDAR
    def save(self, *args, **kwargs):
        # Validamos que exista una foto cargada y que sea un archivo nuevo/modificado
        if self.foto and hasattr(self.foto, "file"):
            # Abrimos la imagen desde la memoria RAM usando Pillow
            img = PIL.Image.open(self.foto)

            # Forzamos conversion a RGB para evitar errores de transparencia (ej. sube PNG)
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")

            # Redimensionado para fotos de perfil: Limitamos a un ancho maximo de 600px
            max_width = 600
            if img.width > max_width:
                output_size = (max_width, int((max_width / img.width) * img.height))
                img = img.resize(output_size, PIL.Image.Resampling.LANCZOS)

            # Creamos el contenedor binario temporal en memoria RAM
            output = io.BytesIO()

            # Comprimimos y convertimos nativamente a formato WEBP con calidad del 75%
            img.save(output, format="WEBP", quality=75, optimize=True)
            output.seek(0)

            # Cambiamos la extensión del archivo original a .webp de forma limpia
            nombre_base = self.foto.name.split(".")[0]
            nuevo_nombre_webp = f"{nombre_base}.webp"

            # Reconstruimos el archivo para que Django y Cloudinary lo procesen con normalidad
            self.foto = django.core.files.uploadedfile.InMemoryUploadedFile(
                file=output,
                field_name="ImageField",
                name=nuevo_nombre_webp,
                content_type="image/webp",
                size=sys.getsizeof(output),
                charset=None,
            )

            # Cerramos el objeto Pillow para liberar espacio inmediatamente en el servidor
            img.close()

        # Ejecutamos el guardado original de Django (Guarda datos y envia a Cloudinary en Render)
        super().save(*args, **kwargs)


# HERRAMIENTAS / TECNOLOGÍAS
class Herramienta(django.db.models.Model):

    TIPOS = [
        ('programacion', 'Programación'),
        ('datos', 'Gestión de Datos'),
        ('framework', 'Framework'),
        ('devops', 'DevOps'),
        ('diseno', 'Diseño'),
        ('otros', 'Otros'),
    ]

    NIVELES = [
        ('basico', 'Básico'),
        ('intermedio', 'Intermedio'),
        ('avanzado', 'Avanzado'),
    ]

    nombre = django.db.models.CharField(
        max_length=100
    )

    tipo = django.db.models.CharField(
        max_length=30,
        choices=TIPOS
    )

    descripcion = django.db.models.TextField()

    nivel_dominio = django.db.models.CharField(
        max_length=20,
        choices=NIVELES
    )

    icono = django.db.models.ImageField(
        upload_to='herramientas/',
        null=True,
        blank=True
    )

    creado = django.db.models.DateTimeField(
        auto_now_add=True
    )

    actualizado = django.db.models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Herramienta'
        verbose_name_plural = 'Herramientas'

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):

        if self.icono and hasattr(self.icono, "file"):

            img = PIL.Image.open(self.icono)

            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")


            max_width = 600
            if img.width > max_width:
                output_size = (max_width, int((max_width / img.width) * img.height))
                img = img.resize(output_size, PIL.Image.Resampling.LANCZOS)


            output = io.BytesIO()

            img.save(output, format="WEBP", quality=75, optimize=True)
            output.seek(0)

            nombre_base = self.icono.name.split(".")[0]
            nuevo_nombre_webp = f"{nombre_base}.webp"

            self.icono = django.core.files.uploadedfile.InMemoryUploadedFile(
                file=output,
                field_name="ImageField",
                name=nuevo_nombre_webp,
                content_type="image/webp",
                size=sys.getsizeof(output),
                charset=None,
            )

            img.close()

        super().save(*args, **kwargs)


# CATEGORÍAS DE PROYECTOS
class Categoria(django.db.models.Model):

    nombre = django.db.models.CharField(
        max_length=100
    )

    creado = django.db.models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.nombre


# PROYECTOS
class Proyecto(django.db.models.Model):

    ESTADOS = [
        ('desarrollo', 'En desarrollo'),
        ('completado', 'Completado'),
    ]

    nombre = django.db.models.CharField(
        max_length=100
    )

    slug = django.db.models.SlugField(
        unique=True,
        blank=True,
        null=True
    )

    descripcion = django.db.models.TextField()

    categoria = django.db.models.ForeignKey(
        Categoria,
        on_delete=django.db.models.CASCADE
    )

    imagen = django.db.models.ImageField(
        upload_to='proyectos/',
        null=True,
        blank=True
    )

    github_url = django.db.models.URLField(
        blank=True
    )

    demo_url = django.db.models.URLField(
        blank=True
    )

    estado = django.db.models.CharField(
        max_length=20,
        choices=ESTADOS
    )
    
    destacado = django.db.models.BooleanField(
        default=False
    )

    fecha_creacion = django.db.models.DateField(
        auto_now_add=True
    )

    actualizado = django.db.models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['-fecha_creacion']
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):

        if self.imagen and hasattr(self.imagen, "file"):

            img = PIL.Image.open(self.imagen)

            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")


            max_width = 600
            if img.width > max_width:
                output_size = (max_width, int((max_width / img.width) * img.height))
                img = img.resize(output_size, PIL.Image.Resampling.LANCZOS)


            output = io.BytesIO()

            img.save(output, format="WEBP", quality=75, optimize=True)
            output.seek(0)

            nombre_base = self.imagen.name.split(".")[0]
            nuevo_nombre_webp = f"{nombre_base}.webp"

            self.imagen = django.core.files.uploadedfile.InMemoryUploadedFile(
                file=output,
                field_name="ImageField",
                name=nuevo_nombre_webp,
                content_type="image/webp",
                size=sys.getsizeof(output),
                charset=None,
            )

            img.close()

        super().save(*args, **kwargs)


# EXPERIENCIA LABORAL
class ExperienciaTrabajo(django.db.models.Model):

    empresa = django.db.models.CharField(
        max_length=100
    )

    cargo = django.db.models.CharField(
        max_length=100
    )

    descripcion = django.db.models.TextField()

    fecha_inicio = django.db.models.DateField()

    fecha_fin = django.db.models.DateField(
        null=True,
        blank=True
    )

    logo_empresa = django.db.models.ImageField(
        upload_to='empresas/',
        null=True,
        blank=True
    )

    creado = django.db.models.DateTimeField(
        auto_now_add=True
    )

    actualizado = django.db.models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['-fecha_inicio']
        verbose_name = 'Experiencia Laboral'
        verbose_name_plural = 'Experiencias Laborales'

    def __str__(self):
        return f"{self.cargo} - {self.empresa}"
    
    def save(self, *args, **kwargs):

        if self.logo_empresa and hasattr(self.logo_empresa, "file"):

            img = PIL.Image.open(self.logo_empresa)

            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")


            max_width = 600
            if img.width > max_width:
                output_size = (max_width, int((max_width / img.width) * img.height))
                img = img.resize(output_size, PIL.Image.Resampling.LANCZOS)


            output = io.BytesIO()

            img.save(output, format="WEBP", quality=75, optimize=True)
            output.seek(0)

            nombre_base = self.logo_empresa.name.split(".")[0]
            nuevo_nombre_webp = f"{nombre_base}.webp"

            self.logo_empresa = django.core.files.uploadedfile.InMemoryUploadedFile(
                file=output,
                field_name="ImageField",
                name=nuevo_nombre_webp,
                content_type="image/webp",
                size=sys.getsizeof(output),
                charset=None,
            )

            img.close()

        super().save(*args, **kwargs)



# CERTIFICACIONES
class Certificacion(django.db.models.Model):

    nombre = django.db.models.CharField(
        max_length=100
    )

    institucion = django.db.models.CharField(
        max_length=100
    )

    fecha = django.db.models.DateField()

    descripcion = django.db.models.TextField(
        blank=True
    )

    imagen = django.db.models.ImageField(
        upload_to='certificaciones/',
        null=True,
        blank=True
    )

    url = django.db.models.URLField(
        blank=True
    )

    creado = django.db.models.DateTimeField(
        auto_now_add=True
    )

    actualizado = django.db.models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['-fecha']
        verbose_name = 'Certificación'
        verbose_name_plural = 'Certificaciones'

    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):

        if self.imagen and hasattr(self.imagen, "file"):

            img = PIL.Image.open(self.imagen)

            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")


            max_width = 600
            if img.width > max_width:
                output_size = (max_width, int((max_width / img.width) * img.height))
                img = img.resize(output_size, PIL.Image.Resampling.LANCZOS)


            output = io.BytesIO()

            img.save(output, format="WEBP", quality=75, optimize=True)
            output.seek(0)

            nombre_base = self.imagen.name.split(".")[0]
            nuevo_nombre_webp = f"{nombre_base}.webp"

            self.imagen = django.core.files.uploadedfile.InMemoryUploadedFile(
                file=output,
                field_name="ImageField",
                name=nuevo_nombre_webp,
                content_type="image/webp",
                size=sys.getsizeof(output),
                charset=None,
            )

            img.close()

        super().save(*args, **kwargs)


# SKILLS BLANDAS
class Skill(django.db.models.Model):

    nombre = django.db.models.CharField(
        max_length=100
    )

    porcentaje = django.db.models.IntegerField(
        validators=[
            django.core.validators.MinValueValidator(0),
            django.core.validators.MaxValueValidator(100)
        ]
    )

    creado = django.db.models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['-porcentaje']
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.nombre