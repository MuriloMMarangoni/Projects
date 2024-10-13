# função de quantidade no estoque, avisar quando estiver 0, colocar mais no estoque quando chegar do depósito
# gerar relatório do dia, juntar os 7 pro da semana , e os 28/29/30/31 pro mês
from collections import namedtuple
from pathlib import Path
import json
import subprocess

sample:namedtuple = namedtuple('sample',['codigo','nome','preco']) # formato de inserção do produto no json
nome:str = ''
preco:float = 0
l:list[namedtuple] = [] 
d:list[dict] = []
opcao:str = '1' # opção do menu, se for qualquer coisa fora de 1234 fecha o loop
dados:json = [] # lista de dicionários -> json

def gerarCodigosDeBarra():
    '''
    Gerar um pdf com cada código de barras de cada produto
    '''
    pass

def gerarNota():
    '''
    Gera a nota com os gastos e o horário de emissão
    '''
    pass

def caminho(): 
    '''
    procura o json uma pasta acima desse arquivo
    '''
    diretorio = __file__.split('/')
    caminho_do_json = '/'
    for each in diretorio[1:-2]:
        caminho_do_json += f'{each}/'
    del diretorio
    caminho_do_json += 'produtos.json'
    path = Path(caminho_do_json)
    if path.exists():
        return caminho_do_json
    del path
    subprocess.run('touch produtos.json',shell=True)
    return caminho_do_json

path = Path(caminho())

def adicionar_produto():
    '''
    Adiciona um produto no json, se o produto já existir ele altera o preço automaticamente
    '''
    nome = input("Insira o nome:\n")
    try:
        preco = input('Insira o preço:\n')
        if ',' in preco:
            preco = preco.replace(',','.')
        l.append(sample(None,nome.strip().title(),float(preco)))
    except ValueError:
        print('! Dados Inválidos')
    else:
        for each in l:
            d.append(each._asdict()) # namedtuple pra dict
        with (open(path,'r')) as file: # pega o que está no json, se não tiver nada coloca []
            try:
                dados = json.load(file)
            except json.JSONDecodeError: # se estiver vazio coloca um [] pra depois reescrever o json
                path.write_text(json.dumps([],indent=4,ensure_ascii=False))
            else:
                if (len(d) != 0):
                    nomes = [each['nome'] for each in dados]
                    for each in d:
                        if each['nome'] not in nomes:
                            dados.append(*d)
                        else:
                            for another_each in dados:
                                if another_each['nome'] == each['nome']:
                                    another_each.update({'preco':each['preco']})
        for each in dados:
            each.update({'codigo': dados.index(each)+1}) # atribui os códigos pra cada produto do json(antigo+novo)
        escritajson = json.dumps(dados,indent=4,ensure_ascii=False)
        path.write_text(escritajson)
        d.clear() # limpa as listas pra poderem ser usadas posteriormente
        l.clear()
        dados.clear()
def remover_produto():
    '''
    Se o produto existir, ele remove o produto pelo código
    '''
    with (open(path,'r')) as file:
        try:
            dados = json.load(file)
        except json.JSONDecodeError:
            print('Nenhum Produto Registrado.')
        else:
            if dados == []:
                print('Nenhum Produto Registrado.')
            else:
                print('Insira o Código do produto que vai ser removido (0 pra cancelar)')
                i = int(input(''))
                if i != 0:
                    for each in dados:
                        if each['codigo'] == i:
                            del dados[dados.index(each)]
                            for each in dados:
                                each.update({'codigo': dados.index(each)+1})
                            escritajson = json.dumps(dados,indent=4,ensure_ascii=False)
                            path.write_text(escritajson)
                            dados.clear()
                del i           
