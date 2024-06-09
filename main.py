from flask import Flask, request, render_template, redirect, url_for
import string as st
import secrets as sc

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gerar_senha', methods=['GET'])
def gerar_senha():
    letras = st.ascii_letters
    numeros = st.digits
    caracteres = st.punctuation[0:5]
    lista_caracteres = letras + numeros + caracteres

    tamanho_senha = int(request.args.get('tamanho', default=8))

    senha_segura = ''.join(sc.choice(lista_caracteres) for i in range(tamanho_senha))

    return redirect(url_for('resultado', senha=senha_segura))

@app.route('/resultado')
def resultado():
    senha = request.args.get('senha')
    return render_template('resultado.html', senha=senha)

if __name__ == '__main__':
    app.run(debug=True)
