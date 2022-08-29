from django.urls import path
from AppCoder.views import curso, inicio

urlpatterns = [
    path('', inicio),
    path('curso/', curso)
]
