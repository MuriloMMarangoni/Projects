import matplotlib.pyplot as plt
import pandas as pd
import sympy as sp
import numpy as np
def manual():
    '''
    Essa função diz quais operações podem ser utilizadas
    '''
    print(64*"-")
    print("log(resultado,base) -> logaritmo")
    print("E                   -> 2.718...")
    print("pi                  -> 3.1415...")
    print("*                   -> multiplicação")
    print("**                  -> potência")
    print("**(1/2)             -> raiz quadrada")
    print("sin(rad)            -> seno em radiano")
    print("cos(rad)            -> cosseno em radiano")
    print("tan(rad)            -> tangente em radiano")
def expr():
    '''
    Calcula o resultado de uma Expressão numérica
    '''
    valores = 0
    while valores != '':
        funcao = input(f"Insira uma expressao:\n->")
        if funcao == '':
            break
        try:
            f = sp.lambdify(sp.Symbol(''), sp.sympify(funcao),'numpy')
            lista = []
            y = f(np.array(lista))
        except Exception:
            print(64*"-","\n","! Operação Inválida","\n"+64*"-")
            continue
        else:
            if funcao == str(y):
                print(64*"-","\n","! Operação Inválida","\n"+64*"-")
            else:
                print(64*"-",'\n',y,'\n'+64*"-")
def fun():
    '''
    Usa valores de x em uma função
    '''
    valores = 1
    while valores != '':
        lista = []
        try:
            funcao = input("Insira uma função de x:\n")
            if funcao == '':
                break
            if 'x' not in list(funcao):
                print(64*"-","\n","! Dados Inválidos","\n"+64*"-")
                continue
            f = sp.lambdify(sp.Symbol('x'), sp.sympify(funcao),'numpy')
        except Exception:
            print(64*"-","\n","! Dados Inválidos","\n"+64*"-")
            continue
        else:
            while valores != '':
                valores = 0
                valores = input(f"Insira os valores específicos de: {funcao}\n")
                if valores == '':
                    break
                try:
                    valores = float(valores)
                except Exception:
                    print(64*"-","\n","! Dados Inválidos","\n"+64*"-")
                    continue
                else:
                    lista.append(valores)
            try:
                y = f(np.array(lista))
                i = 0
                for n in y:
                    print(lista[i] ,' | ', y[i])
                    i = i + 1
            except Exception:
                print(64*"-","\n","! Dados Inválidos","\n"+64*"-") 
                continue
            else:
                valores = 1
                continue
def fungraf():
    '''
    Mostra o período de uma função em um gráfico simples
    '''
    valores = 0
    while valores != '':
        try:
            funcao = input("Insira uma função de x:\n")
            if funcao == '':
                break
            if 'x' not in list(funcao):
                print(64*"-","\n","! Dados Inválidos","\n"+64*"-")
                continue
            f = sp.lambdify(sp.Symbol('x'), sp.sympify(funcao),'numpy')
            x0 = input("Período onde o gráfico que começa\n")
            if x0 == '':
                break
            fx0 = sp.lambdify(sp.Symbol(''), sp.sympify(x0),'numpy')
            xf = input("Quando o gráfico termina\n")
            if xf == '':
                break
            fxf = sp.lambdify(sp.Symbol(''), sp.sympify(xf),'numpy')
        except Exception:
                print(64*"-","\n","! Dados Inválidos","\n"+64*"-")
                continue
        else:
            lista = []
            try:
                x0 = fx0(np.array(lista))
                xf = fxf(np.array(lista))
                x = np.linspace(x0,xf,100)
                y = f(x)
                plt.plot(x,y,color='blue')
                plt.show()
            except Exception:
                print(64*"-","\n","! Dados Inválidos","\n"+64*"-")
                continue
