import os

os.system("cls")

# Definição/Atribuição de Listas
lista_simples_inteiro = [1,2,2,2,4,5]
lista_simples_string = ["Olá", "Mundo"]
lista_simples_mesclada = [1, "Olá", True, 1.5]
nested_list = [[1,2,True], ["Olá", "Mundo"]] # LISTAS ENCADEADAS

print("Lista Inteiro: ", lista_simples_inteiro)
print("Lista String: ", lista_simples_string)
print("Lista Mesclada: ", lista_simples_mesclada)
print("Lista Encadeada", nested_list)

#---------------------------------------
# *** METODOS P/ MANIPULAR LISTAS *****
#---------------------------------------
# Len() - Retornar tamanho da lista
print("Tamanho Lista Inteiro:", len(lista_simples_inteiro))
print("Tamanho da Lista (nested_list):", len(nested_list))

# Append() - Insere no Final da Lista
lista_simples_inteiro.append(8)
print("Append(8) -> Lista Inteiro:", lista_simples_inteiro)

# Insert() - Insere em  una posição da lista
lista_simples_mesclada.insert(0,99)
print("Insert(0,99) -> Lista Mesclada:", lista_simples_mesclada)

# Remove() - Remove item da lista
lista_simples_inteiro.remove(1)
print("Remove(1) -> Lista Inteiro:", lista_simples_inteiro)

# Index() - Retorna posição de item na lista
index = lista_simples_inteiro.index(8)
print("Index(8) -> Lista Inteiro:", index)

# Count() - Retorna Qtd. Ocorrências de um Item na Lista
count = lista_simples_inteiro.count(2)
print("Count(2) -> Lista Inteiro:", count)

# Sort() - Ordena a Lista Crescente ou Decrescente
lista_simples_inteiro.sort(reverse=True)
print("Sort(reverse=True) -> Lista Inteiro:", lista_simples_inteiro)


