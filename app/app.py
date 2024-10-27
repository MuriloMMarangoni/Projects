# fazer um app que lide com todos os procedimentos de um software full-stack
# o app deve ter sistema de cadastro e autenticação
# emails
# poder enviar relatórios em pdf pra outros emails
# quando fazer login na conta, o seu email já é utilizado automaticamente pros envios
# trazer o pdf já pronto pro app

import tkinter as tk
app = tk.Tk() # Objeto da janela
app.title('Nome da janela') # nome da janela
app.geometry("1000x500") # tamanho da janela

texto1 = tk.Label(app,text='aqui está escrito algo') # objeto de texto
texto1.pack() # mostrar o texto
count=0
botao1 = tk.Button(app,text='botaozinho',command=lambda:print('algo'))
botao1.pack()
# no command, precisa criar usar uma função anonima OU o objeto de uma função, porque se for chamada, ela é executada na criação do objeto do botão

app.mainloop() # abre a janela