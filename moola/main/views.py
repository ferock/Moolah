# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from models import *
from datetime import date
#from forms import *


def home(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/dashboard')
	return render(request,'index.html',{})

def registro(request):
	if request.POST:
		usr = request.POST.get('loginName')
		eml = request.POST.get('loginEmail')
		pasw = request.POST.get('loginPassw')
		cuenta = User.objects.filter(Q(username = usr)|Q(email = eml)).count()

		if cuenta == 0:
			usuario = User.objects.create_user(username = usr,email = eml,password = pasw)
			usu = authenticate(username = usr,password = pasw)
			if usu is not None:
				login(request,usu)
				acct = Cuenta(Token = "123123123123")
				acct.save()
				rem = Remitente(Usuario = request.user,Bits = 0, Cuenta = acct,Notificaciones="")
				rem.save()
				return HttpResponseRedirect('/perfil')
		else:
			mensaje = "El usuario o correo ya esta registrado"
			return render(request,'index.html',{'regMsj':mensaje})
	else:
		return HttpResponseRedirect('/')

def perfil(request):
	infoUser = User.objects.get( username = request.user )
	try:
		extInfo = perfilUsuario.objects.get(Usuario = request.user)
	except:
		extInfo = []

	beneficiarios = Beneficiario.objects.filter(Remitente__Usuario = request.user)
	return render(request, 'profile.html',
		{'userInfo': infoUser,
		 'extInfo': extInfo,
		 'beneficiarios' : beneficiarios
		 })

def addBenef(request):
	if request.POST:
		account = Cuenta(Token = "12312312312")
		account.save()

		user = User.objects.create_user(username = request.POST.get('name'),email= request.POST.get('email'),password = 'paranguricutirimicuaro')
		nuevo = Beneficiario()
		nuevo.Usuario = user
		nuevo.Remitente = Remitente.objects.get(Usuario = request.user)
		
		nuevo.Cuenta = account
		nuevo.Bits = 0
		nuevo.Notificacion = ""
		nuevo.save()
	return HttpResponse(request.POST.get('name'))

def savePerf(request):
	perfil,created = perfilUsuario.objects.get_or_create(Usuario = request.user, defaults = {'Nacimiento': date(1940, 10, 9)})
	if not created:

		#perfil.Usuario = request.user
		perfil.Identidad = request.POST.get('identidad')
		perfil.Direccion = request.POST.get('loginsAddrs')
		perfil.Pais = request.POST.get('country')
		perfil.Ciudad = request.POST.get('city')
		perfil.Nacimiento = request.POST.get('birthday')
		perfil.Telefono = request.POST.get('telephone')
		perfil.save()

	return HttpResponseRedirect('/perfil')

def acceso(request):
	if request.POST:
		usu = authenticate(username=request.POST.get('userLogin'),password = request.POST.get('passwLogin'))
		if usu is not None:
			login(request,usu)
			return HttpResponseRedirect("/dashboard")
	return render(request,'index.html',{'logMsj':'Usuario o contrasena no validos!'})

def salir(request):
	logout(request)
	return HttpResponseRedirect('/')

def dashboard(request):
	infoUser = User.objects.get( username = request.user )
	try:
		extInfo = perfilUsuario.objects.get(Usuario = request.user)
	except:
		extInfo = []

	beneficiarios = Beneficiario.objects.filter(Remitente__Usuario = request.user)

	return render(request, 'dashboard.html',
		{'userInfo': infoUser,
		 'extInfo': extInfo,
		 'beneficiarios' : beneficiarios
		 })