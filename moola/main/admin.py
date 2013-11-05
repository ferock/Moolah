from django.contrib import admin
from models import *

class perfilUsuarioAdmin(admin.ModelAdmin):
	list_display = ('Usuario','Identidad','Ciudad','Pais')

class RemitenteAdmin(admin.ModelAdmin):
	list_display = ('Usuario','Bits','Cuenta','Notificaciones')

class BeneficiarioAdmin(admin.ModelAdmin):
	list_display = ('Usuario','Remitente','Cuenta','Notificaciones')

class ComercioAdmin(admin.ModelAdmin):
	list_display = ('Nombre','Rtn')

class SucursalAdmin(admin.ModelAdmin):
	list_display = ('Nombre','Telefono','Correo','Rtn','Bits')

class UsuarioAfiliadoAdmin(admin.ModelAdmin):
	list_display = ('Sucursal','Usuario','FechaHora','Factura','Monto','StarCoins','Tipo')

admin.site.register(perfilUsuario,perfilUsuarioAdmin)
admin.site.register(Remitente,RemitenteAdmin)
admin.site.register(Beneficiario,BeneficiarioAdmin)
admin.site.register(Comercio,ComercioAdmin)
admin.site.register(Sucursal,SucursalAdmin)
admin.site.register(UsuarioAfiliado,UsuarioAfiliadoAdmin)
admin.site.register(Cuenta)