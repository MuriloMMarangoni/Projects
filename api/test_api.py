import requests

url = 'http://127.0.0.1:5000'

r = requests.get(url)

if r.status_code == 200:
    print(r.json())