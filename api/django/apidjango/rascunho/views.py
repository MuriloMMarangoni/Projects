from django.shortcuts import render # usa uma template html
from django.http import HttpResponse # texto simples em html
import datetime

def texto(request): return HttpResponse('textoSimples') # pra funcionar, em urls.py da pasta app, em urlpatterns, um url deve referenciar essa função

def home(request):

    context = {
        'nomehtml' : 'Pessoa',
        'data' : datetime.date.today()
    }

    return render(request,'html.html',context) # carrega o html, onde a var nomehtml vai ter o valor Pessoa

def outrapg(request):

    texto1=request.GET['texto'] # pegar campos name="" do html
    texto2=request.GET['texto2']

    return HttpResponse(texto1+texto2)

def outrapgp(request):

    botao_post = request.POST['botao_post']
    
    return HttpResponse(botao_post)