def ver_json():
    '''
    Mostra o conteúdo do json, pode ser exibido de várias formas
    '''
    with (open(path,'r')) as file:
        try:
            dados = json.load(file)
        except json.JSONDecodeError:
            print('Nenhum Produto Registrado.')
        else:
            if dados == []:
                print('Nenhum Produto Registrado.')
            else:
                print('1 - Código\n2 - Preço Maior\n3 - Preço Menor\n4 - A-Z\n5 - Z-A')
                i = input('')
                match (i):
                    case '1':
                        for each in dados:
                            print(each)
                    case '2':
                        temp = []
                        tempd = []
                        for each in dados:
                            temp.append(each['preco'])
                        temp.sort(reverse=True)
                        for each in temp:
                            for another_each in dados:
                                if (each == another_each['preco']) and (another_each not in tempd):
                                    tempd.append(another_each)
                        for each in tempd:
                            print(each)
                        del temp
                        del tempd
                    case '3':
                        temp = []
                        tempd = []
                        for each in dados:
                            temp.append(each['preco'])
                        temp.sort(reverse=False)
                        for each in temp:
                            for another_each in dados:
                                if (each == another_each['preco']) and (another_each not in tempd):
                                    tempd.append(another_each)
                        for each in tempd:
                            print(each)
                        del temp
                        del tempd
                    case '4':
                        abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                        temp = []
                        tempd = []
                        for each in dados:
                            temp.append(each['nome'])
                        for each in abc:
                            for another_each in temp:
                                if another_each[0] == each:
                                    tempd.append(another_each)
                        for each in tempd:
                            for another_each in dados:
                                if another_each['nome'] == each:
                                    print(another_each)
                        del abc
                        del temp
                        del tempd
                    case '5':
                        abc = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
                        temp = []
                        tempd = []
                        for each in dados:
                            temp.append(each['nome'])
                        for each in abc:
                            for another_each in temp:
                                if another_each[0] == each:
                                    tempd.append(another_each)
                        for each in tempd:
                            for another_each in dados:
                                if another_each['nome'] == each:
                                    print(another_each)
                        del abc
                        del temp
                        del tempd
                dados.clear()
def modificar_json():
    '''
    Se o produto existir, modifica o nome ou o preço dele
    '''
    with (open(path,'r')) as file:
        try:
            dados = json.load(file)
        except json.JSONDecodeError:
            print('Nenhum Produto Registrado.')
        else:
            if dados == []:
                print('Nenhum Produto Registrado.')
            else:
                print('Dados atuais no json:')
                for each in dados:
                    print(each)
                print('Escolha qual produto vai ser modificado pelo código:')
                i = input('')
                for each in dados:
                    if int(each['codigo']) == int(i):
                        j = input(f"Modificar o preco ou o nome de {each['nome']} a R${each['preco']}\n")
                        if j == 'preco':
                            k = input('Qual o novo preço?\n')
                            each.update({'preco':float(k)})
                        elif j == 'nome':
                            k = input('Qual o novo nome?\n')
                            each.update({'nome':k.strip().title()})
                        if j == 'preco' or j == 'nome':
                            escritajson = json.dumps(dados,indent=4,ensure_ascii=False)
                            path.write_text(escritajson)
                d.clear()
                l.clear()
                dados.clear()

def sessao() -> bool:
    login = input('Insira o login:\n')
    senha = input('Insira a senha:\n')
    if login == 'admin' and senha==login:
        print('Bem vindo administrador!')
        return True
    print('Bem vindo Caixa!')
    return False

if __name__ == '__main__':
    if sessao():
        while opcao in '1234':
            print('0 - Sair')
            print('1 - Adicionar produtos')
            print('2 - Remover produtos')
            print('3 - Visualizar Produtos')
            print('4 - Modificar Produtos')
            opcao = input('')
            match(opcao):
                case '1':
                    adicionar_produto()
                case '2':
                    remover_produto()
                case '3':
                    ver_json()
                case '4':
                    modificar_json()
    else:
        with (open(path,'r')) as file:
            try:
                dados = json.load(file)
            except json.JSONDecodeError:
                print('Nenhum Produto Registrado.')
            else:
                if dados == []:
                    print('Nenhum Produto Registrado.')
                else:
                    receita = 0
                    while opcao == '1':
                        print('1 - Carrinho')
                        print('2 - Sair')
                        opcao = input('')
                        if opcao == '1':
                            nome_carrinho = ''
                            preco_carrinho = 0
                            total = 0
                            codigo = ''
                            while codigo != '0':
                                for each in dados:
                                    print(each)
                                print('\nInsira o código do produto (0 Pra Cancelar/Concluir) :')
                                codigo = input('')
                                if codigo == '0':
                                    break
                                try:
                                    int(codigo)
                                except ValueError:
                                    print('! Dado Inválido (quantidade é um número inteiro)')
                                    break
                                for each in dados:
                                    if each['codigo'] == int(codigo):
                                        nome_carrinho = each['nome']
                                        preco_carrinho = each['preco']
                                print(f'Insira a quantidade de {nome_carrinho}')
                                qtd = int(input(''))
                                total += qtd*preco_carrinho
                            if total != 0:
                                receita += total
                                print('-'*40)
                                print(f'O preço é R${total}')
                                print('-'*40)
                                # algo pro pagamento
                    print('-'*40)
                    print(f'A quantidade de receita desse caixa foi de R${receita}')
                    print('-'*40)
                    # relatório         