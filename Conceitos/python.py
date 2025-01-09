#tipos de dados--------------------------------------------------------------------------------------------------------------
inteiro = 10
real = 10.1
complexo = 1 + 1j
booleano = True | False
vazio = None
string = '123' | f"123"
lista = [1,2,3]
tupla = (1,2,3)
conjunto = {1,2,3}
dicionario = {"1":2}
CONSTANTE = 1
file = open("arquivo.txt",'a')
vetor = np.array([])
matriz = np.array([],[],[])
tabela = pd.DataFrame([1,2,3])
vetorpd = pd.Series([1,2,3])
valor:int = 1 # forma de tipar uma variável
algo:int # declara mas não inicializa
'''
comentário da variável
'''
#f-strings-----------------------------------------------------------------------------------------------------------------
f'{real:.2e}' #-> Notação científica
f'{real:.5f}' #-> Casas decimais
f'{string:<10}' #-> alinha um texto a esquerda em tantas casas
f'{string:>10}' #-> alinha um texto a direita em tantas casas
f'{string:^10}' #-> alinha um texto ao centro em tantas casas
#tipos de funções------------------------------------------------------------------------------------------------------------
def procedimento(): #procedimento
    print('Não retorna nada')
def definida(arg): #função definida com input obrigatório arg
    '''
    Comentário da função
    '''
    return arg # saída da função
definida() #chamada da função
anonima = lambda arg1 , arg2: arg1/arg2 # função anônima (lambda argumentos:operação)
anonima(1,2) # chamada da função anônima, retorna o resultado da operação
def geradora(n):
    for i in range(n+1): 
        yield i**2 #guarda as iterações em um iterador
objeto_gerador = geradora(10) #guarda o iterador na memória
for i in range(10+1):
    print(next(objeto_gerador)) #usa as iterações
def g(list):
    yield 'começando' # mostra essas mensagens antes e depois da execução principal
    yield from list # cria o iterador baseado em um iterável
    yield 'terminando'
iterador = g([1,2,3])
def fun(recomendacao:int | float)->int:
    # o input deve ser int ou float
    # a saída é int
    pass
def fun(recomendacao=0):
    # input opcional, se não for definido, usa o valor padrão
    pass
def fun(*args):
    # pega só argumentos posicionais e coloca todos em uma tupla
    return args
fun(1,2,3) #argumento posicional
fun(*[1,2,3]) # desempacota lista como se fosse vários argumentos posicionais
def fun(**kwargs):
    #pega só argumentos nomeados e coloca em um dicionário
    return kwargs
fun(chave1=1,chave2=2) # argumento nomeado
fun(**{'chave1':1,'chave2':2}) # desempacota um dicionário como se fossem argumentos nomeados
def fun(pos,/,qualquer):
    #tudo que estiver antes da / tem que ser posicional
    pass
fun(1,qualquer=1)
def fun(qualquer,*,nomeado):
    # tudo que estiver depois do * tem que ser nomeado
    pass
fun(1,nomeado=1)
def decorador(fun): #decorador
    def wrapper(): # o que o decorador vai modificar na func
        fun()
        print(f"{fun.__name__}") # diz o nome da função
    return wrapper
@decorador # usa essa função como input do decorador
def fun():
    pass
#condições-----------------------------------------------------------------------------
object == object # se o objeto1 é  igual ao objeto2
object != object # se o objeto1 é diferente do objeto2
object < object # se o objeto1 é menor que o objeto2
object > object # se o objeto1 é maior que o objeto2
object >= object # se o objeto1 é maior ou igual ao objeto2
object <= object # se o objeto1 é menor ou igual ao objeto2
inteiro is inteiro # se dois espaços na memória vem da mesma variável
True and True # E
True or True # OU
not True # Não
while True: # loop infinito
    if True==True: # quebra do loop infinito
        break
#operações----------------------------------------------------------------------------------
o = object # faz uma variável apontar pra um objeto na memória
(value := 1*1) # atribuição dinâmica sem ter que inicializar
o += 1 # o = o + 1
o -= 1 # o = o - 1
o *= 1 # o = o * 1
o /= 1 # o = o / 1
o %= 1 # o = o % 1
o **= 1  # o = o ** 1
o //= 1  # o = o // 1
4 & 8 # 100 and 1000 = 0000 = 0
4 | 8 # 100 or 1000 = 1100 = 12
~ 4 # not , ele aumenta em 1 e troca o sinal = -5
4 ^ 8 # 100 xor 1000 = 1100 = 12
4 << 1 # 100 <- 1000 = 8
4 >> 1 # 100 -> 10 = 4
i & 255 == i % 256
i & 1 == i % 2
i & i == i
i ^ 0 == i
i ^ i == 0
def swap(a:int,b:int) -> tuple[int, int]:
    # troca dois valores (memory efficient)
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a,b
bitmask = 2 ** (i.bit_length()) -1 # todos os bits preenchidos com 1
i ^ bitmask == bitmask - i
lista[0] # acessa uma posição (0)
lista[0:2] # acessa um começo e um fim (0,1)
lista[0:10:3] # acessa um começo e um fim num passo(0,3,6,9)
lista = [x**2 for x in range(0,11) if x!=0] # cria uma lista baseada em uma regra
dict['1'] # acessa o valor da chave '1'
dict['2'] = 2 # dinamicamente cria um par chave-valor
#classes---------------------------------------------------------------------------------------------------------------------
type(object) # diz a classe que um objeto pertence
range(comeco=int,fim=int,passo=int) # iterador com começo,fim e passo
object #
int() # numero inteiro
float() # numero decimal de até 17 casas
complex() # número complexo
bool() # valor lógico
str() # sequência de texto
list() # sequência de vários valores modificáveis com posição que pode repetir
tuple() # sequência de vários valores não modificáveis com posição que pode repetir
set() # sequência de vários valores modificáveis sem posição que não pode repetir
dict() # sequência de vários valores em par chave-valor
map() # muda uma lista inteira
l = [0,1,2,3,4,5,6,7,8,9,10]
mp = map(lambda x: x % 2 == 0,l) # muda uma lista inteira(expressão,lista)
print(list(mp)) # transforma o objeto do mapa em uma lista

filter() # filtra a lista
l = [0,1,2,3,4,5,6,7,8,9,10]
ft = filter(lambda x: x % 2 == 0,l) # filtra a lista
print(list(ft)) # transforma o objeto do filtro em uma lista

zip() #
enumerate(list) # cria um iterável que pode ser aberto com index,valor
frozenset() #

class Cobra: # classe
    #self se refere a instância
    def __init__(self,nome,cor,especie): #onde define os atributos
        self.nome = nome # diz como que o atributo vai ser acessado
        self.cor = cor
        self.especie = especie
        self.modelo = 0 # atributo que pode ser mudado na instancia, mas não é usado na chamada
    def nomeCompleto(self): # método
        print(f'{self.nome:<15}',f'\n{self.cor:<15}',f'\n{self.especie:<15}')
instancia = Cobra('minha','verde','piton') # aplica a classe com os atributos obrigatório
instancia.nomeCompleto() # executa o método sem atribuição
atributo = instancia.nome # acessa o valor do atributo
atributo_nao_obrigatorio = instancia.modelo # valor do não obrigatório
class SuperClasse(): # HERANÇA (essa é superclasse)
    def __init__(self,atributo1,atributo2):
        self.atributo1 = atributo1
        self.atributo2 = atributo2
    def metodo1(self):
        return 'Herdado direto'     
