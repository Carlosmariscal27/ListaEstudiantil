from django.shortcuts import render
from datetime import datetime
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from Academico.models import *
from django.urls import reverse_lazy
from Academico.archivos.archivo import *

class Menu_P(TemplateView):
    template_name = 'menu.html'


class Carrera(CreateView):
    model = Carrera
    fields = ['codigo', 'nombre', 'duracion']
    template_name = 'carrera.html'
    success_url = reverse_lazy("menu")


class Estudiante(CreateView):
    model = Estudiante
    fields = ['cedula', 'apellidos', 'nombres', 'genero', 'carrera']
    template_name = 'estudiante.html'
    success_url = reverse_lazy("menu")


class Curso(CreateView):
    model = Curso
    fields = ['codigo', 'estudiante', 'docente']
    template_name = 'curso.html'
    success_url = reverse_lazy("menu")


class Matricula(CreateView):
    model = Matricula
    fields = ['cedula', 'apellidos', 'carrera', 'curso', 'nombre',]
    template_name = 'matricula.html'
    success_url = reverse_lazy("menu")


def login(request):
    ruta = "C:\ListaEstudiantil\datos.txt"
    usu = request.POST.get('user')
    pas = request.POST.get('password')
    arch = Archivo()
    obj = arch.getLogin(usu, pas, ruta)
    if obj is None:
        return render(request, "login.html")
    else :
        if obj.usuario == usu:
            return render(request, "menu.html")








