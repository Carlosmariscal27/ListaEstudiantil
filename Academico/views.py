from django.shortcuts import render
from datetime import datetime
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from Academico.models import *
from django.urls import reverse_lazy

class Carrera(TemplateView):
    model = Carrera
    fieds = ['codigo', 'nombre', 'duracion']
    template_name = "carrera.html"

class Estudiante(CreateView):
    model = Estudiante
    fields = ['cedula', 'nombre', 'apellido','direccion','telefono']
    template_name = "estudiante.html"
    success_url = reverse_lazy("estudiante.html")

class Curso(CreateView):
    model = Curso
    fields = ['codigo', 'nombre' ,'docente']
    template_name = "curso.html"
    success_url = reverse_lazy("curso.html")

class Matricula(CreateView):
    model = Matricula
    fields = ['cedula', 'estudiante', 'apePaterno','apeMaterno', 'curso', 'fechaMatricula']
    template_name = "matricula.html"
    success_url = reverse_lazy("matricula.html")
