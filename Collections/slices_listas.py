import os

os.system("cls")

lista_simples = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

# Retornar somente os 5 primeiros 
list_cinco_primeiros = lista_simples[0:5]
print("5 Primeiros: ", list_cinco_primeiros)

# Retornar somente os 5 útimos
list_cinco_ultimos = lista_simples[len(lista_simples)-5:len(lista_simples)]
print("5 Últimos: ", list_cinco_ultimos)

# Retornar todo conteúdo a partir de um índice
list_menos_primeiro = lista_simples[1:]
print("Tudo Menos o Primeiro: ", list_menos_primeiro)

# Slice - Criando Intervalo
intervalo = slice(1,4)
list_com_interv_slice = lista_simples[intervalo]
print("Utilizando Intervalo Slice: ", list_com_interv_slice)