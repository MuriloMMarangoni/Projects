# fazer um app que lide com todos os procedimentos de um software full-stack
# o app deve ter sistema de cadastro e autenticação
# quando fazer login na conta, o seu email já é utilizado automaticamente pros envios
# trazer o pdf já pronto pro app
# sugestões: colocar indicadores nos Entrys
# fazer um arquivo que tem o 'login' do ultimo usuário conectado, assim quando abrir o app, se tiver o nome de algum login la, essa conta vai ser logada automaticamente, mas se o usuário clicar em 'sair', o arquivo fica vazio
# suporte pra email no lugar do login
# enviar um email de registro, com um numero aleatorio de 6 digitos, daí se o usuario colocar o codigo correto, registre, se não, espere 45s pra enviar outro codigo
import tkinter as tk
import tkinter.font as tkFont
import sqlite3
import subprocess

def databases():
    '''
    Cria e/ou usa um banco de dados pras contas
    '''
    s = subprocess.run("ls",shell=True,capture_output=True,text=True)
    files = s.stdout.splitlines()
    if 'appDatabase.db' in files:
        return [sqlite3.connect('appDatabase.db'),'existe']
    else:
        subprocess.run(f"touch appDatabase.db",shell=True,text=True)
        return [sqlite3.connect('appDatabase.db'),'criou']

def validar():
    '''
    Diz se o login e a senha da tela de login é admin
    '''
    global login
    global senha
    global erro_login
    global senhaReal
    global ver_senha_confirmacao
    if login.get() == 'admin':
        if senha.get() == 'admin' or senhaReal == 'admin':
            tela_principal.tkraise()
            ver_senha_confirmacao.set(False)
            menu.title("Utilitários")
            clear_fields()
        else:
            if len(tela_de_login.winfo_children()) == 9: # já tem mensagem de erro
                erro_login.destroy()
            erro_login = tk.Label(tela_de_login,text='Senha Incorreta',fg='red')
            erro_login.pack()
    else:
        if len(tela_de_login.winfo_children()) == 8: # ainda não tem mensagem de erro
            erro_login = tk.Label(tela_de_login,text='Login Incorreto',fg='red')
            erro_login.pack()
        else:
            erro_login.config(text='Login Incorreto')

def cripto():
    '''
    Substitui a senha por asteriscos
    '''
    global senha
    global senhaReal
    temp = senha.get()
    senha.delete(0,tk.END)
    senha.insert(0,f'{len(temp)*'*'}')
    senhaReal = temp
    
def discripto():
    '''
    Quando a senha ficar em asteriscos, ele volta ao normal
    '''
    global senha
    global senhaReal
    senha.delete(0,tk.END)
    senha.insert(0,senhaReal)

def mostrar_widgets():
    validar()
    print(tela_de_login.winfo_children())

def registre():
    erro_login.config(text='')
    '''
    Muda pra tela de registrar
    '''
    tela_de_registro.tkraise()
    menu.title("Registre-se")
    clear_fields()
    nome.focus()

def logue():
    erro_registro.config(text='')
    erro_login.config(text='')
    '''
    Muda pra tela de login
    '''
    tela_de_login.tkraise()
    menu.title('Login')
    clear_fields()
    login.focus()

def clear_fields():
    '''
    Limpa todos os campos da tela de registro e Login
    '''
    login.delete(0,tk.END)
    senha.delete(0,tk.END)

    nome.delete(0,tk.END)
    email.delete(0,tk.END)
    senha_registro.delete(0,tk.END)
    senha_registro_confirmar.delete(0,tk.END)

def enterProBotao():
    '''
    Se apertar enter vai no botão de registro ou de login e executa ele
    '''
    if menu.focus_get().master == tela_de_login:
        confirmar.focus()
        validar()
    elif menu.focus_get().master == tela_de_registro: # se ta nesse frame
        confirmar_registro.focus()
        verificar()

def verificar():
    global erro_registro
    senhas_iguais = senha_registro.get() == senha_registro_confirmar.get()
    email_valido = '@' in email.get()
    erro_registro.pack()
    if senhas_iguais and email_valido:
        credenciais = [nome.get(),email.get(),senha_registro.get(),1]
        comando2 = f"INSERT INTO Contas"f"(nome,email,senha,conectado)"f"VALUES (?,?,?,?)"
        sql.execute(comando2,tuple(credenciais))
        tela_principal.tkraise()
    elif not senhas_iguais:
        erro_registro.config(text='As senhas são diferentes')
    elif not email_valido:
        erro_registro.config(text='O e-mail é inválido')
#banco de dados
db_connection,status = databases()
sql = db_connection.cursor()
if status == 'criou':
    comando = '''CREATE TABLE IF NOT EXISTS Contas(
    id INTEGER PRIMARY KEY,
    nome TEXT,
    email TEXT,
    senha TEXT,
    conectado INTEGER DEFAULT 0
    )
    '''
    sql.execute(comando)
