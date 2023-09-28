from django.shortcuts import render, redirect
from .models import Alumno
from .forms import AlumnoForm

def listar_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'listar_alumnos.html', {'alumnos': alumnos})

def registrar_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_alumnos')
    else:
        form = AlumnoForm()
    return render(request, 'registrar_alumno.html', {'form': form})

