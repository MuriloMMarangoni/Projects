# o objetivo desse script é aquecer pra sessões de programação, com questões de TI, matemática e lógica
import random

def primeiro_metodo(): # ideia inicial, foco em fazer o core do script
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
def segundo_metodo(): # ideia encorpada, várias funcionalidades, mas sem organização
    PI = 3.14
    sinais = ['+','-','*','/','**','**(1/2)','fatorar','%','%%','pa','pg','area','volume','m','not','xor','or','and']
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
        'area':'',
        'volume':'',
        'm':'',
        'not':'',
        'or':'',
        'xor':'',
        'and':''
    }

    def area():
        figura = random.choice(['quadrado','triângulo','círculo'])
        l = random.randint(2,20)
        h = random.randint(2,20)
        formula = {
            'quadrado': l*l,
            'triângulo':l*h / 2,
            'círculo': PI*l*l
        }
        match (figura):
            case 'quadrado': 
                print(f"Qual é a área de um quadrado com lado {l}")
                i = input('')
                if i == f"{formula['quadrado']:.2f}":
                    print('Correto')
                    return 0
                else:
                    print('Incorreto')
                    print(f"{formula['quadrado']:.2f}")
            case 'triângulo':
                print(f"Qual é a área de um triângulo com base {l} e altura {h}")
                i = input('')
                if i == f"{formula['triângulo']:.2f}":
                    print('Correto')
                    return 0
                else:
                    print('Incorreto')
                    print(f"{formula['triângulo']:.2f}")
            case 'círculo':
                print(f"Qual é a área de uma circunferência de raio {l}")
                i = input('')
                if i == f"{formula['círculo']:.2f}":
                    print('Correto')
                    return 0
                else:
                    print('Incorreto')
                    print(f"{formula['círculo']:.2f}")
                    
    def volume():
        figura = random.choice(['cubo','pirâmide','esfera'])
        l = random.randint(2,20)
        h = random.randint(2,20)
        formula = {
            'cubo': f'{l * l * l:.2f}',
            'pirâmide':f'{l*h / 3:.2f}',
            'esfera': f'{(float(f"{4/3:.2f}")) * PI * l*l*l:.2f}'
        }
        match (figura):
            case 'cubo':
                print(f"Qual é o volume de um cubo de lado {l}?")
                i = input('')
                if i == formula['cubo']:
                    print('Correto')
                    return 0
                print('Incorreto')
                print(formula['cubo'])
            case 'pirâmide':
                print(f"Qual é o volume de uma pirâmide de base {l} e altura {h}?")
                i = input('')
                if i == formula['pirâmide']:
                    print('Correto')
                    return 0
                print('Incorreto')
                print(formula['pirâmide'])
            case 'esfera':
                print(f"Qual é o volume de uma esfera de raio {l}?")
                i = input('')
                if i == formula['esfera']:
                    print('Correto')
                    return 0
                print('Incorreto')
                print(formula['esfera'])
    def mem():
        memory1 = { # quanto que é relativo aos bytes
            'b': 1,
            'kb': 1024
        }
        memory2 = {
            'mb': 1024 * 1024,
            'gb': 1024 * 1024 * 1024
        }

        primeira = random.choice([*memory1.keys()])
        segunda  = random.choice([*memory2.keys()])
        num = random.randint(1,100)
        resposta = num * (memory2[segunda]//memory1[primeira])
        print(f"Quantos {primeira} tem em {num} {segunda}")
        i = input('')
        if i == str(resposta):
            print('Correto')
            return 0
        print('Errado')
        print(resposta)

    def not_bitwise():
        '''
        n xor mascara = not n
        '''
        n = random.randint(1,100)
        print(f"~ {n}")
        i = input("")
        tamanho = int.bit_length(n) # 5
        b = '0b'
        for each in range(0,tamanho):
            b += '1'
        mascara = int(b,base=2)
        if i == str(n ^ mascara):
            print('Correto')
            return 0
        print('Errado')
        print(n ^ mascara)
    def and_bitwise():
        n = random.randint(1,100)
        m = random.randint(1,100)
        r = n & m
        print(f'{n} & {m}')
        i = input()
        if i == str(r):
            print('Correto')
            return 0
        print('Errado')
        print(r)
    def or_bitwise():
        n = random.randint(1,100)
        m = random.randint(1,100)
        r = n | m
        print(f'{n} | {m}')
        i = input()
        if i == str(r):
            print('Correto')
            return 0
        print('Errado')
        print(r)
    def xor_bitwise():
        n = random.randint(1,100)
        m = random.randint(1,100)
        r = n ^ m
        print(f'{n} ^ {m}')
        i = input()
        if i == str(r):
            print('Correto')
            return 0
        print('Errado')
        print(r)

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
    elif aleatorio == 'area':
        area()
    elif aleatorio == 'volume':
        volume()
    elif aleatorio =='m': mem()
    elif aleatorio =='not': not_bitwise()
    elif aleatorio =='and': and_bitwise()
    elif aleatorio =='xor': xor_bitwise()
    elif aleatorio =='or': or_bitwise()
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

