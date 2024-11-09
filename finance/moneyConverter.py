import requests
import json
import tkinter as tk
import subprocess
from pathlib import Path
from datetime import datetime,timezone,timedelta
nomes_das_moedas = {
    "USD": "Dólar Americano",
    "AED": "Dirham dos Emirados Árabes Unidos",
    "AFN": "Afegane",
    "ALL": "Lek Albanês",
    "AMD": "Dram Armênio",
    "ANG": "Florim das Antilhas Holandesas",
    "AOA": "Kwanza Angolano",
    "ARS": "Peso Argentino",
    "AUD": "Dólar Australiano",
    "AWG": "Florim de Aruba",
    "AZN": "Manat Azerbaijano",
    "BAM": "Marco Conversível da Bósnia",
    "BBD": "Dólar de Barbados",
    "BDT": "Taka de Bangladesh",
    "BGN": "Lev Búlgaro",
    "BHD": "Dinar do Bahrein",
    "BIF": "Franco do Burundi",
    "BMD": "Dólar das Bermudas",
    "BND": "Dólar de Brunei",
    "BOB": "Boliviano",
    "BRL": "Real Brasileiro",
    "BSD": "Dólar das Bahamas",
    "BTN": "Ngultrum do Butão",
    "BWP": "Pula do Botswana",
    "BYN": "Rublo Bielorrusso",
    "BZD": "Dólar de Belize",
    "CAD": "Dólar Canadense",
    "CDF": "Franco Congolês",
    "CHF": "Franco Suíço",
    "CLP": "Peso Chileno",
    "CNY": "Yuan Chinês",
    "COP": "Peso Colombiano",
    "CRC": "Colón Costarriquenho",
    "CUP": "Peso Cubano",
    "CVE": "Escudo de Cabo Verde",
    "CZK": "Coroa Checa",
    "DJF": "Franco do Djibouti",
    "DKK": "Coroa Dinamarquesa",
    "DOP": "Peso Dominicano",
    "DZD": "Dinar Argelino",
    "EGP": "Libra Egípcia",
    "ERN": "Nakfa da Eritreia",
    "ETB": "Birr Etíope",
    "EUR": "Euro",
    "FJD": "Dólar de Fiji",
    "FKP": "Libra das Ilhas Malvinas",
    "FOK": "Coroa das Ilhas Faroé",
    "GBP": "Libra Esterlina",
    "GEL": "Lari Georgiano",
    "GGP": "Libra de Guernsey",
    "GHS": "Cedi de Gana",
    "GIP": "Libra de Gibraltar",
    "GMD": "Dalasi de Gâmbia",
    "GNF": "Franco Guineano",
    "GTQ": "Quetzal da Guatemala",
    "GYD": "Dólar da Guiana",
    "HKD": "Dólar de Hong Kong",
    "HNL": "Lempira de Honduras",
    "HRK": "Kuna Croata",
    "HTG": "Gourde Haitiano",
    "HUF": "Forint Húngaro",
    "IDR": "Rupia Indonésia",
    "ILS": "Novo Shekel Israelense",
    "IMP": "Libra da Ilha de Man",
    "INR": "Rupia Indiana",
    "IQD": "Dinar Iraquiano",
    "IRR": "Rial Iraniano",
    "ISK": "Coroa Islandesa",
    "JEP": "Libra de Jersey",
    "JMD": "Dólar Jamaicano",
    "JOD": "Dinar Jordaniano",
    "JPY": "Iene Japonês",
    "KES": "Xelim Queniano",
    "KGS": "Som do Quirguistão",
    "KHR": "Riel Cambojano",
    "KID": "Dólar das Ilhas Kiribati",
    "KMF": "Franco Comorense",
    "KRW": "Won Sul-Coreano",
    "KWD": "Dinar do Kuwait",
    "KYD": "Dólar das Ilhas Cayman",
    "KZT": "Tenge do Cazaquistão",
    "LAK": "Kip do Laos",
    "LBP": "Libra Libanesa",
    "LKR": "Rupia do Sri Lanka",
    "LRD": "Dólar Liberiano",
    "LSL": "Loti do Lesoto",
    "LYD": "Dinar Líbio",
    "MAD": "Dirham Marroquino",
    "MDL": "Leu Moldávio",
    "MGA": "Ariary Malgaxe",
    "MKD": "Dinar Macedônio",
    "MMK": "Kyat de Mianmar",
    "MNT": "Tugrik Mongol",
    "MOP": "Pataca de Macau",
    "MRU": "Ouguiya Mauritana",
    "MUR": "Rupia Mauriciana",
    "MVR": "Rufiyaa Maldiva",
    "MWK": "Kwacha Malauiana",
    "MXN": "Peso Mexicano",
    "MYR": "Ringgit Malaio",
    "MZN": "Metical Moçambicano",
    "NAD": "Dólar da Namíbia",
    "NGN": "Naira Nigeriana",
    "NIO": "Córdoba Nicaraguense",
    "NOK": "Coroa Norueguesa",
    "NPR": "Rupia Nepalesa",
    "NZD": "Dólar Neozelandês",
    "OMR": "Rial Omanense",
    "PAB": "Balboa Panamenho",
    "PEN": "Sol Peruano",
    "PGK": "Kina Papua-Nova Guiné",
    "PHP": "Peso Filipino",
    "PKR": "Rupia Paquistanesa",
    "PLN": "Zloty Polonês",
    "PYG": "Guarani Paraguaio",
    "QAR": "Rial Catarense",
    "RON": "Leu Romeno",
    "RSD": "Dinar Sérvio",
    "RUB": "Rublo Russo",
    "RWF": "Franco Ruandês",
    "SAR": "Rial Saudita",
    "SBD": "Dólar das Ilhas Salomão",
    "SCR": "Rupia de Seychelles",
    "SDG": "Libra Sudanesa",
    "SEK": "Coroa Sueca",
    "SGD": "Dólar de Singapura",
    "SHP": "Libra de Santa Helena",
    "SLE": "Leone de Serra Leoa",
    "SLL": "Leone de Serra Leoa",
    "SOS": "Xelim Somali",
    "SRD": "Dólar do Suriname",
    "SSP": "Libra do Sudão do Sul",
    "STN": "Dobra de São Tomé e Príncipe",
    "SYP": "Libra Síria",
    "SZL": "Lilangeni de Essuatíni",
    "THB": "Baht Tailandês",
    "TJS": "Somoni Tajique",
    "TMT": "Manat Turcomeno",
    "TND": "Dinar Tunisiano",
    "TOP": "Pa'anga de Tonga",
    "TRY": "Lira Turca",
    "TTD": "Dólar de Trinidad e Tobago",
    "TVD": "Dólar Tuvaluano",
    "TWD": "Novo Dólar Taiwanês",
    "TZS": "Xelim Tanzaniano",
    "UAH": "Hryvnia Ucraniana",
    "UGX": "Xelim Ugandense",
    "UYU": "Peso Uruguaio",
    "UZS": "Som Uzbeque",
    "VES": "Bolívar Venezuelano",
    "VND": "Dong Vietnamita",
    "VUV": "Vatu de Vanuatu",
    "WST": "Tala Samoana",
    "XAF": "Franco CFA de BEAC",
    "XCD": "Dólar do Caribe Oriental",
    "XDR": "Direito Especial de Saque",
    "XOF": "Franco CFA de BCEAO",
    "XPF": "Franco CFP",
    "YER": "Rial Iemenita",
    "ZAR": "Rand Sul-Africano",
    "ZMW": "Kwacha Zambiano",
    "ZWL": "Dólar Zimbabuano"
}
simbolos_das_moedas = {
    "USD": "$", "AED": "د.إ", "AFN": "؋", "ALL": "L", "AMD": "֏", "ANG": "ƒ",
    "AOA": "Kz", "ARS": "$", "AUD": "A$", "AWG": "ƒ", "AZN": "₼", "BAM": "KM",
    "BBD": "$", "BDT": "৳", "BGN": "лв", "BHD": ".د.ب", "BIF": "FBu",
    "BMD": "$", "BND": "$", "BOB": "Bs.", "BRL": "R$", "BSD": "$",
    "BTN": "Nu.", "BWP": "P", "BYN": "Br", "BZD": "$", "CAD": "$",
    "CDF": "FC", "CHF": "CHF", "CLP": "$", "CNY": "¥", "COP": "$",
    "CRC": "₡", "CUP": "$", "CVE": "$", "CZK": "Kč", "DJF": "Fdj",
    "DKK": "kr", "DOP": "$", "DZD": "د.ج", "EGP": "£", "ERN": "Nfk",
    "ETB": "Br", "EUR": "€", "FJD": "$", "FKP": "£", "FOK": "kr",
    "GBP": "£", "GEL": "₾", "GGP": "£", "GHS": "₵", "GIP": "£",
    "GMD": "D", "GNF": "FG", "GTQ": "Q", "GYD": "$", "HKD": "$",
    "HNL": "L", "HRK": "kn", "HTG": "G", "HUF": "Ft", "IDR": "Rp",
    "ILS": "₪", "IMP": "£", "INR": "₹", "IQD": "ع.د", "IRR": "﷼",
    "ISK": "kr", "JEP": "£", "JMD": "$", "JOD": "د.ا", "JPY": "¥",
    "KES": "KSh", "KGS": "с", "KHR": "៛", "KID": "$", "KMF": "CF",
    "KRW": "₩", "KWD": "د.ك", "KYD": "$", "KZT": "₸", "LAK": "₭",
    "LBP": "ل.ل", "LKR": "Rs", "LRD": "$", "LSL": "L", "LYD": "ل.د",
    "MAD": "د.م.", "MDL": "L", "MGA": "Ar", "MKD": "ден", "MMK": "Ks",
    "MNT": "₮", "MOP": "MOP$", "MRU": "UM", "MUR": "₨", "MVR": ".ރ",
    "MWK": "MK", "MXN": "$", "MYR": "RM", "MZN": "MT", "NAD": "$",
    "NGN": "₦", "NIO": "C$", "NOK": "kr", "NPR": "रू", "NZD": "$",
    "OMR": "ر.ع.", "PAB": "B/.", "PEN": "S/", "PGK": "K", "PHP": "₱",
    "PKR": "₨", "PLN": "zł", "PYG": "₲", "QAR": "ر.ق", "RON": "lei",
    "RSD": "дин.", "RUB": "₽", "RWF": "FRw", "SAR": "﷼", "SBD": "$",
    "SCR": "₨", "SDG": "ج.س.", "SEK": "kr", "SGD": "$", "SHP": "£",
    "SLE": "Le", "SLL": "Le", "SOS": "Sh", "SRD": "$", "SSP": "£",
    "STN": "Db", "SYP": "£", "SZL": "L", "THB": "฿", "TJS": "ЅМ",
    "TMT": "m", "TND": "د.ت", "TOP": "T$", "TRY": "₺", "TTD": "$",
    "TVD": "$", "TWD": "$", "TZS": "Sh", "UAH": "₴", "UGX": "USh",
    "UYU": "$U", "UZS": "сўм", "VES": "Bs.", "VND": "₫", "VUV": "VT",
    "WST": "WS$", "XAF": "FCFA", "XCD": "$", "XDR": "SDR", "XOF": "CFA",
    "XPF": "₣", "YER": "﷼", "ZAR": "R", "ZMW": "ZK", "ZWL": "$"
}
s = subprocess.run("ls",shell=True,capture_output=True,text=True)
files = s.stdout.splitlines()
jsons = [each for each in files if each=='dados.json']
pegoujson = False
if jsons == []:
    api_key = '80b7fffe2afc47478dd0f986' # autentica o uso de uma api
    moeda_relativa = 'USD' # pega a taxa de câmbio baseada nessa moeda
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{moeda_relativa}" # api de conversão de moedas
    r = requests.get(url)
    dados = r.json()
    with open("dados.json",'w') as f: json.dump(dados,f,indent=4)
    ultima_atualizacao = dados['time_last_update_utc'] # ultima atualização em utc+0
    proxima_atualizacao = dados['time_next_update_utc'] # próxima atualização em utc+0
    taxa_de_cambio = dados['conversion_rates'] # taxa de câmbio {valor:moeda} é baseada na moeda do urls
    pegoujson = True
