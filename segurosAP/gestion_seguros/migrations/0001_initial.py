# Generated by Django 4.2.1 on 2023-06-26 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64, verbose_name='Nombre o Razón Social')),
                ('documento', models.CharField(max_length=16, verbose_name='CUIT/CUIL')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('domicilio_provincia', models.CharField(choices=[('BUE', 'Buenos Aires'), ('SFE', 'Santa Fe'), ('COR', 'Córdoba')], max_length=32, verbose_name='Provincia')),
                ('domicilio_ciudad', models.CharField(max_length=128, verbose_name='Ciudad')),
                ('domicilio_calle', models.CharField(max_length=128, verbose_name='Calle')),
                ('domicilio_numero', models.IntegerField(verbose_name='Número')),
                ('domicilio_depto', models.CharField(blank=True, max_length=128, null=True, verbose_name='Depto')),
                ('telefono', models.CharField(max_length=12, null=True, verbose_name='Teléfono')),
                ('tipo_persona', models.CharField(choices=[('PF', 'Persona Física'), ('PJ', 'Persona Jurídica')], max_length=16, verbose_name='Tipo de persona')),
            ],
        ),
        migrations.CreateModel(
            name='Poliza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(verbose_name='Número de póliza')),
                ('tomador', models.CharField(max_length=128, verbose_name='Tomador')),
                ('limite_asegurados', models.IntegerField(verbose_name='Límite de cantidad de asegurados')),
                ('fecha_inicio', models.DateField(verbose_name='Fecha de inicio cobertura')),
                ('fecha_fin', models.DateField(verbose_name='Fecha de fin cobertura')),
                ('fecha_limite_carga', models.DateField(verbose_name='Fecha límite de actualización de nómina')),
                ('condiciones', models.TextField(max_length=2048, verbose_name='Resumen condiciones de póliza')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_seguros.cliente', verbose_name='Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Asegurado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=64, verbose_name='Apellido')),
                ('documento', models.IntegerField(verbose_name='Documento')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('poliza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_seguros.poliza', verbose_name='Poliza')),
            ],
        ),
    ]
