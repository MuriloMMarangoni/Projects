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



test = {'1':localOfIp(myIp()[1]),
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
        '12':html('https://youtube.com')
        }
for each,function in test.items():
    print(function)
