from django.db import models

# Create your models here.

class Capacitacion(models.Model):
    titulo= models.CharField(max_length=250)
    objetivo = models.CharField(max_length=250)
    informacionAlPublico = models.CharField(max_length=250)
    anio = models.IntegerField()


def __str__(self):
    return self.titulo