class SubClasse(SuperClasse): # herda os métodos automaticamente (essa é a subclasse)
    def __init__(self,atributo1,atributo2): # todos os atributos que vão ser usados (exclusivos e herdados)
        super().__init__(atributo1,atributo2) #libera a utilização de atributos herdados
    
instanciaSub = SubClasse('novo','a1','a2') #exclusivo , herdado, herdado
instanciaSub.metodo1() # herdado
instanciaSub.metodo2('a3') # herdado
instanciaSub.metodo3() # exclusivo
class Planta():
    @staticmethod # não precisa instanciar pra usar, é só fazer classe.método
    def especie():
        print('espécie desconhecida')
Planta.especie() # uso de um método estático
class Texto:
    def __init__(self,paragrafos,linhas):
        self._paragrafos = paragrafos # semi privado (funciona normal)
        self.__linhas = linhas # privado, não pode ser chamado diretamente
caderno = Texto(3,18)
print(caderno._paragrafos) # funciona
print(caderno.__linhas) # erro
# Design Pattern: Factory (classe que cria objetos de outra classe)
class Produto:
    def __init__(self,nome:str,preco:int):
        self.nome = nome
        self.preco = preco
class Factory:
    @staticmethod # NÃO USA SELF
    def criar(nome:str,preco:int):
        return Produto(nome=nome,preco=preco)
    
primeiro = Factory.criar('cebola',1)

l = []
for each in range(1,11):
    l.append(Factory.criar(f'{each}',each))
print(l)
#dunder--------------------------------------------------------------------------------------
object.__class__ # diz a classe que um objeto faz parte
object.__class__.__name__ # diz a classe com nome mais legível
class dunder():
    def __init__(self):# definir atributos de uma instância
        pass
    def __str__(self): # quando o objeto for tratado como str ou usado no print
        return str
    def __repr__(self): # só é usado se a instância for acessada com repr(instância)
        return str
    def __len__(self): # o que acontece quando usa len()
        return int
    def __add__(self,algo): # quando soma a instância + algo
        return str|int
    def __getitem__(self,index): # quando for iterado
        return self.list[index]
    def __call__(self,arg): # faz a instância ser tratada como função, os argumentos aqui são os usados na chamada
        pass
print(__file__) # mostra caminho pro arquivo atual
#funções---------------------------------------------------------------------------------------------------------------------
print('',end='') # Escreve algo no CLI                                                            (object) -> None
sum() # soma os valores de um iteravel e uma constante                                            (iteravel,num) -> num
round() # arredonda um float em n casas                                                           (float,num) -> float
len() # comprimento de um iteravel                                                                (iteravel) -> int
input() # pede uma str via CLI                                                                    (str) -> str
sorted() # organiza um iteravel de str ou reais                                                   (iteravel)->(list)
min(list,key=definida) # pega o menor valor de um iteravel                                                         (iteravel) -> num
max(list,key=definida) # pega o maior valor de um iteravel                                                         (iteravel) -> num
open('nome','forma') # abre um arquivo de uma forma                                                             (str,str) -> TextIOWrapper
#formas (x -> criar,r -> ler,a -> adicionar, w -> sobrescrever)
abs(int) # retorna o módulo de um número                                                             (num) -> num
bin(int) # pega um valor e retorna o binário                                                         (num) -> str
hex(int) # pega um valor e retorna o hexadecimal                                                     (num) -> str
oct(int) # pega um valor e retorna o octal                                                           (num) -> str
ord('d') # diz o valor unicode de um caractere                                                       (str) -> int
chr(100) # diz o caractere de um unicode                                                             (int) -> str
isinstance(inteiro,int) # diz se um dado é de uma classe (pode ser o construtor ou a referência da classe [int ou <class 'int'>])                                                        (object,type) -> bool
iterador = iter([1,2,3]) # converte um iterável em um iterador
dir(object) # diz todos os métodos e atributos que um objeto tem
hasattr(inteiro,'__call__') # diz se o objeto tem esse atributo/nome do método
getattr(object,'atributo','valorSeNãoExistir') # mesmo que objeto.atributo
next(iterador,'valorquandoexaurido') # percorre o iterador                                          
help() # da dicas de como usar alguma instrução                                                   (object) -> None
repr() # mostra o __repr__ de uma instância
globals()['nome'] = 'algo' # cria uma variável com esse nome e esse valor
eval('expressãoQualquer') # executa uma str como comando
globals() # dicionário com o par nomedavariável:valor , com escopo global
locals() # dicionário com o par nomedavariável:valor , com valores do escopo atual
boo = any(number < 5 for number in [1,2,3,4,5]) # tem pelo menos um valor que é True?
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
str.removeprefix('') # tira uma substring do prefixo                                                (str) -> str
str.removesuffix('') # tira uma substring do sufixo                                                 (str) -> str
str.maketrans() # faz uma tabela de tradução                                                      (str) -> dict
str.translate() # traduz baseado em uma tabela de tradução                                        (dict) -> str
str.endswith() # diz se a string termina com os caracteres especificados                          (str) -> bool
str.startswith() # diz se uma string começa assim
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
set ^ set # diferença simétrica (único dos dois)
dict.get() #pega o valor de uma chave especificada                                                (dict) -> object
dict.keys() #iteravel sobre o nome das chaves de um dict                                          (dict) -> iterável
dict.values() #iteravel sobre os valores de um dict                                               (dict) -> iterável
dict.items() #iteravel sobre chave,valor                                                          (dict) -> iterável
dict.update({}) # adiciona um par {chave:valor} no dict                                           (dict) -> None
dict.fromkeys(list) # cria um dicionário apartir de uma lista                                     (list) -> dict
int.bit_length() # quantos bits são usados pra representar
#exceções-------------------------------------------------------------------------------------------------------------------
ValueError # Quando o problema está no valor, não no tipo
TypeError # Quando o problema está no tipo
Exception # Qualquer erro genérico
FileNotFoundError # Arquivo não encontrado
ZeroDivisionError #Divisão por zero
NameError # Variável não encontrada
IndexError # Acessar index que não existe
StopIteration # quando você tenta acessar um iterador exausto
AssertionError # quando assert é falso
KeyboardInterrupt # quando usar algum comando pro sistema sair
SystemExit # Erro que encerra o programa na hora
import json
json.JSONDecodeError # quando você lê um arquivo json vazio
import socket
socket.error # erro geral em sockets
ConnectionRefusedError # Cliente não consegue conectar (connect)
socket.gaierror # Procurou nome que não existe (gethostbyname)
socket.herror # se o ip não corresponde a um host (gethostbyaddr)
TimeoutError # se o client demorar muito pra conectar no servidor via socket ou interagir
import sqlite3
sqlite3.OperationalError # erro de comandos
import requests
requests.exceptions.JSONDecodeError # quando vc tenta transformar um url não json, em json
requests.exceptions.MissingSchema # falta prefixo
requests.exceptions.InvalidSchema # prefixo inválido
requests.exceptions.ConnectionError # não conseguiu estabelecer conexão
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
except Exception as e: # 'e' é a mensagem do erro
    print(type(e)) # diz qual é o erro que ocorreu
else: # se não der erro nenhum 
    raise Exception("Texto no CLI") # mostra um erro personalizado, bom pra programas específicos
finally: # se der erro ou não
    pass
del list[1] # tira o valor dessa posição

