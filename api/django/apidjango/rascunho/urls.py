from django.urls import path # ligar um url a um html
from . import views # arquivo com as funções de html

urlpatterns = [
    path('',views.home), # referencia uma função de views.py pra uma url http://127.0.0.1:8000/rascunho/
    path('texto/', views.texto), #http://127.0.0.1:8000/rascunho/texto/
    path('outrapg/',views.outrapg),
    path('outrapgp',views.outrapgp)
]