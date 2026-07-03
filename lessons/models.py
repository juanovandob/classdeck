from django.db import models

from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre del Curso")
    codigo = models.CharField(max_length=20, blank=True, null=True, verbose_name="Código del Curso")
    
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return self.nombre


class Leccion(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="lecciones", verbose_name="Curso")
    titulo = models.CharField(max_length=200, verbose_name="Tema / Título de la Lección")
    id_url = models.SlugField(max_length=100, unique=True, help_text="ID corto para la URL. Ej: carga-electrica o combinaciones")
    universidad = models.CharField(max_length=200, default="Universidad Mariano Gálvez de Guatemala")
    facultad = models.CharField(max_length=200, default="Facultad de Ingeniería en Sistemas", verbose_name="Facultad / Escuela")

    class Meta:
        verbose_name = "Lección / Tema"
        verbose_name_plural = "Lecciones / Temas"

    def __str__(self):
        return f"[{self.curso.nombre}] {self.titulo}"


class Diapositiva(models.Model):
    leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE, related_name="diapositivas")
    orden = models.PositiveIntegerField(default=1, help_text="Número o posición de la diapositiva (1, 2, 3...)")
    titulo = models.CharField(max_length=200, verbose_name="Título de la Diapositiva")
    contenido = models.TextField(verbose_name="Contenido (Soporta código HTML o texto plano)")
    imagen = models.ImageField(upload_to="diaporamas/", blank=True, null=True, verbose_name="Imagen de soporte (Opcional)")

    class Meta:
        ordering = ['orden']
        verbose_name = "Diapositiva"
        verbose_name_plural = "Diapositivas"

    def __str__(self):
        return f"Diapo {self.orden}: {self.titulo}"
