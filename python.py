#tipos de dados--------------------------------------------------------------------------------------------------------------
inteiro = 10
'''
comentário da variável
'''
real = 10.1
complexo = 1 + 1j
booleano = True | False
vazio = None
string = '123' | f"123"
lista = [1,2,3]
tupla = (1,2,3)
conjunto = {1,2,3}
dicionario = {"1":2}
file = open("arquivo.txt",'a')
vetor = np.array([])
matriz = np.array([],[],[])
tabela = pd.DataFrame([1,2,3])
vetorpd = pd.Series([1,2,3])
#f-strings-------------------------------------------------------------------------------------------------------------------
f'{real:.2e}' #-> Notação científica
f'{real:.5f}' #-> Casas decimais



#tipos de funções------------------------------------------------------------------------------------------------------------
def definida(): #função definida
    '''
    Comentário da função
    '''
    return True # saída da função
definida() #chamada da função

anonima = lambda arg1 , arg2: arg1/arg2 # função anônima (lambda argumentos:operação)
anonima(arg1=1,arg2=2) # chamada da função anônima, retorna o resultado da operação

def geradora(n):
    for i in range(n+1): 
        yield i**2 #guarda as iterações em um iterador
objeto_gerador = geradora(10) #guarda o iterador na memória
for i in range(10+1):
    print(next(objeto_gerador)) #usa as iterações
#classes---------------------------------------------------------------------------------------------------------------------
type(object) # diz a classe que um objeto pertence
range(comeco=int,fim=int,passo=int) #
object #
int() #
float() #
complex() #
bool() #
str() #
list() #
tuple() #
set() #
dict() #
map() #
filter() #
zip() #
enumerate() #
frozenset() #
#funções---------------------------------------------------------------------------------------------------------------------
print('',end='') # Escreve algo no CLI                                                            (object) -> None
sum() # soma os valores de um iteravel e uma constante                                            (iteravel,num) -> num
round() # arredonda um float em n casas                                                           (float,num) -> float
len() # comprimento de um iteravel                                                                (iteravel) -> int
input() # pede uma str via CLI                                                                    (str) -> str
sorted() # organiza um iteravel de str ou reais                                                   (iteravel)->(list)
min(list,key=definida) # pega o menor valor de um iteravel                                                         (iteravel) -> num
max(list,key=definida) # pega o maior valor de um iteravel                                                         (iteravel) -> num
open() # abre um arquivo de uma forma                                                             (str,str) -> TextIOWrapper
abs() # retorna o módulo de um número                                                             (num) -> num
bin() # pega um valor e retorna o binário                                                         (num) -> str
hex() # pega um valor e retorna o hexadecimal                                                     (num) -> str
oct() # pega um valor e retorna o octal                                                           (num) -> str
ord() # diz o valor unicode de um caractere                                                       (str) -> int
chr() # diz o caractere de um unicode                                                             (int) -> str
isinstance() # diz se um dado é de um tipo                                                        (object,type) -> bool
next() # vai pra próxima iteração de um objeto gerador                                            (obj) -> obj
help() # da dicas de como usar alguma instrução                                                   (object) -> None
#métodos--------------------------------------------------------------------------------------------------------------------
list.append() # adiciona um objeto no final da lista                                              (list) -> None
list.remove() # remove o primeiro elemento com esse valor                                         (list) -> None
list.insert() # coloca no index um elemento e reposiciona o resto                                 (index,object) -> None
list.extend() # adiciona uma lista na outra                                                       (list,list) -> None
list.clear() # limpa uma lista e deixa ela vazia                                                  (list) -> None
list.count() # quantas vezes um elemento se repete                                                (list) -> int
list.sort() # organiza a lista                                                                    (list) -> None
list.pop() # tira um valor de um index e guarda ele em uma variável                               (list) -> object
list.index() # diz a posição do primeiro elemento com esse valor                                  (list) -> int
list.reverse() # inverte os elementos de uma lista                                                (list) -> None
str.capitalize() # se o primeiro caracter for uma letra, deixa a primeira letra maiúscula         (str) -> str
str.upper() # tudo maiúsculo                                                                      (str) -> str
str.lower() # tudo minúsculo                                                                      (str) -> str
str.split() # separa a string em partes específicas e devolve uma lista                           (str) -> list
str.replace('antigo','novo') # substitui todos os caracteres especificados por outros                            (str) -> str
str.join() # formata uma string com caracteres específicos                                        (str) -> str
str.strip() # tira os caracteres especificados do sufixo e prefixo                                (str) -> str
str.removeprefix() # tira os caracteres do prefixo                                                (str) -> str
str.removesuffix() # tira os caracteres do sufixo                                                 (str) -> str
str.maketrans() # faz uma tabela de tradução                                                      (str) -> dict
str.translate() # traduz baseado em uma tabela de tradução                                        (dict) -> str
str.endswith() # diz se a string termina com os caracteres especificados                          (str) -> bool
str.isalpha() #A-Z diz se a string só tem letras                                                  (str) -> bool
str.isdecimal() #0-9 diz se a string inteira tem números positivos ou zero, não pode ser negativo (str) -> bool
str.find() # pega o primeiro index de uma substring na string                                     (str) -> int
str.title() # deixa a primeira letra de cada palavra maiúscula                                    (str) -> str
file.close() # fecha um arquivo                                                                   (TextIOWrapper) -> None
file.read() # faz a leitura do arquivo e guarda em uma variável                                   (TextIOWrapper) -> str
file.write() # escreve em um arquivo e move o cursor pro final do arquivo                         (TextIOWrapper) -> None
file.seek(0) # move o cursor pro começo do arquivo                                                (TextIOWrapper) -> None
set.add() # adiciona um elemento no final do conjunto                                             (set) -> None
set.discard() # remove o elemento do conjunto                                                     (set) -> None
set.issubset() # diz se o conjunto é subconjunto de outro                                         (set) -> bool
set.issuperset() # diz se o conjunto tem o outro como subconjunto                                 (set) -> bool
set | set # união
set & set # intersecção
set - set # diferença
set ^ set # diferença simétrica
dict.get() #pega o valor de uma chave especificada                                                (dict) -> object
dict.keys() #iteravel sobre o nome das chaves de um dict                                          (dict) -> iterável
dict.values() #iteravel sobre os valores de um dict                                               (dict) -> iterável
dict.items() #iteravel sobre chave,valor                                                          (dict) -> iterável
dict.update({}) # adiciona um par {chave:valor} no dict                                           (dict) -> None
dict.fromkeys(list) # cria um dicionário apartir de uma lista                                     (list) -> dict
dict['1'] # acessa a chave '1'
#exceções-------------------------------------------------------------------------------------------------------------------
ValueError #
TypeError # Usar argumento de tipo errado
Exception # Qualquer erro
FileNotFoundError # Arquivo não encontrado
ZeroDivisionError #Divisão por zero
NameError # Variável não encontrada
IndexError # Acessar index que não existe
#keywords--------------------------------------------------------------------------------------------------------------------
from math import sin as sen #from módulo import função sin, mas escreva como sen
sen() == math.sin()

