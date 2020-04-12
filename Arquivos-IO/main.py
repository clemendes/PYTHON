from contato import Contato
from arquivo_services import *
import os

os.system("cls")

opcao_menu = 1
#lista_contatos = list()

while(opcao_menu != 0):
    os.system("cls")
    print("-" * 30)
    print(("-" *2) + " Agenda de contatos - TXT " + ("-" *2))
    print("-" * 30)
    print("1. Listar contatos")
    print("2. Cadastrar contato")
    print("3. Remover contato")
    print("4. Buscar contato")
    print("0. Sair")
    opcao_menu = int(input("Digite a opção desejada: "))

    if opcao_menu == 1: # LISTAR CONTATOS
        print("-" * 30)
        contatos = listar_contatos()
        for contato in contatos:
            print(f"Nome: {contato.nome}")
            print(f"Email: {contato.email}")
            print(f"Telefone: {contato.telefone}")
        input("Pressione [ENTER] para continuar...")

    elif opcao_menu == 2: # CADASTRAR CONTATO
        print("-" * 30)
        nome_contato = input("Digite o nome do contato: ")
        email_contato = input("Digite o email do contato: ")
        telefone_contato = input("Digite o telefone do contato: ")
        contato_novo = Contato(nome_contato, email_contato, telefone_contato)
        if cadastrar_contato(contato_novo):
            print("Contato cadastrado!")
        else:
            print("Erro: Contato já existe!")    
        input("Pressione [ENTER] para continuar...")

    elif opcao_menu == 3: # REMOVER CONTATO
        print("-" * 30)
        contato_remover = input("Digite o email do contato que deseja remover: ")
        if remover_contato(contato_remover):
            print("Contato removido!")
        else:
            print("Contato não encontrado")
        input("Pressione [ENTER] para continuar...")
        
    elif opcao_menu == 4: # BUSCAR CONTATO
        print("-" * 30)
        contato_buscar = input("Digite o email do contato que deseja buscar: ")
        contato_encontrado = buscar_dados_contato(contato_buscar)
        if contato_encontrado:
            print(f"Nome: {contato_encontrado.nome}")
            print(f"Email: {contato_encontrado.email}")
            print(f"Telefone: {contato_encontrado.telefone}")
        else:
            print("Contato não encontrado")
        input("Pressione [ENTER] para continuar...")
            
    elif opcao_menu != 0:
        print("Opcao invalida!")
        input("Pressione [ENTER] para continuar...")
    else:
        print("Obrigado por usar a agenda de contatos TW")