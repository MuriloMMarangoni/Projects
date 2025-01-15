import requests
import sys
# python testUrl.py --url 'url'
if '--url' not in sys.argv:
    print('Use --url flag to specify a url via CLI')
else:
    temp = sys.argv.index('--url')
    url = sys.argv[temp+1]
    try:
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        print(False)
    else:
        existe = True if r.status_code == 200 else False
        print(existe)