None # ausência de dados
True # bool diferente de 0
False # bool 0

match(inteiro): # se o valor da variável for um desses valores faça isso
    case 1: pass
    case 2: pass
    case _: pass # se não for nenhum deles

pass # não faz nada, serve pra quando uma instrução precisa de complemento

if 1==1: # se condição for True
    pass
elif 2==2: # se o if for False e essa condição for True
    pass
else: # se todas as condições forem False
    pass

if 1>1 and 2<2: # and é o E
    pass
if 1>=1 or 2<=2: # or é o OU
    pass
if not 1==1: # not é o NÃO
    pass

while 1==1: # repete até que a condição vá de True para False
    pass

for elemento in lista: # repete todos os elementos dentro de uma coleção
    break # quebra a estrutura de repetição inteira
for elemento in lista:
    continue # vai direto pra próxima repetição, ignorando o resto

try: # tente executar o código
    pass
except Exception: # se der esse erro faça isso
    pass
else: # se não der erro nenhum 
    raise Exception("Texto no CLI") # mostra um erro personalizado, bom pra programas específicos
finally: # se der erro ou não
    pass

str is str # condição , se eles apontam pro mesmo objeto na memória

del list[1] # tira o valor dessa posição

#with
#assert
#class
#global
#nonlocal
#async
#await

#Funções dos módulos---------------------------------------------------------------------------------------------------------
import this # zen do python

import math
math.ceil() # arredonda pra cima                                                                            (num) -> num
math.floor() # arredonda pra baixo                                                                          (num) -> num
math.dist() # distância entre dois pontos                                                                   (num) -> num
math.trunc() # parte inteira                                                                                (num) -> num
float - math.trunc() # parte decimal                                                                        (num) -> num
math.radians() # grau -> rad                                                                                (num) -> num
math.degrees() # rad -> grau                                                                                (num) -> num
math.log() # logaritmo de numero e base                                                                     (num,num) -> num
math.lcm() # Mínimo múltiplo comum                                                                          (num) -> num
math.gcd() # Maior divisor comum                                                                            (num) -> num
math.hypot() # diz a hipotenusa de dois catetos                                                             (num,num) -> num
math.factorial() # diz o fatorial de um número                                                              (num) -> num
math.e # 2,7
math.pi # 3.14
math.sin() # seno em radianos
math.cos() # cosseno em radianos
math.tan() # tangente em radianos

