from tkinter import *  # Importa todos os componentes do Tkinter
from tkinter import ttk  # Importa o módulo ttk do Tkinter para widgets estilizados
from tkinter import messagebox  # Importa messagebox do Tkinter para exibir mensagens
import random  # Importa o módulo random
import time  # Importa o módulo time
import datetime  # Importa o módulo datetime
import mysql.connector

class Hospital:
    def __init__(self, janela):
        # Inicializa a janela principal
        self.janela = janela
        self.janela.title('Sistema de Gestão Hospitalar')  # Define o título da janela principal
        self.janela.geometry('1540x800+0+0')  # Define o tamanho e a posição da janela
        
        # Cria e configura o rótulo do título
        titulo_label = Label(self.janela, bd=10, relief=RIDGE, 
                            text='SISTEMA DE GESTÃO HOSPITALAR', fg='red', bg='white', 
                            font=('times new roman', 50, 'bold'))
        titulo_label.pack(side=TOP, fill=X)  # Posiciona o rótulo no topo e o preenche horizontalmente
        
        # Cria o frame de dados
        dados_frame = Frame(self.janela, bd=10, relief=RIDGE)
        dados_frame.place(x=0, y=130, width=1530, height=400)  # Define a posição e o tamanho do frame de dados
        #  essa linha de código está posicionando o dados_frame 130 pixels 
        # abaixo do topo da janela principal e 
        # ocupando toda a largura da janela (1530 pixels), com uma altura de 400 pixels.
        
        # Cria e configura o frame de dados à esquerda
        dados_frame_esquerda = LabelFrame(dados_frame, bd=5, relief=RIDGE, padx=10,
                                        font=('times new roman', 12, 'bold'),
                                        text='Informação do Paciente')
        dados_frame_esquerda.place(x=0, y=5, width=1000, height=350)  # Define a posição e o tamanho do frame à esquerda
        
        # Cria e configura o frame de dados à direita
        dados_frame_direita = LabelFrame(dados_frame, bd=5, relief=RIDGE, padx=10,
                                        font=('times new roman', 12, 'bold'),
                                        text='Prescrição Médica')
        dados_frame_direita.place(x=1010, y=5, width=490, height=350)  # Define a posição e o tamanho do frame à direita
        
        # Cria o frame para os botões
        botao_frame = Frame(self.janela, bd=10, relief=RIDGE)
        botao_frame.place(x=0, y=530, width=1530, height=70)  # Define a posição e o tamanho do frame de botões
        
        # Cria o frame para os detalhes
        detalhes_frame = Frame(self.janela, bd=10, relief=RIDGE)
        detalhes_frame.place(x=0, y=600, width=1530, height=190)  # Define a posição e o tamanho do frame de detalhes
        
        # Dados frame à esquerda (aqui podem ser adicionados os widgets específicos para informações do paciente)
        # Código adicional necessário para adicionar widgets específicos como Labels, Entries, etc.
        
        self.nome_medicamento = StringVar()
        self.referencia = StringVar()
        self.dose = StringVar()
        self.numero_de_comprimidos = StringVar()
        self.lote = StringVar()
        self.data_de_emissao = StringVar()
        self.data_de_validade = StringVar()
        self.dose_diaria = StringVar()
        self.efeito_colateral = StringVar()
        self.informacao_adicionais = StringVar()
        self.pressao_arterial = StringVar()
        self.orientacao_de_armazenamento = StringVar()
        self.medicamento = StringVar()
        self.id_do_paciente = StringVar()
        self.numero_do_NHS = StringVar()
        self.nome_do_paciente = StringVar()
        self.data_de_nascimento = StringVar()
        self.endereco_do_paciente = StringVar()
        
        
        
        nome_medicamento_label = Label(dados_frame_esquerda, text='Nomes de Medicamentos', 
                                font=('Arial', 12, 'bold'),
                                padx=2, pady=6)
        nome_medicamento_label.grid(row=0, column=0, sticky='w')
        
        nome_medicamento_combobox = ttk.Combobox(dados_frame_esquerda, 
                                        textvariable=self.nome_medicamento, state='readonly',
                                        font=('times new roman', 12, 'bold'),
                                        width=27)
        nome_medicamento_combobox['values'] = ('Vacina Corona', 'Paracetamol', 'Ritalina', 'Amlodipina', 'Lorazepam')
        nome_medicamento_combobox.grid(row=0, column=1)
        
        referencia_label = Label(dados_frame_esquerda, text='Referência:', 
                        font=('Arial', 12, 'bold'), padx=2)
        referencia_label.grid(row=1, column=0, sticky='w')
        texto_referencia_entry = Entry(dados_frame_esquerda, textvariable=self.referencia, 
                                    font=('Arial', 13, 'bold'), width=27)
        texto_referencia_entry.grid(row=1, column=1)

        dose_label = Label(dados_frame_esquerda, text='Dose:', 
                        font=('Arial', 12, 'bold'), padx=2, pady=4)
        dose_label.grid(row=2, column=0, sticky='w')
        texto_dose_entry = Entry(dados_frame_esquerda, textvariable=self.dose,
                                font=('Arial', 13, 'bold'), width=27)
        texto_dose_entry.grid(row=2, column=1)
        
        num_de_comprimidos_label = Label(dados_frame_esquerda, text='Nº de Comprimidos:', 
                            font=('Arial', 12, 'bold'), padx=2, pady=6)
        num_de_comprimidos_label.grid(row=3, column=0, sticky='w')

        texto_num_de_comprimidos_entry = Entry(dados_frame_esquerda, textvariable=self.numero_de_comprimidos,
                                        font=('Arial', 13, 'bold'), width=27)
        texto_num_de_comprimidos_entry.grid(row=3, column=1)
        
        lote_label = Label(dados_frame_esquerda, text='Lote:', 
                            font=('Arial', 12, 'bold'), padx=2, pady=6)
        lote_label.grid(row=4, column=0, sticky='w')
        texto_lote_entry = Entry(dados_frame_esquerda, textvariable=self.lote,
                                        font=('Arial', 13, 'bold'), width=27)
        texto_lote_entry.grid(row=4, column=1)
        
        data_de_emissao_label = Label(dados_frame_esquerda, text='Data de Emissao:', 
                            font=('Arial', 12, 'bold'), padx=2, pady=6)
        data_de_emissao_label.grid(row=5, column=0, sticky='w')
        texto_data_de_emissao_entry = Entry(dados_frame_esquerda, textvariable=self.data_de_emissao,
                                        font=('Arial', 13, 'bold'), width=27)
        texto_data_de_emissao_entry.grid(row=5, column=1)
        
        data_de_validade_label = Label(dados_frame_esquerda, text='Data de Validade:', 
                            font=('Arial', 12, 'bold'), padx=2, pady=6)
        data_de_validade_label.grid(row=6, column=0, sticky='w')
        texto_data_de_validade_entry = Entry(dados_frame_esquerda, textvariable=self.data_de_validade,
                                        font=('Arial', 13, 'bold'), width=27)
        texto_data_de_validade_entry.grid(row=6, column=1)
        
        dose_diaria_label = Label(dados_frame_esquerda, text='Dose Diária:', 
                            font=('Arial', 12, 'bold'), padx=2, pady=6)
        dose_diaria_label.grid(row=7, column=0, sticky='w')
        texto_dose_diaria_entry = Entry(dados_frame_esquerda, textvariable=self.dose_diaria,
                                        font=('Arial', 13, 'bold'), width=27)
        texto_dose_diaria_entry.grid(row=7, column=1)
        
        efeito_colateral_label = Label(dados_frame_esquerda, text='Efeito Colateral:', 
                            font=('Arial', 12, 'bold'), padx=2, pady=6)
        efeito_colateral_label.grid(row=8, column=0, sticky='w')
        texto_efeito_colateral_entry = Entry(dados_frame_esquerda, textvariable=self.efeito_colateral,
                                        font=('Arial', 13, 'bold'), width=27)
        texto_efeito_colateral_entry.grid(row=8, column=1)
        
        informacoes_adicionais_label = Label(dados_frame_esquerda, text='Informação Adicionais:', 
                            font=('Arial', 12, 'bold'), padx=2)
        informacoes_adicionais_label.grid(row=0, column=2, sticky='w')
        texto_informacoes_adicionais_entry = Entry(dados_frame_esquerda, textvariable=self.informacao_adicionais,
                                        font=('Arial', 12, 'bold'), width=27)
        texto_informacoes_adicionais_entry.grid(row=0, column=3)
        
        pressao_arterial_label = Label(dados_frame_esquerda, text='Pressão Arterial:', 
                            font=('Arial', 12, 'bold'), padx=2, pady=6)
        pressao_arterial_label.grid(row=1, column=2, sticky='w')
        texto_pressao_arterial_entry = Entry(dados_frame_esquerda, textvariable=self.pressao_arterial,
                                        font=('Arial', 12, 'bold'), width=27)
        texto_pressao_arterial_entry.grid(row=1, column=3)
        
        orientacao_de_armazenamento_label = Label(dados_frame_esquerda, text='Orientação de Amarzenamento:', 
                            font=('Arial', 12, 'bold'), padx=2, pady=6)
        orientacao_de_armazenamento_label.grid(row=2, column=2, sticky='w')
        texto_orientacao_de_armazenamento_entry = Entry(dados_frame_esquerda, textvariable=self.orientacao_de_armazenamento,
                                        font=('Arial', 12, 'bold'), width=27)
        texto_orientacao_de_armazenamento_entry.grid(row=2, column=3)
        
        medicamento_label = Label(dados_frame_esquerda, text='Medicamento', 
                            font=('Arial', 12, 'bold'), padx=2, pady=6)
        medicamento_label.grid(row=3, column=2, sticky='w')
        texto_medicamento_entry = Entry(dados_frame_esquerda, textvariable=self.medicamento,
                                        font=('Arial', 12, 'bold'), width=27)
        texto_medicamento_entry.grid(row=3, column=3)
        
        id_do_paciente_label = Label(dados_frame_esquerda, text='Id do Paciente', 
                            font=('Arial', 12, 'bold'), padx=2, pady=6)
        id_do_paciente_label.grid(row=4, column=2, sticky='w')
        texto_id_do_paciente_entry = Entry(dados_frame_esquerda, textvariable=self.id_do_paciente,
                                        font=('Arial', 12, 'bold'), width=27)
        texto_id_do_paciente_entry.grid(row=4, column=3)
        
        # Número do Sistema de Saúde
        numero_do_nhs_label = Label(dados_frame_esquerda, text='Número do NHS', 
                            font=('Arial', 12, 'bold'), padx=2, pady=6)
        numero_do_nhs_label.grid(row=5, column=2, sticky='w')
        texto_numero_do_nhs_entry = Entry(dados_frame_esquerda, textvariable=self.numero_do_NHS,
                                        font=('Arial', 12, 'bold'), width=27)
        texto_numero_do_nhs_entry.grid(row=5, column=3)
        
        nome_do_paciente_label = Label(dados_frame_esquerda, text='Nome do Paciente', 
                            font=('Arial', 12, 'bold'), padx=2, pady=6)
        nome_do_paciente_label.grid(row=6, column=2, sticky='w')
        texto_nome_do_paciente_entry = Entry(dados_frame_esquerda, textvariable=self.nome_do_paciente,
                                        font=('Arial', 12, 'bold'), width=27)
        texto_nome_do_paciente_entry.grid(row=6, column=3)
        
        data_de_nascimento_label = Label(dados_frame_esquerda, text='Data de Nascimento:', 
                            font=('Arial', 12, 'bold'), padx=2, pady=6)
        data_de_nascimento_label.grid(row=7, column=2, sticky='w')
        texto_data_de_nascimento_entry = Entry(dados_frame_esquerda, textvariable=self.data_de_nascimento,
                                        font=('Arial', 12, 'bold'), width=27)
        texto_data_de_nascimento_entry.grid(row=7, column=3)
        
        endereco_do_paciente_label = Label(dados_frame_esquerda, text='Endereço do Paciente:', 
                            font=('Arial', 12, 'bold'), padx=2, pady=6)
        endereco_do_paciente_label.grid(row=8, column=2, sticky='w')
        texto_endereco_do_paciente_entry = Entry(dados_frame_esquerda, textvariable=self.endereco_do_paciente,
                                        font=('Arial', 12, 'bold'), width=27)
        texto_endereco_do_paciente_entry.grid(row=8, column=3)
        
        
        # Dados frame à direita
        self.textoPrescricao = Text(dados_frame_direita, font=('Arial', 11), 
                                width=57, height=18, padx=2, pady=6)
        self.textoPrescricao.grid(row=0, column=0)
        
        # Botões
        botao_Prescricao = Button(botao_frame, command=self.informacao_Prescricao, text='Prescrição', bg='#007ACC', fg='white', 
                                font=('Arial', 12, 'bold'), 
                                width=23, height=2, padx=2, pady=2)
        botao_Prescricao.grid(row=0, column=0)
        
        botao_Dados_de_Prescricao = Button(botao_frame,command=self.info_de_Dados_de_Prescricao, text='Dados de Prescrição', bg='#007ACC', fg='white', 
                                font=('Arial', 12, 'bold'), 
                                width=23, height=2, padx=2, pady=2)
        botao_Dados_de_Prescricao.grid(row=0, column=1)

                
        botao_Atualizar = Button(botao_frame, command=self.autualizar_Dados, text='Atualizar', bg='#007ACC', fg='white', 
                                font=('Arial', 12, 'bold'), 
                                width=23, height=2, padx=2, pady=2)
        botao_Atualizar.grid(row=0, column=2)
        
        botao_excluir = Button(botao_frame,command=self.deletar_Dados, text='Excluir', bg='#007ACC', fg='white', 
                                font=('Arial', 12, 'bold'), 
                                width=23, height=2, padx=2, pady=2)
        botao_excluir.grid(row=0, column=3)
        
        botao_limpar = Button(botao_frame, command=self.limpar, text='Limpar', bg='#007ACC', fg='white', 
                                font=('Arial', 12, 'bold'), 
                                width=23, height=2, padx=2, pady=2)
        botao_limpar.grid(row=0, column=4)
        
        botao_sair = Button(botao_frame, command=self.sair, text='Sair', bg='#007ACC', fg='white', 
                                font=('Arial', 12, 'bold'), 
                                width=23, height=2, padx=2, pady=2)
        botao_sair.grid(row=0, column=5)
        
        # Tabela
        scroll_x = Scrollbar(detalhes_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(detalhes_frame, orient=VERTICAL)
        self.hospital_tabela = ttk.Treeview(detalhes_frame, columns=('Nomes de Medicamentos', 'Referência', 
                                                            'Dose', 'Nº de Comprimidos', 
                                                            'Lote', 'Data de Emissão', 
                                                            'Data de Validade', 'Dose Diária', 
                                                            'Efeito Colateral', 'Informações Adicionais',
                                                            'Pressão Arterial', 'Orientação de Armazenamento',  # Adicione a vírgula aqui
                                                            'Medicamento', 'Id do Paciente',
                                                            'Número do NHS', 'Nome do Paciente',
                                                            'Data de Nascimento', 'Endereço do Paciente'), 
                                    xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.hospital_tabela.xview)
        scroll_y.config(command=self.hospital_tabela.yview)
        
        
        self.hospital_tabela.heading('Nomes de Medicamentos', text='Nomes de Medicamentos')
        self.hospital_tabela.heading('Referência', text='Referência')
        self.hospital_tabela.heading('Dose', text='Dose')
        self.hospital_tabela.heading('Nº de Comprimidos', text='Nº de Comprimidos')
        self.hospital_tabela.heading('Lote', text='Lote')
        self.hospital_tabela.heading('Data de Emissão', text='Data de Emissão')
        self.hospital_tabela.heading('Data de Validade', text='Data de Validade')
        self.hospital_tabela.heading('Dose Diária', text='Dose Diária')
        self.hospital_tabela.heading('Efeito Colateral', text='Efeito Colateral')
        self.hospital_tabela.heading('Informações Adicionais', text='Informações Adicionais')
        self.hospital_tabela.heading('Pressão Arterial', text='Pressão Arterial')
        self.hospital_tabela.heading('Orientação de Armazenamento', text='Orientação de Armazenamento')
        self.hospital_tabela.heading('Medicamento', text='Medicamento')
        self.hospital_tabela.heading('Id do Paciente', text='Id do Paciente')
        self.hospital_tabela.heading('Número do NHS', text='Número do NHS')
        self.hospital_tabela.heading('Nome do Paciente', text='Nome do Paciente')
        self.hospital_tabela.heading('Data de Nascimento', text='Data de Nascimento')
        self.hospital_tabela.heading('Endereço do Paciente', text='Endereço do Paciente')
        
        self.hospital_tabela['show']='headings'
        self.hospital_tabela.pack(fill=BOTH, expand=1)
        self.hospital_tabela.bind('<ButtonRelease-1>', self.acessar_cursor)
        self.buscar_dados()
        
        
    def info_de_Dados_de_Prescricao(self, event=None):
        if self.nome_medicamento.get() == '' or self.referencia.get() == '':
            messagebox.showerror('Erro', 'Todos os campos são necessários.')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', user='root', password='coloque_sua_senha', database='Mydata')
                my_cursor = conn.cursor()
                
                # Corrigindo a consulta SQL e inserindo os dados no banco
                my_cursor.execute('INSERT INTO hospital VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                                (self.nome_medicamento.get(), self.referencia.get(), self.dose.get(), self.numero_de_comprimidos.get(),
                                self.lote.get(), self.data_de_emissao.get(), self.data_de_validade.get(), self.dose_diaria.get(),
                                self.efeito_colateral.get(), self.informacao_adicionais.get(), self.pressao_arterial.get(),
                                self.orientacao_de_armazenamento.get(), self.medicamento.get(), self.id_do_paciente.get(),
                                self.numero_do_NHS.get(), self.nome_do_paciente.get(), self.data_de_nascimento.get(),
                                self.endereco_do_paciente.get()))
                
                conn.commit()
                self.buscar_dados()
                conn.close()
                self.limpar()
                
                messagebox.showinfo('Sucesso', 'O registro foi inserido com sucesso!')
            
            except mysql.connector.Error as error:
                messagebox.showerror('Erro', f'Erro ao inserir registro: {error}')


    def buscar_dados(self):
        try:
            conn = mysql.connector.connect(host='localhost', user='root', password='coloque_sua_senha', database='Mydata')
            my_cursor = conn.cursor()
                    
            # Corrigindo a consulta SQL e inserindo os dados no banco
            my_cursor.execute('SELECT * FROM hospital')
            rows = my_cursor.fetchall()
            
            if len(rows)!=0:
                self.hospital_tabela.delete(*self.hospital_tabela.get_children())
                for i in rows:
                    self.hospital_tabela.insert('', END, values=i)
                conn.commit()
                    
            conn.close()
            
        except mysql.connector.Error as error:
            messagebox.showerror('Erro', f'Erro ao buscar dados: {error}')
    
    
    def autualizar_Dados(self, event=None):
        try:
            conn = mysql.connector.connect(host='localhost', user='root', password='coloque_sua_senha', database='Mydata')
            my_cursor = conn.cursor()
                
            # Corrigindo a consulta SQL para atualizar apenas o registro selecionado
            my_cursor.execute('UPDATE hospital SET Nomes_de_Medicamentos=%s, Referencia=%s, Dose=%s, Numero_de_Comprimidos=%s, Lote=%s, Data_de_Emissao=%s, Data_de_Validade=%s, Dose_Diaria=%s, Efeito_Colateral=%s, Infomacao_Adicionais=%s, Pressao_Arterail=%s, Orientacao_De_Armazenamento=%s, Medicamento=%s, Id_do_Paciente=%s, Numero_do_NHS=%s, Nome_do_Paciente=%s, Data_de_Nascimento=%s, Endereco_do_Paciente=%s WHERE Numero_do_NHS=%s',
                            (self.nome_medicamento.get(), self.referencia.get(), self.dose.get(), self.numero_de_comprimidos.get(),
                            self.lote.get(), self.data_de_emissao.get(), self.data_de_validade.get(), self.dose_diaria.get(),
                            self.efeito_colateral.get(), self.informacao_adicionais.get(), self.pressao_arterial.get(),
                            self.orientacao_de_armazenamento.get(), self.medicamento.get(), self.id_do_paciente.get(),
                            self.numero_do_NHS.get(), self.nome_do_paciente.get(), self.data_de_nascimento.get(),
                            self.endereco_do_paciente.get(), self.numero_do_NHS.get()))
            
            conn.commit()
            self.buscar_dados()
            conn.close()
            
            
            messagebox.showinfo('Sucesso', 'O registro foi atualizado com sucesso!')
        
        except mysql.connector.Error as error:
            messagebox.showerror('Erro', f'Erro ao atualizar registro: {error}')

    
    def acessar_cursor(self, event=''):
        cursor_row = self.hospital_tabela.focus()
        content=self.hospital_tabela.item(cursor_row)
        row = content['values']
        self.nome_medicamento.set(row[0])
        self.referencia.set(row[1])
        self.dose.set(row[2])
        self.numero_de_comprimidos.set(row[3])
        self.lote.set(row[4])
        self.data_de_emissao.set(row[5])
        self.data_de_validade.set(row[6])
        self.dose_diaria.set(row[7])
        self.efeito_colateral.set(row[8])
        self.informacao_adicionais.set(row[9])
        self.pressao_arterial.set(row[10])
        self.orientacao_de_armazenamento.set(row[11])
        self.medicamento.set(row[12])
        self.id_do_paciente.set(row[13])
        self.numero_do_NHS.set(row[14])
        self.nome_do_paciente.set(row[15])
        self.data_de_nascimento.set(row[16])
        self.endereco_do_paciente.set(row[17])

    def informacao_Prescricao(self):
        self.textoPrescricao.insert(END, 'Nomes de Medicamentos:\t\t\t'+self.nome_medicamento.get()+'\n')
        self.textoPrescricao.insert(END,'Referência:\t\t\t'+self.referencia.get()+'\n')
        self.textoPrescricao.insert(END,'Dose:\t\t\t'+self.dose.get()+'\n')
        self.textoPrescricao.insert(END,'Nº de Comprimidos:\t\t\t'+self.numero_de_comprimidos.get()+'\n')
        self.textoPrescricao.insert(END,'Lote:\t\t\t'+self.lote.get()+'\n')
        self.textoPrescricao.insert(END,'Data de Emissão:\t\t\t'+self.data_de_emissao.get()+'\n')
        self.textoPrescricao.insert(END,'Data de Validade:\t\t\t'+self.data_de_validade.get()+'\n')
        self.textoPrescricao.insert(END,'Dose Diária:\t\t\t'+self.dose_diaria.get()+'\n')
        self.textoPrescricao.insert(END,'Efeito Colateral:\t\t\t'+self.efeito_colateral.get()+'\n')
        self.textoPrescricao.insert(END,'Informações Adicionais:\t\t\t'+self.informacao_adicionais.get()+'\n')
        self.textoPrescricao.insert(END,'Pressão Arterial:\t\t\t'+self.pressao_arterial.get()+'\n')
        self.textoPrescricao.insert(END,'Orientação de Armazenamento:\t\t\t'+self.orientacao_de_armazenamento.get()+'\n')
        self.textoPrescricao.insert(END,'Medicamento:\t\t\t'+self.medicamento.get()+'\n')
        self.textoPrescricao.insert(END,'Id do Paciente:\t\t\t'+self.id_do_paciente.get()+'\n')
        self.textoPrescricao.insert(END,'Número do NHS:\t\t\t'+self.numero_do_NHS.get()+'\n')
        self.textoPrescricao.insert(END,'Nome do Paciente:\t\t\t'+self.nome_do_paciente.get()+'\n')
        self.textoPrescricao.insert(END,'Data de Nascimento:\t\t\t'+self.data_de_nascimento.get()+'\n')
        self.textoPrescricao.insert(END,'Endereço do Paciente:\t\t\t'+self.endereco_do_paciente.get()+'\n')
        

    def deletar_Dados(self):
        try:
            conn = mysql.connector.connect(host='localhost', user='root', password='coloque_sua_senha', database='Mydata')
            my_cursor = conn.cursor()
            
            query = 'DELETE FROM hospital WHERE Numero_do_NHS=%s'
            value = (self.numero_do_NHS.get(),)    
            my_cursor.execute(query, value)
            
            conn.commit()
            conn.close()
            self.limpar()
            self.buscar_dados()
            
            messagebox.showinfo('Sucesso', 'O registro foi excluíndo com sucesso!')
        
        except mysql.connector.Error as error:
            messagebox.showerror('Erro', f'Erro ao deletar registro: {error}')
    
    def limpar(self):
        self.nome_medicamento.set('')
        self.referencia.set('')
        self.dose.set('')
        self.numero_de_comprimidos.set('')
        self.lote.set('')
        self.data_de_emissao.set('')
        self.data_de_validade.set('')
        self.dose_diaria.set('')
        self.efeito_colateral.set('')
        self.informacao_adicionais.set('')
        self.pressao_arterial.set('')
        self.orientacao_de_armazenamento.set('')
        self.medicamento.set('')
        self.id_do_paciente.set('')
        self.numero_do_NHS.set('')
        self.nome_do_paciente.set('')
        self.data_de_nascimento.set('')
        self.endereco_do_paciente.set('')
        self.textoPrescricao.delete('1.0', END)
        
    
    def sair(self):
        sair=messagebox.askyesno('Sistema de Gestão Hospitalar', 'Confirme que deseja sair?')
        if sair>0:
            janela.destroy()
            return
        
# Inicializa a janela principal
janela = Tk()
# Cria uma instância da classe Hospital
obj = Hospital(janela)
# Inicia o loop principal do Tkinter
janela.mainloop()
