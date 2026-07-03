from django.contrib import admin
from .models import Curso, Leccion, Diapositiva

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo')
    search_fields = ('nombre',)

class DiapositivaInline(admin.StackedInline):
    model = Diapositiva
    extra = 1  # Formulario en blanco listo para rellenar rápido

@admin.register(Leccion)
class LeccionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'curso', 'id_url')
    list_filter = ('curso',)
    search_fields = ('titulo', 'curso__nombre')
    prepopulated_fields = {"id_url": ("titulo",)} # Autocompleta la URL usando el título del tema
    inlines = [DiapositivaInline]

