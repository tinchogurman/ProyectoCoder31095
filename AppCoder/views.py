from django.shortcuts import render

from AppCoder.models import Familiares

def familia(request):

    familia1 = Familiares(nombre="Federico Gurman", edad=36, fecha_de_nacimiento='1987-04-07')
    familia1.save()
    familia2 = Familiares(nombre="Evelyn Gurman", edad=38, fecha_de_nacimiento='1984-01-11')
    familia2.save()
    familia3 = Familiares(nombre="Luis Gurman", edad=45, fecha_de_nacimiento='1977-10-05')
    familia3.save()
    contexto = {
        'familia': familia1,
        'familia2': familia2,
        'familia3': familia3
    }

    return render(request, 'curso.html', contexto)