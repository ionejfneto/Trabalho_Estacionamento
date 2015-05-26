# -*- encoding: utf-8 -*-
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.shortcuts import render, redirect, get_object_or_404
from forms import ClienteForm
from forms import CarroForm
from forms import VagaForm
from models import *
###################################################################################
###################################  index  #######################################
###################################################################################
def index(request):	
	#filtro para trazer apenas saidas não cadastradas 
	result = Vaga.objects.filter(horaSaida__isnull=True)		
	lista = []
	a = ''
	for x in range(20):		
		for y in result:
			if y.numero == x:							
				a = y.numero
				lista.append([False,y.id])
				break		
		if a != x:			
			lista.append([True,x])			
	return render_to_response('index.html',{'lista':lista})
###################################################################################	
###################################  Cliente  #####################################
###################################################################################
CONTEXT_CLI = "Cliente"
def Clientes(request):
	a =  request.GET.get('query')
	if(a):
		result = Cliente.objects.filter(nome__contains=a)		
	else:
		result = ''				
	return render_to_response('list.html',{'post': result,'contexto':CONTEXT_CLI})
	
def fCliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('Clientes')
    else:
        form = ClienteForm() 
    return render(request,"form.html",{'form':form, 'contexto':CONTEXT_CLI})
	
def eCliente(request,id=None):
	obj = get_object_or_404(Cliente, pk=id)
	if request.method == 'POST':
		form = ClienteForm(request.POST, instance=obj) 
		if form.is_valid():
			form.save()
			return redirect('Clientes')
	else:	
		form = ClienteForm(instance=obj) 
	return render(request,"form.html",{'form':form})
###################################################################################
###################################  carro  #######################################
###################################################################################
CONTEXT_CAR = "Carro"
def Carros(request):
	a =  request.GET.get('query')	
	if(a):
		result = Carro.objects.filter(nome__contains=a)
		#cont = Cliente.objects.filter(nome__contains=a).count()
	else:
		result = ''				
	return render_to_response('list.html',{'post': result,'contexto':CONTEXT_CAR})
	
def fCarro(request):
    if request.method == 'POST':
        form = CarroForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('Carros')
    else:
        form = CarroForm() 
    return render(request,"form.html",{'form':form, 'contexto':CONTEXT_CAR})
	
def eCarro(request,id=None):
	obj = get_object_or_404(Carro, pk=id)
	if request.method == 'POST':
		form = CarroForm(request.POST, instance=obj) 
		if form.is_valid():
			form.save()
			return redirect('Carros')
	else:	
		form = CarroForm(instance=obj) 
	return render(request,"form.html",{'form':form})
###################################################################################	
###################################  Vaga  ########################################
###################################################################################
CONTEXT_VAGA = "Vaga"
def fVaga(request):
    if request.method == 'POST':
        form = VagaForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('home')
    else:		
        form = VagaForm() 
    return render(request,"form.html",{'form':form, 'contexto':CONTEXT_VAGA})
	
def eVaga(request,id=None):
	obj = get_object_or_404(Vaga, pk=id)
	if request.method == 'POST':
		form = VagaForm(request.POST, instance=obj) 
		if form.is_valid():
			form.save()
			return redirect('home')
	else:	
		form = VagaForm(instance=obj) 
	return render(request,"form.html",{'form':form})