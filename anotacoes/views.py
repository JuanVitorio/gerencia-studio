from django.shortcuts import redirect, render
from .models import anotacao, devendo
from .forms import *

# função que lista os clientes
def clientes(request):
    clientes = {}
    clientes['clientes'] = anotacao.objects.all()
    return render(request, 'clientes.html', clientes)

#criar nova anotação
def nova_anotacao(request):
    data = {}
    form = clienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('clientes')
    
    data['form'] = form
    return render(request, 'form_cliente.html', data)

#atualizar anotação
def update_anotacao(request, pk):
    data = {}
    anotacao_up = anotacao.objects.get(pk=pk)
    form = clienteForm(request.POST or None, instance = anotacao_up)

    if form.is_valid():
        form.save()
        return redirect('clientes')
    
    data['form'] = form
    return render(request, 'form_cliente.html', data)

#deletar anotação
def delete_anotacao(request, pk):
    delete = anotacao.objects.get(pk=pk)
    delete.delete()
    return redirect('clientes')

#Lista os detalhes da pessoa selecionada
def lista_detalhes(request, pk):
    data = {}
    data['cliente'] = anotacao.objects.get(pk=pk)
    data['devendo'] = devendo.objects.all()
    return render(request, 'cliente_detalhe.html', data)

  