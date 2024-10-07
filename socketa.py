import socket # módulo de comunicação de processos ou de máquinas da mesma rede
import ftplib # transferência de arquivos
host = socket.gethostname() # nome do host ou ip
port = 12345 # porta de acesso 1-65000
obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # cria um socket com comunicação(ipv4,tcp)

def ask() -> bool:
    perm = input("Press 0 for server or 1 for client\n")
    try:
        perm = bool(int((perm)))
    except Exception:
        print('! Invalid input')
    else:
        return perm
    
def server(host,port,obj):
    obj.bind((host,port)) # associa o host e a porta (servidores)
    obj.listen() # aceita conexões (servidores)
    host_client,port_client = obj.accept() # quem conectou[socket,[ip,porta]] (servidores)
    print(f"[Server] Connection stablished with {port_client[0]} with port {port_client[1]}")
    while True:
        data = host_client.recv(1024) # recebe os dados do cliente
        if data == b'': # se não receber encerra
            break
        print(f"[Client] {data.decode()}")
        i = input("[Server] ")
        host_client.sendall(i.encode()) # mostra pro cliente
    obj.close()

def client(host,port,obj):
    i = ' '
    obj.connect((host,port))
    while i != '':
        i = input("[Client] ")
        obj.sendall(i.encode())
        data = obj.recv(1024)
        print(f"[Server] {data.decode()}")
    obj.close()

if ask():
    client(host,port,obj)
else:
    server(host,port,obj)