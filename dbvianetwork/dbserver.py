import sqlite3 # interagir com um banco de dados
import socket # usar sockets pra comunicar via rede
import threading # threads pra conexão e threads pro banco de dados

comando_criar = '''CREATE TABLE IF NOT EXISTS banco(
linha INTEGER PRIMARY KEY AUTOINCREMENT,
coluna1 TEXT,
coluna2 TEXT,
coluna3 TEXT
)
'''

comando_inserir ="INSERT INTO banco""(coluna1,coluna2,coluna3)""VALUES (?,?,?)"

comando_selecionar="SELECT * from banco"


dados = [
    ('1','2','3'),
    ('4','5','6'),
    ('7','8','9'),
    ('10','11','12')
]

conectar = sqlite3.connect('database.db')
selecionar = conectar.cursor()
selecionar.execute(comando_criar)

for dado in dados:
    selecionar.execute(comando_inserir,dado)

selecionar.execute(comando_selecionar)
dados_do_banco = selecionar.fetchall()

for data in dados_do_banco:
    print(data)