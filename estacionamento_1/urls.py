from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'estacionamento_1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^$', 'app_models.views.index', name='home'),
    url(r'^admin/', include(admin.site.urls), name='admin'),
	url(r'^fCliente/$', 'app_models.views.fCliente', name='fCliente'),
	url(r'^eCliente/(.*)$', 'app_models.views.eCliente', name='eCliente'),
	url(r'^Clientes/$', 'app_models.views.Clientes', name='Clientes'),
	
	url(r'^fCarro/$', 'app_models.views.fCarro', name='fCarro'),
	url(r'^eCarro/(.*)$', 'app_models.views.eCarro', name='eCarro'),
	url(r'^Carros/$', 'app_models.views.Carros', name='Carros'),

	url(r'^fVaga/$', 'app_models.views.fVaga', name='fVaga'),
	url(r'^eVaga/(.*)$', 'app_models.views.eVaga', name='eVaga'),
	
	(r'^media/(.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
)
