import sqlite3
# Importa o módulo sqlite3 para trabalhar com banco de dados SQLite
# import mysql.connector
# conn = mysql.connector.connect(host='localhost', user='root', 
#   password='coloque_sua_senha', database='seu banco de dados')

# Função para conectar ao banco de dados e criar a tabela se ela não existir
def conectar():
    conexao = sqlite3.connect('pessoas.db')
    # Conecta ao banco de dados chamado 'pessoas.db'. Se não existir, ele será criado
    curso = conexao.cursor()
    # Cria um cursor para executar comandos SQL no banco de dados
    curso.execute('''
                CREATE TABLE IF NOT EXISTS pessoa (
                    id INTEGER PRIMARY KEY,
                    nome TEXT NOT NULL,
                    idade INTEGER,
                    email TEXT
                )
                ''')
    # Cria uma tabela chamada 'pessoa' com as colunas 'id', 'nome', 'idade' e 'email'
    # Se a tabela já existir, o comando não faz nada
    conexao.commit()
    # Confirma as mudanças no banco de dados
    conexao.close()
    # Fecha a conexão com o banco de dados

# Função para inserir uma nova pessoa no banco de dados
def inserir_pessoa(nome, idade, email):
    conexao = sqlite3.connect('pessoas.db')
    # Conecta ao banco de dados 'pessoas.db'
    curso = conexao.cursor()
    # Cria um cursor para executar comandos SQL
    curso.execute('INSERT INTO pessoa (nome, idade, email) VALUES (?, ?, ?)', (nome, idade, email))
    # Insere uma nova linha na tabela 'pessoa' com os valores fornecidos para nome, idade e email
    conexao.commit()
    # Confirma as mudanças no banco de dados
    conexao.close()
    # Fecha a conexão com o banco de dados

# Função para atualizar as informações de uma pessoa no banco de dados
def atualizar_pessoa(id_pessoa, nome, idade, email):
    conexao = sqlite3.connect('pessoas.db')
    # Conecta ao banco de dados 'pessoas.db'
    curso = conexao.cursor()
    # Cria um cursor para executar comandos SQL
    curso.execute('UPDATE pessoa SET nome = ?, idade = ?, email = ? WHERE id = ?', (nome, idade, email, id_pessoa))
    # Atualiza os dados da pessoa com o ID fornecido, definindo novo nome, idade e email
    conexao.commit()
    # Confirma as mudanças no banco de dados
    conexao.close()
    # Fecha a conexão com o banco de dados

# Função para deletar uma pessoa do banco de dados
def deletar_pessoa(id_pessoa):
    conexao = sqlite3.connect('pessoas.db')
    # Conecta ao banco de dados 'pessoas.db'
    curso = conexao.cursor()
    # Cria um cursor para executar comandos SQL
    curso.execute('DELETE FROM pessoa WHERE id = ?', (id_pessoa,))
    # Deleta a linha da tabela 'pessoa' que possui o ID fornecido
    conexao.commit()
    # Confirma as mudanças no banco de dados
    conexao.close()
    # Fecha a conexão com o banco de dados

# Função para pesquisar pessoas no banco de dados pelo nome
def pesquisar_pessoa(nome):
    conexao = sqlite3.connect('pessoas.db')
    # Conecta ao banco de dados 'pessoas.db'
    curso = conexao.cursor()
    # Cria um cursor para executar comandos SQL
    curso.execute('SELECT * FROM pessoa WHERE nome LIKE ?', ('%' + nome + '%', ))
    # Seleciona todas as linhas da tabela 'pessoa' onde o nome contém o texto fornecido
    linhas = curso.fetchall()
    # Busca todas as linhas correspondentes e armazena na variável 'linhas'
    conexao.close()
    # Fecha a conexão com o banco de dados
    return linhas
    # Retorna a lista de linhas encontradas

# Função para listar todas as pessoas no banco de dados
def lista_as_pessoas():
    conexao = sqlite3.connect('pessoas.db')
    # Conecta ao banco de dados 'pessoas.db'
    curso = conexao.cursor()
    # Cria um cursor para executar comandos SQL
    curso.execute('SELECT * FROM pessoa')
    # Seleciona todas as linhas da tabela 'pessoa'
    linhas = curso.fetchall()
    # Busca todas as linhas e armazena na variável 'linhas'
    conexao.close()
    # Fecha a conexão com o banco de dados
    return linhas
    # Retorna a lista de todas as pessoas
