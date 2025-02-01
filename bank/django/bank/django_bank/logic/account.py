import sqlite3
con = sqlite3.connect('db.sqlite3')
# fazer lógica de cadastro no banco de dados via o site, se a conta ja existir avisar, se a senha der errado 5 vezes um timeout, mecanica de mudar de senha