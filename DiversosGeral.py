# Aprendendo a comentar ----
""" Assim também comenta """
# --------------------------

# Comando Print String
print("OLÁ MUNDO!")
print("----------------------")

# Comando Print (Número)
print(5)
print("----------------------")

# Comando Print + \n (quebra de linha)
print("OLÁ \nMUNDO!")
print("----------------------")

# Comando Print (Texto + Número)
print("EU TENHO",28,"ANOS")
print("----------------------")

# Atribuições de variáveis
print("IMPRIMINDO INTEIRO / FLOAT / STRING / LISTA / BOOLEAN")
varInt = 10
varFloat = 1.0
varString = ("STRING")
varLista = ["T","X","G","O","B","P",120.1,111,5,3,2.0,2.2,120]
varBoolean = 1==1

print("INT = ", varInt)
print("FLOAT =" ,varFloat)
print("STRING = ", varString)
print("LISTA = ", varLista)
print("BOOLEAN = ", varBoolean)
print("----------------------")

# ATRIBUICOES MULTIPLAS
x, y, z = 10, 20 ,30
print("ATRIBUICOES MULTIPLAS DE X, Y, Z =", x,y,z)
print("----------------------")

# FORMATANDO SAIDA INT
print("FORMATANDO varInt 03 CASAS DECIMAIS = %.3f" %varInt)
print("----------------------")

# FORMATANDO SAIDA FLOAT
print("FORMATANDO varFloat 05 CASAS DECIMAIS = %.5f" %varFloat)
print("----------------------")

# FORMATANDO SAIDA STRING
print("FORMATANDO SAIDA DE STRINGS = %s" %varString)
print("----------------------")

# CONVERSAO DE VARIÁVEIS
print("INT EM FLOAT =", float(varInt))
print("----------------------")

print("FLOAT EM INT =", int(varFloat))
print("----------------------")

print("CONVERTE PARA STRING = (FLOAT + FLOAT)", str(varFloat) + str(varFloat))
print("----------------------")

# OPERACOES MATEMATICAS
a = 9
b = 16
adicao = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
divisao_int = a // b
resto = a % b
potencia = a**b
raiz = (a **(1/2))
print("A = 5 |  B = 2")
print("ADICAO (A + B) =", adicao)
print("SUBTRACAO (A - B) =", subtracao)
print("MULTIPLICACAO (A * B) =", multiplicacao)
print("DIVISAO (A / B) =", divisao)
print("DIVISAO INTEIROS (A // B) =", divisao_int)
print("RESTO DA DIVISAO (A % B) =", resto)
print("POTENCIA (A**B) =", potencia)
print("RADICIACAO (RAIZ QUADRADA DE A) =",raiz)
print("----------------------")

# OPERADORES COMPOSTOS (ATRIBUICOES E OPERACOES MANIPULACAO DE VARIAVEIS)
print("OPERADORES COMPOSTOS (ATRIBUICOES E MANIPULACAO DE VARIAVEIS")
print("INCREMENTO, DECREMENTO")
maisIgual = menosIgual = vezesIgual = divididoIgual = moduloIgual = 9
print("CONSIDERE 9 INICIAL")

maisIgual += 1 #resultado 10
menosIgual -= 1 #resultado 8
vezesIgual *= 1 #resultado 9
divididoIgual /= 1 #resultado 9
moduloIgual %= 2 #resultado 3

print("9 MAIS IGUAL += 1",maisIgual)
print("9 MENOS IGUAL -= 1",menosIgual)
print("9 VEZES IGUAL *= 1",vezesIgual)
print("9 DIVIDIDO IGUAL /= 1",divididoIgual)
print("9 MODULO IGUAL %= 2",moduloIgual)

print("----------------------")

# RETORNANDO TIPO DE VARIAVEL
tipo = type(varFloat)
print("TYPE - RETORNANDO TIPO DA VARIAVEL 'varFloat =",tipo)
tipo = type(varString)
print("TYPE - RETORNANDO TIPO DA VARIAVEL 'varString =",tipo)
tipo = type(varInt)
print("TYPE - RETORNANDO TIPO DA VARIAVEL 'varInt =",tipo)
""" tipo = type(varLista
 print("RETORNANDO TIPO DA VARIAVEL 'varLista' =",tipo) """
tipo = type(varBoolean)
print("TYPE - RETORNANDO TIPO DA VARIAVEL ''varBoolean' =",tipo)
print("----------------------")