nome = 'primeiro'
def muda_o_nome(novo_nome):
    global nome # var muda o valor pra todo o arquivo mesmo dentro de uma função
    nome = novo_nome
print(nome)
muda_o_nome('segundo') # só que ela tem que estar inicializada antes e a função deve ser chamada pra alteração ser feita
print(nome)

if __name__ == '__main__': # só se esse arquivo for executado, é útil pra criar módulos
    pass

with(open('arq.txt','a')) as file: # mecher com dados de um arquivo externo
    file.write('Escrever algo')

def f1():
    teste = 1
    def f2():
        nonlocal teste # muda 1 escopo acima (funções aninhadas)
        teste = 2
    f2()
    return teste
print(f1()) # 2

a = 'x'
assert a == 'xx' # o código da erro se for False

#async
#await

#Funções dos módulos---------------------------------------------------------------------------------------------------------
from bibliotecapy import modulo # importa um módulo de uma biblioteca
from bibliotecapy.modulo import funcaoDoModulo # importa uma função de um módulo de uma biblioteca
from bibliotecapy.modulo import ClasseDoModulo # importa uma classe
from bibliotecapy.modulo import CONSTANTEDOMODULO # importa uma variável

import random

random.randint(1,10) # escolhe um número ente esse período
random.choice(l) # escolhe um elemento aleatório
random.shuffle(l) # organiza aleatoriamente uma sequência

import os

os.remove('arquivo')#apaga um arquivo
os.rename('nome anterior','nome novo')#renomeia um arquivo
string = os.getcwd() #diretório atual
lista = os.listdir('.') # lista os arquivos da pasta e guarda cada nome na lista
os.chdir('pasta') # entra em uma pasta
os.rmdir('pasta') # apaga uma pasta
os.system('comandos bash') # executa comandos bash
os.mkdir('pasta') # cria uma pasta
os.makedirs('pasta',exist_ok=True) # cria pasta e se já existir não faz nada
os.path.join('pasta','arquivo') # cria um diretório pra pasta/arquivo

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

import numpy as np # pip install numpy

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
listacomzeros = np.zeros(100000000,dtype='uint8') # cria um array de zeros usando inteiros de 8 bits
array.min() #menor elemento
array.max() # maior elemento

import sympy as sp # pip install sympy

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

import matplotlib.pyplot as plt # pip install matplotlib

fonte = {'family':'serif','color':'red','size':12}
x0 = 1
xf = 3
y0 = 10
yf = 30
linhas = 2
colunas = 3
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
plt.ticklabel_format(useOffset=False)

from scipy.interpolate import * # pip install scipy

pontox = [1,2,3,4]
pontoy = [5,6,7,8]
interpolacao = lagrange(pontox,pontoy) # função que passa pelos pontos (pontox[n],pontoy[n])

import pandas as pd # pip install pandas

media = vetorpd.mean() # media de um vetor
moda = vetorpd.mode().iloc[0] # moda de um vetor, com suporte a excessões
mediana = vetorpd.median() # mediana de um vetor
variancia = vetorpd.var() # variância de um vetor
desvio_padrao = vetorpd.std() # desvio padrão de um vetor

import tkinter as tk # pip install tkinter

menu = tk.Tk() # janela nova
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
botao = tk.Button(menu , # janela que vai estar o botao
               text='textodobotao', # texto do botão
               command= lambda: print("e")) # o que acontece ao clique
botao.pack() # exibe o botão
texto = tk.Label(menu, # janela que vai estar o texto
               text='Texto Qualquer1\noutroTexto', # texto 
               bg = 'gray', # cor de fundo
               fg = 'white', # cor da letra
               font = 'Arial 12 bold italic', # fonte / tamanho / formatação
               width=20, # comprimento
               height=3, # altura
               relief='solid', # borda
               borderwidth= 1) #espessura da borda
texto.pack() # exibe o texto
campo_de_texto = tk.Entry(menu) # cria um campo de inserir texto
campo_de_texto.pack()
mostrar = lambda:print(campo_de_texto.get()) # pega o que tiver dentro dele ao ser acionado, retorna uma str
mudar = lambda:texto.config(text='mudei o texto') # muda argumentos de widgets
checar = tk.BooleanVar() # objeto de bools (verificações)
estado = lambda: print('true') if checar.get() else print('false') # diz se foi ou não selecionado
s = tk.Checkbutton(menu,text='algo',variable=checar,command=estado) # cria uma caixa de selecionar
s.pack()
opcao = tk.StringVar() # objeto de checar strings (opções)
r1 = tk.Radiobutton(menu,text='op1',variable=opcao,value='1') # cria uma opção múltipla
r2 = tk.Radiobutton(menu,text='op2',variable=opcao,value='2') # value,se for igual vale por mais de uma opção,se for diferente vale só por si
r3 = tk.Radiobutton(menu,text='op3',variable=opcao,value='2') # op1 vale por si só, op2 e op3 valem pelos 2 porque o value é igual
r1.pack()
r2.pack()
r3.pack()
mostrar = lambda:opcao.get() # diz o 'value' da opção escolhida
text_area = tk.Text(menu,width=50,height=20) # área de texto
text_area.pack()
mostrar = lambda: print(text_area.get('1.0',tk.END)) # mostra o texto a partir da primeira linha até o final
lista = tk.Listbox(menu) # lista de opções
lista.insert(1,'primeiro')
lista.insert(2,'segundo')
lista.insert(3,'terceiro')
lista.insert(4,'quarto')
lista.insert(5,'quinto')
lista.pack()
mostrar = lambda:print(lista.get(lista.curselection())) # mostra a opção selecionada
botao.grid(row=0,column=0,padx=0,pady=0) # exibe os elementos de forma linha,coluna; pode ter distância de elementos com 'pad'
botao.pack() # exibe centralizado
imagem = tk.PhotoImage(file='imagem.png ou .gif') # objeto de imagem
l = tk.Label(menu,image=imagem) # aplica a imagem
menu.iconphoto(False,imagem) # faz o ícone do app ter uma imagem
menu.config(bg='orange', # cor do fundo
            bd=100) # borda invisível