# pega o conteúdo do json
caminho_atual = subprocess.run("pwd",shell=True,capture_output=True,text=True).stdout[:-1] # caminho atual sem /n
path = Path(f'{caminho_atual}/dados.json')
conteudo_json = json.loads(path.read_text())

data_posterior = conteudo_json['time_next_update_unix'] # 1730930400 pra testar a condição
data_utc = datetime.fromtimestamp(data_posterior, tz=timezone.utc)
data_utc = data_utc.astimezone(timezone(timedelta(hours=-3))) # data da api em horário de brasília

agora = datetime.now(timezone.utc)
agora = agora.astimezone(timezone(timedelta(hours=-3))) # horário de brasília

if agora>data_utc and not pegoujson: # o arquivo não existe ou está desatualizado
    api_key = '80b7fffe2afc47478dd0f986' # autentica o uso de uma api
    moeda_relativa = 'USD' # pega a taxa de câmbio baseada nessa moeda
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{moeda_relativa}" # api de conversão de moedas
    r = requests.get(url)
    dados = r.json()
    with open("dados.json",'w') as f: json.dump(dados,f,indent=4)
    ultima_atualizacao = dados['time_last_update_utc'] # ultima atualização em utc+0
    proxima_atualizacao = dados['time_next_update_utc'] # próxima atualização em utc+0
    taxa_de_cambio = dados['conversion_rates'] # taxa de câmbio {valor:moeda} é baseada na moeda do urls