def graf():
    '''
    Mostra gráficos customizáveis
    '''
    opcao = 0
    lista = []
    while opcao != '':
        print(64*"-")
        print("1 - Função")
        print("2 - Lista de Pontos")
        print("3 - Pontuado")
        print("4 - Barra Vertical")
        print("5 - Barra Horizontal")
        print("6 - Pizza")
        print("ENTER - Sair")
        opcao = input('-> ')
        if opcao == '':
            break
        try:
            opcao = int(opcao)
        except Exception:
            continue
        else:
            match(opcao):
                case 1: 
                        valores = 0
                        while valores != '':
                            try:
                                print(64*"-")
                                funcao = input("Insira uma função de x:\n")
                                if funcao == '':
                                    break
                                if 'x' not in list(funcao):
                                    print(64*"-","\n","! Dados Inválidos","\n"+64*"-")
                                    continue
                                f = sp.lambdify(sp.Symbol('x'), sp.sympify(funcao),'numpy')
                                print(64*"-")
                                x0 = input("Período onde o gráfico que começa\n")
                                if x0 == '':
                                    break
                                fx0 = sp.lambdify(sp.Symbol(''), sp.sympify(x0),'numpy')
                                print(64*"-")
                                xf = input("Quando o gráfico termina\n")
                                if xf == '':
                                    break
                                fxf = sp.lambdify(sp.Symbol(''), sp.sympify(xf),'numpy')
                            except Exception:
                                print(64*"-","\n","! Dados Inválidos","\n"+64*"-")
                                continue
                            else:
                                lista = []
                                font = {'family':'serif',
                                        'color':'black',
                                        'size':12}
                                try:
                                    x0 = fx0(np.array(lista))
                                    xf = fxf(np.array(lista))
                                    x = np.linspace(x0,xf,(int(xf)-int(x0)))
                                    y = f(x)
                                    print(64*"-")
                                    print("Insira a cor do gráfico:")
                                    print("r - Vermelho\nb - Azul\ng - Green\nk - Preto\nm - Magenta")
                                    print(64*"-")
                                    cor = input("")
                                    print(64*"-")
                                    print("Insira a marcação do gráfico:")
                                    print("o - Ponto Grande\n. - Ponto Pequeno")
                                    print(64*"-")
                                    marcacao = input("")
                                    print(64*"-")
                                    print("Insira o estilo de linha do gráfico:")
                                    print("- - Linha Comum\n-- - Linha Riscada\n: - Linha Pontuada")
                                    print(64*"-")
                                    linha = input("")
                                    print(64*"-")
                                    grade = input("O gráfico tem grade?(S/N):\n")
                                    if grade == 'S':
                                        plt.grid()
                                    plt.xlabel('x', fontdict=font)
                                    plt.ylabel("f(x)", fontdict=font)
                                    plt.title(f"f(x) = {funcao}",fontdict=font)
                                    plt.plot(x,y,color=cor,marker=marcacao,linestyle=linha)
                                    plt.axis((x0,xf,f(x0),f(xf)))
                                    print(64*"-")
                                    plt.show()
                                except Exception:
                                    print(64*"-","\n","! Dados Inválidos","\n"+64*"-")
                                    continue
                case 2: 
                    listax = []
                    listay = []
                    x = 0
                    y = 0
                    while x != '' and y != '':
                        try:
                            x = input("Escreva valores de x\n")
                            if x == '':
                                break
                            x = float(x)
                            y = input("Escreva valores de y\n")
                            if y == '':
                                break
                            y = float(y)
                        except Exception:
                            print(64*"-","\n","! Dados Inválidos","\n"+64*"-")
                            continue
                        else:
                            listax.append(x)
                            listay.append(y)
                    if len(listax) < 2:
                        print(64*"-","\n","! O gráfico precisa de pelo menos 2 pontos","\n"+64*"-")
                        continue
                    x = np.array(listax)
                    y = np.array(listay)
                    plt.plot(x,y)
                    plt.axis((x.min(),x.max(),y.min(),y.max()))
                    plt.show()
                case 3:
                    listax = []
                    listay = []
                    x = 0
                    y = 0
                    while True:
                        x = input("Insira um valor de x:\n")
                        y = input("Insira um valor de y:\n")
                        if x == '' or y == '':
                            break
                        try:
                            x = float(x)
                            y = float(y)
                        except Exception:
                            print(64*"-","\n","! Dados Inválidos","\n"+64*"-")
                            continue
                        else:
                            listax.append(x)
                            listay.append(y)
                    if len(listax) < 2:
                        print(64*"-","\n","! O gráfico precisa de pelo menos 2 pontos","\n"+64*"-")
                        continue
                    plt.scatter(listax,listay,s=50)
                    plt.show()
                case 4:
                    barras = []
                    valores = []
                    while True:
                        barra = input("Insira o que a barra representa:\n")
                        valor = input("Insira o valor da barra:\n")
                        if barra == '' or valor == '':
                            break
                        try:
                            valor = float(valor)
                        except Exception:
                            print(64*"-","\n","! Dados Inválidos","\n"+64*"-")
                            continue
                        else:
                            barras.append(barra)
                            valores.append(valor)
                            continue
                    plt.bar(barras,valores,width=0.5)
                    plt.show()
                case 5:
                    barras = []
                    valores = []
                    while True:
                        barra = input("Insira o que a barra representa:\n")
                        valor = input("Insira o valor da barra:\n")
                        if barra == '' or valor == '':
                            break
                        try:
                            valor = float(valor)
                        except Exception:
                            print(64*"-","\n","! Dados Inválidos","\n"+64*"-")
                            continue
                        else:
                            barras.append(barra)
                            valores.append(valor)
                            continue
                    plt.barh(barras,valores,height=0.5)
                    plt.show() # barra horizontal
                case 6:
                    amostra = 0
                    cores=[]
                    nomes=[]
                    while True:
                        try:
                            nome = input("Insira um nome pra fatia\n")
                            cor = input("Insira a cor da fatia:\n")
                            amostra = input("Adicione um valor à amostra:\n")
                            if amostra == '' or cor =='' or nome == '':
                                break
                            amostra = float(amostra)
                        except Exception:
                            print(64*"-","\n","! Dados Inválidos","\n"+64*"-")
                            continue
                        else:
                            lista.append(amostra)
                            cores.append(cor)
                            nomes.append(nome)
                    plt.pie(lista,colors=cores,labels=nomes)
                    plt.show()
