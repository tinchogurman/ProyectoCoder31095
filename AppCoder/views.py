from django.shortcuts import render

from AppCoder.models import Curso

def curso(request):

    curso1 = Curso(nombre="Martin Gurman", camada=36)
    curso1.save()

    contexto = {
        'curso': curso1

    }

    return render(request, 'curso.html', contexto)