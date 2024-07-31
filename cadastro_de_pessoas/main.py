import database
# Importa o módulo 'database' que contém as funções de banco de dados definidas anteriormente

# Função para exibir o menu de opções
def menu():
    print(f'________MENU_______')
    # Exibe o título do menu
    print(f'1. INSERIR PESSOA')
    # Exibe a opção 1: Inserir pessoa
    print(f'2. ATUALIZAR PESSOA')
    # Exibe a opção 2: Atualizar pessoa
    print(f'3. DELETAR PESSOA')
    # Exibe a opção 3: Deletar pessoa
    print(f'4. PESQUISAR PESSOA')
    # Exibe a opção 4: Pesquisar pessoa
    print(f'5. LISTAR PESSOA')
    # Exibe a opção 5: Listar pessoas
    print(f'6. SAIR')
    # Exibe a opção 6: Sair

# Função para inserir uma nova pessoa
def inserir_pessoa():
    nome = input('Nome: ')
    # Solicita o nome da pessoa
    idade = int(input('Idade: '))
    # Solicita a idade da pessoa e converte para inteiro
    email = input('Email: ')
    # Solicita o email da pessoa
    database.inserir_pessoa(nome, idade, email)
    # Chama a função para inserir a pessoa no banco de dados
    print('Pessoa inserida com sucesso!')
    # Informa que a pessoa foi inserida com sucesso
    lista_as_pessoas()
    # Exibe a lista atualizada de pessoas

# Função para listar todas as pessoas
def lista_as_pessoas():
    pessoas = database.lista_as_pessoas()
    # Chama a função para obter a lista de pessoas do banco de dados
    print('Lista de Pessoas: ')
    # Exibe o título da lista
    for pessoa in pessoas:
        # Itera sobre cada pessoa na lista
        print(pessoa)
        # Exibe os dados de cada pessoa

# Função para atualizar os dados de uma pessoa
def atualizar_pessoa():
    id_pessoa = int(input('ID da Pessoa: '))
    # Solicita o ID da pessoa e converte para inteiro
    nome = input('Nome: ')
    # Solicita o novo nome da pessoa
    idade = int(input('Idade: '))
    # Solicita a nova idade da pessoa e converte para inteiro
    email = input('Email: ')
    # Solicita o novo email da pessoa
    database.atualizar_pessoa(id_pessoa, nome, idade, email)
    # Chama a função para atualizar a pessoa no banco de dados
    print('Pessoa atualizada com sucesso!')
    # Informa que a pessoa foi atualizada com sucesso
    lista_as_pessoas()
    # Exibe a lista atualizada de pessoas

# Função para deletar uma pessoa
def deletar_pessoa():
    id_pessoa = int(input('ID da Pessoa: '))
    # Solicita o ID da pessoa a ser deletada e converte para inteiro
    database.deletar_pessoa(id_pessoa)
    # Chama a função para deletar a pessoa no banco de dados
    print('Pessoa deletada com sucesso!')
    # Informa que a pessoa foi deletada com sucesso
    lista_as_pessoas()
    # Exibe a lista atualizada de pessoas

# Função para pesquisar uma pessoa pelo nome
def pesquisar_pessoa():
    nome = input('Nome: ')
    # Solicita o nome da pessoa a ser pesquisada
    resultado = database.pesquisar_pessoa(nome)
    # Chama a função para pesquisar a pessoa no banco de dados
    for linha in resultado:
        # Itera sobre cada linha no resultado da pesquisa
        print(f'{linha[0]}, {linha[1]}, {linha[2]}, {linha[3]}')
        # Exibe os dados de cada pessoa encontrada

# Função principal que controla o menu e a navegação entre opções
def main():
    database.conectar()
    # Chama a função para conectar ao banco de dados e criar a tabela se necessário
    while True:
        # Inicia um loop infinito para exibir o menu e processar as opções
        menu()
        # Exibe o menu de opções
        opcao = int(input('Escolha uma opção: '))
        # Solicita que o usuário escolha uma opção e converte para inteiro
        if opcao == 1:
            inserir_pessoa()
            # Se a opção for 1, chama a função para inserir pessoa
        elif opcao == 2:
            atualizar_pessoa()
            # Se a opção for 2, chama a função para atualizar pessoa
        elif opcao == 3:
            deletar_pessoa()
            # Se a opção for 3, chama a função para deletar pessoa
        elif opcao == 4:
            pesquisar_pessoa()
            # Se a opção for 4, chama a função para pesquisar pessoa
        elif opcao == 5:
            lista_as_pessoas()
            # Se a opção for 5, chama a função para listar pessoas
        elif opcao == 6:
            break
            # Se a opção for 6, sai do loop e encerra o programa
        else:
            print('Opção inválida')
            # Se a opção for inválida, informa o usuário

# Verifica se o arquivo está sendo executado diretamente
if __name__ == '__main__':
    main()
    # Chama a função principal para iniciar o programa
