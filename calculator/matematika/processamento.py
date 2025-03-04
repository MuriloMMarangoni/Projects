import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
from datetime import *# contas de datas

#cambio relativo ao dolar ( futuramente vai ser implementado via API)
moedas = {
    'USD':1,
    'BRL':0.173,
    'EUR':1.05
}

def conversao_moeda(cambio:dict,de:str,para:str,quantidade:float) -> float:
    '''
    Converte uma moeda pra outra usando o Dólar como base
    '''
    return f'{quantidade * (cambio[de] / cambio[para]):.2f}'

conversao_moeda(moedas,'USD','BRL',1)

# peso relativo a gramas
peso = {
    'g':1,
    'kg':1_000,
    't':1_000_000,
    'mg':0.001,
    'lb':453.592
}

#constantes matemáticas
const = {
    'PI':3.141,
    'e':2.718
}

#distâncias relativas a metros
distancia = {
    'm':1,
    'km':1_000,
    'cm':0.01,
    'mm':0.001,
    'mi':1_609.344
}

def data_dif(de:list,para:list)->int:
    '''
    Quantos dias se passaram (+), Quantos dias faltam (-)
    '''
    if len(de) != len(para) != 3: return -1
    d1 = date(*de)
    d2 = date(*para)
    return (d1 - d2).days

print(data_dif([2025,3,3],[2025,3,31]))

#quantos dias tem cada mês
mes = {
    'jan':31,
    'fev':[28,29],
    'mar':31,
    'abr':30,
    'mai':31,
    'jun':30,
    'jul':31,
    'ago':31,
    'set':30,
    'out':31,
    'nov':30,
    'dez':31
}
# tempo relativo a segundos
tempo = {
    's':1,
    'm':60,
    'h':3_600,
    'd':86_400,
    'm':[2_419_200,2_505_600,2_592_000,2_678_400],
    'a':[31_536_000,31_622_400]
}

def is_leap(year:int) -> bool | None:
    '''
    Se um ano é bissexto
    '''
    if year < 1: return None

    return True if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0) else False

def is_segundo_grau(equacao:str):
    '''
    Diz se uma equação é do segundo grau
    '''
    return True if ('**2' or '^2') in equacao else False
def bhaskara(equacao:str,complexo:bool=True):
    '''
    Valores, ou valor de x que faz y = 0
    '''
    if complexo: x = sp.symbols('x')
    else: x = sp.symbols('x',real=True)

    eq = parse_expr(equacao,transformations='all')
    return sp.solve(eq,x)

equacao = "x**2-1"
print(bhaskara(equacao))
print(is_segundo_grau(equacao))

print(bhaskara('2*x**2+x-1'))