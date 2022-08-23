from django.shortcuts import render

from AppCoder.models import Familiares

def familia(request):

    familia1 = Familiares(nombre="Federico", edad=36, fecha_de_nacimiento='1987-04-07')
    familia1.save()
    contexto = {
        'familia': familia1
    }

    return render(request, 'curso.html', contexto)