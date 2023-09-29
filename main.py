from flask import Flask, request, render_template, redirect  
import sqlite3

app = Flask(__name__)

# Função para criar a tabela
def criar_tabela():
    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS pessoas (
                        id INTEGER PRIMARY KEY,
                        nome TEXT,
                        idade INTEGER
                    )''')
    conexao.commit()
    conexao.close()

# Rota GET para exibir a página inicial com o formulário
@app.route('/', methods=['GET'])
def mostrar_formulario():
    criar_tabela()
    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM pessoas")
    pessoas = cursor.fetchall()
    conexao.close()
    return render_template('index.html', pessoas=pessoas)

# Rota POST para lidar com a submissão do formulário
@app.route('/', methods=['POST'])
def adicionar_nome():
    nome = request.form['nome']
    idade = request.form['cah']
    if nome:
        conexao = sqlite3.connect('exemplo.db')
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO pessoas (nome, idade) VALUES (?, ?)", (nome, idade))
        conexao.commit()
        conexao.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
