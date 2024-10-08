import socket
import threading # incluir depois
import pickle # não sei o que é mas da pra aprender

def tcplh():
    d = {
        's' : socket.socket(socket.AF_INET,socket.SOCK_STREAM),
        'c' : socket.socket(socket.AF_INET,socket.SOCK_STREAM),
        'ip' : socket.gethostbyname(socket.gethostname()),
        'localhost' : socket.gethostname(),
        'port' : 12345
    }
    return d
def tcpl():
    d = {
        's' : socket.socket(socket.AF_INET,socket.SOCK_STREAM),
        'c' : socket.socket(socket.AF_INET,socket.SOCK_STREAM),
        'ip_server' : '0.0.0.0',
        'ip' : '',
        'port' : 12345
    }
    return d
def udp():
    raise NotImplementedError

def client(d:dict):
    c = d['c']
    ip = d['ip']
    port = d['port']
    if mostrar_ip:
        ip = input('Insira o ip do servidor:\n')
    c.connect((ip,port))
    print(c.recv(1024).decode())
    c.send("O cliente está funcionando".encode())
    c.close()
def server(d:dict):
    s = d['s']
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # deixa o servidor elegivel a ser iniciado 1s depois do encerramento
    try:
        ip = d['ip_server']
    except Exception:
        ip = d['ip']
    port = d['port']
    s.bind((ip,port))
    if mostrar_ip:
        print(f"o ip pra acesso remoto é {socket.gethostbyname(socket.gethostname())}")
    s.listen(1)
    c,adr = s.accept()
    c.send(f"O servidor está funcionando!".encode())
    print(c.recv(1024).decode())
    while True:
        break
    c.close()
if __name__ == '__main__':
    print(f"{30*'-'}\nEscolha qual o tipo de comunicação Cliente-Servidor")
    tipo = input("1-TCP Localhost\n2-TCP Local\n3-UDP\n")
    if tipo not in '123':
        raise SystemExit
    print(f"{30*'-'}\nEscolha qual o seu papel na comunicação")
    papel = input("1-Servidor\n2-Cliente\n")
    if papel not in '123':
        raise SystemExit
    mostrar_ip = False #mostrar o ip pra conexão remota (tcpl)
    if tipo == '1':
        if papel == '1':
            server(tcplh())
        if papel == '2':
            client(tcplh())
    elif tipo =='2':
        mostrar_ip = True
        if papel == '1':
            server(tcpl())
        if papel == '2':
            client(tcpl())
    else:
        if papel == '1':
            server(udp())
        if papel == '2':
            client(udp())