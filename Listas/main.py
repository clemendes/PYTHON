from array import array
import classe_lista
import os

# FUNÇÕES MENU LISTA
def lista_op1(lista):
    reg = int(input("DIGITE UM VALOR P/ O REGISTRO (Nº INTEIRO): "))
    lista.inserir_elemento_final(reg)
    input(f"REGISTRO [{reg}] INSERIDO NA LISTA..." )

def lista_op2(lista):
    reg = int(input("DIGITE UM VALOR P/ O REGISTRO (Nº INTEIRO): "))
    pos = int(input("INFORME A POSIÇÃO NA LISTA QUE DESEJA INSERIR: "))
    lista.inserir_elemento_posicao(reg,pos)
    input(f"REGISTRO [{reg}] INSERIDO NA POSIÇÃO [{pos}] DA LISTA...")

def lista_op3(lista):
    reg = int(input("DIGITE UM VALOR PARA CONSULTA: "))
    pos = lista.indice(reg)
    if pos != -1:
        input(f"REGISTRO [{reg}] ENCONTRADO NA POSIÇÃO [{pos}] DA LISTA...")
    else:
        input(f"REGISTRO [{reg}] NÃO ENCONTRADO NA LISTA!...")

def lista_op4(lista):
    input(f"TAMANHO: {lista.tamanho_vetor()} POSIÇÕES...")

def lista_op5(lista):
    input(f"REGISTROS: {lista.listar_elementos()} ...")

# MAPEANDO OS INPUTS PARA AS CHAMADAS DE FUNÇÕES
opcoes_lista = {1: lista_op1, 2: lista_op2, 3: lista_op3, 4:lista_op4, 5:lista_op5}

# INICIO DO PROGRAMA
opcao = None
# INFORME QTD. POSICOES PARA LISTA
os.system('cls')
qtd = int(input(">>> INFORME A QTD. REGISTROS P/ LISTA: "))
lista = classe_lista.Lista(qtd)
input("LISTA INICIALIZADA...")

# APRESENTA OPÇÕES PARA LISTA
while opcao != 0:
    os.system('cls')
    lista.menu()
    opcao = int(input(">>> ESCOLHA UMA OPÇÃO: "))
    if (opcao >= 1 and opcao <= 6):
        try:
            opcao_interna = opcoes_lista[opcao](lista)
        except KeyError:
            pass
    elif (opcao != 0):
        input("OPÇÃO INVÁLIDA...")
        os.system('cls')
