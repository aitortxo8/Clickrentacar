from django.db import models


class Vehiculo(models.Model):
    id = models.IntegerField(primary_key=True)
