from operator import truediv
from tkinter import CASCADE
from django.db import models

class Carrera(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    nombre = models.CharField(max_length=100)
    duracion = models.CharField(max_length=100)

class Estudiante(models.Model):
    rut = models.CharField(max_length=8, primary_key=True )
    nombres = models.CharField(max_length=100)
    apellidoPaterno = models.CharField(max_length=100)
    apellidoMaterno = models.CharField(max_length=100)
    fechaNac = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    vigencia = models.CharField(max_length=100)

    
    ###sexo = models.CharField(max_length=1,###choices= sexos, default='F')
    carrera = models.ForeignKey(Carrera, null=False, blank=False, on_delete=models.CASCADE)


    def __str__(self):
        return self.nombres

    

class Curso(models.Model):
    codigo = models.CharField(max_length=100)
    seccion = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    docente = models.CharField(max_length=100)

class Matricula(models.Model):
    codigo = models.CharField(max_length=50, primary_key=True)
    idEstudiante = models.ForeignKey(
        Estudiante,
        on_delete=models.CASCADE
    )
    codigoCurso = models.CharField(max_length=100)
    fechaMatricula = models.CharField(max_length=100)


# Create your models here.