menu.attributes('-fullscreen',True) # tela cheia, sem bordas de janela
sair = lambda event: print('sair') # funções pro bind precisam da variável 'event' pra identificar o evento
sair = lambda event: menu.quit() # fecha o app
menu.bind("<Escape>",sair) # se apertar ESC 
posicao_mouse = lambda event: print(event.x,event.y) # posição do mouse
nome_tecla = lambda event: print(event.keysym) # tecla pressionada
menu.bind("<Key>",posicao_mouse) # quando apertar uma tecla
menu.bind('<Button-1>',lambda event: print('clicou esquerdo')) # clicar esquerdo
menu.bind('<Button-3>',lambda event: print('clicou direito')) # clicar direito
botao.bind("<Enter>",lambda e: print('entrou o mouse')) # mouse entrar no botão
botao.bind("<Leave>",lambda e: print('sair o mouse')) # mouse sair do botão
menu.bind_class("Button","<Enter>", lambda e: print('passar o mouse'))# todos os botões tem isso agora
menu.unbind("<Button-1>") # tira o bind de um widget com evento específico
f1 = tk.Frame(menu) # cria frames (telas)
f2 = tk.Frame(menu) # cria frames (telas)
f1.place(relwidth=1, relheight=1) # frames vão ocupar a janela inteira
f2.place(relwidth=1, relheight=1) # frames vão ocupar a janela inteira
b1 = tk.Button(f1,text='botao da tela 1',command= lambda:f2.tkraise()).pack()# botão do frame1 que troca pro frame2
b2 = tk.Button(f2,text='botao da tela 2',command= lambda: f1.tkraise()).pack()# botão do frame2 que troca pro frame1
t2 = tk.Label(f2,text='TELA DOIS',bg='yellow',font=('Arial',12)).pack() # texto com fonte
f1.tkraise() # começa no frame1
campo_de_texto.delete(0,tk.END) # Zera o conteúdo de um entry
campo_de_texto.insert(0,'algo') # coloca um texto em um campo vazios
tk.Label(fg='red') # muda a cor do texto
widgets = menu.winfo_children() # lista com o objeto de cada widget de uma janela ou frame
proximo_widget = lambda event:event.widget.tk_focusNext().focus() # cursor vai pro próximo widget
widget_anterior = lambda event:event.widget.tk_focusPrev().focus() # cursor vai pro widget anterior
checar.set(False) # muda o valor bool de uma BooleanVar, sem fazer a conversão pra bool
menu.focus_get().master # diz qual frame está ativo
botao.focus() # foca em um widget ( mesmo que um clique manual)
botao.place(x=500,y=250) # posicão relativa a janela pra exibir elementos
def mudar():
    texto.config(text=f"algo")# complemento
    texto.after(200,mudar) # chama a função em tanto tempo pra modificar o comportamento de um widget
menu.mainloop() # janela aberta

import tkinter.font as tkFont

fonte_personalizada = tkFont.Font(family="Helvetica",size=18,weight='bold',slant='italic',underline=1) # objeto de fonte
tk.Label(font=fonte_personalizada) # aplica a fonte Helvetica de tamanho 18 em negrito,itálico e sublinhado

import sys #---------------------------------------------------------

sys.getsizeof(object) # diz o espaço em bytes que algo ocupa
sys.exit() # encerra o programa
frame_duma_func = sys._getframe() # pega o frame atual da função que está dentro
def fun():
    for each in range(10):pass
def tracer(frame, event, arg): # tracer é uma função especial que tem informações do estado do programa
    #frame é automaticamente definido, é o frame atual da função observada por settrace() 
    if event in ['call','return','line','exception']: pass # eventos da execução do programa
    arg # complemento do evento, se for return 0, o arg = 0
    frame.f_code.co_name # nome da função
    frame.f_lineno # número da linha int
    frame.f_locals # dict com as variáveis locais e os valores (útil pra loops)
    frame.f_globals# dict com variáveis globais em nível de frames
    return tracer # precisa pra continuar executando a cada evento encontrado

sys.settrace(tracer) # usa uma função que busca eventos no programa
fun()
sys.settrace(None) # encerra a buscar eventos
sys.platform # diz o sistema operacional
sys.argv # lista com os argumentos de cli [__file__,arg1,arg2]

import cProfile #--------------------------------------------------

cProfile.run('anonima(1,2)') # roda uma função com parâmetros especificados e diz o tempo de execução

import subprocess #-----------------------------------------------

subprocess.run('ls',shell=True) # roda um comando bash, pausa o script até terminar a execução
out = subprocess.run('ls',shell=True,text=True,capture_output=True) # pega a saída de um comando ao invés de mostrar no terminal
subprocess.run('mkdir teste',shell=True,stdout=subprocess.DEVNULL) # não mostra a saída do comando
saida = out.stdout # usa a saída do comando
linhas = out.stdout.splitlines() # lista com o output do comando
p = subprocess.Popen('sleep 5',shell=True,cwd='caminhoQueVaiRodarESSEComando') # roda um comando assíncrono
p = subprocess.Popen('pwd',shell=True,stdout=subprocess.PIPE,text=True) # pega a saída de um Popen
saida = p.communicate() # tupla com a saída e o erro, usar saida[0] pra pegar a saída
p.wait() # Espera que o comando seja executado pra continuar o script (só com Popen)
comandos_bash = {
    '1': subprocess.run('sudo ip link set wlan0 down',shell=True),  # Desativa a interface de rede `wlan0`
    '2': subprocess.run('sudo ip link set wlan0 up',shell=True),    # Ativa a interface de rede `wlan0`
    '3': subprocess.run('whois 8.8.8.8',shell=True),                # Consulta informações de WHOIS para o IP 8.8.8.8 (Google DNS)
    '4': subprocess.run('nslookup google.com',shell=True),          # Realiza uma consulta DNS para resolver o domínio google.com
    '5': subprocess.run('dnsenum google.com',shell=True),           # Executa varredura de DNS avançada em google.com, listando subdomínios
    '6': subprocess.run('theHarvester -d google.com -b duckduckgo',shell=True),  # Coleta informações sobre google.com usando o theHarvester, focando em resultados do DuckDuckGo
    '7': subprocess.run('wireshark',shell=True),                    # Abre o Wireshark, ferramenta para análise de pacotes de rede
    '8': subprocess.run('host 8.8.8.8',shell=True),                 # Realiza uma consulta DNS reversa para o IP 8.8.8.8
    '9': subprocess.run('ifconfig',shell=True),                     # Exibe as configurações das interfaces de rede (não é mais padrão em alguns sistemas)
    '10': subprocess.run('route',shell=True),                       # Mostra a tabela de roteamento IP do sistema
    '11': subprocess.run('iwconfig',shell=True),                    # Exibe as configurações de interfaces sem fio
    '12': subprocess.run('ip route',shell=True),                    # Exibe ou manipula a tabela de roteamento IP do sistema (substitui `route` em sistemas modernos)
    '13': subprocess.run('ping google.com -c 10',shell=True),       # Envia 10 pacotes ICMP para google.com para testar conectividade
    '14': subprocess.run('hostname',shell=True),                    # Mostra o nome do host da máquina
    '15': subprocess.run('hostname -i',shell=True),                 # Exibe o endereço IP associado ao nome do host
    '16': subprocess.run('cd /etc/NetworkManager/system-connections && sudo cat *',shell=True),  # Lista o conteúdo das conexões salvas no NetworkManager
    '17': subprocess.run('nmcli dev wifi list',shell=True),         # Lista as redes Wi-Fi disponíveis
    '18': subprocess.run("sudo nmcli dev wifi connect 'MARANGONI NET'",shell=True),  # Conecta-se à rede Wi-Fi "MARANGONI NET"
    '19': subprocess.run("sudo nmcli dev wifi connect 'MARANGONI NET' password '123456789@'",shell=True),  # Conecta-se à rede Wi-Fi "MARANGONI NET" com senha
    '20': subprocess.run('nmcli device status',shell=True),         # Exibe o status dos dispositivos de rede (conectado, desconectado, etc.)
    '21': subprocess.run('nmcli connection show --active',shell=True),  # Lista as conexões de rede ativas
    '22': subprocess.run("nmcli connection modify 'MARANGONI NET' connection.autoconnect yes",shell=True),  # Configura a rede "MARANGONI NET" para conectar automaticamente
    '23': subprocess.run("nmcli connection modify 'MARANGONI NET' connection.autoconnect no",shell=True),   # Configura a rede "MARANGONI NET" para não conectar automaticamente
    '24': subprocess.run("sudo nmcli connection delete 'Marcia'",shell=True),  # Exclui a conexão de rede chamada "Marcia"
    '25': subprocess.run('traceroute google.com',shell=True),       # Mapeia o caminho dos pacotes até google.com
    '26': subprocess.run('netstat -tuln',shell=True),               # Mostra todas as conexões de rede abertas e suas portas de escuta
    '27': subprocess.run('sudo iw dev wlan0 scan',shell=True),      # Realiza uma varredura de redes Wi-Fi disponíveis usando a interface `wlan0`
    '28': subprocess.run('sudo arp-scan --localnet',shell=True),    # Realiza uma varredura ARP para detectar dispositivos na rede local
    '29': subprocess.run('dig google.com',shell=True),              # Realiza uma consulta DNS detalhada para google.com
    '30': subprocess.run('mtr google.com',shell=True),              # Combina as funcionalidades de `traceroute` e `ping` para monitorar a rota até google.com
    '31': subprocess.run('speedtest-cli',shell=True),               # Executa um teste de velocidade de internet (download/upload)
    '32': subprocess.run('cat /etc/resolv.conf',shell=True),         # Exibe o conteúdo do arquivo resolv.conf, onde ficam armazenados os servidores DNS
    '33': subprocess.run('curl ifconfig.me',shell=True), # ip publico
    '34': subprocess.run('pyinstaller arquivo.py',shell=True) # cria um executável de um arquivo.py
}

