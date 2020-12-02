from django.db import models

# Create your models here.

class Casa(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    m2 = models.FloatField(max_length=10)
    habitaciones = models.IntegerField()
    banhos = models.IntegerField()
    precio = models.FloatField()


class Cliente(models.Model):
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=60)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=100)
