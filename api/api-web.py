# api that picks a value and says the amount of money and coins it will use

from flask import *
from collections import Counter

app = Flask(__name__)

@app.route("/favicon.ico",methods=['GET'])
def icon():
    return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route("/<value>.<value2>")
def dec(value,value2):
    currency = float(f"{value}.{value2}")
    if currency > 1_000_000:
        return f"{currency} é um valor muito alto, insira um valor menor do que 1000000"
    elif currency < 0.05:
        return f"{currency} é um valor muito pequeno, insira um valor maior do que 0.04"
    steps = []
    while currency >= 0.05: # if it compares to 0 rounding error occour
        if currency >= 200:
            currency -= 200
            steps.append(200)
        elif currency >= 100:
            currency -= 100
            steps.append(100)
        elif currency >= 50:
            currency -= 50
            steps.append(50)
        elif currency >= 20:
            currency -= 20
            steps.append(20)
        elif currency >= 10:
            currency -= 10
            steps.append(10)
        elif currency >= 5:
            currency -= 5
            steps.append(5)
        elif currency >= 2:
            currency -= 2
            steps.append(2)
        elif currency >= 1:
            currency -= 1
            steps.append(1)
        elif currency >= 0.50:
            steps.append(0.50)
            currency -= 0.50
        elif currency >= 0.25:
            steps.append(0.25)
            currency -= 0.25
        elif currency >= 0.10:
            steps.append(0.10)
            currency -= 0.10
        elif currency >= 0.05:
            steps.append(0.05)
            currency -= 0.05
    return jsonify(Counter(steps))

@app.route("/<value>")
def index_page(value):
    return redirect (url_for('dec',value=value,value2=0))

if __name__ == '__main__':
    app.run(debug=True)
# noção de tantas notas em estoque