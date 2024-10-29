# fazer um app que lide com todos os procedimentos de um software full-stack
# o app deve ter sistema de cadastro e autenticação
# emails
# poder enviar relatórios em pdf pra outros emails
# quando fazer login na conta, o seu email já é utilizado automaticamente pros envios
# trazer o pdf já pronto pro app

import tkinter as tk

menu = tk.Tk()

largura = 1000
altura= 500
menu.geometry(f'{largura}x{altura}')

estado = tk.BooleanVar()

login = tk.Entry(menu)
senha = tk.Entry(menu)
caixa = tk.Checkbutton(menu,variable=estado)
texto = tk.Label(menu,text='Exibir senha')
botao = tk.Button(menu,text='Fazer Login')

login.grid(row=0,column=0,padx=0)
senha.grid(row=1,column=0,padx=0)
caixa.grid(row=2,column=0,padx=0)
texto.grid(row=2,column=1,padx=0,ipadx=0)
botao.grid(row=3,column=0,padx=0)

menu.mainloop()
