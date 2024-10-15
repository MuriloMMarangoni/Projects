import sqlite3 # interagir com um banco de dados
import socket # usar sockets pra comunicar via rede
import threading # threads pra conexão e threads pro banco de dados
# criar ou/e conectar

db_connection = sqlite3.connect('database.db')
sql = db_connection.cursor()
# se for ter while loop, tem que fazer um cursor pra cada funcionalidade, que abre e fecha
def id_system():
    #pegar todas as tabelas, em cada tabela, em cada linha, atribuir de 1 á quantidade de linhas pro valor do id
    s = "SELECT name FROM sqlite_master WHERE type='table';"
    sql.execute(s)
    tables = sql.fetchall()[1:]
    sql.close()
    tabela_corrigida = []
    for t in tables:
        for s in t:
            tabela_corrigida.append(s)
    
    for each in tabela_corrigida:
        s = f"PRAGMA table_info({each})"
        sql.execute(s)
        primeira_coluna = sql.fetchall[1]
        sql.close()
        s = f"SELECT {primeira_coluna} from {each}"
        sql.execute()
        primeiro_valor = sql.fetchall()[0]    
        sql1 = db_connection.cursor()
        s = f"SELECT * FROM {each}"
        sql1.execute(s)
        data = sql1.fetchall()
        sql1.close()
        count = 0
        for row in data:
            count += 1
            sql1 = db_connection.cursor()
            s = f"UPDATE {each} SET id={count} where {primeira_coluna}={primeiro_valor}"
            print(s) # teste
            sql1.execute(s)
            sql1.close()
    pass
def show_tables():
    s = "SELECT name FROM sqlite_master WHERE type='table';"
    sql.execute(s)
    tables = sql.fetchall()[1:]
    if len(tables) == 0:
        print("[!] Esse banco não tem tabelas")
        return 0
    else:
        print("The database has the following tables:")
        for each in tables: 
            print(*each) # [()]

def adicionar_tabelas():
    print("Insira os dados da tabela:")
    name = input('Nome: ')
    quantity = input('Quantidade de Colunas: ')
    quantity = int(quantity)
    colums = []
    for each in range(quantity):
        if each == quantity - 1:
            colums.append(f"{input(f"Coluna {each+1}:")} TEXT")
        else:
            colums.append(f"{input(f"Coluna {each+1}:")} TEXT,")
    temp = ""
    for each in colums:
        temp += each
    command = f'''CREATE TABLE IF NOT EXISTS {name}(
    id INTEGER DEFAULT 0,
    {temp}
    )'''
    sql.execute(command)
    
def remover_tabelas():
    if show_tables() == 0:
        print("[!] O banco não tem tabelas pra remover")
    else:
        print("Qual das tabelas vai remover?")
        op = input()
        try:
            s = f"DROP TABLE {op}"
            sql.execute(s)
        except sqlite3.OperationalError:
            print("[!] Essa tabela não existe")
# deixar o usuário poder visualizar, adicionar,remover e filtrar o banco de dados
# deixando ele escrever comandos sql via terminal, se eles derem ele vai, se não da o erro sqlite3.OperationalError
# modificar dado específico da coluna (col3, linha10)
def ver_tabela():
    show_tables()
    print("Qual das tabelas você quer ver?")
    op = input()
    try:
        s = f"SELECT * FROM {op}"
        sql.execute(s)
    except sqlite3.OperationalError:
        print("[!] Essa tabela não existe")
    else:
        data = sql.fetchall()
        for each in data:
            print(each)
def inserir_dados():
    show_tables()
    print("Qual das tabelas você quer inserir dados?")
    op = input()
    try:
        pass # tem que testar se a tabela existe
    except sqlite3.OperationalError:
        print("[!] Essa tabela não existe")
    else:
        s = f"PRAGMA table_info({op})"
        # PRAGMA returns rows with 6 columns, each row contains info about each column of the table
        # the order is (number of column,name,datatype,notnull,defaultvalue,primarykey)
        sql.execute(s)
        data = sql.fetchall()[1:]
        print("A tabela tem as seguintes colunas:")
        count = 0
        for each in data: # not include IDs
            print(each[1]) # only the names of the columns
            count += 1
        print(f"Essa tabela tem {count} colunas, então insira cada dado em uma linha:")
        inps = []
        for each in range(count):
            inps.append(input())
        parentesis = ""
        parentesis2 = ""
        for each in data:
            if each == data[-1]:
                parentesis += f"{each[1]}"
            else:
                parentesis += f"{each[1]},"
        for each in range(count):
            if each == count-1:
                parentesis2 += "?"
            else:
                parentesis2 += "?,"
        sql.close()
        sql2 = db_connection.cursor()
        s = f"INSERT INTO {op}"f"({parentesis})"f"VALUES ({parentesis2})"
        sql2.execute(s,tuple(inps))
        sql2.execute(f"SELECT * FROM {op}")
        t = sql2.fetchall()
        print(t)
        sql2.close()




