from sqlite3 import Cursor
from django.contrib import admin
from.models import (Carrera, Estudiante,Curso,Matricula)
from Academia.models import *
admin.site.register(Carrera)
admin.site.register(Estudiante)
admin.site.register(Curso)

admin.site.register(Matricula)

# Register your models here.
