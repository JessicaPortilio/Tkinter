import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import date
from PIL import Image, ImageTk
from tkinter import filedialog
import mysql.connector
from datetime import datetime

class Camiseta:
    def __init__(self, root):
        self.root = root
        self.root.title('T-Shirt Management System')
        self.root.geometry('1540x800+0+0')
        self.root.config(bg='#F0F0F0')

        # Título
        titulo_label = tk.Label(self.root, bd=2, relief=tk.RIDGE, text='T-Shirt Management System', font=('Helvetica', 35, 'bold'), bg='#4A90E2', fg='white')
        titulo_label.pack(side=tk.TOP, fill=tk.X)
        
        dados_frame = tk.Frame(self.root, bd=3, relief=tk.RIDGE, bg='#F0F0F0')
        dados_frame.place(x=0, y=65, width=1535, height=720)
        
        dados_frame_esquerda = tk.LabelFrame(dados_frame, bd=2, relief=tk.RIDGE, padx=10, font=('Helvetica', 15, 'bold'), text='Cadastro de Produtos', bg='#EAEAEA')
        dados_frame_esquerda.place(x=10, y=10, width=1110, height=700)

        imagem_frame = tk.LabelFrame(dados_frame, bd=2, relief=tk.RIDGE, padx=10, font=('Helvetica', 15, 'bold'), text='Imagem da Camiseta', bg='#EAEAEA')
        imagem_frame.place(x=1130, y=10, width=390, height=700)
        
        # Nome da Camiseta
        nome_da_camiseta_label = tk.Label(dados_frame_esquerda, text='Nome da Camiseta:', font=('Helvetica', 12), bg='#EAEAEA')
        nome_da_camiseta_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        
        self.nome_da_camiseta_entry = tk.Entry(dados_frame_esquerda, font=('Helvetica', 12), width=35)
        self.nome_da_camiseta_entry.grid(row=0, column=1, padx=10, pady=10)
        
        # Categoria
        categoria_label = tk.Label(dados_frame_esquerda, text='Categoria:', font=('Helvetica', 12), bg='#EAEAEA')
        categoria_label.grid(row=0, column=2, padx=10, pady=10, sticky='w')

        self.categoria_combobox = ttk.Combobox(dados_frame_esquerda, values=[
            'Básica', 'Estampada', 'Polo', 'Regata', 'Manga Longa', 
            'Esportiva', 'Fashion', 'Temática', 'Personalizada', 'Ecológica'
            ], font=('Helvetica', 12))
        self.categoria_combobox.grid(row=0, column=3, padx=10, pady=10)
        
        # Tamanho e Quantidade
        tamanho_label = tk.Label(dados_frame_esquerda, text='Tamanho:', font=('Helvetica', 12), bg='#EAEAEA')
        tamanho_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        tamanhos = ['PP', 'P', 'M', 'G', 'GG']
        self.checkbuttons = []
        self.spinboxes = []
        for idx, tamanho in enumerate(tamanhos):
            check_var = tk.StringVar(value='Não registrado')
            check = tk.Checkbutton(dados_frame_esquerda, text=tamanho, variable=check_var, onvalue=tamanho, offvalue='Não registrado', font=('Helvetica', 12), bg='#EAEAEA')
            check.grid(row=1, column=1 + idx, padx=10, pady=10)
            self.checkbuttons.append((tamanho, check, check_var))
            
            spinbox = tk.Spinbox(dados_frame_esquerda, from_=0, to=100, font=('Helvetica', 12), width=4)
            spinbox.grid(row=2, column=1 + idx, padx=10, pady=10)
            self.spinboxes.append((tamanho, spinbox))
        
        # Valor Unitário
        valor_unitario_label = tk.Label(dados_frame_esquerda, text='Valor Unitário:', font=('Helvetica', 12), bg='#EAEAEA')
        valor_unitario_label.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        
        self.valor_unitario_entry = tk.Entry(dados_frame_esquerda, font=('Helvetica', 12), width=35)
        self.valor_unitario_entry.grid(row=3, column=1, padx=10, pady=10)
        
        # Data de Cadastro
        data_cadastro_label = tk.Label(dados_frame_esquerda, text='Data de Cadastro:', font=('Helvetica', 12), bg='#EAEAEA')
        data_cadastro_label.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        
        self.data_cadastro_entry = tk.Entry(dados_frame_esquerda, font=('Helvetica', 12), width=12)
        self.data_cadastro_entry.grid(row=4, column=1, padx=10, pady=10)
        
        # Data de Entrega
        data_entrega_label = tk.Label(dados_frame_esquerda, text='Data de Entrega:', font=('Helvetica', 12), bg='#EAEAEA')
        data_entrega_label.grid(row=5, column=0, padx=10, pady=10, sticky='w')
        
        self.data_entrega_entry = tk.Entry(dados_frame_esquerda, font=('Helvetica', 12), width=12)
        self.data_entrega_entry.grid(row=5, column=1, padx=10, pady=10)


        # Status de Entrega
        status_label = tk.Label(dados_frame_esquerda, text='Status de Entrega:', font=('Helvetica', 12), bg='#EAEAEA')
        status_label.grid(row=6, column=0, padx=10, pady=10, sticky='w')

        self.status_combobox = ttk.Combobox(dados_frame_esquerda, values=['Pendente', 'Em Produção', 'Pronto para Envio', 'Enviado', 'Entregue'], font=('Helvetica', 12))
        self.status_combobox.grid(row=6, column=1, padx=10, pady=10)

        # Indicação de Atraso
        atraso_label = tk.Label(dados_frame_esquerda, text='Indicação de Atraso:', font=('Helvetica', 12), bg='#EAEAEA')
        atraso_label.grid(row=6, column=2, padx=10, pady=10, sticky='w')

        self.atraso_var = tk.StringVar(value='Não')
        atraso_combobox = ttk.Combobox(dados_frame_esquerda, textvariable=self.atraso_var, values=['Sim', 'Não'], font=('Helvetica', 12))
        atraso_combobox.grid(row=6, column=3, padx=10, pady=10)

        # Observações
        obs_label = tk.Label(dados_frame_esquerda, text='Observações:', font=('Helvetica', 12), bg='#EAEAEA')
        obs_label.grid(row=7, column=0, padx=10, pady=10, sticky='nw')

        self.obs_text = tk.Text(dados_frame_esquerda, font=('Helvetica', 12), width=80, height=4)
        self.obs_text.grid(row=7, column=1, columnspan=3, padx=10, pady=10)

	# Imagem da Camiseta
        imagem_label = tk.Label(imagem_frame, text='Imagem da Camiseta:', font=('Helvetica', 12), bg='#EAEAEA')
        imagem_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        self.imagem_path = tk.StringVar()
        imagem_entry = tk.Entry(imagem_frame, textvariable=self.imagem_path, font=('Helvetica', 12), width=20, state='readonly')
        imagem_entry.grid(row=0, column=1, padx=5, pady=10)

        imagem_btn = tk.Button(imagem_frame, text='Selecionar Imagem', command=self.selecionar_imagem, font=('Helvetica', 12), bg='#4A90E2', fg='white')
        imagem_btn.grid(row=1, column=0, padx=15, pady=10)

        self.imagem_label = tk.Label(imagem_frame, bg='#EAEAEA')
        self.imagem_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        # Botões na parte inferior
        visualizar_btn = tk.Button(dados_frame, text='Visualizar', command=self.visualizar_dados, font=('Helvetica', 12), bg='#4A90E2', fg='white')
        visualizar_btn.place(x=10, y=680, width=150, height=30)

        salvar_btn = tk.Button(dados_frame, text='Salvar', command=self.salvar_dados, font=('Helvetica', 12), bg='#4A90E2', fg='white')
        salvar_btn.place(x=170, y=680, width=150, height=30)

        limpar_btn = tk.Button(dados_frame, text='Limpar', command=self.limpar_campos, font=('Helvetica', 12), bg='#4A90E2', fg='white')
        limpar_btn.place(x=330, y=680, width=150, height=30)

        sair_btn = tk.Button(dados_frame, text='Sair', command=root.quit, font=('Helvetica', 12), bg='#4A90E2', fg='white')
        sair_btn.place(x=490, y=680, width=150, height=30)


    def selecionar_imagem(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.imagem_path.set(file_path)
            image = Image.open(file_path)
            image = image.resize((350, 350), Image.Resampling.LANCZOS)  # Alterado para Image.Resampling.LANCZOS
            photo = ImageTk.PhotoImage(image)
            self.imagem_label.config(image=photo)
            self.imagem_label.image = photo

    def visualizar_dados(self):
        top = tk.Toplevel(self.root)
        top.title('Visualizar Dados')
        top.geometry('1540x750+0+0')

        # Criar Treeview
        tree = ttk.Treeview(top)
        tree.pack(expand=True, fill=tk.BOTH)

        # Definir colunas
        tree["columns"] = ("Id", "Nome da Camiseta", "Categoria", "Tamanho PP", "Tamanho P", "Tamanho M",
                        "Tamanho G", "Tamanho GG", "Valor Unitário", "Valor Total", "Data de Cadastro",
                        "Data de Entrega", "Status de Entrega", "Atraso", "Observações")

        # Definir cabeçalhos das colunas
        tree.heading("Id", text="Id")
        tree.heading("Nome da Camiseta", text="Nome da Camiseta")
        tree.heading("Categoria", text="Categoria")
        tree.heading("Tamanho PP", text="Tamanho PP")
        tree.heading("Tamanho P", text="Tamanho P")
        tree.heading("Tamanho M", text="Tamanho M")
        tree.heading("Tamanho G", text="Tamanho G")
        tree.heading("Tamanho GG", text="Tamanho GG")
        tree.heading("Valor Unitário", text="Valor Unitário")
        tree.heading("Valor Total", text="Valor Total")
        tree.heading("Data de Cadastro", text="Data de Cadastro")
        tree.heading("Data de Entrega", text="Data de Entrega")
        tree.heading("Status de Entrega", text="Status de Entrega")
        tree.heading("Atraso", text="Atraso")
        tree.heading("Observações", text="Observações")

        # Remover a primeira coluna em branco (padrão do Treeview)
        tree["show"] = "headings"

        try:
            conn = mysql.connector.connect(host='localhost', user='root', password='1234', database='camisetas_db')
            my_cursor = conn.cursor()

            # Executar consulta para obter os dados das camisetas
            my_cursor.execute("SELECT * FROM camisetas")
            rows = my_cursor.fetchall()

            for row in rows:
                tree.insert("", tk.END, values=row)

            conn.close()

        except mysql.connector.Error as error:
            messagebox.showerror('Erro', f'Erro ao obter dados do banco de dados: {error}')

        # Adicionar scrollbar
        scroll_x = ttk.Scrollbar(top, orient=tk.HORIZONTAL, command=tree.xview)
        scroll_y = ttk.Scrollbar(top, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)




    def salvar_dados(self):
        if self.nome_da_camiseta_entry.get() == '' or self.categoria_combobox.get() == '':
            messagebox.showerror('Erro', 'Todos os campos são necessários.')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', user='root', password='1234', database='camisetas_db')
                my_cursor = conn.cursor()

                # Obter os valores dos campos do formulário
                nome_camiseta = self.nome_da_camiseta_entry.get()
                categoria = self.categoria_combobox.get()
                tamanho_pp = self.spinboxes[0][1].get()
                tamanho_p = self.spinboxes[1][1].get()
                tamanho_m = self.spinboxes[2][1].get()
                tamanho_g = self.spinboxes[3][1].get()
                tamanho_gg = self.spinboxes[4][1].get()
                
                # Tratar o valor unitário
                valor_unitario_str = self.valor_unitario_entry.get().replace(',', '.')  # Substituir vírgula por ponto para garantir formato numérico
                valor_unitario = float(valor_unitario_str) if valor_unitario_str else 0.0
                
                # Calcular o valor total
                quantidade_pp = int(tamanho_pp)
                quantidade_p = int(tamanho_p)
                quantidade_m = int(tamanho_m)
                quantidade_g = int(tamanho_g)
                quantidade_gg = int(tamanho_gg)
                
                valor_total = (quantidade_pp + quantidade_p + quantidade_m + quantidade_g + quantidade_gg) * valor_unitario

                # Converter datas para o formato adequado (YYYY-MM-DD)
                data_cadastro = self.convert_data(self.data_cadastro_entry.get())
                data_entrega = self.convert_data(self.data_entrega_entry.get())

                status_entrega = self.status_combobox.get()
                atraso = self.atraso_var.get()
                observacoes = self.obs_text.get('1.0', tk.END)

                # Inserir os dados na tabela camisetas
                sql = """
                INSERT INTO camisetas (nome, categoria, tamanho_pp, tamanho_p, tamanho_m, tamanho_g, tamanho_gg,
                                    valor_unitario, valor_total, data_cadastro, data_entrega, status_entrega,
                                    atraso, observacoes)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                values = (nome_camiseta, categoria, tamanho_pp, tamanho_p, tamanho_m, tamanho_g, tamanho_gg,
                        valor_unitario, valor_total, data_cadastro, data_entrega, status_entrega, atraso, observacoes)
                
                my_cursor.execute(sql, values)

                conn.commit()
                conn.close()
                self.limpar_campos()  # Limpa os campos após salvar os dados

                messagebox.showinfo('Sucesso', 'O registro foi inserido com sucesso!')
            except mysql.connector.Error as error:
                messagebox.showerror('Erro', f'Erro ao inserir registro: {error}')

    def convert_data(self, data):
        try:
            return datetime.strptime(data, '%d/%m/%Y').strftime('%Y-%m-%d')
        except ValueError:
            messagebox.showerror('Erro', f'Formato de data inválido: {data}. Use o formato DD/MM/AAAA.')
            return None


    def limpar_campos(self):
        # Limpar todos os campos do formulário
        self.nome_da_camiseta_entry.delete(0, tk.END)
        self.categoria_combobox.set('')
        for _, check, var in self.checkbuttons:
            var.set('Não registrado')
            check.deselect()
        for _, spinbox in self.spinboxes:
            spinbox.delete(0, tk.END)
        self.valor_unitario_entry.delete(0, tk.END)
        self.data_cadastro_entry.delete(0, tk.END)
        self.data_entrega_entry.delete(0, tk.END)
        self.status_combobox.set('')
        self.atraso_var.set('Não')
        self.obs_text.delete('1.0', tk.END)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = Camiseta(root)
    app.run()
