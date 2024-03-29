from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    opinion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    