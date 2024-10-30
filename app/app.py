# fazer um app que lide com todos os procedimentos de um software full-stack
# o app deve ter sistema de cadastro e autenticação
# emails
# poder enviar relatórios em pdf pra outros emails
# quando fazer login na conta, o seu email já é utilizado automaticamente pros envios
# trazer o pdf já pronto pro app
# fazer um app com tela de cadastro

import tkinter as tk

menu = tk.Tk()
menu.geometry('1000x500')
ver_senha_confirmacao = tk.BooleanVar()
tela_de_login = tk.Frame(menu)
tela_principal = tk.Frame(menu)
tela_de_login.place(relwidth=1,relheight=1)
tela_principal.place(relwidth=1,relheight=1)
login = tk.Entry(tela_de_login)
senha = tk.Entry(tela_de_login)
senhaReal = ''
def validar():
    global login
    global senha
    if login.get() == 'admin':
        if senha.get() == 'admin':
            tela_principal.tkraise()
        else:
            print('Senha Incorreta')
    else:
        print('Login Incorreto')
def cripto():
    global senha
    global senhaReal
    temp = senha.get()
    senha.delete(0,tk.END)
    senha.insert(0,f'{len(temp)*'*'}')
    senhaReal = temp
    
def discripto():
    global senha
    global senhaReal
    senha.delete(0,tk.END)
    senha.insert(0,senhaReal)
    

ver_senha = tk.Checkbutton(tela_de_login,text='Visualizar Senha',variable=ver_senha_confirmacao,command=lambda:cripto() if ver_senha_confirmacao.get() else discripto())
confirmar = tk.Button(tela_de_login,text='Próximo',command=validar)
tela1 = [login,senha,ver_senha,confirmar]
for each in tela1: each.pack()

l1 = tk.Label(tela_principal,text='texto')
l1.pack()

tela_de_login.tkraise()
menu.mainloop()