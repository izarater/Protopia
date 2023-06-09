# Generated by Django 4.0.4 on 2022-12-07 22:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Oficio',
            fields=[
                ('IdOficio', models.AutoField(primary_key=True, serialize=False)),
                ('NombreOficio', models.CharField(max_length=50, verbose_name='Oficio')),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('IdContacto', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('Telefono', models.CharField(max_length=12, verbose_name='Teléfono')),
                ('Direccion', models.CharField(max_length=100, verbose_name='Dirección')),
                ('Barrio', models.CharField(max_length=100, verbose_name='Barrio')),
                ('Municipio', models.CharField(max_length=100, verbose_name='Municipio')),
                ('xCoor', models.FloatField(verbose_name='Latitud (x)')),
                ('yCoor', models.FloatField(verbose_name='Longitud (y)')),
                ('Ubicación', models.CharField(max_length=100, verbose_name='Nombre')),
                ('Descripcion', models.TextField(verbose_name='Descripción')),
                ('IdCreador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Oficios', models.ManyToManyField(to='complete_form.oficio', verbose_name='Oficio(s)')),
                ('nombresoficios', models.CharField(max_length=300, verbose_name="nombreoficio")),
            ],
        ),
    ]
