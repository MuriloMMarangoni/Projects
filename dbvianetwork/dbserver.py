import sqlite3 # interagir com um banco de dados
import socket # usar sockets pra comunicar via rede
import threading # threads pra conexão e threads pro banco de dados
# criar ou/e conectar

db_connection = sqlite3.connect('database.db')
sql = db_connection.cursor()
tabela = 'python'
colunas = ('Module','Topic','Features')

def create():
    comando_criar = f'''CREATE TABLE IF NOT EXISTS {tabela}(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    {colunas[0]} TEXT,
    {colunas[1]} TEXT,
    {colunas[2]} TEXT
    )
    '''
    sql.execute(comando_criar)

def inserir():
    comando_inserir =f"INSERT INTO {tabela}"f"({colunas[0]},{colunas[1]},{colunas[2]})""VALUES (?,?,?)"

    dados = [
        ('','',''),('','','')
    ]

    for dado in dados:
        sql.execute(comando_inserir,dado)

def pegar():
    comando_selecionar=f"SELECT * FROM {tabela}"

    sql.execute(comando_selecionar)
    dados_do_banco = sql.fetchall()

    #mostra os dados

    for data in dados_do_banco:
        print(data)


create()

def show_tables():
    print("The database has the following tables:")
    s = "SELECT name FROM sqlite_master WHERE type='table';"
    sql.execute(s)
    tables = sql.fetchall()
    for each in tables: 
        print(*each) # [()]

def adicionar_tabelas():
    print("Insira os dados da tabela:")
    name = input('Nome: ')
    quantity = input('Quantidade: ')
    quantity = int(quantity)
    colums = []
    for each in range(quantity):
        if each == quantity - 1:
            colums.append(f"{input(f"Coluna {each}:")} TEXT")
        else:
            colums.append(f"{input(f"Coluna {each}:")} TEXT,")
    temp = ""
    for each in colums:
        temp += each
    # pensar em como fazer um COLUMN TEXT pra cada nome em colums
    command = f'''CREATE TABLE IF NOT EXISTS {name}(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    {temp}
    )'''
    sql.execute(command)
    
# deixar o usuário poder visualizar, adicionar,remover e filtrar o banco de dados
# deixando ele escrever comandos sql via terminal, se eles derem ele vai, se não da o erro sqlite3.OperationalError
# modificar dado específico da coluna (col3, linha10)
show_tables()
adicionar_tabelas()

db_connection.commit()
db_connection.close()