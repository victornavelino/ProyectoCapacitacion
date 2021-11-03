from django.db import models

# Create your models here.

class Area(models.Model):
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre