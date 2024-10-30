# fazer um app que lide com todos os procedimentos de um software full-stack
# o app deve ter sistema de cadastro e autenticação
# emails
# poder enviar relatórios em pdf pra outros emails
# quando fazer login na conta, o seu email já é utilizado automaticamente pros envios
# trazer o pdf já pronto pro app
# fazer um app com tela de cadastro
# quando der enter, ativar o botão
import tkinter as tk
import tkinter.font as tkFont
import sqlite3

menu = tk.Tk()
menu.geometry('1000x500')
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
    if login.get() == 'admin':
        if senha.get() == 'admin':
            tela_principal.tkraise()
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

ver_senha = tk.Checkbutton(tela_de_login,text='Visualizar Senha',variable=ver_senha_confirmacao,command=lambda:cripto() if ver_senha_confirmacao.get() else discripto())
confirmar = tk.Button(tela_de_login,text='Próximo',command=validar)
registrar = tk.Label(tela_de_login,text='Não tem uma conta?\nRegistre-se.',font=fonte_padrao)
registrar.bind('<Button-1>',lambda event:tela_de_registro.tkraise())
registrar.bind('<Enter>', lambda event:registrar.config(font=fonte_hover))
registrar.bind('<Leave>', lambda event:registrar.config(font=fonte_padrao))

tela1 = [login,senha,ver_senha,confirmar,registrar]
for each in tela1: each.pack()

l1 = tk.Label(tela_principal,text='bem-vindo')
voltar = tk.Label(tela_principal,text='<-')
voltar.bind('<Button-1>',lambda event:tela_de_login.tkraise())

tela2 = [l1,voltar]
for each in tela2: each.pack()

l2 = tk.Label(tela_de_registro,text='registre')

tela3 = [l2]
for each in tela3: each.pack()

tela_de_login.tkraise()
menu.mainloop()