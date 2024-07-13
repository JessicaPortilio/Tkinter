from tkinter import *
import pyshorteners

# Função para encurtar a URL
def encurtarURL():
    encurtar = pyshorteners.Shortener()
    encurtar_url = encurtar.tinyurl.short(campo_de_entrada_link.get())
    campo_resultado.delete(0, END)  # Limpa o campo de resultado antes de inserir o novo link
    campo_resultado.insert(0, encurtar_url)  # Insere o link encurtado no campo de resultado

# Configuração da janela principal
janela = Tk()
janela.title('Encurtador de Link')
janela.geometry('500x300')
janela.config(bg='#2e3f4f')  # Cor de fundo da janela

# Texto de instrução
texto_link = Label(janela, text='Cole um link aqui', bg='#2e3f4f', fg='#ffffff', font=('Arial', 16, 'bold'))
texto_link.pack(pady=10)  # Adiciona espaço vertical ao redor do texto

# Campo de entrada do link
campo_de_entrada_link = Entry(janela, font=('Arial', 14), bd=2, relief=SOLID, width=40)
campo_de_entrada_link.pack(pady=5)

# Texto de resultado
resultado = Label(janela, text='Saída do Link Encurtado', bg='#2e3f4f', fg='#ffffff', font=('Arial', 16, 'bold'))
resultado.pack(pady=10)

# Campo de resultado do link encurtado
campo_resultado = Entry(janela, font=('Arial', 14), bd=2, relief=SOLID, width=40)
campo_resultado.pack(pady=5)

# Botão para encurtar o link
botao_gerar_lik_curto = Button(janela, text='Encurtar Link', command=encurtarURL, bg='#007acc', fg='#ffffff', font=('Arial', 14, 'bold'), bd=0, relief=SOLID, width=20)
botao_gerar_lik_curto.pack(pady=20)

# Inicia o loop principal da interface gráfica
janela.mainloop()
