from django.contrib.postgres.fields import ArrayField
from django.db import models


# Create your models here.

class Capacitacion(models.Model):
    titulo = models.CharField(max_length=250)
    objetivo = models.CharField(max_length=250)
    informacion_al_publico = models.CharField(max_length=250, help_text="Informacion que se desea publicar")
    anio = models.IntegerField(blank=True, null=True)
    fechas = ArrayField(models.DateTimeField(null=True), blank=True)
    cantidad_Minima_Asistencia = models.IntegerField(blank=True, null=True)
    cantidad_Horas = models.IntegerField(blank=True, null=True)
    lugar = models.CharField(max_length=100, null=True)
    apertura = models.DateTimeField(null=True)
    cierre = models.DateTimeField(null=True)
    observaciones = models.CharField(max_length=250)
    area = models.ManyToManyField('capacitacion.Area', help_text="Seleccione Area para esta Capacitacion")

    def __str__(self):
        return self.titulo


class Area(models.Model):
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre
