# basic info about networks
import psutil
import subprocess
import requests
import socket
import pprint
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import ipaddress
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
    if psutil.pid_exists(pid):
        p = psutil.Process(pid)
        return (p.name(),p.connections())
    return "Pid não está em execução"

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

def rede_wireless(interface:str)->tuple[str,str,str]:
    '''
    Informações da rede wireless que está conectada(rede_conectada,velocidade,sinal)
    '''

    dados = subprocess.run(f'iwconfig {interface}',shell=True,text=True,capture_output=True)
    saida = dados.stdout

    termos = ''
    for each in saida:
        if each != ' ':
            termos += each

    rede_conectada = ''
    velocidade = ''
    sinal = ''

    for each in termos[termos.find('ESSID:"') + 7:]:
        if each == '"':
            break
        rede_conectada += each
    
    for each in termos[termos.find('BitRate=') + 8:]:
        if each == 'T':
            break
        velocidade += each

    for each in termos[termos.find('Signallevel=') + 12:]:
        if each == '\n':
            break
        sinal += each

    return rede_conectada,velocidade,sinal

def get_pids()->dict[int,str]:
    '''
    Diz os pids e nomes de cada processo rodando
    '''
    d = {}
    for p in psutil.process_iter():
        d.update({p.pid:p.name()})
    return d

def redes_disponiveis():
    '''
    List with available wifis
    '''
    s = subprocess.run('nmcli dev wifi list',shell=True,text=True,capture_output=True)
    saida = s.stdout.splitlines()
    linhas = ''
    todas_linhas = []
    final = []
    for line in saida[1:]:
        for each in line:
            if each != ' ':
                linhas += each
        todas_linhas.append(linhas)
        linhas = ''

    for each in todas_linhas:
        if each[0] == '*':
            final.append(each[18:each.find('Infra')])
        else:
            final.append(each[17:each.find('Infra')])
    return final

def download_images(url:str)->None:
    '''
    Baixa png,webp,jpeg e gifs de uma página simples
    '''
    resp = requests.get(url)
    repr_str = resp.text 
    soup = BeautifulSoup(features="html.parser",markup=repr_str)
    formats = [".png",".webp",".jpeg",".gif"]

    todas_as_imagens = []
    for images in formats:
        for each in soup.find_all("img",src=lambda src: str(src).endswith(images)):
            todas_as_imagens.append(each)

    ocorrencias = []
    for images in todas_as_imagens:
        ocorrencias.append(images.get('src'))


    ocorrencias_acessiveis = []
    for each in ocorrencias:
        ocorrencias_acessiveis.append(urljoin(url,each))
    del ocorrencias

    if ocorrencias_acessiveis != []: os.makedirs("img",exist_ok=True)

    for each in ocorrencias_acessiveis:
        if each.endswith(formats[0]):
            path = os.path.join("img",f"{ocorrencias_acessiveis.index(each)}{formats[0]}")
            with open(path,'wb') as f:
                f.write(requests.get(each).content)
        elif each.endswith(formats[1]):
            path = os.path.join("img",f"{ocorrencias_acessiveis.index(each)}{formats[1]}")
            with open(path,'wb') as f:
                f.write(requests.get(each).content)
        elif each.endswith(formats[2]):
            path = os.path.join("img",f"{ocorrencias_acessiveis.index(each)}{formats[2]}")
            with open(path,'wb') as f:
                f.write(requests.get(each).content)
        elif each.endswith(formats[3]):
            path = os.path.join("img",f"{ocorrencias_acessiveis.index(each)}{formats[3]}")
            with open(path,'wb') as f:
                f.write(requests.get(each).content)

    pprint.pprint(f"Foram baixadas {len(todas_as_imagens)} imagens")

def privateIp(ip:str)->bool:
    '''
    Returns True if ipv4 is private
    '''
    return ipaddress.ip_address(ip).is_private

conexoes()
download_images("https://en.wikipedia.org/wiki/World_War_II_casualties")

test_return = {'1':localOfIp(myIp()[1]),
        '2':myIp(),
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
        '16':processo(1),
        '17':rede_wireless('wlan0'),
        '18':get_pids(),
        '19':redes_disponiveis(),
        '20':privateIp('192.168.1.10')
}


for each,function in test_return.items():
    print(each)
    pprint.pprint(function)
