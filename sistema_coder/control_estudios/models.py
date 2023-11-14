from django.db import models

# Create your models here.

class equipo(models.Model):
    
    nombre = models.CharField(max_length=60)
    liga = models.CharField(max_length=60)

class jugador(models.Model):
    
    apellido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True)
    nacionalidad = models.CharField(max_length=100)
    liga = models.CharField(max_length=100)

class estadio(models.Model):
    
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    creacion = models.IntegerField()    
