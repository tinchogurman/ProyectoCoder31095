from django.db import models

# Create your models here.
class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField(unique=True)

class Estudiante(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(unique=True)

class Profesor(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    profesion = models.CharField(max_length=30)

class Entregable(models.Model):

        nombre = models.CharField(max_length=30)
        fecha_de_entrega = models.DateField()
        entregado = models.BooleanField()