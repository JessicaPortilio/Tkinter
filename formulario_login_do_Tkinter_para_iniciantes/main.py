from tkinter import * # Importa todas as funções e classes do módulo tkinter
from tkinter import messagebox # Importa a função messagebox do módulo tkinter

# Função para centralizar o frame na janela principal
def centralizar_frame(event=None):
    janela.update_idletasks() # Atualiza todas as tarefas pendentes da interface gráfica
    largura_janela = janela.winfo_width() # Obtém a largura da janela
    altura_janela = janela.winfo_height() # Obtém a altura da janela
    largura_frame = frame.winfo_reqwidth() # Obtém a largura requerida do frame
    altura_frame = frame.winfo_reqheight() # Obtém a altura requerida do frame
    pos_x = (largura_janela - largura_frame) // 2 # Calcula a posição x para centralizar o frame
    pos_y = (altura_janela - altura_frame) // 2 # Calcula a posição y para centralizar o frame
    frame.place(x=pos_x, y=pos_y) # Coloca o frame na posição calculada

# Função para abrir uma nova janela após o login bem-sucedido
def abrir_nova_janela(nome):
    nova_janela = Toplevel(janela) # Cria uma nova janela filha
    nova_janela.title("Bem-vindo(a)") # Define o título da nova janela
    nova_janela.geometry("720x500") # Define o tamanho da nova janela
    nova_janela.config(bg='#010e1c') # Define a cor de fundo da nova janela
    
    mensagem = Label(nova_janela, text=f"Bem-vindo(a), {nome.capitalize()}!", bg='#010e1c', fg='#0076f5', font=('Arial', 30))
    mensagem.pack(pady=20) # Adiciona uma mensagem de boas-vindas à nova janela
    
    descricao = Label(nova_janela, text="Você está na área do usuário.", bg='#010e1c', fg='#FFFFFF', font=('Arial', 16))
    descricao.pack(pady=10) # Adiciona uma descrição à nova janela
    
    frame_botoes = Frame(nova_janela, bg='#010e1c') # Cria um frame para os botões
    frame_botoes.pack(pady=10) # Adiciona o frame à nova janela
    
    botao_opcao1 = Button(frame_botoes, text="Opção 1", bg='#0076f5', fg='#FFFFFF', font=('Arial', 16))
    botao_opcao1.grid(row=0, column=0, padx=10) # Adiciona o botão Opção 1 ao frame de botões
    
    botao_opcao2 = Button(frame_botoes, text="Opção 2", bg='#0076f5', fg='#FFFFFF', font=('Arial', 16))
    botao_opcao2.grid(row=0, column=1, padx=10) # Adiciona o botão Opção 2 ao frame de botões
    
    botao_sair = Button(nova_janela, text="Sair", bg='#FF0000', fg='#FFFFFF', font=('Arial', 16), command=nova_janela.destroy)
    botao_sair.pack(pady=10) # Adiciona o botão Sair à nova janela, que fecha a janela ao ser clicado

# Função para processar o login
def login():
    nome = campo_de_entrada_Usuario.get() # Obtém o nome de usuário do campo de entrada
    senha = campo_de_entrada_Senha.get() # Obtém a senha do campo de entrada
    
    if nome == 'jessica' and senha == '1234': # Verifica se o nome de usuário e a senha estão corretos
        messagebox.showinfo('Sucesso de login', f'Bem-Vindo(a) ao sistema, {nome.capitalize()}') # Mostra uma mensagem de sucesso
        campo_de_entrada_Usuario.delete(0, END) # Limpa o campo de entrada de usuário
        campo_de_entrada_Senha.delete(0, END) # Limpa o campo de entrada de senha
        abrir_nova_janela(nome) # Abre a nova janela
    else:
        messagebox.showerror('Error', 'Usuário ou Senha Inválida!') # Mostra uma mensagem de erro
        campo_de_entrada_Usuario.delete(0, END) # Limpa o campo de entrada de usuário
        campo_de_entrada_Senha.delete(0, END) # Limpa o campo de entrada de senha

janela = Tk() # Cria a janela principal
janela.title('Formulário Login') # Define o título da janela principal
janela.geometry('720x500') # Define o tamanho da janela principal
janela.config(bg='#010e1c') # Define a cor de fundo da janela principal

frame = Frame(janela, bg='#010e1c') # Cria um frame dentro da janela principal

texto_Login = Label(frame, text='Login', bg='#010e1c', fg='#0076f5', font=('Arial', 30)) # Cria um label para o título Login
texto_Usuario = Label(frame, text='Usuário', bg='#010e1c', fg='#FFFFFF', font=('Arial', 16)) # Cria um label para o campo de usuário
campo_de_entrada_Usuario = Entry(frame, font=('Arial', 16), bd=3) # Cria um campo de entrada para o usuário
texto_Senha = Label(frame, text='Senha', bg='#010e1c', fg='#FFFFFF', font=('Arial', 16)) # Cria um label para o campo de senha
campo_de_entrada_Senha = Entry(frame, show='*', font=('Arial', 16), bd=3) # Cria um campo de entrada para a senha
botao_de_login = Button(frame, text='Login', bg='#0076f5', fg='#FFFFFF', font=('Arial', 16), command=login) # Cria um botão de login

# Adiciona os widgets ao frame usando o método grid
texto_Login.grid(row=0, column=0, columnspan=2, pady=40) # Adiciona o título Login ao frame
texto_Usuario.grid(row=1, column=0, sticky='E') # Adiciona o label Usuário ao frame
campo_de_entrada_Usuario.grid(row=1, column=1, pady=20, padx=10) # Adiciona o campo de entrada de usuário ao frame
texto_Senha.grid(row=2, column=0, sticky='E') # Adiciona o label Senha ao frame
campo_de_entrada_Senha.grid(row=2, column=1, pady=20, padx=10) # Adiciona o campo de entrada de senha ao frame
botao_de_login.grid(row=3, column=0, columnspan=2, pady=30) # Adiciona o botão de login ao frame

# Centraliza o frame inicialmente
centralizar_frame()

# Vincula a função centralizar_frame ao evento de redimensionamento da janela
janela.bind('<Configure>', centralizar_frame)

# Inicia o loop principal da interface gráfica
janela.mainloop()