def listas():
    lista = []
    while True:
        elemento = input("Adicione um valor à amostra:\n")
        if elemento == '':
            break
        try:
            elemento = float(elemento)
        except Exception:
            print(64*"-","\n","! Dados Inválidos","\n"+64*"-")
            continue
        else:
            lista.append(elemento)
    lista = pd.Series(lista)
    tamanho = lista.size
    organizado = np.sort(lista)
    media = lista.mean() 
    moda = lista.mode().iloc[0]
    mediana = lista.median() 
    desvio_padrao = lista.std()
    variancia = lista.var()
    print(64*"-")
    print(f"| Tamanho : {tamanho}")
    print(f"| Lista Organizada : {organizado}")
    print(f"| Média : {media}")
    print(f"| Moda : {moda}")
    print(f"| Mediana : {mediana}")
    print(f"| Variância : {variancia}")
    print(f"| Desvio Padrão : {desvio_padrao}")
menu = 0
while menu != '':
    print(64*"-")
    print("1 - Expressões Numéricas")
    print("2 - Valores de uma Função")
    print("3 - Gráfico de uma Função")
    print("4 - Gráfico de dados")
    print("5 - Operações com Listas")
    print("0 - Manual")
    print("ENTER - Sair")
    menu = input('-> ')
    if menu == '':
        break
    try:
        menu = int(menu)
    except Exception:
        continue
    else:
        match(menu):
            case 0: manual()
            case 1: expr()
            case 2: fun()
            case 3: fungraf()
            case 4: graf()
            case 5: listas()