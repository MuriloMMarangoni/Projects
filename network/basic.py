# basic info about networks
import psutil
import subprocess
import requests
import socket
def localOfIp(ip:str)->list[str]:
    '''
    Uses API for knowledge of an Public ip location [country,state,city,(coordinates)]
    '''
    url = f'http://www.geoplugin.net/json.gp?ip={ip}'
    r = requests.get(url)
    data = r.json()
    return [data['geoplugin_countryName'],data['geoplugin_regionName'],data['geoplugin_city'],(float(data['geoplugin_latitude']),float(data['geoplugin_longitude']))]

def myIp()->tuple[str]:
    '''
    Uses API to get a Tuple with your private and public IPV4s Adress
    '''
    s = subprocess.run('hostname -I',shell=True,capture_output=True,text=True)
    r = requests.get('https://ifconfig.me')
    return (s.stdout[:-2],r.text)

def myMask()->str:
    '''
    Says your current newtork mask
    '''
    s = subprocess.run('hostname -I',shell=True,capture_output=True,text=True)
    ip = s.stdout
    ip += '.'
    bits = []
    temp = ''
    for each in ip:
        if each != '.':
            temp += each
        else:
            bits.append(int(temp))
            temp = ''

    if bits[0] == 10:
        return '255.0.0.0'
    elif bits[0] == 172 and bits[1] >= 16:
        if bits[1] < 32:
            return '255.255.0.0'
    elif bits[0] == 192 and bits[1] == 168:
        if bits[2] >= 0 and bits[2] < 256:
            return '255.255.255.0'

def maskOfIp(ip:str)->str:
    '''
    Says the newtork mask of a private IPV4 address
    '''
    ip += '.'
    bits = []
    temp = ''
    for each in ip:
        if each != '.':
            temp += each
        else:
            bits.append(int(temp))
            temp = ''

    if bits[0] == 10:
        return '255.0.0.0'
    elif bits[0] == 172 and bits[1] >= 16:
        if bits[1] < 32:
            return '255.255.0.0'
    elif bits[0] == 192 and bits[1] == 168:
        if bits[2] >= 0 and bits[2] < 256:
            return '255.255.255.0'
    else:
        return '[!] IP is not private'

def networkInterfaces()->list[str]:
    '''
    Shows the available network interfaces
    '''
    return [*psutil.net_if_addrs().keys()]

def deviceName()->str:
    '''
    Says the name of this device
    '''
    return socket.gethostname()

def reverseDNSLookup(ip:str):
    '''
    Returns the name of the device in the network
    '''
    return socket.gethostbyaddr(ip)[0]

def DNSLookup(link:str):
    '''
    Returns the IP of the given Domain
    '''
    return socket.gethostbyname(link)

def usedPorts()->list[int]:
    '''
    Give a list of all used ports on all TCP and UDP connections
    '''
    ports=[conn.laddr.port for conn in psutil.net_connections(kind='inet')]
    ports = list(set(ports))
    ports.sort()
    return ports

def link_exists(link:str)->bool:
    '''
    Returns True if the link exists and says if the format is invalid
    '''
    try:
        return True if requests.get(link).status_code == 200 else False
    except (requests.exceptions.MissingSchema ,requests.exceptions.InvalidSchema):
        return 'Link não está formatado da forma correta'
    except requests.exceptions.ConnectionError:
        return False

def sockets_for_connection(domain:str)->dict:
    '''
    Says 4 different ways of configuring sockets to make a connection to a domain
    '''
    ways= socket.getaddrinfo(domain,'https')
    d = {
        'INET_TCP':ways[0],
        'INET_UDP':ways[1],
        'INET6_TCP':ways[2],
        'INET6_UDP':ways[3]
    }
    return d

def html(link:str)->None:
    '''
    Downloads the html file of a given url
    '''
    r = requests.get(link)
    with open(f'html.html','wb') as f:
        f.write(r.content)

