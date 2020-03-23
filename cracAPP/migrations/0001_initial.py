# Generated by Django 3.0.4 on 2020-03-23 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombreUsuario', models.CharField(max_length=30, unique=True)),
                ('contrasenia', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('mail', models.EmailField(max_length=50, unique=True)),
                ('telefono', models.IntegerField(verbose_name=20)),
                ('antiguedad', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('ciudad', models.CharField(max_length=30)),
                ('pais', models.CharField(
                    choices=[('UY', 'Uruguay'), ('AR', 'Argentina'), ('BR', 'Brasil'), ('CL', 'Chile'),
                             ('BO', 'Bolivia'), ('CO', 'Colombia'), ('EC', 'Ecuador'), ('PY', 'Paraguay'),
                             ('PE', 'Perú'), ('VE', 'Venezuela')], default='UY', max_length=2)),
            ],
            options={
                'unique_together': {('ciudad', 'pais')},
            },
        ),
        migrations.CreateModel(
            name='Licencia',
            fields=[
                ('idLicencia', models.IntegerField(primary_key=True, serialize=False)),
                ('catA', models.BooleanField(default=False)),
                ('catB', models.BooleanField(default=False)),
                ('catC', models.BooleanField(default=False)),
                ('catD', models.BooleanField(default=False)),
                ('catE', models.BooleanField(default=False)),
                ('catF', models.BooleanField(default=False)),
                ('catG1', models.BooleanField(default=False)),
                ('catG2', models.BooleanField(default=False)),
                ('catG3', models.BooleanField(default=False)),
                ('catH', models.BooleanField(default=False)),
                ('vencimiento', models.DateField()),
                ('restricciones', models.IntegerField(blank=True, verbose_name=2)),
                ('observaciones', models.CharField(blank=True, max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('ci', models.IntegerField(primary_key=True, serialize=False)),
                ('nombreUsuario', models.CharField(max_length=30, unique=True)),
                ('contrasenia', models.CharField(max_length=30)),
                ('mail', models.EmailField(max_length=50, unique=True)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('telefono', models.IntegerField(verbose_name=20)),
                ('fechaNacimiento', models.DateField()),
                ('calle', models.CharField(max_length=50)),
                ('esquina', models.CharField(max_length=50)),
                ('numDireccion', models.IntegerField(verbose_name=4)),
                ('bizz', models.IntegerField(verbose_name=4)),
                ('antiguedad', models.DateField(auto_now_add=True)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cracAPP.Ciudad')),
                ('libretaConducir',
                 models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Licencia',
                                      to='cracAPP.Licencia')),
            ],
            options={
                'unique_together': {('nombre', 'apellido')},
            },
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('matricula', models.CharField(max_length=12, unique=True)),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=15)),
                ('anio', models.IntegerField(blank=True, default=1900)),
                ('asientos', models.IntegerField(blank=True, verbose_name=2)),
                ('puertas', models.IntegerField(blank=True, verbose_name=2)),
                ('categoria', models.CharField(
                    choices=[('auto', 'Auto'), ('camioneta', 'Camioneta'), ('camion', 'Camion'), ('moto', 'Moto')],
                    default='auto', max_length=15)),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cracAPP.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='VehiculoPapeles',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('documentacion', models.CharField(max_length=200)),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cracAPP.Vehiculo')),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudRegistro',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('estadoSolicitud',
                 models.CharField(choices=[('PEN', 'Pendiente'), ('APR', 'Aprobada'), ('DEN', 'Denegada')],
                                  default='PEN', max_length=3)),
                ('fechaSolicitud', models.DateField(auto_now_add=True)),
                ('horaSolicitud', models.TimeField(auto_now_add=True)),
                ('fechaGestion', models.DateField(blank=True)),
                ('horaGestion', models.TimeField(blank=True)),
                ('comentarioAprobador', models.CharField(max_length=100)),
                ('aprobador',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cracAPP.Administrador')),
                ('usuarioSolicitante',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cracAPP.Usuario')),
            ],
        ),
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
                ('usarioSolicitante',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cracAPP.Usuario')),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cracAPP.Vehiculo')),
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
                ('tramiteSolicitud',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cracAPP.SolicitudAlquiler')),
            ],
        ),
        migrations.CreateModel(
            name='PerfilPropietario',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('cuenta', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cracAPP.Usuario')),
                ('solicitud',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cracAPP.SolicitudRegistro')),
            ],
        ),
        migrations.CreateModel(
            name='PerfilAlquila',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('cuenta', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cracAPP.Usuario')),
                ('libreta', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cracAPP.Licencia')),
                ('solicitud',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cracAPP.SolicitudRegistro')),
            ],
        ),
        migrations.AddField(
            model_name='licencia',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Titular',
                                       to='cracAPP.Usuario'),
        ),
        migrations.CreateModel(
            name='Denegacion',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('comentarioDenegacion', models.CharField(max_length=100)),
                ('fechaDenegacion', models.DateTimeField(auto_now_add=True)),
                ('adminDenegador',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Administrador',
                                   to='cracAPP.Administrador')),
                ('solicitudDenegada',
                 models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Solicitud',
                                      to='cracAPP.SolicitudRegistro')),
                ('usuarioSolicitante',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Solicitante',
                                   to='cracAPP.Usuario')),
            ],
        ),
        migrations.AddField(
            model_name='administrador',
            name='ciudad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cracAPP.Ciudad'),
        ),
    ]
