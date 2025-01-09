import requests
import random


def gerar_random_entre_0_e_1kk():
    l = [x for x in range(0,10)]
    random.shuffle(l)
    num = ''
    places = random.randint(3,8) # 0.00 à 999999.99
    for each in range(0,places):
        num += str(l[each])
    return int(num) / 100

url1 = "http://127.0.0.1:5000/BRL/"
url2 = "http://127.0.0.1:5000/USD/"

numeros = [gerar_random_entre_0_e_1kk() for x in range(0,10)]

for x in range(0,10):
    r = requests.get(url1+f'{numeros[x]}')
    print(r.json())
for x in range(0,10):
    r = requests.get(url2+f'{numeros[x]}')
    print(r.json())