# api-web simples que retorna os valores de um formulário, ele pede nome(str), senha(str) e conectado(bool)

from flask import *

app = Flask(__name__)

@app.route('/formulario',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        nome = request.form.get('nome')
        senha = request.form.get('senha')
        conectado = request.form.get('conectado')
    return render_template('main.html') 

@app.route('/')
def alt():
    return redirect(url_for('index'))

if __name__ == '__main__': app.run(debug=True)