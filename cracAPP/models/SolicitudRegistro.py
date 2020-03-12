from django.db import models

from . import cuentaUsuario, cuentaAdministrador, pais, ciudad


class SolicitudRegistro(models.Model):
    id = models.IntegerField(primary_key=True)
    pais = models.ForeignKey(pais.Pais, on_delete=models.CASCADE())
    ciudad = models.ForeignKey(ciudad.Ciudad, on_delete=models.CASCADE)
    ciSolicitante = models.ForeignKey(cuentaUsuario.Usuario, on_delete=models.CASCADE())
    nroSolicitud = models.IntegerField()
    estadoSolicitud = models.TextChoices('Pendiente', 'Aprobada', 'Denegada')
    fechaSolicitud = models.DateField()
    horaSolicitud = models.TimeField()
    aprobador = models.ForeignKey(cuentaAdministrador.Administrador, on_delete=models.CASCADE())
    fechaGestion = models.DateField()
    horaGestion = models.TimeField()
    comentarioAprobador = models.CharField(max_length=100)
