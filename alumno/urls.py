from django.urls import path
from . import views

urlpatterns = [
    path('listar_alumnos/', views.listar_alumnos, name='listar_alumnos'),
    path('registrar_alumno/', views.registrar_alumno, name='registrar_alumno'),
]
