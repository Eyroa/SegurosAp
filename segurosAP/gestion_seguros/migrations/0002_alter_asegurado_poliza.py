# Generated by Django 4.2.1 on 2023-06-26 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_seguros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asegurado',
            name='poliza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asegurados', to='gestion_seguros.poliza', verbose_name='Poliza'),
        ),
    ]
