# Generated by Django 3.0.4 on 2020-03-14 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cracAPP', '0002_cuenta'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='categoria',
            field=models.CharField(choices=[('auto', 'Auto'), ('camioneta', 'Camioneta'), ('camion', 'Camion'), ('moto', 'Moto')], default='auto', max_length=15),
        ),
    ]