from django.db import models


# Create your models here.
class Carrera(models.Model):
    codigo = models.CharField(max_length=5, primary_key=True)
    nombre = models.CharField(max_length=40)
    duracion = models.PositiveSmallIntegerField(default=5)
    class Meta:
        db_table = 'carrera'


class Estudiante(models.Model):
    cedula = models.CharField(max_length=10, primary_key=True)
    appePaterno = models.CharField(max_length=40)
    appeMaterno = models.CharField(max_length=40)
    nombres = models.CharField(max_length=40)
    fechaNacimiento = models.DateField()
    sexo = models.CharField(max_length=10)
    carrera = models.ForeignKey(Carrera, null=False, blank=False, on_delete=models.CASCADE)
    class Meta:
        db_table = 'estudiante'


class Curso(models.Model):
    codigo = models.CharField(max_length=5, primary_key=True)
    nombre = models.CharField(max_length=40)
    docente = models.CharField(max_length=50)
    class Meta:
        db_table = 'curso'


class Matricula(models.Model):
    cedula = models.CharField(max_length=10, primari_key=True)
    estudiante = models.ForeignKey(Estudiante, null=False, blank=False, on_delete=models.CASCADE)
    apePaterno = models.CharField(max_length=40)
    apeMaterno = models.CharField(max_length=40)
    curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    fechaMatricula = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'matricula'