from fpdf import FPDF # pip install fpdf

class PDF(FPDF): # Coloca métodos além dos da FPDF que se repetem pra ter menos boilerplate
    def header(self): # Cabeçalho
        self.set_font('Arial', 'B', 12) # Fonte(Família, Estilo, Tamanho)
        self.cell(w=0, h=10, txt='Texto Que Aparece em Todas As Páginas', border=0,ln= 1, align='C')#faz uma célula que ocupa todo o espaço, tem 10 de altura, não tem borda , pula 1 linha e é centralizada
    def footer(self): # Rodapé
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C') # Número da Página
    def titulo(self, title): # Título
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln() # Pula um Espaço
    def celulaInteira(self, body, borda): # Célula que ocupa todo o espaço da linha
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 8, body,border=borda) # Esse 0 pega a linha toda
        self.ln()
    def celulaParticionada(self, body, w): # A Célula é uma caixa na mesma linha
        self.set_font('Arial', '', 12)
        self.cell(w, 10, body,border=1) # w é o comprimento != 0
    def tabela(self,cellh,cellv,w,l): # Tabela
        temp = 0
        for each in range(1,cellh+1):
            for anothereach in range(1, cellv+1):
                self.cell(w,10,border=1,txt=l[temp])
                temp += 1
            self.ln()
pdf = PDF() # Instancia a classe na variável pdf
pdf = PDF(format=(70, 100)) # Especifica dimensões do documento
pdf = PDF(format=('A4')) # Padrão A4
pdf.add_page() # Cria a Próxima Página
pdf.add_page('L') # Página Horizontal
pdf.add_page('P') # Página Vertical
pdf.titulo('Título')
pdf.celulaInteira('linha inteira', 1)
pdf.celulaParticionada('Primeiro Bloco',30)
pdf.ln() # Pula Linha
l=['1','2','3','4','5','6','7','8','9'] # células
pdf.tabela(2,3,30,l) # faz uma tabela 2x3 com 30 de comprimento por célula usando a lista l
print(pdf.w, pdf.h) # vê as dimensões do pdf
pdf.text(209,297,'texto') # Coloca um texto em uma posição absoluta
pdf.set_text_color(200,100,100) # Diz a cor de um texto em rgb
pdf.image(name="caminho completo",x=60,y=120,w=120) # coloca uma imagem (posição absoluta)
pdf.output('out.pdf') # Cria arquivo ou sobrescreve

import qrcode # pip install qrcode

qr = qrcode.QRCode(
    version=1, # quantidade de dados (1-40)
    error_correction=qrcode.constants.ERROR_CORRECT_L, #(correção de erros (L M Q H))
    box_size=10, # tamanho dos quadrados
    border=4, # pixels da borda
)
qr.add_data("https://en.wikipedia.org/wiki/Drake%E2%80%93Kendrick_Lamar_feud") # significado
qr.make(fit=True) # faz correção do tamanho do qrcode
img = qr.make_image(fill_color="black", back_color="white") # preto e branco
img.save("qrcode.png") # gera a imagem

from barcode import Code128 # pip install python-barcode
from barcode.writer import ImageWriter

codigo = Code128("algo", writer=ImageWriter()) # faz no formato code128 um texto
filename = codigo.save("codigo_de_barras") # gera a imagem

from datetime import datetime,timezone,timedelta,date,time # opera com datas

tempo = datetime.now() # objeto de tempo atual em ano/mes/dia hora/minuto/segundo/milissegundo
tempo.time() # horário atual em hora/minuto/segundo/milissegundo
tempo.strftime("Dia %d do mês %m do ano %Y com horário %H : %M : %S") # formata o texto com dia mes ano hora minuto segundo
tempo.date() # dia atual em ano/mes/dia
tempo.weekday() # diz o dia da semana segunda -> 0 domingo -> 6
datetime(2024,11,10,3,54,12,1) # tempo personalizado pra uma data e horário
date(2024,12,1) # objeto de data
time(22,30,12) # objeto de hora
tempo+timedelta(days=11) # soma 11 dias a data
tempo.timestamp() # pega o POSIX de qualquer data com horário
datetime.fromtimestamp(tempo.timestamp()) # pega a data de um posix
fuso_brasilia = timezone(timedelta(hours=-3)) # objeto de fuso horário
tempo.astimezone(fuso_brasilia) # aplica um fuso horário a uma data
tempo.astimezone() # aplica o fuso horário local no horário
agora = datetime.now(timezone.utc) # objeto em utc 00, útil pra posix globais
tempo.isocalendar()[1]# numero da semana do ano

import pytz # pip install pytz

l = pytz.all_timezones # todos os fuso-horários
fuso = pytz.timezone('Asia/Dubai') # fuso horário manual
aplicado = datetime.now(fuso).strftime('%H:%M:%S') # aplica o fuso-horário

from functools import lru_cache

@lru_cache # quando a função executar esse parâmetro denovo, guarda ele no cache
def somas(n):
    return n+1

from collections import *

cliente = namedtuple('cliente',['Nome','Gastos']) # cria uma via de regra
cliente1 = cliente('nometal','gastostal') 
globals()['cliente1'] = cliente('nometal','gastostal') # cria uma tupla nessa via de regra
cliente1._asdict() # transforma o namedtuple em dict
cliente1 = cliente1._replace(Nome='nometal2') # substitui a namedtuple por essa nova com o valor trocado
listaBase = [1,2,3,4,5]
fila = deque(listaBase) #lista que só meche nas extremidades otimizada O(1)
fila.append(6) # adiciona no final
fila.appendleft(0) # adiciona no começo
fila.pop() # remove no final
fila.popleft() # remove no começo
listaBase = list(fila) # converte queue pra lista
lista = Counter(['ab','ab','ac','ac']) # quantas repetições tem cada termo?
palavra = Counter('abacaxi') # quantas repetições tem cada símbolo?

import time

time.sleep(1) # espera tantos segundos pra executar um código
cronometro = time.time() # começa a contar o tempo a apartir daqui
tempoFinal = time.time() # mede o tempo desde o último time.time()
total = cronometro - tempoFinal # tempo percorrido

from abc import ABC, abstractmethod # classe e métodos abstratos

