from tkinter import *
from tkinter import filedialog
import PyPDF2

def abrirarquivo():
    nomearquivo = filedialog.askopenfilename(title='Abrir Arquivo PDF',
                                            initialdir='D:\\Tkinter',
                                            filetypes=[('Arquivos PDF', '*.pdf')])
    
    leitura = PyPDF2.PdfReader(nomearquivo)
    
    texto_completo = ""
    for i in range(len(leitura.pages)):
        pagina = leitura.pages[i]
        texto_atual = pagina.extract_text()
        texto_completo += texto_atual + "\n"
    
    nome_de_arquivo_label.config(text=nomearquivo)
    arquivo_de_saida_texto.delete(1.0, END)
    arquivo_de_saida_texto.insert(END, texto_completo)

janela = Tk()
janela.title('Extrair texto do PDF')

nome_de_arquivo_label = Label(janela, text='Nenhum arquivo selecionado')
nome_de_arquivo_label.pack()
arquivo_de_saida_texto = Text(janela)
arquivo_de_saida_texto.pack()
abrir_arquivo_botao = Button(janela, text='Abrir arquivo PDF', command=abrirarquivo)
abrir_arquivo_botao.pack()

janela.mainloop()
