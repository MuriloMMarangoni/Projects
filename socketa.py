import socket

def tcplh():
    d = {
        's' : socket.socket(socket.AF_INET,socket.SOCK_STREAM),
        'c' : socket.socket(socket.AF_INET,socket.SOCK_STREAM),
        'ip' : socket.gethostbyname(socket.gethostname()),
        'localhost' : socket.gethostname(),
        'port' : 12345,
        'type': 'tcp'
    }
    return d
def tcpl():
    d = {
        's' : socket.socket(socket.AF_INET,socket.SOCK_STREAM),
        'c' : socket.socket(socket.AF_INET,socket.SOCK_STREAM),
        'ip_server' : '0.0.0.0',
        'ip' : '',
        'port' : 12345,
        'type': 'tcp'
    }
    return d
def udplh():
    d = {
        "s":socket.socket(socket.AF_INET,socket.SOCK_DGRAM),
        "c":socket.socket(socket.AF_INET,socket.SOCK_DGRAM),
        'ip' : socket.gethostbyname(socket.gethostname()),
        'localhost' : socket.gethostname(),
        "port": 12345,
        'type': 'udp'
    }
    return d
def udpl():
    d = {
        "s":socket.socket(socket.AF_INET,socket.SOCK_DGRAM),
        "c":socket.socket(socket.AF_INET,socket.SOCK_DGRAM),
        'ip' : socket.gethostbyname(socket.gethostname()),
        'ip_server' : '0.0.0.0',
        "port": 12345,
        'type': 'udp'
    }
    return d
def client(d:dict):
    if d['type'] == 'tcp':
        c = d['c']
        ip = d['ip']
        port = d['port']
        if mostrar_ip:
            ip = input('Insira o ip do servidor:\n')
        c.connect((ip,port))
        c.send("O cliente está funcionando".encode())
        print(c.recv(1024).decode())
        while True:
            sendit = input("[Client] ")
            c.send(sendit.encode())
            message = c.recv(1024).decode()
            if message == 'quit' or message == '':
                break
            print(f"[Client] {message}")
        c.close()
    if d['type'] == 'udp':
        c = d['c']
        if mostrar_ip:
            ip_server = input("Insira o ip do servidor:\n")
        i = input("[Client] ")
        c.sendto(i.encode(),(ip_server,d['port'])) # envia pro endereço
        print(f"[Server] {c.recvfrom(1024)[0].decode()}")
def server(d:dict):
    if d['type'] == 'tcp':
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
        print(c.recv(1024).decode())
        c.send(f"O servidor está funcionando!".encode())
        while True:
            message = c.recv(1024).decode()
            if message == 'quit' or message == '':
                break
            print(f"[Client] {message}")
            sendit = input("[Server] ")
            c.send(sendit.encode())
        c.close()
    if d['type'] == 'udp':
        s = d['s']
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if mostrar_ip:
            s.bind(('0.0.0.0',d['port']))
            print(f"O ip do servidor é :{d['ip']}")
        else:
            s.bind((d['ip'],d['port']))
        msg,adr = s.recvfrom(1024)
        print(f"[Client] {msg.decode()}")
        i = input("[Server] ")
        s.sendto(i.encode(),adr)
        
if __name__ == '__main__':
    print(f"{30*'-'}\nEscolha qual o tipo de comunicação Cliente-Servidor")
    tipo = input("1-TCP Localhost\n2-TCP Local\n3-UDP Localhost\n4-UDP Local")
    if tipo not in '1234':
        raise SystemExit
    print(f"{30*'-'}\nEscolha qual o seu papel na comunicação")
    papel = input("1-Servidor\n2-Cliente\n")
    if papel not in '12':
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
    elif tipo == '3':
        if papel == '1':
            server(udplh())
        if papel == '2':
            client(udplh())
    elif tipo == '4':
        mostrar_ip = True
        if papel == '1':
            server(udpl())
        if papel == '2':
            client(udpl())