from django.test import TestCase

from AppCoder.models import Curso


class CursoTestCase(TestCase):
    def setUp(self):
        Curso.objects.create(nombre="Python1", camada=1)
        Curso.objects.create(nombre="Python2", camada=2)

    def test_animals_can_speak(self):
        p1 = Curso.objects.get(camada=1)
        p2 = Curso.objects.get(camada=2)
        self.assertEqual(p1.nombre, 'Python1')
        self.assertEqual(p2.nombre, 'Python2')