import random
random.randint(1,10)
random.choice(lista)
random.shuffle(lista)

import time
time.sleep(1)

import os
os.remove('arquivo')#apaga um arquivo
os.rename('nome anterior','nome novo')#renomeia um arquivo
string = os.getcwd() #diretório atual
lista = os.listdir('.') # lista os arquivos da pasta e guarda cada nome na lista
os.chdir('pasta') # entra em uma pasta
os.rmdir('pasta') # apaga uma pasta
os.system('comandos bash') # executa comandos bash
os.mkdir('pasta') # cria uma pasta

import numpy as np
produto_escalar = np.inner(matriz,matriz) #produto escalar de duas matrizes
multiplicacao = np.matmul(matriz,matriz) # multiplicação de matrizes
amostra =  np.random.normal(10,3,20) # distribuição normal pra um Histograma(centro,desvio padrão,quantidade)
matriz[0,0] # acessa a matriz[linha,coluna]
x = np.linspace(0,10,100) # gera números igualmente espaçados(começo,fim,numerodepontos)
organizado = np.sort(vetor) # organiza de menor pra maior
vetor[0] # acessa parte do vetor
tamanho = vetor.size # quantidade total de elementos de um vetor
array = np.arange(0,20,5) # cria um vetor em (começo,fim,passo) [0 5 10 15]
quantidadeporlinha = matriz.shape # linhas,colunas de uma matriz
dimensoes = array.ndim # quantas dimensões tem 1 [colunas] 2 [linhas[colunas]] 3 [[[]]]
np.pi # 3.14
np.e # 2.7
np.sin() # seno em radiano
np.cos() # cosseno em radiano
np.tan() # tangente em radiano
np.rad2deg()# radiano pra grau
np.round(np.pi) # arredonda
np.sum([1,2,3]) # Soma tudo da lista
np.prod([1,2,3]) # multiplica tudo da lista e retorna um int
array.min() #menor elemento
array.max() # maior elemento

import sympy as sp
#função
funcao = '2*x'
f = sp.lambdify(sp.Symbol('x'), sp.sympify(funcao),'numpy') #pega o x da função e da significado algébrico
x = np.array([1,2,3,4,5]) # valores de x da função
y = f(x) # usa um np.array e aplica a função nele
#expressao algébrica
x = sp.symbols('x')
y = sp.symbols('y')
expressao_algebrica = (x+y)**2
expansao = sp.expand(expressao_algebrica)
simplificar = sp.simplify(expressao_algebrica)
#equação
equacao = 2*x+1 # forma da equação
resolucao = sp.solve(equacao) # resolver ela = 0

import matplotlib.pyplot as plt

fonte = {'family':'serif',
         'color':'red',
         'size':12}
x0 = 1
xf = 3
y0 = 10
yf = 30

linhas = 2
colunas = 3
###
###
plt.subplot(linhas,colunas,1) # cria múltiplos gráficos
plt.title('linha',fontdict=fonte) # Nome do gráfico
x = [1,2,3,4,5]
y = [10,20,30,40,50]
plt.axis((x0,xf,y0,yf)) # usa parte do gráfico
plt.xlabel('Título do x',fontdict=fonte) # texto do eixo x
plt.ylabel('Título do y',fontdict=fonte) # texto do eixo y
plt.plot(x,y,color='r',marker='o',linestyle='--',linewidth=2,label='significado') # gráfico de linha

plt.subplot(linhas,colunas,2)
plt.title('vertical',fontdict=fonte)
plt.bar(x,y,width=0.4,color='red',edgecolor='black') # gráfico de barra vertical

plt.subplot(linhas,colunas,3)
plt.title('horizontal',fontdict=fonte)
plt.barh(x,y,height=0.4,color='red',edgecolor='black') # gráfico de barra horizontal

plt.subplot(linhas,colunas,4)
plt.title('função',fontdict=fonte)
f = sp.lambdify(sp.Symbol('x'), sp.sympify('x**2'),'numpy')
pontox=np.array([2,4,6,8,10])
pontoy = f(pontox)
plt.grid(axis='y') # grade 
plt.plot(pontox,pontoy,color='r',marker='o',linestyle='--',linewidth=2,label='significado')#gráfico de função matemática

