import django.db.models
import django.core.validators


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