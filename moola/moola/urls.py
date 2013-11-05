from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'main.views.home', name='home'),
    url(r'^registro' , 'main.views.registro',name = 'registro'),
    url(r'^login' , 'main.views.acceso', name = 'acceso'),
    url(r'^salir' , 'main.views.salir', name = 'salir'),
    url(r'^dashboard' , 'main.views.dashboard', name = 'dashboard'),
    url(r'^perfil' , 'main.views.perfil', name = 'perfil'),
    url(r'^addBeneficiario' , 'main.views.addBenef', name = 'addBenf'),
    url(r'^savePerf' , 'main.views.savePerf', name = 'savePerf'),
    #url(r'^main' , 'main.views.dashboard', 'dashboard'),
    # url(r'^moola/', include('moola.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