class Abstrata(ABC): # não pode ser instânciada, só herdada
    @abstractmethod # toda classe herdeira DEVE ter uma cópia aplicada de cada método abstrato
    def metodoabstrato(self):
        print('Esse método deve ser implementado na classe herdeira')
    @abstractmethod
    def metodoabstrato2(self):
        print('Esse método também deve ser implementado na classe herdeira')
class Real(Abstrata):
    def metodoabstrato(self):
        print('Usando a classe abstrata como base pra classe real')
    def metodoabstrato2(self):
        print('Todos os métodos abstratos precisam ser implementados')
r = Real().metodoabstrato() # a classe abstrata não pode ser usada aqui, só a real
rr = Real().metodoabstrato2()

import sched # agendar eventos

def evento_agendado(agendador,intervalo,mensagem):
    agendador.enter( # vai chamar uma função com parâmetros a cada tantos segundos
                    intervalo, # tempo entre chamadas
                    1, # prioridade
                    evento_agendado, # chama a função
                    (agendador,intervalo,mensagem)) # com esses argumentos
    print(mensagem) # o que a função vai fazer
agendador = sched.scheduler(time.time,time.sleep) # cria o agendador
evento_agendado(agendador,1,'Essa mensagem é mostrada a cada 1s')
agendador.run() # roda

import smtplib # enviar e-mail
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email_login = "seu@gmail.com"  # Seu endereço de e-mail
email_password = "tem16digitos"  # Senha de app (tem na conta do google)
email_para = "emaildestino@gmail.com"
titulo = f"titulo do email"
conteudo = f"texto do email"
mensagem = MIMEMultipart() # estrutura do e-mail
mensagem["From"] = email_login
mensagem["To"] = email_para
mensagem["Subject"] = titulo
mensagem.attach(MIMEText(conteudo, "plain"))
try:
    server = smtplib.SMTP("smtp.gmail.com", 587) # fazer login e enviar o e-mail
    server.starttls()  
    server.login(email_login, email_password)
    server.sendmail(email_login, email_para, mensagem.as_string())
except Exception as e:
    print(f"Erro ao enviar o e-mail: {e}") # mostra o erro
else:
    print("E-mail enviado com sucesso!")
finally:
    server.quit() # encerra conexão

import sqlite3 # banco de dados

conectar = sqlite3.connect('banco.db') # criar ou conectar
cursor = conectar.cursor()             # interagir com o banco
cursor.execute('''CREATE TABLE IF NOT EXISTS planta (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT,
               price REAL
               )''')                     # comando SQL de criação de tabela
dados_do_banco = [ 
    ('Orquídea',3.4),
    ('Samambaia',6.5),
    ('Rosa',2.3)
]                                       # dados pra inserir
for dado in dados_do_banco:
    cursor.execute("INSERT INTO planta"
                   "(nome,price)"
                   "VALUES (?,?)",dado) # comando sql de inserção dos dados(comando,origemdosdados)
cursor.execute('SELECT * FROM planta') # comando sql de selecionar
linhas = cursor.fetchall() # pega todas as linhas do arquivo.db
for linha in linhas:
    print(f"ID:{linha[0]},Nome:{linha[1]},Price:{linha[2]}")
comandos = {
    'PRAGMA table_info(Tabela)':'metadados da tabela',
    'SELECT * FROM Tabela':'diz o que tem na tabela',
    'SELECT Coluna FROM Tabela WHERE ColunaTal="Tal"':'pega todas as linhas que tem coluna que tem algo igual a algo e diz a coluna',
    'SELECT * FROM Tabela WHERE ColunaTal="Tal"':'pega todas as linhas que tem coluna=algo e diz tudo das linhas',
    'UPDATE Tabela SET colunaQueVaiMudar=Algo WHERE colunaComparativa=Algo':'muda todas as linhas que tem colunaComparativa igual a algo e muda o dado de ColunaQueVaiMudar pra algo',
    'DELETE FROM Tabela WHERE coluna="algo"':'apaga todas as linhas com essa ocorrência',
    '':''
}
conectar.commit()                       # enviar
conectar.close()                        # terminar conexão

from pynput import keyboard # pip install pynput                                 # Pega informações do teclado

def pressionado(tecla): # dizer a tecla pressionada 
    try:
        print(tecla.char)
    except Exception:
        print(tecla)
with keyboard.Listener(on_press=pressionado) as listener: # checar teclas em segundo plano
    listener.join()

from pynput.mouse import Button, Controller                 # informações e acesso ao mouse

teclado = KeyBoardController()
mouse = Controller()         # começa a monitorar o mouse
print(mouse.position)        # diz as coordenadas do mouse
mouse.position = (500, 500)  # modifica o lugar do mouse
mouse.move(100, 0)           # Move 100 pixels para a direita
mouse.move(-100,0)           # Move 100 pixels pra esquerda
mouse.click(Button.left, 1)  # Clica 1x com o botão esquerdo
mouse.click(Button.right,1)  # Clica 1x com o botão direito
mouse.scroll(0, 2)           # scroll pra cima
mouse.scroll(0, -2)          # scroll pra baixo
mouse.scroll(2,0)            # scroll pra direita
mouse.scroll(-2,0)           # scroll pra esquerda

from pynput import keyboard                                 # Pega informações do teclado
from pynput.keyboard import Controller as KeyBoardController,Key# acesso ao teclado

keyboard = KeyBoardController() # Monitora o Teclado
keyboard.press('a')  # Pressiona a tecla
keyboard.release('a')  # Solta a tecla
Key.enter # tecla enter

import pygame # pip install pygame

pygame.init()                                    # inicia a janela
window = pygame.display.set_mode((578,324),pygame.RESIZABLE) # tamanho da janela; quadrado de trocar de resolução
pygame.display.set_caption("Nome da Janela") # nome da janela
pygame.mixer_music.load('') # escolha o audio
pygame.mixer_music.play(-1) # toque o audio
#Image
surf_img = pygame.image.load('caminhodaimagem').convert_alpha()# carrega a imagem, transforma em surface = área do desenho
rect_img = surf_img.get_rect(left=0,top=0)# rectangle = posição que o surf fica(topo esquerdo)
window.blit(source=surf_img,dest=rect_img)               # aplica surface e rectangle na tela
pygame.display.flip()                            # atualiza a janela com todas as modificações feitas do blit
#Text
tamanho = 20 # elementos básicos de um texto
fonte = 'Lucida Sans Typewriter'
texto = 'texto'
cor = (255,255,255)
posicao = (576/2 , 200)
fonteAplicada  = pygame.font.SysFont(name=fonte, size=tamanho) # cria uma fonte pro texto
surf_txt  = fonteAplicada.render(texto, True, cor).convert_alpha() # aplica a cor ao texto e transforma em surface; suporte pra fundo transparente
rect_txt  = surf_txt.get_rect(center=posicao)   # o centro do texto fica na posição                  
window.blit(source=surf_txt, dest=rect_txt)
window.fill((0,0,0)) # preenche a janela inteira com essa cor
pygame.display.flip()
#
rect_txt.centerx # centro horizontal do rect
rect_txt.left    # esqurda do rect
rect_txt.right   # parte direita do rect
rect_txt.x       # coordenada do rect na tela
rect_txt.y       # coordenada do rect na tela
clock = pygame.time.Clock()
while window:                       # em loops infinitos, capture eventos e use blit e flip apenas
    for event in pygame.event.get():# checa os eventos
        if event.type == pygame.QUIT:# tipos de eventos, se clicar no X da tela
            pygame.quit()            # fechar janela
            quit()                   # encerrar pygame
        if event.type == pygame.KEYDOWN: # se apertar tecla
            if event.key == pygame.K_a: pass# checa as teclas, se for 'a'
            if event.key == pygame.K_RETURN: pass        # tecla enter
            if event.key == pygame.K_0: pass             # tecla 0
        if event.type == pygame.KEYUP: # se soltar a tecla
            print(nome_das_teclas := pygame.key.name(event.key)) # diz o nome da tecla apertada
        if event.type == pygame.VIDEORESIZE: pass # se o tamanho da janela mudar
    clock.tick(60) # deixa o jogo a tantos Hz
    fps = f'{clock.get_fps():.0f}' # depois do tick definido, ele diz o fps
    teclas_pressionadas = pygame.key.get_pressed() # diz as teclas que estão sendo pressionadas
    if teclas_pressionadas[pygame.K_0]: pass # se o 0 faz parte das teclas pressionadas
