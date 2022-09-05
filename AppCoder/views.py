from django.shortcuts import render

from AppCoder.models import Curso, Entregable

def inicio(request):
    return render(request, 'index.html')

def curso(request):

    curso1 = Curso(nombre="Python", camada=31095)
    curso1.save()

    contexto = {
        'curso': curso1

    }

def entregable(request):

    entregable1 = Entregable(nombre="Entregable", fechaDeEntrega="2022-05-09")
    entregable1.save()

    contexto1 = {
        'entregable': entregable1
    }
    return render(request, 'AppCoder/curso.html', contexto1)