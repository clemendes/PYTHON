import os

os.system("cls")

lista_simples = [1,2,3,4,5,6]

nova_lista = []

# Nova Lista -> lista_simples -> Elementos ao Quadrado
for i in lista_simples:
   nova_lista.append(i * i)
print(nova_lista)

# Comprehension -> new_list -> lista_simples -> Elementos ao Quadrado
new_list = [ i * i for i in lista_simples]
print(new_list)