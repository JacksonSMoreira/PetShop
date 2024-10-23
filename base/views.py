from django.shortcuts import render
#from django.http import HttpResponse
from base.forms import ContatoForm
from base.models import Contato

def inicio(request):
    return render(request,'inicio.html')

def contato(request):
    sucesso = False
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        sucesso = True
        form.save()
    contexto = {
        'telefone': '(99) 9999.9999',
        'responsavel': 'Mario da Silva',
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'contato.html', contexto)
