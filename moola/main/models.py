from django.db import models
from django.contrib.auth.models import User

class perfilUsuario(models.Model):
    class Meta:
        verbose_name = ('perfilUsuario')
        verbose_name_plural = ('perfilesUsuarios')

    Usuario = models.ForeignKey(User)
    Identidad = models.CharField(max_length=50)
    Ciudad = models.CharField(max_length=40)
    Pais = models.CharField(max_length=40)
    Nacimiento = models.DateField(auto_now_add=False,auto_now=False)
    Telefono = models.CharField(max_length=15)
    Direccion = models.CharField(max_length=40)

    def __unicode__(self):
        return self.Identidad

class Cuenta(models.Model):
    class Meta:
	   verbose_name = ('Cuenta')
	   verbose_name_plural = ('Cuentas')

    Token = models.CharField(max_length=40)

    def __unicode__(self):
        return self.Token

class Remitente(models.Model):
    class Meta:
    	verbose_name = ('Remitente')
    	verbose_name_plural = ('Remitentes')

    Usuario = models.ForeignKey(User)
    Bits = models.IntegerField()
    Cuenta = models.ForeignKey(Cuenta)
    Notificaciones = models.CharField(max_length=30,choices=(('email','Email'),('sms','SMS')))

class Beneficiario(models.Model):
	class Meta:
		verbose_name = ('Beneficiario')
		verbose_name_plural = ('Beneficiarios')

	Usuario = models.ForeignKey(User)
	Remitente = models.ForeignKey(Remitente)
	Cuenta = models.ForeignKey(Cuenta)
	Bits = models.IntegerField()
	Notificaciones = models.CharField(max_length=30,choices=(('email','Email'),('sms','SMS')))


class Comercio(models.Model):
    class Meta:
        verbose_name = ('Comercio')
        verbose_name_plural = ('Comercios')

    Nombre = models.CharField(max_length=50)
    Rtn = models.CharField(max_length=30)

    def __unicode__(self):
        return self.Nombre

class Sucursal(models.Model):
    class Meta:
        verbose_name = ('Sucursal')
        verbose_name_plural = ('Sucursales')

    Nombre = models.CharField(max_length=50)
    Direccion = models.CharField(max_length=100)
    Telefono = models.CharField(max_length=15)
    Correo = models.EmailField()
    Rtn = models.ForeignKey(Comercio)
    Bits = models.IntegerField()
    latitud = models.CharField(max_length=25)
    longitud = models.CharField(max_length=25)
    altitud = models.CharField(max_length=25)

    def __unicode__(self):
        return self.Nombre

class UsuarioAfiliado(models.Model):
    class Meta:
        verbose_name = ('UsuarioAfiliado')
        verbose_name_plural = ('UsuarioAfiliados')

    Sucursal = models.ForeignKey(Sucursal)
    Usuario = models.ForeignKey(User)
    FechaHora = models.DateTimeField(auto_now=True,auto_now_add=True)
    Factura = models.CharField(max_length=50)
    Monto = models.DecimalField(decimal_places=2,max_digits=10)
    StarCoins = models.FloatField()
    Tipo = models.CharField(max_length=10,choices=(('in','IN'),('out','OUT')))


    def __unicode__(self):
        return self.Sucursal

    
      