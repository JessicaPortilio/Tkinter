from tkinter import *
from tkinter import ttk
from datetime import datetime

class Camiseta():
    def __init__(self, root):
        self.root = root
        self.root.title('T-Shirt Management System')
        self.root.geometry('1540x800+0+0')
        self.root.config(bg='#F0F0F0')
        
        def format_date_cadastro(event):
            text = self.data_de_cadastro_entry.get().replace("/", "")
            new_text = ""

            for i in range(len(text)):
                if i == 2 or i == 4:
                    new_text += "/"
                new_text += text[i]

            self.data_de_cadastro_entry.delete(0, END)
            self.data_de_cadastro_entry.insert(0, new_text)
            
        def format_date_entrega(event):
            text = self.data_de_entrega_entry.get().replace("/", "")
            new_text = ""

            for i in range(len(text)):
                if i == 2 or i == 4:
                    new_text += "/"
                new_text += text[i]

            self.data_de_entrega_entry.delete(0, END)
            self.data_de_entrega_entry.insert(0, new_text)
        
        def format_currency(event):
            # Remover caracteres não numéricos, exceto vírgula
            text = self.valor_unitario_entry.get().replace("R$", "").replace(".", "").replace(",", "").strip()
            
            # Garantir que o texto é numérico
            if text.isdigit():
                # Preencher com zeros à esquerda, se necessário
                text = text.zfill(3)
                
                # Separar a parte inteira e a parte decimal
                integer_part = text[:-2]
                decimal_part = text[-2:]
                
                # Formatar a parte inteira com pontos
                integer_part = f"{int(integer_part):,}".replace(",", ".")
                
                # Concatenar a parte inteira e a parte decimal com vírgula
                formatted_text = f"{integer_part},{decimal_part}"
                
                self.valor_unitario_entry.delete(0, END)
                self.valor_unitario_entry.insert(0, f"R$ {formatted_text}")
        
        # Dados do Produto
        dados_do_produto_frame = Frame(self.root, bd=3, relief=RIDGE, bg='#F0F0F0')
        dados_do_produto_frame.place(x=0, y=65, width=1535, height=720)
        
        # Label Frame
        dados_frame_esquerda = LabelFrame(dados_do_produto_frame, bd=2, relief=RIDGE, padx=10, font=('Helvetica', 15, 'bold'), text='Cadastro de Produtos', bg='#EAEAEA')
        dados_frame_esquerda.place(x=10, y=10, width=1500, height=300)
        
        # Nome da Camiseta
        nome_da_camiseta_label = Label(dados_frame_esquerda, text='Nome da Camiseta:')
        nome_da_camiseta_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        
        # Campo de Entrada - Nome da Camiseta
        self.nome_da_camiseta_entry = Entry(dados_frame_esquerda, width=30)
        self.nome_da_camiseta_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Categoria
        categoria_label = Label(dados_frame_esquerda, text='Categoria:')
        categoria_label.grid(row=0, column=2, padx=5, pady=5, sticky='w')

        # Combobox - Categoria
        self.categoria_combobox = ttk.Combobox(dados_frame_esquerda, values=[
            'Básica', 'Estampada', 'Polo', 'Regata', 'Manga Longa', 
            'Esportiva', 'Fashion', 'Temática', 'Personalizada', 'Ecológica'
            ], font=('Helvetica', 12))
        self.categoria_combobox.grid(row=0, column=3, padx=5, pady=5)
        
        # Tamanho e Quantidade
        tamanho_label = Label(dados_frame_esquerda, text='Tamanho:')
        tamanho_label.grid(row=0, column=4, padx=5, pady=5, sticky='w')
        
        quantidade_label = Label(dados_frame_esquerda, text='Quantidade:')
        quantidade_label.grid(row=1, column=4, padx=5, pady=5, sticky='w')
        
        tamanhos = ['PP', 'P', 'M', 'G', 'GG']
        self.checkbuttons = []
        self.spinboxes = []
        for idx, tamanho in enumerate(tamanhos):
            check_var = StringVar(value='Não registrado')
            check = Checkbutton(dados_frame_esquerda, text=tamanho, variable=check_var, onvalue=tamanho, offvalue='Não registrado')
            check.grid(row=0, column=5 + idx, padx=5, pady=5)
            self.checkbuttons.append((tamanho, check, check_var))
            
            spinbox = Spinbox(dados_frame_esquerda, from_=0, to=100, width=4)
            spinbox.grid(row=1, column=5 + idx, padx=5, pady=5)
            self.spinboxes.append((tamanho, spinbox))
            
        
        # Data de Cadastro
        data_de_cadastro_label = Label(dados_frame_esquerda, text='Data de Cadastro:')
        data_de_cadastro_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        
        # Data atual no formato DD/MM/YYYY
        current_date = datetime.now().strftime("%d/%m/%Y")
        
        # Campo de Entrada - Data de Cadastro
        self.data_de_cadastro_entry = Entry(dados_frame_esquerda, width=30)
        self.data_de_cadastro_entry.insert(0, current_date)
        self.data_de_cadastro_entry.grid(row=1, column=1, padx=5, pady=5)
        self.data_de_cadastro_entry.bind("<KeyRelease>", format_date_cadastro)
        
        # Data de Entrega
        data_de_entrega_label = Label(dados_frame_esquerda, text='Data de Entrega:')
        data_de_entrega_label.grid(row=1, column=2, padx=5, pady=5, sticky='w')
        
        # Data atual no formato DD/MM/YYYY
        current_date = datetime.now().strftime("%d/%m/%Y")
        
        # Campo de Entrada - Data de Entrega
        self.data_de_entrega_entry = Entry(dados_frame_esquerda, width=30)
        self.data_de_entrega_entry.insert(0, current_date)
        self.data_de_entrega_entry.grid(row=1, column=3, padx=5, pady=5)
        self.data_de_entrega_entry.bind("<KeyRelease>", format_date_entrega)
        
        # Valor Unitário
        valor_unitario_label = Label(dados_frame_esquerda, text='Valor Unitário:')
        valor_unitario_label.grid(row=2, column=0, padx=5, pady=5, sticky='w')
        
        # Campo de Entrada - Valor Unitário
        self.valor_unitario_entry = Entry(dados_frame_esquerda, width=30)
        self.valor_unitario_entry.insert(0, "R$ 0,00")
        self.valor_unitario_entry.grid(row=2, column=1, padx=5, pady=5)
        self.valor_unitario_entry.bind("<KeyRelease>", format_currency)
        
        salvar_btn = Button(dados_do_produto_frame, text='Salvar', command=self.salvar_dados, font=('Helvetica', 12), bg='#4A90E2', fg='white')
        salvar_btn.place(x=170, y=680, width=150, height=30)
        
    def salvar_dados(self):
        # Obter os valores dos campos do formulário
        nome_camiseta = self.nome_da_camiseta_entry.get()
        categoria = self.categoria_combobox.get()
        valor_unitario = self.valor_unitario_entry.get()
        pp_status = self.checkbuttons[0][2].get()
        
        # Acessar os valores dos Spinbox
        tamanho_pp = self.spinboxes[0][1].get()
        tamanho_p = self.spinboxes[1][1].get()
        tamanho_m = self.spinboxes[2][1].get()
        tamanho_g = self.spinboxes[3][1].get()
        tamanho_gg = self.spinboxes[4][1].get()

        # Exibir os valores
        print(f"PP: Quantidade: {tamanho_pp}")
        print(f"P: Quantidade: {tamanho_p}")
        print(f"M: Quantidade: {tamanho_m}")
        print(f"G: Quantidade: {tamanho_g}")
        print(f"GG: Quantidade: {tamanho_gg}")
        data_cadastro = self.data_de_cadastro_entry.get()
        data_entrega = self.data_de_entrega_entry.get()
        print(nome_camiseta, categoria, data_cadastro, data_entrega, valor_unitario)
        
if __name__ == "__main__":
    root = Tk()
    obj = Camiseta(root)
    root.mainloop()