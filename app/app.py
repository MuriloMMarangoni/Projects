# fazer um app que lide com todos os procedimentos de um software full-stack
# o app deve ter sistema de cadastro e autenticação
# emails
# poder enviar relatórios em pdf pra outros emails
# quando fazer login na conta, o seu email já é utilizado automaticamente pros envios
# trazer o pdf já pronto pro app

import tkinter as tk

def campos(obj:tk):
    return obj.get()

app = tk.Tk()
app.geometry('1000x500')

tk.Label(app,text="Seja bem vindo a minha calculadora!\nInsira dois números a serem somados").pack()
primeiro_campo = tk.Entry(app)
primeiro_campo.pack()
segundo_campo = tk.Entry(app)
segundo_campo.pack()
def pegar():
    e1 = int(campos(primeiro_campo))
    e2 = int(campos(segundo_campo))
    return e1+e2
def mudar(obj):
    obj.config(text=pegar())
label1 = tk.Label(app,text='')
somar = tk.Button(app,command=lambda:mudar(label1),text='Somar')
somar.pack()
label1.pack()



app.mainloop()
