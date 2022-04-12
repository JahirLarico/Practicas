from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from urllib import response
from multiprocessing import context

from pkg_resources import require
from .models import Estudiante

# Create your views here.

def index(request):
    estudiantes=Estudiante.objects.order_by('-pub_date')[:5]
    context={
        'estudiantes':estudiantes
    }
    return render(request,'ejercicio/index.html',context)
def crear(request):
    return render(request,'ejercicio/crear.html')
def guardar(request):
    estudiante=Estudiante()
    estudiante.nombre=request.POST['nombre']
    estudiante.apellido=request.POST['apellidos']
    estudiante.edad=request.POST['edad']
    estudiante.email=request.POST['email']
    estudiante.telefono=request.POST['telefono']
    estudiante.carrera=request.POST['carrera']
    estudiante.save()
    return HttpResponseRedirect("/ejercicio/")
def eliminar(request,estudiante_id):
    estudiantes=get_object_or_404(Estudiante,pk=estudiante_id)
    estudiantes.delete()
    return HttpResponseRedirect("/ejercicio/")
def editar(request,estudiante_id):
    estudiante=get_object_or_404(Estudiante,pk=estudiante_id)
    context={
        'estudiante':estudiante
    }
    return render(request,'ejercicio/modificar.html',context)
def modificar(request,estudiante_id):
    selected_estudiante=Estudiante.objects.get(pk=estudiante_id)
    selected_estudiante.nombre=request.POST['nombre']
    selected_estudiante.apellido=request.POST['apellidos']
    selected_estudiante.edad=request.POST['edad']
    selected_estudiante.email=request.POST['email']
    selected_estudiante.telefono=request.POST['telefono']
    selected_estudiante.carrera=request.POST['carrera']
    selected_estudiante.save()
    return HttpResponseRedirect("/ejercicio/")
def info(request,estudiante_id):
    estudiantes=get_object_or_404(Estudiante, pk=estudiante_id)
    return render(request,'ejercicio/info.html',{'estudiantes':estudiantes})