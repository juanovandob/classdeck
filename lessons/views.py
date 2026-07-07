from django.shortcuts import render, get_object_or_404
from .models import Curso, Leccion

def visor_clases(request, id_url=None):
    # Traemos todos los cursos y sus lecciones de forma eficiente
    cursos_disponibles = Curso.objects.prefetch_related('lecciones').all()
    
    if not id_url:
        # Si no hay un tema en la URL, busca la primera lección disponible en la plataforma
        leccion_activa = Leccion.objects.first()
    else:
        leccion_activa = get_object_or_404(Leccion, id_url=id_url)
        
    context = {
        'leccion': leccion_activa,
        'cursos': cursos_disponibles,
    }
    
    return render(request, 'lessons/slide.html', context)


