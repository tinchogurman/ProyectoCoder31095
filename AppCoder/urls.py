from django.urls import path
from AppCoder.views import curso, inicio, entregable

urlpatterns = [
    path('', inicio),
    path('curso/', curso, name='AppCoderCurso'),
    path('entregable/', entregable, name='AppCoderCurso')
]
