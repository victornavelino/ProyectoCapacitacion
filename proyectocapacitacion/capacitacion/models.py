from msilib import CAB

from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.

class Capacitacion(models.Model):
    titulo= models.CharField(max_length=250)
    objetivo = models.CharField(max_length=250)
    informacionAlPublico = models.CharField(max_length=250, help_text="Informacion que se desea publicar")
    anio = models.IntegerField(blank=True, null=True)
    fechas = ArrayField(models.DateTimeField(null=True), blank=True)
    cantidadMinimaAsistencia = models.IntegerField(blank=True, null=True)
    cantidadHoras = models.IntegerField(blank=True, null=True)
    lugar = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.titulo

class Area(models.Model):
    nombre = models.CharField(max_length=250)
    capacitacion = models.ForeignKey('Capacitacion',
        on_delete=models.SET_NULL,
        null=True,
        blank=True)

    def __str__(self):
        return self.nombre