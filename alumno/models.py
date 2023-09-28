
from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    grado = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
