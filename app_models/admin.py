from django.contrib import admin
from models import Cliente
from models import Carro
from models import Vaga

# Register your models here.
class AdminCliente(admin.ModelAdmin):
	list_display 	= ['nome','telefone','dataCad']
	search_fields 	= ['nome']	
	list_display_links = ['nome']
	
class AdminCarro(admin.ModelAdmin):
	list_display 	= ['dono','marca','nome','placa']
	list_filter = ['marca']
	list_display_links = ['nome']
	
class AdminVaga(admin.ModelAdmin):
	list_display 	= ['carro','data','entrada','numero','descricao','horaSaida']
	search_fields 	= ['numero']
	list_filter = ['data','carro']	

admin.site.register(Cliente, AdminCliente)
admin.site.register(Carro, AdminCarro)
admin.site.register(Vaga, AdminVaga)
