from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


lista_tarefas = []

@app.route('/')
def index():
    return render_template('index.html')

#Função pra adicionar tarefas
@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar_tarefa():
    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        horario = request.form['horario']
        
        nova_tarefa = {
            "titulo" : titulo,
            "descricao" : descricao,
            "horario" : horario
        }
        lista_tarefas.append(nova_tarefa)
        return redirect(url_for('listar_tarefas'))
    
    return render_template('adicionar_tarefa.html')

#Função pra consultar Tarefas
@app.route('/listar')
def listar_tarefas():
    return render_template('listar_tarefas.html', tarefas=lista_tarefas)

@app.route('/concluir', methods=['GET', 'POST'])
def concluir_tarefa():
    if request.method == 'POST':
        titulo = request.form['titulo']
        for tarefa in lista_tarefas:
            if tarefa["titulo"].lower() == titulo.lower():
                lista_tarefas.remove(tarefa)
                return redirect(url_for('listar_tarefas'))
    
    return render_template('concluir_tarefa.html')

#Função pra excluir Tarefas
@app.route('/remover', methods=['GET', 'POST'])
def remover_tarefa():
    if request.method == 'POST':
        titulo = request.form['titulo']
        for tarefa in lista_tarefas:
            if tarefa["titulo"].lower() == titulo.lower():
                lista_tarefas.remove(tarefa)
                return redirect(url_for('listar_tarefas'))
    
    return render_template('remover_tarefa.html')

if __name__ == '__main__':
    app.run(debug=True)
