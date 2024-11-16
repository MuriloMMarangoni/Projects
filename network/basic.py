# basic info about networks
import psutil
import subprocess
import requests
def localOfIp(ip):
    '''
    Uses API for knowledge of an Public ip location
    '''
    url = f'http://www.geoplugin.net/json.gp?ip={ip}'
    r = requests.get(url)
    print(r.json())

def myIp()->list[str]:
    # says your current private and public ipv4
    s = subprocess.run('hostname -I',shell=True,capture_output=True,text=True)
    ss = subprocess.run('curl ifconfig.me',shell=True,capture_output=True,text=True)
    return [s.stdout[:-2],ss.stdout]

def myMask()->str:
    # says your current mask
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

def broadcast(ip:str)->str:
    # says the broadcast ip of a subnet
    pass
def maskOfIp(ip:str)->str:
    '''
    Says the newtork mask of a private IP address (ipv4)
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