available_fonts = pygame.font.get_fonts()         # lista de fontes disponíveis do sistema operacional
print(available_fonts)

import socket #comunicar com qualquer dispositivo da rede

nome_da_maquina = socket.gethostname() # fala o nome dessa máquina
ip = socket.gethostbyname(nome_da_maquina) # busca o [nome da máquina ou de um domínio] e via DNS diz o IPV4 dele
ip_geral = '0.0.0.0'                       # ip especial onde qualquer máquina pode conectar (servidores usam)
porta = 12345                              # porta de acesso 
socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # socket do servidor(ivp4,tcp)
socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # deixa o servidor elegivel a ser iniciado 1s depois do encerramento
socket_server.bind((ip,porta)) # liga o SOCKET ao IP e PORTA (mesmo pc)
socket_server.bind((ip_geral,porta)) # (cliente de outro dispositivo)
socket_server.listen() # faz o SOCKET permitir conexões
info = socket_server.accept() # aceita uma conexão e diz quem conectou
socket_client = info[0] # socket do cliente
ip_client = info[1][0] # ip do cliente
port_client = info[1][1] # porta do cliente
mensagem_servidor = input("[Server] ").encode() # converte o texto pra bytes
socket_client.send(mensagem_servidor) # envia os bytes pro cliente
mensagem_cliente = socket_client.recv(1024).decode() # decodifica e lê o que o cliente mandou
socket_server.close() # fecha conexão do socket
socket_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # socket do cliente
socket_client.connect((ip,porta))# busca um servidor com esse IP e PORTA
mensagem_servidor = socket_client.recv(1024).decode() # decodifica e lê o que o servidor mandou
print(f"[Server] {mensagem_servidor}")
i = input("[Client] ")
socket_client.send(i.encode()) # envia os bytes pro servidor
socket_client.close() # fecha conexão do socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # ipv4 udp
mensagem,endereco = s.recvfrom(1024) # mensagem em bytes e endereço
s.sendto("enviar".encode(),(ip,porta)) # envia pro endereço
print(s.recvfrom(1024)[0].decode()) # recebe do endereço
name,alias,ip = socket.gethostbyaddr('10.0.1.10') #nome,nomealt e ip de um ip
port = socket.getservbyname('https') # porta de um servidor https
servidor = socket.getservbyport(80) # servidor com essa porta
info = socket.getaddrinfo('www.google.com','https')# muitas informações pra criar sockets
socket_server.settimeout(10) # se o servidor não conectar/interagir em 10s da erro
socket_server.settimeout(None) # pode demorar o quanto for pro handshake/interação
socket_client.settimeout(5) # 5s pro cliente conectar/receber/enviar dados
socket.setdefaulttimeout(5) # todos os sockets criados vão ter timeout 5s

import threading # partes diferentes do programa rodando simultaneamente

def func1(n):
    for each in range(n):
        print(each)
def func2(n):
    for each in range(n):
        print(each)
t1 = threading.Thread(target=func1,args=[5]) # cria um fluxo alternativo que roda uma função target com lista de argumentos args
t2 = threading.Thread(target=func2,args=[5]) # cria outro fluxo
t3 = threading.Thread(target=func2,daemon=True,args=[20])
# daemons não impedem o sistema de terminar, se todos os threads principais terminarem, o programa é encerrado mesmo com o daemon rodando
t1.start() # roda o primeiro fluxo, continua o código
t1.join() # espera thread terminar
t2.start() #roda o outro fluxo
t3.start()
t1.is_alive() # bool dizendo se a thread está rodando
# thread main, que seria o principal do programa
for each in range(5): print(__name__)

import multiprocessing # gera processos(coleção de threads) que tem threads(fluxos)

def func1():
    for each in range(500000):
        print(each)
def func2():
    for each in range(500000):
        print(each)
if __name__ == '__main__': # obrigatório usar no multiprocessing
    p1 = multiprocessing.Process(target=func1) # cria processo que executa a função
    p2 = multiprocessing.Process(target=func2)
    p1.start() # inicia processo
    p2.start() # inicia processo simultâneo
    p1.join() # espera processo finalizar
    p2.join()

from pathlib import Path # no linux é o caminho completo

path = Path('/home/maxinne/Downloads/rasc/algo.txt') # caminho do arquivo
leitura = path.read_text() # ler
linhas = leitura.splitlines() # lista com o conteúdo de cada linha
path.write_text('texto') # sobrescreve o arquivo e/ou cria ele
path.exists() # se o arquivo existe

import json # com Path

sample = ['texto','de','exemplo']
path = Path('/home/maxinne/Downloads/rasc/algo.json') # json
escritajson = json.dumps(sample,indent=4,ensure_ascii=False) # converte python pra json e formata pra suporte UNICODE
path.write_text(escritajson) # sobrescreve json o texto convertido e/ou cria o json
leiturajson = path.read_text() # lê o código json
novasample = json.loads(leiturajson) # converte json pra python
with open("novojson.json",'w') as f: json.dump({},f,indent=4) # salva qualquer dict em json

import requests # Solicitações HTTP  # pip install requests

url = "https://hacker-news.firebaseio.com/v0/item/31353677.json" # link de um json
url = "https://en.wikipedia.org/wiki/Web_scraping" # link regular
url = "https://tabok.s3.eu-central-1.amazonaws.com/tabs_ready/Metallica%20-%20Don%27t%20Tread%20On%20Me.pdf" # link de um pdf
resp:requests.Response = requests.get(url) # solicitação GET HTTP, retorna um objeto Response
status = resp.status_code # vê status da solicitação HTTP ,200 se o link abre, 404 se não existir
respostaJson = resp.json() # SE o link for .json; pega a resposta json e transforma em dict
repr_str = resp.text # pega a representação da página em str (html em str,json em str, ou binário em str)
binar = resp.content # pega a representação da página em binário, útil pra mídias e docs
with open("nomeDoArquivo.algumacoisa","wb") as f: f.write(binar) # baixa qualquer tipo de mídia de um site, usando binário

from bs4 import BeautifulSoup # filtra conteúdos de um HTML # pip install beautifulsoup4

soup = BeautifulSoup(features="html.parser",markup=repr_str) # objeto parser
tag = soup.find_all('span') # filtra todas as ocorrências dessa tag HTML
tag = soup.find_all('img',src=lambda src : str(src).endswith('.png')) # filtra formatos
conteudo = [each.text for each in tag] # pega o conteúdo dessas tags
for atributes in tag:
    a = atributes.get('width') # pega o atributo de uma tag
    url_do_elemento = atributes.get('src') # pega a url de um elemento

