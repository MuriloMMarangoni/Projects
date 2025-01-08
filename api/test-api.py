#testa a api

import requests

valor = input("Qual o valor?\n")

url = f"http://127.0.0.1:5000/{valor}"

r = requests.get(url)
print("nota/moeda | quatidade")
for valor,quantidade in r.json().items():
    print(f"{valor} | {quantidade}")