# COMPARADORES LOGICOS AND 
x = 10
e = (x > 0) and (x == 10)
print("OPERADOR AND")
print("X = 10")
print("(X > 0) AND (X == 10) ---> RESULTADO ",e)
print("----------------------")

# COMPARADORES LOGICOS OR  
x = 0
ou = (x == 1) or (x == 10)
nao = not(x == 1)
print("OPERADOR OR")
print("X = 0")
print("(X == 1) OR  (X == 10) ---> RESULTADO ",ou)
print("NOT -  NAO((X == 1))?",nao)
print("----------------------")

# OPERADORES LOGICOS == , !=, > , < , >=, <=
print("OPERADOR == IGUAL")
print("OPERADOR != DIFERENTE")
print("OPERADOR > MAIOR")
print("OPERADOR < MENOR")
print("OPERADOR >= MAIOR OU IGUAL")
print("OPERADOR <= MENOR OU IGUAL")

numero1 = 10
numero2 = 20

if(numero1 == numero2):#operador de igualdade
    print("O número %d é igual a %d. "%(numero1, numero2) )
if(numero1 != numero2):#operador de diferença
    print("O número %d é diferente de %d "%(numero1, numero2))
if(numero1 < numero2):#operador menor que
    print("O número %d é menor que o %d "%(numero1, numero2))
if(numero1 > numero2):#operdor de maior que
    print("O número %d é maior que o %d "%(numero1, numero2))
if(numero1 >= numero2):#maior ou igual que
    print("O número %d é maior ou igual que %d "%(numero1, numero2))
if(numero1 <= numero2):#menor ou igual que
    print("O número %d é menor ou igual que %d "%(numero1, numero2))

ee = 10 is 10
isnot = 10 is not 10
print("É - IS (10 É 10 ?)",ee)
print("NÃO É - IS NOT (10 NÃO É 10 ?)",isnot)
print("----------------------")

# RETORNA FALSE SE TIVER CARACTERE QUE NAO SEJA LETRAS
fullletter = varString.isalpha()
print("ISALPHA - VERIFICA SE TODOS CARACTERES SAO LETRAS =",fullletter)
print("----------------------")

# RETIRA ESPACOES EM BRANCO NO COMECO E NO FIM
print("             STRIP - TESTE DE TEXTO COM ESPAÇOS      ")
print("    STRIP TESTE DE TEXTO S/ ESPAÇOS      ".strip())
print("----------------------")

# JOIN - UNE COM DELIMITADOR
print("JOIN - JUNTA CADA ITEM DA STRING COM UM DELIMITADOR ESPECIFICADO")
juncao = ("/".join(varString))
print(juncao)
print("----------------------")

# JOIN - EM LISTAS 
print("JOIN - EM LISTAS")
juncao = ("-".join(varLista[0:5]))
print(juncao)
print("----------------------")

""" # SPLIT - SEPARA COM DELIMITADOR
print("SPLIT - SEPARA CADA ITEM DA STRING COM UM DELIMITADOR ESPECIFICADO")
print(juncao)
juncao.split("-")
print(juncao)
print("----------------------") """

# ACESSANDO CARACTERES STRING
teste = "TESTE = 112233445566778899"
print("ACESSANDO NUMEROS DA STRING TESTE =", teste[8:])
print("----------------------")

# FOR EM UMA STRING
print("FOR DENTRO DA STRING - DECOMPONDO-A")
palavra = "PYTHON É FODA!"
for x in palavra:
    print(x)
print("----------------------")

# PESQUISANDO CARACTERE OU STRING DENTRO DE UMA STRING
print("IN - PESQUISANDO CARACTERE OU STRING DENTRO DE UMA STRING")
pesquisa = 'É' in palavra
print("RESULTADO PESQUISA 'É' =",pesquisa)
print("----------------------")

# TAMANHO DA STRING
print("LEN - TAMANHO DE UMA STRING")
tamanho = len(palavra)
print(tamanho)
print("----------------------")

# UPPER MAIUSCULA
print("UPPER - MAIUSCULA")
maiuscula = palavra.upper()
print(maiuscula)
print("----------------------")

# LOWER MINUSCULA
print("LOWER - MINUSCULA")
minuscula = palavra.lower()
print(minuscula)
print("----------------------")

