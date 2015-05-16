#-*- encoding: utf-8 -*-
from django.db import models
from datetime import *  #para uso de datas em python
from django.core.exceptions import ValidationError

#####################################################################################
################################ CLIENT ############################################
#####################################################################################
class Cliente(models.Model):
	nome 		= models.CharField(max_length=150)
	telefone 	= models.CharField(max_length=150)
	dataCad 	= models.DateField(auto_now_add=True)
	#Pagamento 	= models.BooleanField(default=False)
	
	def __unicode__(self):
		return unicode("%s - %s ") % ("Nome :"+self.nome, "Telefone : "+self.telefone)
	
	#ordena visualização no admin 	
	class Meta:
		ordering = ['nome']
###################################################################################	
################################ CAR ############################################	
###################################################################################
class Carro(models.Model):
	dono 	= models.ForeignKey(Cliente,verbose_name="Cliente",null=False)
	marca 	= models.CharField(max_length=30)
	nome 	= models.CharField(max_length=30)
	placa 	= models.CharField(max_length=100)
	
	def __unicode__(self):
		return unicode("%s - %s - %s") % (self.dono,self.marca, self.nome)
###################################################################################		
################################ VACANCY ############################################
###################################################################################
class Vaga(models.Model):
	data 		= models.DateField(auto_now_add=True)
	entrada		= models.TimeField()
	horaSaida	= models.TimeField(null=True, blank=True)
	numero 		= models.IntegerField()
	descricao 	= models.CharField(max_length=100,default="vazia")
	carro 		= models.ForeignKey(Carro,verbose_name="Carro",null=False)
	
	class Meta:
		ordering = ['horaSaida']
#########################################################################################	
################################ VALIDATE ############################################
#########################################################################################
	def clean(self):
		maximo = 19									
					
		q  = Vaga.objects.filter(numero=self.numero, horaSaida=self.horaSaida)
		q1 = Vaga.objects.filter(carro=self.carro, horaSaida=self.horaSaida)
				
		#carro estacionado e vaga ocupada
		if q & q1:		
			raise ValidationError("Esta vaga já está ocupada e o carro já está estacionado !")	
		
		#carro estacionado
		if q1:
			#vaga não existe no estacionamento que tem só 20 vagas
			if self.numero > maximo:
				raise ValidationError("O carro já está estacionado e esta vaga não existe !")	
			else:
				raise ValidationError("Este Carro já está estacionado !")
		
		#Vaga já ocupada 
		if q:
			raise ValidationError("Esta vaga já está ocupada")
		
		#vaga não existe no estacionamento apenas
		if self.numero > maximo:
			raise ValidationError("Esta vaga não existe !  Apenas de 0 a 19 estão disponíveis !")
		
