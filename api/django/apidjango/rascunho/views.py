from django.shortcuts import render # usa uma template html
from django.http import HttpResponse # texto simples em html

def texto(request): return HttpResponse('textoSimples') # pra funcionar, em urls.py da pasta app, em urlpatterns, um url deve referenciar essa função

def home(request):
    return render(request,'html.html',{'nome':f'{home.__name__}'})