# Tamanho de uma lista
tamanho = len(varLista)
print("TAMANHO DA LISTA E IMPRIMINDO \nTAMANHO =", tamanho)
print("----------------------")

# Formas de Imprimir uma lista
print("Imprimindo lista varLista[5] =", varLista[5])
print("Imprimindo lista varLista[0:3] =", varLista[0:3])
print("Imprimindo lista varLista[:3] =", varLista[:3])
print("Imprimindo lista varLista[3:] =", varLista[3:])
print("Imprimindo lista varLista[:] =", varLista[:])
print("----------------------")

# Menor Valor da lista
novalista = varLista[6:13]
minimo = min(novalista)
print("MENOR VALOR da Lista (slicing) = ",minimo)

print("----------------------")

# Maior Valor da lista
novalista = varLista[6:13]
maximo = max(novalista)
print("MAIOR VALOR da Lista (slicing) = ",maximo)

print("----------------------")

# Somando Valores da Lista
novalista = varLista[6:13]
soma = sum(novalista)
print("SOMANDO valores Lista (slicing) = ",soma)
print("----------------------")

# Contando Valores da Lista
novalista = varLista[6:13]
cont = novalista.count(120)
print("CONTANDO valores Lista = 120 (slicing) = ",cont)
print("----------------------")

# FOR in Listas
print("Varredura usando FOR in varLista: ")
for x in varLista:
    print(x)
else:
    print("Final x =", x)

print("----------------------")

# While in Listas
print("Varredura usando WHILE in varLista: ")

i = 0

while i < len(varLista):
    print(varLista[i])
    i = i + 1
    if i > 12: break
""" break || continue """

print("----------------------")

# RANGE - Sequencias e Listas
lista = list(range(2,20,2))
print("RANGE - Gerando lista de numeros pares de 1 a 20 \n",lista)

print("----------------------")

# FOR + RANGE
print("FOR + RANGE - Números ímpares de 1 a 20")
for i in range(1, 20, 2):
    print(i)
    
print("----------------------")

# SORT - CLASSIFICANDO  
print(".SORT ORDENANDO")
listaClassificada = varLista[6:13]
listaClassificada.sort()
print(listaClassificada)
    
print("----------------------")

# SORTED EM LISTAS - CLASSIFICANDO NUMERICA
print("SORTED ORDENANDO CRESCENTE (LISTA NUMERICA)")
listaOrdenada = sorted(varLista[6:13])
print(listaOrdenada)
    
print("----------------------")

# SORTED EM LISTAS - CLASSIFICANDO STRING
print("SORTED ORDENANDO CRESCENTE (LISTA ALFABETICA)")
listaOrdenada = sorted(varLista[0:6])
print(listaOrdenada)
    
print("----------------------")

# SORTED - CLASSIFICANDO REVERSE NUMERICO
print("SORTED ORDENANDO DECRESCENTE REVERSE (LISTA NUMERICA)")
listaOrdenada = sorted(varLista[6:13], reverse=True)
print(listaOrdenada)
    
print("----------------------")

# SORTED - CLASSIFICANDO REVERSE ALFABETICO
print("SORTED ORDENANDO DECRESCENTE REVERSE (LISTA ALFABETICA)")
listaOrdenada = sorted(varLista[0:6], reverse=True)
print(listaOrdenada)
    
print("----------------------")

# COPIANDO UMA LISTA
print("COPIANDO UMA LISTA")
listaCopiada = listaOrdenada[:]
print("Lista Oficial", listaOrdenada)
print("Lista Copiada", listaCopiada)
    
print("----------------------")

# JUNTANDO UMA LISTA
print("JUNTANDO UMA LISTA")
listaJuntada = listaOrdenada + listaCopiada
print("Lista Oficial", listaJuntada)
    
print("----------------------")

# APPEND EM LISTA
print("APPEND - INSERINDO ITEM NA LISTA POSICAO FINAL")
listaOrdenada.append("APPEND1")
listaOrdenada.append("APPEND2")
listaOrdenada.append("APPEND3")
print("Lista Oficial", listaOrdenada)
    
print("----------------------")

# INSERT EM LISTA
print("INSERT - INSERINDO ITEM NA LISTA (POSICAO ESPECIFICA)")
listaOrdenada.insert(6,"INSERT1")
listaOrdenada.insert(7,"INSERT2")
listaOrdenada.insert(8,"INSERT3")
print("Lista Oficial", listaOrdenada)
    
