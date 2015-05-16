#-*- encoding: utf-8 -*-
from django import forms
from models import Cliente
from models import Carro
from models import Vaga
 
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome','telefone']
		
class CarroForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = ['dono','marca','nome','placa']	

class VagaForm(forms.ModelForm):
    class Meta:
        model = Vaga
        fields = ['carro','entrada','numero','descricao','horaSaida']			
		