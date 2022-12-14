# Generated by Django 4.1.3 on 2022-11-28 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('duracion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=100)),
                ('seccion', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('docente', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('rut', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidoPaterno', models.CharField(max_length=100)),
                ('apellidoMaterno', models.CharField(max_length=100)),
                ('fechaNac', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100)),
                ('vigencia', models.CharField(max_length=100)),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academia.carrera')),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('codigo', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('codigoCurso', models.CharField(max_length=100)),
                ('fechaMatricula', models.CharField(max_length=100)),
                ('idEstudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academia.estudiante')),
            ],
        ),
    ]
