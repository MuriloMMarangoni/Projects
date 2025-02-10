# o objetivo desse script é aquecer pra sessões de programação, com questões de TI, matemática e lógica
import random
def primeiro_metodo(): # obsoleto, só deixo aqui pra referência
    sinais = ['+','-','*','/','**','**(1/2)'] # sinais

    sinal_aleatorio:str = random.choice(sinais) # escolhe sinal aleatório
    if sinal_aleatorio == '**(1/2)':
        n = random.choice([x**2 for x in range(0,11)])
    else:
        n = random.randint(0,100) # qualquer número

    if sinal_aleatorio == '/': # 0 não pode estar no denominador
        m = random.randint(1,100)
    elif sinal_aleatorio == '**(1/2)':
        m = 2
    elif sinal_aleatorio == '**':
        m = random.randint(0,3)
    else:
        m = random.randint(0,100)

    if sinal_aleatorio == '**(1/2)':
        expressao = f"{n} {sinal_aleatorio}"
    else:
        expressao = f"{n} {sinal_aleatorio} {m}"
    print(expressao)

    if sinal_aleatorio == '/' or sinal_aleatorio == '**(1/2)':
        resultado = f"{eval(expressao):.2f}" # se for divisão, arredondar pra 2 casas
    else:
        resultado = eval(expressao)

    inp = input("")
    if str(resultado)[-3:] == '.00': # se terminar com casa decimal 00 arredonda logo
        resultado = int(float(resultado))
    if str(resultado) in inp: # permite não precisar formatar
        print('Correto')
    else:
        print('Incorreto')

    print(resultado)

sinais = ['+','-','*','/','**','**(1/2)','fatorar','%','%%','pa','pg']
aleatorio = random.choice(sinais)
n = 1
m = 1
match(aleatorio):
    case '/':
        n = random.randint(0,100)
        m = random.randint(1,100)
    case '**':
        n = random.randint(0,100)
        m = random.randint(2,3)
    case '**(1/2)':
        n = random.choice([x**2 for x in range(0,20)])
    case 'fatorar':
        n = random.randint(2,100)
    case '%':
        n = random.randint(1,100)
        m = random.randint(1,100)
    case '%%':
        n = random.randint(1,100)
        m = random.randint(1,100)
    case _:
        n = random.randint(0,100)
        m = random.randint(0,100)


def fatorar(number:int):
    numeros = [x for x in range(2,101)]
    fatores = []
    for each in numeros:
        while number % each == 0:
            fatores.append(each)
            number //= each
    a = ''
    for each in fatores:
        a += f"{each}*"

    if len(fatores) == 1: return 'primo'

    return a[:-1]

operacoes = {
    '+': f'{n} + {m}',
    '-': f'{n} - {m}',
    '*': f'{n} * {m}',
    '/': f'{n} / {m}',
    '**': f'{n} ** {m}',
    '**(1/2)': f'{n} ** (1/2)',
    'fatorar':fatorar(n),
    '%':f'{(n / m)*100}',
    '%%': f'{(n/100)*m}',
    'pa':'',
    'pg':'',
}

resultado = operacoes[aleatorio]
if aleatorio == 'fatorar':
    print(f"Fatorar {n}")
    i = input('')
    if i == resultado:
        print('Correto')
    else:
        print('Incorreto')
    print(resultado)
elif aleatorio == '%':
    print(f"Quantos % {n} é de {m}?")
    i = input('')
    final = float(f"{eval(resultado):.2f}")
    if str(final)[-2:] == '.0':
        final = int(final)
    if str(i) == str(final):
        print('Correto')
    else:
        print('Incorreto')
    print(f"{final} %")
elif aleatorio == '%%':
    print(f"Quantos é {n}% de {m}?")
    i = input('')
    final = float(f"{eval(resultado):.2f}")
    if str(final)[-2:] == '.0':
        final = int(final)
    if str(i) == str(final):
        print('Correto')
    else:
        print('Incorreto')
    print(f"{final} %")
elif aleatorio == 'pa':
    sinais = ['-','+'] # mais ou menos 
    escolha = random.choice(sinais) # pa positiva ou negativa
    num = random.randint(1,100) # primeiro termo de 1 a 100
    r = random.randint(1,num) # a razão tem que ser menor que o primeiro termo porque sim
    seq = [num]
    for each in range(1,5):
        seq.append(eval(f"{seq[-1]}{escolha}{r}"))
    print('Qual é a razão da Progressão Aritmética?')
    print(seq)
    i = input("")
    if escolha == '-': r = int(f"-{r}")
    if i == f"{str(r)}": print('Correto')
    else:
        print('Incorreto')
        print(r)
elif aleatorio == 'pg':
    sinal = random.choice(['*','/'])
    l = []
    n = random.randint(1,100)
    m = random.randint(2,10)
    l.append(n)
    if sinal == '/':
        for each in range(1,5):
            l.append(float(f"{ float(l[-1]) / m :.2f}"))
    elif sinal == '*':
        for each in range(1,5):
            l.append(int(f"{int(l[-1])*m}"))
    print('Qual é a razão da Progressão Geométrica?')
    print(l)
    i = input('')
    if i == str(m):
        print('Correto')
    else:
        print('Incorreto')
        print(m)
else:
    print(resultado)
    i = input('')
    final = float(f"{eval(resultado):.2f}")
    if str(final)[-2:] == '.0':
        final = int(final)
    if str(i) == str(final):
        print('Correto')
    else:
        print('Incorreto')
    print(final)

