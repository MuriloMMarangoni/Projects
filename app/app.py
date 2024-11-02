# fazer um app que lide com todos os procedimentos de um software full-stack
# o app deve ter sistema de cadastro e autenticação
# quando fazer login na conta, o seu email já é utilizado automaticamente pros envios
# trazer o pdf já pronto pro app
# fazer um app com tela de cadastro
# quando der enter, ativar o botão
# sugestões: colocar indicadores nos Entrys
# fazer um arquivo que tem o 'login' do ultimo usuário conectado, assim quando abrir o app, se tiver o nome de algum login la, essa conta vai ser logada automaticamente, mas se o usuário clicar em 'sair', o arquivo fica vazio
# suporte pra email no lugar do login
# apagar mensagens de erro quando trocar de tela
# enviar um email de registro, com um numero aleatorio de 6 digitos, daí se o usuario colocar o codigo correto, registre, se não, espere 45s pra enviar outro codigo
import tkinter as tk
import tkinter.font as tkFont
import sqlite3

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

login = tk.Entry(tela_de_login)
senha = tk.Entry(tela_de_login)
login.bind("<Down>", lambda event:event.widget.tk_focusNext().focus())
senha.bind("<Up>", lambda event:event.widget.tk_focusPrev().focus())
senhaReal = '' # variável temporária 
temp = tk.Label(menu) # variável temporária pra ver se já tem mensagem de erro

def validar():
    '''
    Diz se o login e a senha da tela de login é admin
    '''
    global login
    global senha
    global temp
    global senhaReal
    global ver_senha_confirmacao
    if login.get() == 'admin':
        if senha.get() == 'admin' or senhaReal == 'admin':
            tela_principal.tkraise()
            ver_senha_confirmacao.set(False)
            menu.title("Utilitários")
            clear_fields()
        else:
            if len(tela_de_login.winfo_children()) == 6: # se na tela tiver 2 entry,caixa,botao,registre  e mensagem de erro
                temp.destroy()
            temp = tk.Label(tela_de_login,text='Senha Incorreta',fg='red')
            temp.pack()
    else:
        if len(tela_de_login.winfo_children()) == 5: # ainda não tem mensagem de erro
            temp = tk.Label(tela_de_login,text='Login Incorreto',fg='red')
            temp.pack()
        else:
            temp.config(text='Login Incorreto')

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
    '''
    Muda pra tela de registrar
    '''
    tela_de_registro.tkraise()
    menu.title("Registre-se")
    clear_fields()

def logue():
    '''
    Muda pra tela de login
    '''
    tela_de_login.tkraise()
    menu.title('Login')
    clear_fields()

def clear_fields():
    '''
    Limpa todos os campos da tela de registro e Login
    '''
    login.delete(0,tk.END)
    senha.delete(0,tk.END)

    nome.delete(0,tk.END)
    email.delete(0,tk.END)
    registro.delete(0,tk.END)
    senha_registro.delete(0,tk.END)
    senha_registro_confirmar.delete(0,tk.END)

ver_senha = tk.Checkbutton(tela_de_login,text='Visualizar Senha',variable=ver_senha_confirmacao,command=lambda:cripto() if ver_senha_confirmacao.get() else discripto())
confirmar = tk.Button(tela_de_login,text='Próximo',command=validar)
registrar = tk.Label(tela_de_login,text='Não tem uma conta?\nRegistre-se.',font=fonte_padrao)
registrar.bind('<Button-1>',lambda event:registre())
registrar.bind('<Enter>', lambda event:registrar.config(font=fonte_hover))
registrar.bind('<Leave>', lambda event:registrar.config(font=fonte_padrao))

erro_registro:tk.Label = tk.Label(tela_de_registro,text='',fg='red')

tela1 = [login,senha,ver_senha,confirmar,registrar]
for each in tela1: each.pack()

l1 = tk.Label(tela_principal,text='App de utilidades')
voltar = tk.Label(tela_principal,text='<-')
voltar.bind('<Button-1>',lambda event:logue())

tela2 = [l1,voltar]
for each in tela2: each.pack()

nome           = tk.Entry(tela_de_registro)
email          = tk.Entry(tela_de_registro) 
registro       = tk.Entry(tela_de_registro) 
senha_registro = tk.Entry(tela_de_registro)
senha_registro_confirmar = tk.Entry(tela_de_registro)

def verificar():
    global erro_registro
    senhas_iguais = senha_registro.get() == senha_registro_confirmar.get()
    email_valido = '@' in email.get()
    erro_registro.pack()
    if senhas_iguais and email_valido:
        tela_principal.tkraise()
    elif not senhas_iguais:
        erro_registro.config(text='As senhas são diferentes')
    elif not email_valido:
        erro_registro.config(text='O e-mail é inválido')
    

confirmar_registro = tk.Button(tela_de_registro,text='Verificar',command=verificar)
l3 = tk.Label(tela_de_registro,text='<-')
l3.bind('<Button-1>',lambda event: logue())

tela3 = [nome,email,registro,senha_registro,senha_registro_confirmar,confirmar_registro,l3]
for each in tela3: each.pack()

tela_de_login.tkraise()
menu.mainloop()



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
    'february':29 if isLeap() else 28,
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

year:int = 365 if not isLeap() else 366

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