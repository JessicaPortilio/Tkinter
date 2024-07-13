# Importando as bibliotecas necessárias
from tkinter import *
from tkinter import ttk
from tkinter import messagebox  # Para caixas de diálogo de mensagem
import openpyxl  # Para manipulação de arquivos Excel
import os  # Para operações de sistema, como verificar a existência de arquivos
import sqlite3  # Para trabalhar com banco de dados SQLite

# Função para inserir dados no banco de dados SQLite
def inserir_dados_no_banco(primeiro_nome, sobrenome, titulo, idade, nacionalidade, registrado_status, num_cursos, num_semestres):
    try:
        # Conectar ao banco de dados
        conectar = sqlite3.connect('dados.db')  # Estabelece uma conexão com o banco de dados SQLite 'dados.db'
        cursor = conectar.cursor()  # Cria um cursor para executar comandos SQL no banco de dados
        
        # Criar a tabela se não existir
        criar_tabela_de_consulta = '''CREATE TABLE IF NOT EXISTS Dados_do_Aluno
            (nome TEXT, sobrenome TEXT, titulo TEXT, idade INT, nacionalidade TEXT,
            status_do_registro TEXT, num_cursos INT, num_semestres INT)
        '''
        cursor.execute(criar_tabela_de_consulta)  # Executa o comando SQL para criar a tabela se ela não existir
        
        # Inserir os dados
        consulta_de_insercao_de_dados = '''INSERT INTO Dados_do_Aluno (nome, sobrenome, titulo, idade, nacionalidade, status_do_registro, num_cursos, num_semestres) 
            VALUES  (?, ?, ?, ?, ?, ?, ?, ?)'''
        tupla_insercao_de_dados = (primeiro_nome, sobrenome, titulo, idade, nacionalidade, registrado_status, num_cursos, num_semestres)
        
        cursor.execute(consulta_de_insercao_de_dados, tupla_insercao_de_dados)  # Executa o comando SQL para inserir os dados na tabela
        conectar.commit()  # Salva as alterações no banco de dados
        
    except sqlite3.Error as erro:
        print(f"Erro ao inserir dados: {erro}")  # Em caso de erro, imprime uma mensagem de erro específica
        
    finally:
        # Fechar a conexão com o banco de dados, garantindo que recursos sejam liberados
        if conectar:
            conectar.close()


# Função para inserir dados quando o botão é clicado
def inserir_dados():
    aceito = aceito_var.get()  # Obtém o valor da variável que verifica se os termos foram aceitos ou não

    if aceito == 'Aceito':  # Verifica se os termos foram aceitos
        # informações do usuário
        primeiro_nome = primeiro_nome_entry.get()  # Obtém o valor inserido no campo de primeiro nome
        sobrenome = sobrenome_entry.get()  # Obtém o valor inserido no campo de sobrenome

        if primeiro_nome and sobrenome:  # Verifica se os campos de primeiro nome e sobrenome não estão vazios
            titulo = titulo_combobox.get()  # Obtém o valor selecionado no combobox de título
            idade = idade_spinbox.get()  # Obtém o valor inserido no spinbox de idade
            nacionalidade = nacionalidade_combobox.get()  # Obtém o valor selecionado no combobox de nacionalidade
            
            # informações do curso
            registrado_status = registro_status_check_var.get()  # Obtém o status de registro selecionado
            num_cursos = num_cursos_spinbox.get()  # Obtém o valor inserido no spinbox de número de cursos
            num_semestres = num_semestres_spinbox.get()  # Obtém o valor inserido no spinbox de número de semestres
            
            # Imprimir informações para depuração (debugging)
            print(f'Nome: {primeiro_nome}, Sobrenome: {sobrenome}, Título: {titulo}, Idade: {idade}, Nacionalidade: {nacionalidade}')
            print(f'Nº de Cursos: {num_cursos}, Nº de Semestres: {num_semestres}')
            print(f'Registro: {registrado_status}')
            print('------------------------------------------------')
            
            # Salvando os dados no Excel
            arquivo = 'dados.xlsx'
            if not os.path.exists(arquivo):  # Verifica se o arquivo de Excel existe; se não existir, cria um novo
                workbook = openpyxl.Workbook()
                sheet = workbook.active
                cabecalho = ['Nome', 'Sobrenome', 'Título', 'Idade', 'Nacionalidade', 'Cursos', 'Semestres', 'Status do Registro']
                sheet.append(cabecalho)
                workbook.save(arquivo)
            workbook = openpyxl.load_workbook(arquivo)  # Carrega o arquivo de Excel existente
            sheet = workbook.active
            sheet.append([primeiro_nome, sobrenome, titulo, idade, nacionalidade, num_cursos, num_semestres, registrado_status])  # Adiciona os dados à planilha de Excel
            workbook.save(arquivo)  # Salva as alterações no arquivo de Excel
            
            # Salvando os dados no banco de dados SQLite
            inserir_dados_no_banco(primeiro_nome, sobrenome, titulo, idade, nacionalidade, registrado_status, num_cursos, num_semestres)
            
            # Limpar os campos após a inserção
            primeiro_nome_entry.delete(0, END)  # Limpa o campo de primeiro nome
            sobrenome_entry.delete(0, END)  # Limpa o campo de sobrenome
            titulo_combobox.set('')  # Reseta o combobox de título
            idade_spinbox.delete(0, END)  # Limpa o spinbox de idade
            idade_spinbox.insert(0, 18)  # Resetar o valor da idade para 18
            nacionalidade_combobox.set('')  # Reseta o combobox de nacionalidade
            registro_status_check_var.set('Não registrado')  # Reseta o status de registro
            num_cursos_spinbox.delete(0, END)  # Limpa o spinbox de número de cursos
            num_cursos_spinbox.insert(0, 0)  # Resetar o valor dos cursos para 0
            num_semestres_spinbox.delete(0, END)  # Limpa o spinbox de número de semestres
            num_semestres_spinbox.insert(0, 0)  # Resetar o valor dos semestres para 0
            
            # Exibir mensagem de sucesso
            messagebox.showinfo('Sucesso', 'Dados inseridos com sucesso!')
            
        else:
            messagebox.showwarning('Erro', 'Nome e sobrenome são obrigatórios!')  # Exibe um aviso se o nome ou sobrenome estiverem em branco
    else:
        messagebox.showwarning('Erro', 'Você não aceitou os termos!')  # Exibe um aviso se os termos não forem aceitos