else: # o arquivo existe E a data é anterior a time_next_update_utc
    moeda_relativa = 'USD'
    ultima_atualizacao = conteudo_json['time_last_update_utc']
    proxima_atualizacao = conteudo_json['time_next_update_utc']
    taxa_de_cambio = conteudo_json['conversion_rates']
# Função chamada quando uma opção for selecionada
def mostrar_selecao(*args):
    selecao = var.get() # pega o que ta selecionado
    label.config(text=f"Você selecionou: {selecao}") # muda no texto
def mostrar_selecao2(*args):
    selecao = var2.get()
    label2.config(text=f"Você selecionou: {selecao}")

# Criando a janela principal
def conversao(): # pega e muda o texto do resultado, coloca o simbolo do lado do valor direto no label
    q = quantidade.get()
    if q == '':
        q = 0
    resultado.config(text=f"{float(q)} {var.get()} = {simbolos_das_moedas[var2.get()]} {round(float(q)*(taxa_de_cambio[var2.get()]/taxa_de_cambio[var.get()]),4)}")
app = tk.Tk()
app.geometry('1000x500')
app.title('Conversor de moedas')
quantidade = tk.Entry(app)
quantidade.bind('<KeyRelease>',lambda event:conversao())
quantidade.grid(row=0,column=0)
# Variável para armazenar o valor selecionado
var = tk.StringVar() # texto do valor selecionado
var.set("Moeda base")
var2 = tk.StringVar() # texto do valor selecionado da outra moeda
var2.set("Moeda pra comparar")
opcoes = [k for k,v in conteudo_json['conversion_rates'].items()] # opções
menu = tk.OptionMenu(app, var, *opcoes)
menu.grid(row=0,column=1)
# Ligando a função à mudança na seleção
var.trace_add("write", mostrar_selecao) # muda o texto pra o que foi selecionado
# Criando um label para mostrar a seleção
label = tk.Label(app, text="Selecione um item do menu suspenso.")
label.grid(row=1,column=1)

igual = tk.Label(app,text='=')
igual.grid(row=0,column=2)

opcoes2 = [k for k,v in nomes_das_moedas.items()]
menu2 = tk.OptionMenu(app, var2, *opcoes2)
menu2.grid(row=0,column=3)
var2.trace_add("write", mostrar_selecao2)
label2 = tk.Label(app, text="Selecione um item do menu suspenso.")
label2.grid(row=1,column=3)
resultado = tk.Label(app,text='valor')
resultado.grid(row=0,column=4)
app.mainloop()
