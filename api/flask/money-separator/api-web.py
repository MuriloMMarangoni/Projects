# api that picks a value and says the amount of money and coins it will use

from flask import *
from collections import Counter

app = Flask(__name__)

@app.route("/",methods=['GET'])
def home():
    return "Welcome to my money separator API project!\n You can use BRL/USD and given a amount of money, it says the bills and coins that could be used to make that amount.\n For example : /USD/2.5 shoud return a json with {'2':1,'0.5':1}"

@app.route("/favicon.ico",methods=['GET'])
def icon():
    return send_from_directory(directory='static',path='icon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/<money>/<value>.<value2>")
def dec(money,value,value2):

    BRL = [0.05,0.1,0.25,0.5,1,2,5,10,20,50,100,200]
    USD = [0.01,0.05,0.1,0.25,0.5,1,2,5,10,20,50,100]

    if money not in ['BRL','USD']: return f"Insert valid currency: BRL/USD, instead of {money}"

    currency = float(f"{value}.{value2}")
    steps = []

    if money == 'BRL':
        if currency > 1_000_000:
            return f"{currency} é um valor muito alto, insira um valor menor do que 1 000 000"
        elif currency < 0.05:
            return f"{currency} é um valor muito pequeno, insira um valor maior do que 0.04"

        while currency >= 0.05: # if it compares to 0 a rounding error occour
            for each in BRL[::-1]:
                if currency >= each:
                    currency -= each
                    steps.append(each)
                    break
        return jsonify(Counter(steps))
    else:
        if currency > 1_000_000:
            return f"{currency} is too big, choose a value lower than 1 000 000"
        elif currency < 0.01:
            return f"{currency} is too lower, choose a value bigger than 0.009.."
        while currency >= 0.01: # if it compares to 0 a rounding error occour
            for each in USD[::-1]:
                if currency >= each:
                    currency -= each
                    steps.append(each)
                    break

        result = sum(steps)

        equal = round(result,2) == round(float(f"{value}.{value2}"),2)

        if equal:
            return jsonify(Counter(steps))
        if round(float(f"{value}.{value2}") - sum(steps),2) == 0.01: # 1 cent aproximation handle
            steps.append(0.01)
            return jsonify(Counter(steps))
@app.route("/<money>/<value>")
def index_page(money,value):
    return redirect (url_for('dec',money=money,value=value,value2=0))

if __name__ == '__main__':
    app.run(debug=True)