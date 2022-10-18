import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
import django
from django.views.generic import ListView
from AppCoder.forms import CursoFormulario, BusquedaCamadaFormulario
from AppCoder.models import Curso, Entregable


def editar_curso(request, camada):
    curso_editar = Curso.objects.get(camada=camada)


    if request.method == 'POST':
        mi_formulario = CursoFormulario(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            curso_editar.nombre = data.get('nombre')
            curso_editar.camada = data.get('camada')
            try:
                curso_editar.save()
            except django.db.utils.IntegrityError:
                messages.error(request, "la modificacion falló porque la camada está repetida")

            curso_editar.save()

            return redirect('AppCoderCurso')


    contexto = {
        'form': CursoFormulario(
            initial={
                "nombre": curso_editar.nombre,
                "camada": curso_editar.camada
            }
        )
    }

    return render(request, 'AppCoder/curso_formulario.html',contexto)

def eliminar_curso(request, camada):
    curso_eliminar = Curso.objects.get(camada=camada)
    curso_eliminar.delete()

    messages.info(request, f"El curso {curso_eliminar} fue eliminado")

    return redirect("AppCoderCurso")

def busqueda_camada_post(request):

    camada = request.GET.get('camada')

    cursos = Curso.objects.filter(camada__icontains=camada)
    contexto = {
        'cursos': cursos
    }

    return render(request, 'AppCoder/curso_filtrado.html', contexto)



def busqueda_camada(request):

    contexto = {
        'form': BusquedaCamadaFormulario(),
    }

    return render (request, 'AppCoder/busqueda_camada.html', contexto)

def curso_formulario(request):

    if request.method == 'POST':
        mi_formulario = CursoFormulario(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            curso1 = Curso(nombre=data.get('nombre'), camada = data.get('camada'))
            curso1.save()

            return redirect('AppCoderCurso')


    contexto = {
        'form': CursoFormulario()
    }

    return render(request, 'AppCoder/curso_formulario.html', contexto)
def inicio(request):
    return render(request, 'index.html')



class CursoList(LoginRequiredMixin,ListView):
    model = Curso
    template_name = 'AppCoder/curso.html'

@login_required
def curso(request):

    cursos = Curso.objects.all()
    contexto = {
        'cursos': cursos

    }


    return render(request, 'AppCoder/curso.html', contexto)


@login_required
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