plt.subplot(linhas,colunas,5)
plt.title('pontos',fontdict=fonte)
tamanho = 50
plt.scatter(x,y,color='red',edgecolors='black',s=tamanho) # gráfico de pontos

plt.subplot(linhas,colunas,6)
plt.title('pizza',fontdict=fonte)
nomes = ['primeiro','segundo','terceiro','quarto','quinto']
cores = ['black','red','green','blue','brown']

plt.legend(title='titulo da legenda') # nome da tabela de significados
plt.pie(x,colors=cores,labels=nomes) # gráfico de pizza

plt.suptitle('Vários Gráficos') # Título de um conjunto de tabelas
plt.savefig('arquivo.png') # baixa uma print do gráfico
plt.show() # abre a tela com o gráfico

from scipy.interpolate import *
pontox = [1,2,3,4]
pontoy = [5,6,7,8]
interpolacao = lagrange(pontox,pontoy) # função que passa pelos pontos (pontox[n],pontoy[n])

import pandas as pd
media = vetorpd.mean() # media de um vetor
moda = vetorpd.mode().iloc[0] # moda de um vetor, com suporte a excessões
mediana = vetorpd.median() # mediana de um vetor
variancia = vetorpd.var() # variância de um vetor
desvio_padrao = vetorpd.std() # desvio padrão de um vetor

from tkinter import *
menu = Tk() # janela nova
menu.title("Janela") # nome da janela
altura = 300 # altura da janela
largura = 500 # largura da janela
largurasys  = menu.winfo_screenwidth() # largura do sistema
alturasys = menu.winfo_screenheight() # altura do sistema
posx =int(largurasys / 2 - largura / 2) # centralizar a janela em x
posy =int(alturasys / 2 - altura / 2) # centralizar a janela em y
menu.geometry(f"{largura}x{altura}+{posx}+{posy}") # colocar a janela nessa posição
menu.resizable(True,True) # diz se a janela pode ser redimensionada(x,y)
menu.minsize(720,586) # tamanho mínimo (x,y) (não tem tela cheia)
menu.maxsize(1280,720) # tamanho máximo (x,y) (não tem tela cheia)
menu.state('iconic') # abre minimizado
menu['bg'] = 'black' # muda a cor de fundo da janela
botao = Button(menu , # janela que vai estar o botao
               text='textodobotao', # texto do botão
               command= lambda: print("e"), # o que acontece ao clique
               )
botao.pack() # exibe o botão
texto = Label(menu, # janela que vai estar o texto
               text='Texto Qualquer1\noutroTexto', # texto 
               bg = 'gray', # cor de fundo
               fg = 'white', # cor da letra
               font = 'Arial 12 bold italic', # fonte / tamanho / formatação
               width=20, # comprimento
               height=3, # altura
               relief='solid', # borda
               borderwidth= 1, #espessura da borda
               )
texto.pack() # exibe o texto
menu.mainloop() # janela aberta

import sys
sys.getsizeof(object) # diz o espaço em bytes que algo ocupa

import cProfile
cProfile.run('anonima(1,2)') # roda uma função com parâmetros especificados e diz o tempo de execução

from collections import *
tuplaNomeada = namedtuple('nome dela',['valor1','valor2','valor3']) # tupla nomeada
colocarvalor = tuplaNomeada(1,2,3) # coloca valores nessas chaves
colocarvalor[1] # acessa 'valor2' quando foi colocado na tupla pela posição
colocarvalor.valor2 # acessa 'valor2' pela chave

filaDeSaidaDupla = deque([1,2,3,4,5]) # fila que só pode tirar e adicionar nas bordas
filaDeSaidaDupla.append(6) # adiciona a direita
filaDeSaidaDupla.appendleft(0) # adiciona a esquerda
valorTirado = filaDeSaidaDupla.pop() # remove a direita
valorTirado = filaDeSaidaDupla.popleft() # remove a esquerda

dicionarioOrdenado = OrderedDict({"1":1,"2":2}) # dicionário que só meche no final
dicionarioOrdenado["3"] = 3 # adiciona coisas no final dele

variosDicionarios = ChainMap({1:2,3:4},{"1":"2","3":"4"}) # vários dicionários em um iterável
list(variosDicionarios.keys()) # todas as chaves de todos os dicionários
list(variosDicionarios.values()) # todos os valores de todos os dicionários

