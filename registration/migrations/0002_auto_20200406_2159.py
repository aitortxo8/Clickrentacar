# Generated by Django 3.0.3 on 2020-04-07 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='adress',
            field=models.CharField(max_length=50, null=True, verbose_name='calle'),
        ),
        migrations.AddField(
            model_name='profile',
            name='birthDate',
            field=models.DateField(blank=True, null=True, verbose_name='fechaNacimiento'),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(blank=True, max_length=10, null=True, verbose_name='telefono'),
        ),
    ]