def show_data():
    show_tables()
    print("Qual tabela você quer visualizar?")
    op = input()
    try:
        s = f"SELECT * FROM {op}"
        sql.execute(s)
        data = sql.fetchall()
        sql.close()
    except sqlite3.OperationalError:
        print("[!] A tabela não existe")
    else:
        sql2 = db_connection.cursor()
        s = f"PRAGMA table_info({op})"
        sql2.execute(s)
        data_c = sql2.fetchall()
        columns = []
        for each in data_c:
            columns.append(each[1])
        columns = tuple(columns)

        print(columns) # nome das colunas
        for each in data: # conteudo das linhas
            print(each)

def modify_data():
    # qual table
    # pedir coordenada? ou qual coluna e dps qual row? ou se vai mudar a row inteira?
    show_tables()
    print("Qual tabela?")
    op = input()
    print("1-Modificar linha inteira")
    print("2-Modificar Coluna inteira")
    print("3-Modificar dado específico")
    op2 = input()

    sl =f"SELECT id FROM {op}"
    sql1 = db_connection.cursor()
    sql1.execute(sl)
    data = sql1.fetchall()
    sql1.close()
    linhas = str(*data[-1]) # select last id

    sc =f"PRAGMA table_info({op})"
    sql2 = db_connection.cursor()
    sql2.execute(sc)
    data = sql2.fetchall()
    columns = [each[1] for each in data]
    
    sql2.close()

    match(op2):
        case '1':
            print(f"A tabela tem {linhas} linhas, qual delas você quer modificar?")
            s = f"ALTER TABLE {op} "
        case '2':
            print(f"A tabela tem as colunas {columns}, qual delas você quer modificar?")
        case '3':
            print(f"A tabela tem {linhas} linhas, qual delas você quer modificar?")
            print(f"A tabela tem as colunas {columns}, qual delas você quer modificar?")
    NotImplementedError

def remove_row():
    show_tables()
    print("Escolha uma tabela")
    op = input("")
    s = f"SELECT * FROM {op}"
    sql1 = db_connection.cursor()
    sql1.execute(s)
    data = sql1.fetchall()
    sql1.close()
    print("Qual das linhas você quer remover? (por id)")
    for each in data:
        print(each)
    op2 = input()
    s = f"DELETE FROM {op} WHERE id={op2}"
    sql2 = db_connection.cursor()
    sql2.execute(s)
    sql2.close()
    sql3 = db_connection.cursor()
    s = f"SELECT * FROM {op}"
    sql3.execute(s)
    data = sql3.fetchall()
    for each in data:
        print(each)
def commands():
    print("Insira qualquer comando SQL que bem desejar:")
    op = input()
    sql.execute(op)



print("Select an option:")
print("1- Show All Tables")
print("2- Add Table")
print("3- Remove Table")
print("4- Insert Rows")
print("5- Show Data from Table")
print("6- Modify Data from Table")
print("7- Remove row from Table")
print("10-Comandos SQL")
menu = input()
match (menu):
    case '1': show_tables() # working
    case '2': adicionar_tabelas() # working
    case '3': remover_tabelas() # working
    case '4': inserir_dados() # working
    case '5': show_data() # working
    case '6': modify_data() # NotFinished
    case '7': remove_row() # working
    case '8': id_system() # temporary, have to adjust cursors
    case '10': commands() # debug only
    case _: raise NotImplementedError
db_connection.commit()
db_connection.close()
# escolher arquivo.db ou se não existir criar um, e pedir pra colocar um nome
# se não tiver tabelas avisar
# exportar banco de dados como csv ou excel fds