from urllib.parse import urljoin # transforma URLs

url_de_acesso = urljoin(url,url_do_elemento) # transforma a url do elemento em uma url de acesso

from flask import * # microframework pra manipular websites # pip install flask
# tome bastante cuidado com a sintaxe no html, erros implícitos são sutís (principalmente vírgulas nas tags)
# o url é http://127.0.0.1:5000/ e depois disso, o tratamento individual é feito com o @app.route()
app = Flask(__name__) # objeto da aplicação web / api

option = 1

@app.route("/",methods=['GET']) # faz o roteamento dos endpoints da api;página principal que só é acessada por navegador ou requests.get
def index():
    if option == 1:
        return 'Texto qualquer no site' # texto genérico na tela
    if option == 2:
        return render_template('arquivohtml.html') # carrega página html
    if option == 3:
        return redirect(url_for('form'),param=1,param=2)# vai pra url da função especificada; pode passar argumentos pra função
    if option == 4:
        if request.method == 'GET': # entrar no site, ou usar requests.get()
            if option == 'json':
                return jsonify('dado') # Pelo Método GET, da pra pegar um arquivo .json
            if option == 'query':
                query = request.args.get('q') # pega o valor de ?q= na url
        
@app.route("/formulario",methods=['GET','POST']) # site acessável, que tem um formulário no html
# o formulário html DEVE ter method="POST" e action="/caminhoDoRouteDoForm"
def form():
    if option == 5:
        if request.method == 'POST':
            dados = request.form.get('atributoNAMEDoElementoHtmlDoForm') # pega a resposta de um elemento do form, após o clique do botão submit
            
@app.route("/formulario/<var>",methods=["GET"]) # filtra argumentos via url OU urls que não correspondem
def alternatives(var):
    if var == 'resultado' : return jsonify(var)
    if var != 'resultado' : return redirect(url_for(index))

@app.route("/favicon.ico",methods=['GET']) # colocar ícone no site
def icon():#carregue o arquivo favicon.ico do tipo .icon na pasta static
    return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__' :
    app.run(debug=True) # roda o WSGI pro Servidor Web rotear a aplicação web; o debug atualiza modificações no arquivo python só com F5
    

import dis

cpython = dis.Bytecode(function) # lista com o bytecode otimizado pelo interpretador

import psutil #informações do sistema

for interface_de_rede,detalhes in psutil.net_if_addrs().items():
    print(interface_de_rede) # interface de rede
    for each in detalhes:
        print(f"Família : {each.family}") # familia do ip
        print(f"Endereço : {each.address}") # endereço de ip
        print(f"Máscara de rede : {each.netmask}") # mascara de rede
        print(f"Endereço de broadcast : {each.broadcast}") # endereço de broadcast
        print(f"ptp-Vpn : {each.ptp}") # conexões point-to-point
familias = {
    'AF_INET' : 2, # IPV4
    'AF_INET6' : 10, # IPV6
    'AF_PACKET' : 17 # ENDEREÇO MAC (linux)
}
for interface_de_rede,detalhes in psutil.net_if_stats().items():
    print(interface_de_rede)
    print(detalhes.isup) # se a interface de rede está ativa
    print(detalhes.duplex) # tipo da comunicação duplex
    print(detalhes.speed) # velocidade máxima em megas
    print(detalhes.mtu) # tamanho máximo de pacotes
    print(detalhes.flags) # indicadores da interface (up,running,broadcast,multicast,loopback)
mss = [val.mtu - 40 for k,val in psutil.net_if_stats().items()]# tamanho máximo de pacote que a camada de rede de cada interface pode enviar (bytes)

for interface_de_rede,detalhes in psutil.net_io_counters(pernic=True).items():
    print(interface_de_rede)
    print(detalhes)# informações do envio e recepção de bytes e pacotes das interfaces de rede
for con in psutil.net_connections(kind='inet'): # conexões ativas
    print(con)
for p in psutil.process_iter(['pid','name','username']): # processos
    print(p.info['pid'])
    print(p.info['name'])
    print(p.info['username'])
    print()
pid = 3082
process = psutil.Process(pid)
for conn in process.connections(): # vê as conexões que esse processo faz
    print(f"Tipo: {conn.type}, Status: {conn.status}, Local: {conn.laddr}, Remoto: {conn.raddr}")
uso_cpu = psutil.cpu_percent(interval=1) # porcentagem do uso da cpu
nucleos = psutil.cpu_count(logical=True) # quantidade de núcleos do cpu
ram = psutil.virtual_memory() # informações da ram
ram.total # total de ram do sistema em bytes
ram.available # ram disponível
ram.used # ram usada
ram.percent # porcentagem de ram usada
for particao in psutil.disk_partitions(): # partições do disco
    particao.device # dispositivo
    particao.mountpoint # ponto de montagem
    particao.fstype # esquema de arquivos
    psutil.disk_usage(particao.mountpoint).total # total de espaço de um disco (bytes)
    psutil.disk_usage(particao.mountpoint).used # total usado
    psutil.disk_usage(particao.mountpoint).free  # total livre
    psutil.disk_usage(particao.mountpoint).percent # porcentagem
psutil.cpu_freq().current # Frequencia atual da cpu
psutil.cpu_freq().min # menor frequencia possivel da cpu, abaixo é underclock
psutil.cpu_freq().max # maior frequencia possivel da cpu, acima é overclock
for dispositivo, temperaturas in psutil.sensors_temperatures().items():#temperaturas
    print(dispositivo)
    for temperatura in temperaturas:
        temperatura.current # temperatura atual
        temperatura.high # temperatura máxima
psutil.Process(1) # várias informações de um PID
psutil.process_iter() # iterador com dados de todos os PIDs
psutil.pids() # lista de pids ativos
psutil.pid_exists(1) # diz se um pid está ativo

import platform

platform.system() # sistema operacional
platform.machine() # arquitetura do processador
platform.node() # nome do host

import pprint

pprint.pprint('') # identa um objeto

import ipaddress

ipv4 = '10.0.1.10'
ipv6 = 'fe80::22e9:17ff:fe07:2978'
obj4 = ipaddress.ip_address(ipv4) # objeto ipv4
obj6 = ipaddress.ip_address(ipv6) # objeto ipv6
obj4.version # 4 se for ipv4 e 6 se for ipv6
obj4.reverse_pointer # domínio ptr (ip mais legível)
obj4 = obj4 + 1 # operações com ip
obj4 = obj4 - 1
str(obj4) == '10.0.1.10' # str do ip
obj4.is_private # se é privado
obj4 > obj4-1 # compara ips

import pickle

with open('objeto.pkl','wb') as f: # preciso salvar um objeto na memória?
    pickle.dump([1,2,3],f)
with open('objeto.pkl','rb') as f: # preciso ler um objeto da memória?
    objeto_na_memoria = pickle.load(f)
print(objeto_na_memoria)

#segurança
import hashlib
import cryptography
import pytest
import ssl
import re
#redes
import paramiko
import http.client
import scapy
import ftplib # transferência de arquivos
import select # manuseia vários sockets e faz mais de um cliente conectar com um servidor
import socketserver # framework de sockets
#analise
import sqlalchemy
#backend
import django
import fastapi
import asyncio
import aiohttp
import gunicorn
import jinja2
#desktop
import customtkinter as ct # extensao do tkinter
