# Generated by Django 3.0.4 on 2020-03-24 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehiculo', '0001_initial'),
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolicitudAlquiler',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('fechaSolicitud', models.DateTimeField(auto_now_add=True)),
                ('startDate', models.DateField(blank=True)),
                ('startTime', models.TimeField(blank=True)),
                ('endDate', models.DateField(blank=True)),
                ('endTime', models.TimeField(blank=True)),
                ('costoReserva', models.DecimalField(decimal_places=2, max_digits=6)),
                ('usarioSolicitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.Usuario', verbose_name='Usuario')),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehiculo.Vehiculo', verbose_name='Vehiculo')),
            ],
        ),
        migrations.CreateModel(
            name='RegistroAlquiler',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('startDate', models.DateTimeField(blank=True)),
                ('endDate', models.DateTimeField(blank=True)),
                ('entregaDateReal', models.DateTimeField(blank=True)),
                ('devolucionDateReal', models.DateTimeField()),
                ('costoPorHora', models.DecimalField(decimal_places=2, max_digits=6)),
                ('costoPorHoraRecargo', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=6)),
                ('observaciones', models.CharField(blank=True, max_length=200)),
                ('solicitudAlquiler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alquiler.SolicitudAlquiler', verbose_name='Usuario')),
            ],
        ),
    ]