print("----------------------")

# REMOVE EM LISTA
print("REMOVE - REMOVE ATRAVES DO VALOR DO ELEMENTO '(INSERT2)'")
listaOrdenada.remove("INSERT2")
print("Lista Oficial", listaOrdenada)
    
print("----------------------")

# POP (REMOVE) EM LISTA
print("POP (REMOVE) - REMOVE ATRAVES DO INDICE (12)")
listaOrdenada.pop(8)
print("Lista Oficial", listaOrdenada)
    
print("----------------------")

# DEL (DELETE) EM LISTA
print("DEL (DELETE) - DELETA ATRAVES DO INDICE [0]")
del(listaOrdenada[0])
print("Lista Oficial", listaOrdenada)
    
print("----------------------")


# INDEX EM LISTA
print("INDEX - RETORNAR O INDICE DE UM ELEMENTO")
indice = listaOrdenada.index("APPEND2")
print("INDICE DE APPEND2 =", indice)
    
print("----------------------")

# Verificando a existencia de um item em uma Lista (True/False)
existe = 'APPEND2' in listaOrdenada
print("VERIFICANDO EXISTENCIA DE 'APPEND1' EM LISTA \nResultado =",existe)
print("----------------------")

# IF / ELIF / ELSE
z = 12

if z == 10:
    print("Z = 10")
    print("IMPRIMINDO O IF - SE Z == 10")
elif z != 10: 
    print("Z = 13")
    print("IMPRIMINDO O IF - SE Z != 10")
else:
    print("NENHUM DOS 2")

print("----------------------")

# OPERADOR TERNARIO IF ELSE NUMA LINHA
fruit = 'Orange'
print('Yes' if fruit == 'Apple' else 'No')
print("----------------------")

# ENTRADA DE DADOS - INPUT() E RAW_INPUT()
string1 = input("INPUT - DIGITE SEU NOME: ")
print(string1)
numero1 = int(input("DIGITE SUA IDADE: "))
print(numero1)
numero3 = float(input("DIGITE SEU PESO: "))
print(numero3)
print("----------------------")

#FUNCAO SIMPLES QUE RETORNA UM VALOR
print("FUNCAO SIMPLES QUE RETORNA UM VALOR")
def print_numero():
    return 10

num = print_numero()
print(num)
print("----------------------")

#FUNCAO MULTIPLICACAO UTILIZANDO 2 VARIAVEIS X, Y
print("FUNCAO MULTIPLICACAO ENTRE 02 NUMEROS")
def mult_dois_numeros(x,y):
    mult = x * y
    return mult

resultado = mult_dois_numeros(10,20)
print("mult_dois_numeros(10,20) =",resultado)
print("----------------------")

#FUNCAO SIMPLES IMPRESSAO
print("IMPRIMINDO POR RETORNO DE FUNCAO")
def spam():
    retorno = "*** ISTO É UM RETORNO DE FUNCAO ***"
    return retorno

print(spam())
print("----------------------")

#COMPARANDO TIPO DA VARIAVEL
print("COMPARANDO TIPO DA VARIAVEL")
a = 1
tipo = type(a) == int      # True
print("A = 1 | A é tipo INT? ")
print(tipo)

b = 1.0
tipo = type(b) == int      # True
print("B = 1.0 | B é tipo INT? ")
print(tipo)
print("B é do tipo ",type(b))

result = type(0.99) == float # True
print("0.99 | 0.99 é tipo FLOAT? ")
print(result)
print("----------------------")

# IMPORTANDO MODULOS - MATH
import math
print("RAIZ QUADRADA DE 25 - UTILIZANDO MATH.SQRT(25)")
print(math.sqrt(25))
print("TRANSFORMANDO EM INTEIRO ",int(math.sqrt(25)))
print("----------------------")

#DATAS E HORAS - DATETIME
from datetime import datetime
now = datetime.now()
print("DATEIME.NOW()")
print(now)
print(now.year)
print(now.month)
print(now.day)
print("DATA FORMATO BRASILEIRO")
print('%s/%s/%s' % (now.day, now.month, now.year))
print("IMPRIMINDO AS HORAS")
print('%s:%s:%s' % (now.hour, now.minute, now.second))
print("----------------------")

