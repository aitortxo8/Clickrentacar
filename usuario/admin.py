from django.contrib import admin
from usuario.models import Administrador
from usuario.models import Ciudad
from usuario.models import Denegacion
from usuario.models import Usuario
from usuario.models import Licencia
from usuario.models import SolicitudRegistro
from usuario.models import PerfilAlquila
from usuario.models import PerfilPropietario

admin.site.register(Administrador)
admin.site.register(Ciudad)
admin.site.register(Denegacion)
admin.site.register(Licencia)
admin.site.register(Usuario)
admin.site.register(SolicitudRegistro)
admin.site.register(PerfilAlquila)
admin.site.register(PerfilPropietario)