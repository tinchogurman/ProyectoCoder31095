import datetime
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


    return render(request, 'AppCoder/curso.html', contexto)

def entregable(request):
    entregables = [
        {
            'nombre': "",
            'fecha': "",
            'entregado': True
        },
        {
            'nombre': "",
            'fecha': "",
            'entregado': True
        },
        {
            'nombre': "",
            'fecha': "",
            'entregado': True
        },
    ]
    year = 2022
    month = 9
    day = 5
    entregable1 = Entregable(
        nombre="Martín Gurman",
        fecha_de_entrega=datetime.date(year=year, month=month, day=day),  # date year month day
        entregado=True
    )
    entregable1.save()

    contexto = {
        'entregable': entregable1
    }

    return render(request, 'AppCoder/entregable.html', contexto)