def networkInterfaceInfo(net:str)->tuple[list,list,list,list]:
    '''
    Gives information about
    network interface status (up,mss)
    ipv4 (address,netmask,broadcast)
    ipv6 (address,netmask)
    network card (address)
    '''
    stats = []
    ipv4 = []
    ipv6 = []
    card = []
    
    stats.append(psutil.net_if_stats()[net].isup)
    stats.append(mss := psutil.net_if_stats()[net].mtu-40)

    for data in psutil.net_if_addrs()[net]:
        match(data.family):
            case 2:
                ipv4.append(data.address)
                ipv4.append(data.netmask)
                ipv4.append(data.broadcast)
            case 10:
                ipv6.append(data.address)
                ipv6.append(data.netmask)
            case 17:
                card.append(data.address)
            case _:
                print(f"! Foi encontrada uma interface além das suportadas ({data.family})")
    return (stats,ipv4,ipv6,card)

def interfaces_prontas()->list:
    '''
    Diz as interfaces prontas pra estabelecer conexões
    '''
    return [interface for interface,details in psutil.net_if_stats().items() if details.isup]

def network_traffic(net:str)->list:
    '''
    Se uma interface estiver ligada, diz quantos bytes e pacotes foram enviados e recebidos por ela
    '''
    if net in interfaces_prontas():
        traffic = psutil.net_io_counters(pernic=True)[net]
        return [(traffic.bytes_sent,traffic.bytes_recv),(traffic.packets_sent,traffic.packets_recv)]  
    return None

def processo(pid:int):
    '''
    Nome e conexões de um processo
    '''
    p = psutil.Process(pid)
    return (p.name(),p.connections())

def conexoes():
    '''
    conexões de rede ativas no sistema inteiro
    protocolo de endereçamento,(ip,porta) de quem começou a conexão,(ip,porta) de quem recebeu a conexão,protocolo de transmissão,status da conexão,pid,nome do processo
    '''
    con_unix = psutil.net_connections(kind='unix')
    con_tcp = psutil.net_connections(kind='tcp')
    con_udp = psutil.net_connections(kind='udp')
    cons = [con_unix,con_tcp,con_udp]
    for types in cons:
        print(40*'-')
        for connection in types:
            match(connection.family):
                case 1:
                    print('unix ',end='')
                    print(f"({connection.laddr}) ",end='')
                case 2:
                    print('ipv4 ',end='')
                    print(f"{(connection.laddr.ip,connection.laddr.port)} ", end='')
                    try:
                        print(f"{(connection.raddr.ip,connection.raddr.port)} ", end='')
                    except AttributeError:
                        print(f"() ",end='')
                case 10:
                    print('ipv6 ',end='')
                    print(f"{(connection.laddr.ip,connection.laddr.port)} ", end='')
                    try:
                        print(f"{(connection.raddr.ip,connection.raddr.port)} ", end='')
                    except AttributeError:
                        print(f"() ",end='')
            match(connection.type):
                case 1 : print('tcp ',end='')
                case 2 : print('udp ',end='')
                case 5 : print('packet ',end='')
            print(f"{connection.status} ",end='')
            print(f"{connection.pid} ",end='')
            p = psutil.Process(connection.pid)
            print(f"{p.name()}")

test_return = {'1':localOfIp(myIp()[1]),
        '2':myIp(),
        '3':myMask(),
        '4':maskOfIp(myIp()[0]),
        '5':networkInterfaces(),
        '6':deviceName(),
        '7':reverseDNSLookup(myIp()[1]),
        '8':DNSLookup('www.google.com'),
        '9':usedPorts(),
        '10':link_exists('https://www.google.com'),
        '11':sockets_for_connection('www.google.com'),
        '12':html('https://youtube.com'),
        '13':networkInterfaceInfo('wlan0'),
        '14':interfaces_prontas(),
        '15':network_traffic('wlan0'),
        '16':processo(591)
        }

conexoes()

for each,function in test_return.items():
    print(function)