# Configuração da janela principal
janela = Tk()  # Cria a janela principal
janela.title('Formulário De Entrada De Dados')  # Define o título da janela
janela.geometry('800x600')  # Define as dimensões da janela
janela.config(bg='#2e2e2e')  # Define a cor de fundo da janela

# Frame principal
frame = Frame(janela, bg='#2e2e2e')  # Cria um frame dentro da janela principal com cor de fundo específica
frame.pack(expand=True, fill=BOTH)  # Empacota o frame para expandir e preencher todo o espaço disponível

# Função para centralizar o frame na janela
def centralizar_frame(event=None):
    largura_janela = janela.winfo_width()  # Obtém a largura atual da janela
    altura_janela = janela.winfo_height()  # Obtém a altura atual da janela
    largura_frame = frame.winfo_reqwidth()  # Obtém a largura requisitada do frame
    altura_frame = frame.winfo_reqheight()  # Obtém a altura requisitada do frame
    
    x = max(0, (largura_janela - largura_frame) // 2)  # Calcula a posição x para centralizar o frame
    y = max(0, (altura_janela - altura_frame) // 2)  # Calcula a posição y para centralizar o frame
    
    frame.place_configure(x=x, y=y)  # Configura a posição do frame na janela

# Salvando informações do usuário
informacao_de_usuario_frame = LabelFrame(frame, text='Informação de Usuário', bg='#3e3e3e', fg='#ffffff', font=('Arial', 14, 'bold'))
informacao_de_usuario_frame.grid(row=0, column=0, padx=20, pady=20, ipadx=10, ipady=10)

# Labels e Entries para primeiro nome e sobrenome
primeiro_nome_label = Label(informacao_de_usuario_frame, text='Primeiro Nome', bg='#3e3e3e', fg='#ffffff', font=('Arial', 12))
primeiro_nome_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')

sobrenome_label = Label(informacao_de_usuario_frame, text='Sobrenome', bg='#3e3e3e', fg='#ffffff', font=('Arial', 12))
sobrenome_label.grid(row=0, column=1, padx=5, pady=5, sticky='w')

primeiro_nome_entry = Entry(informacao_de_usuario_frame, font=('Arial', 12))
primeiro_nome_entry.grid(row=1, column=0, padx=5, pady=5)

sobrenome_entry = Entry(informacao_de_usuario_frame, font=('Arial', 12))
sobrenome_entry.grid(row=1, column=1, padx=5, pady=5)

# Label e Combobox para título
titulo_label = Label(informacao_de_usuario_frame, text='Título', bg='#3e3e3e', fg='#ffffff', font=('Arial', 12))
titulo_label.grid(row=0, column=2, padx=5, pady=5, sticky='w')

titulo_combobox = ttk.Combobox(informacao_de_usuario_frame, values=['', 'Sr.', 'Sra.', 'Dr.'], font=('Arial', 12))
titulo_combobox.grid(row=1, column=2, padx=5, pady=5)

# Label e Spinbox para idade
idade_label = Label(informacao_de_usuario_frame, text='Idade', bg='#3e3e3e', fg='#ffffff', font=('Arial', 12))
idade_label.grid(row=2, column=0, padx=5, pady=5, sticky='w')

idade_spinbox = Spinbox(informacao_de_usuario_frame, from_=18, to=110, font=('Arial', 12))
idade_spinbox.grid(row=3, column=0, padx=5, pady=5)

# Label e Combobox para nacionalidade
nacionalidade_label = Label(informacao_de_usuario_frame, text='Nacionalidade', bg='#3e3e3e', fg='#ffffff', font=('Arial', 12))
nacionalidade_label.grid(row=2, column=1, padx=5, pady=5, sticky='w')

nacionalidade_combobox = ttk.Combobox(informacao_de_usuario_frame, values=[
    '', 'Brasileiro(a)', 'Americano(a)', 'Canadense', 'Mexicano(a)', 
    'Argentino(a)', 'Chileno(a)', 'Peruano(a)', 'Colombiano(a)', 
    'Venezuelano(a)', 'Boliviano(a)', 'Paraguaio(a)', 'Uruguaio(a)', 
    'Equatoriano(a)', 'Alemão(ã)', 'Francês(a)', 'Italiano(a)', 'Espanhol(a)', 'Português(a)', 
    'Inglês(a)', 'Chinês(a)', 'Japonês(a)', 'Coreano(a)'
], font=('Arial', 12))
nacionalidade_combobox.grid(row=3, column=1, padx=5, pady=5)

# Configuração do padding para os widgets do informacao_de_usuario_frame
for widget in informacao_de_usuario_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Salvando informações do curso
cursos_frame = LabelFrame(frame, text='Informação do Curso', bg='#3e3e3e', fg='#ffffff', font=('Arial', 14, 'bold'))
cursos_frame.grid(row=1, column=0, sticky='NEWS', padx=20, pady=20, ipadx=10, ipady=10)

# Label e Checkbutton para status de registro
registro_label = Label(cursos_frame, text='Status de registro', bg='#3e3e3e', fg='#ffffff', font=('Arial', 12))
registro_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')

registro_status_check_var = StringVar(value='Não registrado')
registro_check = Checkbutton(cursos_frame, text='Registrado atualmente', variable=registro_status_check_var, onvalue='Registrado', offvalue='Não registrado', bg='#3e3e3e', fg='#ffffff', font=('Arial', 12), selectcolor='#3e3e3e')
registro_check.grid(row=1, column=0, padx=5, pady=5, sticky='w')

# Label e Spinbox para número de cursos concluídos
num_cursos_label = Label(cursos_frame, text='# Cursos Concluídos', bg='#3e3e3e', fg='#ffffff', font=('Arial', 12))
num_cursos_label.grid(row=0, column=1, padx=5, pady=5, sticky='w')

num_cursos_spinbox = Spinbox(cursos_frame, from_=0, to='infinity', font=('Arial', 12))
num_cursos_spinbox.grid(row=1, column=1, padx=5, pady=5)

# Label e Spinbox para número de semestres
num_semestres_label = Label(cursos_frame, text='# Semestres', bg='#3e3e3e', fg='#ffffff', font=('Arial', 12))
num_semestres_label.grid(row=0, column=2, padx=5, pady=5, sticky='w')

num_semestres_spinbox = Spinbox(cursos_frame, from_=0, to='infinity', font=('Arial', 12))
num_semestres_spinbox.grid(row=1, column=2, padx=5, pady=5)

# Configuração do padding para os widgets do cursos_frame
for widget in cursos_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Aceite os termos
termos_frame = LabelFrame(frame, text='Termos & Condições', bg='#3e3e3e', fg='#ffffff', font=('Arial', 14, 'bold'))
termos_frame.grid(row=2, column=0, sticky='NEWS', padx=20, pady=20, ipadx=10, ipady=10)

aceito_var = StringVar(value='Não aceito')
termos_check = Checkbutton(termos_frame, text='Eu aceito os termos e condições.', variable=aceito_var, onvalue='Aceito', offvalue='Não aceito', bg='#3e3e3e', fg='#ffffff', font=('Arial', 12), selectcolor='#3e3e3e')
termos_check.grid(row=0, column=0, padx=5, pady=5)

# Botão para inserir dados
botao = Button(frame, text='Inserir dados', command=inserir_dados, bg='#007acc', fg='#ffffff', font=('Arial', 14, 'bold'))
botao.grid(row=3, column=0, sticky='NEWS', padx=20, pady=20)

# Configuração de eventos para centralizar o frame
janela.bind('<Configure>', centralizar_frame)

# Inicia o loop principal da interface gráfica
janela.mainloop()
