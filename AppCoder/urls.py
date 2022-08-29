from django.urls import path
from AppCoder.views import curso

urlpatterns = [
    path('curso/', curso)
]
