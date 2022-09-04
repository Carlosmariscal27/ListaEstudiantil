from django.db import models


# Create your models here.
class Carrera(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=40)
    duracion = models.PositiveSmallIntegerField(default=5)
    class Meta:
        db_table = 'carrera'


class Estudiante(models.Model):
    cedula = models.CharField(max_length=10, primary_key=True)
    apellidos = models.CharField(max_length=40)
    nombres = models.CharField(max_length=40)
    genero = models.CharField(max_length=10)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    class Meta:
        db_table = 'estudiante'


class Curso(models.Model):
    codigoclase = models.CharField(max_length=5, primary_key=True)
    nombreEstudiante = models.CharField(max_length=40)
    nombreDocente = models.CharField(max_length=50)
    class Meta:
        db_table = 'curso'


class Matricula(models.Model):
    cedula = models.CharField(max_length=10, primary_key=True)
    nombre = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    apellidos = models.CharField(max_length=40)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    class Meta:
        db_table = 'matricula'