# DICIONARIOS - MATRIZES
print("CRIANDO UM DICIONARIO - NOME: (STR), IDADE: (INT) , PESO(FLOAT), PROFISSOES(LISTA):")

dicionario = {
    "nome": "CLEVERSON MENDES",
    "idade": 28,
    "peso": 72,
    "profissoes": ["AUX. LOGISTICA","ANALISTA LOGISTICA","CONSULTOR SAP"]
}
print("IMPRIMINDO DICIONARIO POR TIPO") 
print(dicionario['nome'])
print(dicionario['idade'])
print(dicionario['peso'])
print(dicionario['profissoes'][2])
print("IMPRIMINDO DICIONARIO COMPLETO:") 
print(dicionario)
print("----------------------")

# EXEMPLO DE FUNCAO CALCULAR PAGAMENTO HORAS vs VALOR HORAS
print("EXEMPLO FUNCAO - CALCULAR PAGAMENTO (Qtd.Horas , Valor_Hora)")
def calcular_pagamento(qtd_horas, valor_hora):
     horas = float(qtd_horas)
     taxa = float(valor_hora)
     if horas <= 40:
        salario = horas * taxa
     else:
        h_excd = horas - 40
        salario = 40 * taxa + (h_excd*(1.5*taxa))
     return salario

str_horas = input("Digite as horas: ")
str_taxa = input("Digite a taxa: ")
total_salario = calcular_pagamento(str_horas,str_taxa)
print("O valor de seus rendimentos é R$", total_salario)
print("----------------------")

# FUNCOES FACTORIAL-FLOOR-CEIL-FABS
import math
x = 3.5
print("MATH.FACTORIAL DE X = ",math.factorial(int(x)))
print("MATH.FLOOR DE X = ",math.floor(x))
print("MATH.CEIL DE X = ", math.ceil(x))
print("MATH.FABS DE X = ",math.fabs(x))
print("----------------------")

# FORMATANDO SAIDAS
print("FORMAT INTEIRO --> FLOAT: ", format(2, 'f'))
print("----------------------")

# PRINT COM SEPARADORES
print("PRINT COM SEPARADORES")
num = num1 = num2 = num3 = 3
print(num, num1, num2, num3, sep="|")
print("----------------------")

# FOR TODOS SAO POSITIVO
print("FOR - VERIFICA SE TODOS SAO POSITIVOS EM UMA LISTA")
listaDeInteiros = [2, 6, 4, 7, -2]
todosSaoPositivos = True
for i in listaDeInteiros:
    if i <= 0:
        todosSaoPositivos = False
        break
if todosSaoPositivos:
    print("Todos sao positivos")
else:
    print("Tem algum negativo")
print("----------------------")

# ALL SE TODOS SAO PARES
print("ALL - VERIFICA SE TODOS SAO PARES EM UMA LISTA")
listaDeInteiros = [2, 6, 4, 7, -2]
if all(i % 2 == 0 for i in listaDeInteiros):
   print("Todos sao pares")
else:
    print("Tem algum impar")
print("----------------------")

# ANY SE TEM ALGUM IMPAR
print("ANY - VERIFICA SE ALGUM E IMPAR EM UMA LISTA")
listaDeInteiros = [2, 6, 4, 7, -2]
if not any(i % 2 != 0 for i in listaDeInteiros):
    print("Todos sao pares")
else:
    print("Tem algum impar")
print("----------------------")

# ANY SE TEM ALGUM VAZIO EM LISTA
lista_de_strings = ["ABC", "DEF", "GHI", "JKL"]
if any(s == '' for s in lista_de_strings):
    print("Erro: strings vazias existem na lista!")
else:
    print("NAO EXISTE STRINGS VAZIAS")
print("----------------------")

""" #FUNCAO MAP + SQRT (FAZ SQRT PARA TODA LISTA
print("FUNCAO MAP + SQRT ")
import math
lista1 = [1, 4, 9, 16, 25]
lista2 = map(math.sqrt, lista1)
print(lista2)
print("----------------------") """

#TRATANDO ERRO DE PESQUISA EM DICIONARIO"

dicionario = {'Maria': '1235'}
try:
    valor = dicionario['chave'] 
except KeyError:
    valor = None

valor = dicionario.get('chave')

# FUNCAO MDC
def mdc(num1, num2):
    resto = None
    while resto is not 0:
        resto = num1 % num2
        num1  = num2
        num2  = resto

    return num1
print("----------------------")