#janela 'menu'
menu = tk.Tk()
menu.geometry('1000x500')
menu.title("Login")
ver_senha_confirmacao = tk.BooleanVar()
fonte_padrao = tkFont.Font(family='Arial',size=12)
fonte_hover = tkFont.Font(family='Arial',size=12,underline=1)
tela_de_login = tk.Frame(menu)
tela_principal = tk.Frame(menu)
tela_de_registro = tk.Frame(menu)
tela_de_login.place(relwidth=1,relheight=1)
tela_principal.place(relwidth=1,relheight=1)
tela_de_registro.place(relwidth=1,relheight=1)
#tela de login
login = tk.Entry(tela_de_login)
senha = tk.Entry(tela_de_login)
login.bind("<Down>", lambda event:event.widget.tk_focusNext().focus())
senha.bind("<Up>", lambda event:event.widget.tk_focusPrev().focus())
senhaReal = '' # guarda uma cópia da senha
erro_login = tk.Label(tela_de_login,text='') # mensagem de erro do login
ver_senha = tk.Checkbutton(tela_de_login,text='Visualizar Senha',variable=ver_senha_confirmacao,command=lambda:cripto() if ver_senha_confirmacao.get() else discripto())
confirmar = tk.Button(tela_de_login,text='Próximo',command=validar)
registrar = tk.Label(tela_de_login,text='Não tem uma conta?\nRegistre-se.',font=fonte_padrao)
registrar.bind('<Button-1>',lambda event:registre())
registrar.bind('<Enter>', lambda event:registrar.config(font=fonte_hover))
registrar.bind('<Leave>', lambda event:registrar.config(font=fonte_padrao))
menu.bind('<Return>',lambda event:enterProBotao())
tela1 = [tk.Label(tela_de_login,text='Login'),login,tk.Label(tela_de_login,text='Senha'),senha,ver_senha,confirmar,registrar]
for each in tela1: each.pack()
#tela pós autenticação
l1 = tk.Label(tela_principal,text='Olá Nome')
voltar = tk.Label(tela_principal,text='<-')
voltar.bind('<Button-1>',lambda event:logue())
l1.grid(row=0,column=0)
tk.Label(tela_principal,text=f"{220*' '}").grid(row=0,column=1)
voltar.grid(row=0,column=2)
#tela de registro
nome           = tk.Entry(tela_de_registro)
email          = tk.Entry(tela_de_registro) 
senha_registro = tk.Entry(tela_de_registro)
senha_registro_confirmar = tk.Entry(tela_de_registro)
erro_registro:tk.Label = tk.Label(tela_de_registro,text='',fg='red')
nome.bind("<Down>", lambda event:event.widget.tk_focusNext().focus())
email.bind("<Down>", lambda event:event.widget.tk_focusNext().focus())
senha_registro.bind("<Down>", lambda event:event.widget.tk_focusNext().focus())
email.bind("<Up>", lambda event:event.widget.tk_focusPrev().focus())
senha_registro.bind("<Up>", lambda event:event.widget.tk_focusPrev().focus())
senha_registro_confirmar.bind("<Up>", lambda event:event.widget.tk_focusPrev().focus())
confirmar_registro = tk.Button(tela_de_registro,text='Verificar',command=verificar)
l3 = tk.Label(tela_de_registro,text='<-')
menu.bind('<Return>',lambda event: enterProBotao())
l3.bind('<Button-1>',lambda event: logue())
tela3 = [tk.Label(tela_de_registro,text='Nome'),nome,tk.Label(tela_de_registro,text='E-mail'),email,tk.Label(tela_de_registro,text='Senha'),senha_registro,tk.Label(tela_de_registro,text='Confirmar Senha'),senha_registro_confirmar,confirmar_registro,l3]
for each in tela3: each.pack()
#começar na tela de login e usar a janela 'menu'
tela_de_login.tkraise()
menu.mainloop()

print(sql.execute("SELECT * FROM Contas").fetchall())

db_connection.commit()
db_connection.close()

dma = [] # se fizer tantos por dia, dá tantos por mes, e tantos por ano
jc = [] # juros compostos
prazos = [] # se eu colocar 1/1/2025 ele vai me dizer quantos dias faltam de hoje até essa data
fisica = [] # fórmulas de física que são uteis no dia a dia, como tempo, energia , etc

m:float = 1 # unidade básica de distância
h:float = 1 # distância vertical
km:float = 1000 * m
mile = 1.60934 * km # unidade americana de distâncias altas
foot:float = 0.3048 * m # unidade americana de distâncias médias
inches:float = 25.4/1000 * m # unidade americana de distâncias pequenas

g:float = 1  # unidade básica de massa
kg:float = 1000 * g
pound:float = 0.453592 * kg # unidade americana de peso

s:float = 1 # unidade básica de tempo
mi:float = s / 60
hr:float = mi / 60
day:int = hr / 24
weeks:int = day / 7

def isLeap(year:int)->bool:
    '''
    Checks if the year is leap
    '''
    condition1 = year % 400 == 0
    condition2 = year % 100 != 0
    condition3 = year % 4 == 0
    return (True if condition1 or (condition2 and condition3) else False)

month:dict = {
    'january':31,
    'february':29 if isLeap(0) else 28,
    'march':31,
    'april':30,
    'may': 31,
    'june': 30,
    'july': 31,
    'august': 31,
    'september': 30,
    'october': 31,
    'november': 30,
    'december': 31,
}

year:int = 365 if not isLeap(0) else 366

v:float = m/s # velocidade no SI
kmh:float = v / 3.6 # velocidade usual
a:float = v / s # aceleração
f:float = g*a # força
G:float = 9.8 # constante gravitacional
fp:float = G*g # força peso
e:float= f * m # trabalho(energia)
p = f*v # potência
ec = g*v**2 / 2 # energia cinética
epg = g*G*h # energia potencial gravitacional
em = ec + epg # energia mecanica
units:dict = {
# mapear as conversões
}